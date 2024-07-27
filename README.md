# BlazeAI

## Scrapped and Preprocessed Dataset 
https://drive.google.com/file/d/1uNl3OIGLxTv-2c00XZL8jQ-SbYT6jz3e/view?usp=sharing

# Fine-Tuning Report: Llama 3.1 Model on Crypto Company Filings

## Training Configuration

- **Model:** Llama 3.1
- **Training Framework:** PyTorch
- **Training Platform:** Kaggle (GPU P100)
- **Training Duration:** 1 hour 30 minutes
- **Dataset:** SEC Filings (10-K, 10-Q, 8-K) for:
  - Coinbase Global, Inc. (COIN)
  - Marathon Digital Holdings, Inc. (MARA)
  - Riot Platforms, Inc. (RIOT)
- **Training Arguments:**
  - **Output Directory:** `new_model`
  - **Batch Size:** 1 (per device for both training and evaluation)
  - **Gradient Accumulation Steps:** 2
  - **Optimizer:** `paged_adamw_32bit`
  - **Epochs:** 3
  - **Evaluation Strategy:** Steps
  - **Eval Steps:** 0.2
  - **Logging Steps:** 1
  - **Warmup Steps:** 10
  - **Learning Rate:** 2e-4
  - **Mixed Precision:** FP16/ BF16 (depending on support)
  - **Group by Length:** True
  - **Reporting to:** Weights and Biases (wandb)

## LoRA Configuration

- **Rank:** 16
- **LoRA Alpha:** 32
- **LoRA Dropout:** 0.05
- **Bias:** None
- **Task Type:** CAUSAL_LM
- **Target Modules:** 
  - `['up_proj', 'down_proj', 'gate_proj', 'k_proj', 'q_proj', 'v_proj', 'o_proj']`

## Evaluation Metrics

### Loss

- **Initial Loss:** ~0.225
- **Final Loss:** ~0.2
- **Trend:** The loss consistently decreased over the training steps, indicating effective learning.

### Steps per Second

- **Initial:** ~0.729 steps/sec
- **Trend:** Slight dip in the middle of the training, eventually stabilizing back to ~0.729 steps/sec.

### Runtime

- **Metric:** Fairly stable around 104.31 to 104.33 seconds, showing consistent performance during evaluation steps.

### Samples per Second

- **Initial:** ~0.729 samples/sec
- **Trend:** Noticeable dip during mid-training, recovering to initial value of ~0.729 samples/sec.

## System Usage Evaluation

- **GPU Utilization:**
  - Utilized Kaggle GPU (P100) for training.
  - Employed mixed precision training (FP16 or BF16 based on support) for optimizing memory usage and training speed.

- **Memory Consumption:**
  - Efficient use of LoRA and mixed precision allowed effective memory utilization, enabling fine-tuning with a large dataset and complex model architecture.

- **Training Time:**
  - Completed fine-tuning in approximately 1 hour and 30 minutes, reasonable for the dataset size and model complexity.

## Conclusion

The fine-tuning of the Llama 3.1 model on SEC filings for specified crypto companies was successful. Evaluation metrics indicate steady improvement in model performance throughout training. Efficient training techniques and configurations, such as LoRA and mixed precision, ensured optimal use of computational resources, resulting in effective model training within a reasonable timeframe.

The final model has been pushed to Hugging Face for further usage and evaluation.

## Visualizations

![Evaluation Report][  report-link](https://api.wandb.ai/links/kumarsakthivel3251-sri-eshwar-college-of-engineering/0z72cvjj)

# OUTPUT 
QUERY and RESPONSE for all give examples
Query: What are Coinbase's main revenue streams?
Response: Coinbase's main revenue streams are transaction fees and interest income.
Transaction fees are generated from the spread between the price at which Coinbase buys and sells cryptocurrency, as well as the network fees associated with processing transactions. Coinbase also earns interest income on its holdings of cryptocurrency, which it generates by lending out its cryptocurrency to other entities.
In addition to these primary revenue streams, Coinbase also earns revenue from other sources, such as its Coinbase Pro platform, which allows users to trade cryptocurrency at a lower fee than Coinbase's primary platform. Coinbase

Query: How does Marathon Digital Holdings view the future of Bitcoin mining?
Response: Marathon Digital Holdings is a company that is focused on the development of Bitcoin mining infrastructure. The company believes that Bitcoin mining is a key component of the Bitcoin network, and that it will continue to be an important part of the cryptocurrency ecosystem for the foreseeable future. Marathon Digital Holdings is committed to building and operating the most efficient and cost-effective Bitcoin mining facilities in the world, and to providing its shareholders with a secure and stable investment in the Bitcoin mining industry.

Query: What were the key challenges faced by Riot Platforms in the last fiscal year?
Response: The company's key challenges in the last fiscal year included a decline in revenue, a decrease in the value of its Riot Token, and a drop in its market capitalization.

Query: How has Coinbase's user base grown over the past three years?
Response: Below is Coinbase's user base, as of Q1 2018, Q1 2019, and Q1 2020.
Coinbase's user base, as of Q1 2018, Q1 2019, and Q1 2020.
Coinbase has seen a significant increase in its user base over the past three years, with 20 million users as of Q1 2020. Coinbase's user base has grown from 13 million in Q1 201

Query: What are the primary regulatory concerns mentioned by these companies?
Response: 1. The SEC is concerned that Coinbase is allowing crypto assets to be used for securities transactions, which is a violation of federal law.
2. Coinbase is a crypto asset that is not registered with the SEC, which is a violation of federal law.
3. Coinbase is a crypto asset that is not registered with the SEC, which is a violation of federal law.
4. Coinbase is a crypto asset that is not registered with the SEC, which is a violation of federal law.
5. Coinbase is a crypto

Query: How do these companies manage cryptocurrency price volatility risk?
Response: Company: Riot Platforms, Inc., Input: Riot Platforms, Inc. (RIOT) Q2 2022 Earnings Call, August 8, 2022, 4:30 p.m. ET, Response: Hello, and welcome to the Riot Platforms, Inc. second quarter 2022 results conference call. My name is Oren Livne, and I will be moderating the call today. [Operator instructions] Thank you. I would now like to turn the call over to Riot's

Query: What investments in infrastructure have these companies made recently?
Response: Company: Marathon Digital Holdings, Inc., Investment: Marathon Patent Group, Inc., Amount: 2,000,000,000, Currency: USD, Date: 20161201
Company: Marathon Patent Group, Inc., Investment: Marathon Patent Group, Inc., Amount: 2,000,000,000, Currency: USD, Date: 20161201
Company: Marathon Patent Group, Inc., Investment: American Strategic Minerals Corp., Amount: 2,000,000,000, Currency

Query: How do these companies approach cybersecurity?
Response: Cybersecurity is an ever-evolving challenge that requires a proactive and adaptive approach. Companies that prioritize cybersecurity consider a variety of factors, such as the following:
1. **Risk Assessment:** Companies conduct regular risk assessments to identify and prioritize potential threats, vulnerabilities, and risks. This allows them to develop appropriate security measures and strategies to mitigate those risks.

2. **Security Awareness:** Companies promote cybersecurity awareness among their employees, customers, and partners. This includes training, education, and awareness campaigns to ensure that everyone understands the importance of

Query: What are the companies' strategies for staying competitive in the crypto market?
Response: Company strategies for staying competitive in the crypto market include:
1. Innovation: Companies that are at the forefront of crypto innovation are more likely to stay competitive. This includes companies that are developing new technologies, such as blockchain, or new crypto assets.

2. Customer service: Companies that provide excellent customer service are more likely to stay competitive. This includes companies that are responsive to customer needs and that provide quick and easy access to customer support.

3. Risk management: Companies that have effective risk management practices

Query: How have recent market conditions affected these companies' financial performance?
Response: Company: Marathon Digital Holdings, Inc., Input: Q2 2022, Response: Marathon Digital Holdings, Inc. Reports Second Quarter 2022 Results and Provides Business Update
Company: Riot Platforms, Inc., Input: Q2 2022, Response: Riot Platforms, Inc. Reports Second Quarter 2022 Results and Provides Business Update
