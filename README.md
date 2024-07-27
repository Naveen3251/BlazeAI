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

![Evaluation Report][(path/to/visualizations.png)](https://wandb.ai/kumarsakthivel3251-sri-eshwar-college-of-engineering/Fine-tune%20Llama%203%208B%20on%20Crypto%20Dataset/reports/Llama-3-1-8B-Crypto-Dataset-Fine-Tuning-Evaluation--Vmlldzo4ODI2ODQy)

