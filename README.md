# Multi-Label Text Classification with Hugging Face Transformers and Fastai

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Getting Started](#getting-started)
    - [Clone Repository](#clone-repository)
    - [Run Web Scraping Scripts](#run-web-scraping-scripts)
    - [Model Training](#model-training)
    - [Evaluate Model](#evaluate-model)
    - [Convert Model to ONNX](#convert-model-to-onnx)
4. [Contributions](#contributions)
5. [License](#license)


## Introduction

    This project demonstrates how to perform multi-label text classification using Hugging Face Transformers and Fastai. It involves training a deep learning model to predict multiple genre labels for a given text description.

## Features

- Web scraping using Selenium Webdriver.
- Utilizes the power of pre-trained transformer models from Hugging Face Transformers.
- Implements multi-label classification using Fastai's powerful text processing capabilities.
- Analyzes model performance using various metrics such as F1 score, ROC AUC score, and confusion matrix.
- Provides code snippets and explanations for data preprocessing, model training, and evaluation.

## Getting Started

1. Clone this repository:

```bash
git clone https://github.com/your-username/multi-label-text-classification.git
```

2. Run the web scraping scripts:

    First, run scraper1.py to retrieve the URLs of the files to be scraped.
    Then, run scraper2.py to gather detailed information from the retrieved URLs.

3. Model Training:

    Utilize the power of pre-trained transformer models from Hugging Face Transformers.
    Set up data blocks, model architecture, and training process in the model_training.ipynb notebook.
4. Evaluate Model:

    Analyze your trained model's performance using metrics such as F1 score, ROC AUC score, and confusion matrix.
    Refer to the model_evaluation.ipynb notebook for detailed instructions.
5. Convert Model to ONNX:

    Convert your trained model to the ONNX format for deployment using the convert_to_onnx.ipynb notebook.