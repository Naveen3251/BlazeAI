import os

from FineTuning.Crypto_model_finetuner import CryptoModelFineTuner


hf_token = os.getenv("HUGGINGFACE_TOKEN")
wandb_token = os.getenv("WANDB_API_KEY")
file_path = 'C:/BlazeAI/formatted_sec_filings_with_companies.jsonl'
alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{}

### Input:
{}

### Response:
""" 
fine_tuner = CryptoModelFineTuner(hf_token, wandb_token)
fine_tuner.train_model(file_path, alpaca_prompt)
