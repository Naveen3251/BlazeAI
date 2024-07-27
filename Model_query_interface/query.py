import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

class ModelQueryInterface:
    def __init__(self, model_name: str):
        """
        Initialize the ModelQueryInterface with a specific model.

        :param model_name: The name or path of the model to load.
        """
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)
        
        # Define the Alpaca prompt
        self.alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

        ### Instruction:
        {}

        ### Input:
        {}

        ### Response:
        """
    
    def query(self, instruction: str, input_text: str) -> str:
        """
        Generate a response for a given instruction and input.

        :param instruction: The instruction for the model.
        :param input_text: Additional context for the model.
        :return: The generated response.
        """
        prompt = self.alpaca_prompt.format(instruction, input_text)
        inputs = self.tokenizer(prompt, return_tensors='pt', padding=True, truncation=True).to(self.device)
        
        try:
            outputs = self.model.generate(**inputs, max_length=150, num_return_sequences=1)
            text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            response = text.split("### Response:")[1].strip() if "### Response:" in text else text
            return response
        except Exception as e:
            print(f"Error processing query: {instruction}")
            print(f"Exception: {e}")
            return "Error generating response."

    def batch_query(self, queries: list) -> None:
        """
        Process a batch of queries.

        :param queries: List of dictionaries with 'instruction' and 'input' keys.
        """
        for query in queries:
            response = self.query(query["instruction"], query["input"])
            print(f"Query: {query['instruction']}")
            print(f"Response: {response}\n")