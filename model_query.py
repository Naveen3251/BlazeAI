from Model_query_interface.query import ModelQueryInterface


model_name = "llama-3-8b-crypto-model"
interface = ModelQueryInterface(model_name=model_name)

queries = [
        {"instruction": "What are Coinbase's main revenue streams?", "input": ""},
        {"instruction": "How does Marathon Digital Holdings view the future of Bitcoin mining?", "input": ""},
        {"instruction": "What were the key challenges faced by Riot Platforms in the last fiscal year?", "input": ""},
        {"instruction": "How has Coinbase's user base grown over the past three years?", "input": ""},
        {"instruction": "What are the primary regulatory concerns mentioned by these companies?", "input": ""},
        {"instruction": "How do these companies manage cryptocurrency price volatility risk?", "input": ""},
        {"instruction": "What investments in infrastructure have these companies made recently?", "input": ""},
        {"instruction": "How do these companies approach cybersecurity?", "input": ""},
        {"instruction": "What are the companies' strategies for staying competitive in the crypto market?", "input": ""},
        {"instruction": "How have recent market conditions affected these companies' financial performance?", "input": ""}
]

interface.batch_query(queries)
