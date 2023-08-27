# Story Genre Classification with Hugging Face Transformers and Fastai

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Getting Started](#getting-started)
    - [Clone Repository](#clone-repository)
    - [Run Web Scraping Scripts](#run-web-scraping-scripts)
    - [Model Training](#model-training)
    - [Evaluate Model](#evaluate-model)
    - [Convert Model to ONNX](#convert-model-to-onnx)
4. [Model Deployment](#model-deployment)
    - [Hugging Face](#hugging-face)
    - [Render](#render)
5. [Contributions](#contributions)
6. [License](#license)


## Introduction

This project demonstrates how to perform multi-label text classification using Hugging Face Transformers and Fastai. It involves training a deep learning model to predict multiple genre labels for a given text description.

## Features

- Web scraping using Selenium Webdriver.
- Scaping over 55k data from Royal Road, a popular website for fan made stories/fictions.
- Utilizes the power of pre-trained transformer models from Hugging Face Transformers.
- Implements multi-label classification using Fastai's powerful text processing capabilities.
- Analyzes model performance using various metrics such as F1 score, ROC AUC score, and confusion matrix.
- Provides code snippets and explanations for data preprocessing, model training, and evaluation.

## Getting Started

### 1. Clone this repository:

```bash
git clone https://github.com/2mdipro7/story-genre-classifier.git
```

### 2. Run the web scraping scripts:

    First, run url_scraper.py to retrieve the URLs of the files to be scraped.
    ```bash
    python url_scraper.py
    ```
    Then, run description_scraper.py to gather detailed information from the retrieved URLs.
    ```bash
    python description_scraper.py
    ```
### 3. Model Training:

#### Leveraging Pre-trained Transformer Models
    In this project, we harnessed the power of pre-trained transformer models from Hugging Face Transformers to elevate our text classification capabilities. By tapping into these models, we gained access to their extensive knowledge of language and context, allowing us to achieve impressive results in genre classification.

#### Our Choice: bert-base-uncased Architecture
    For this project, we selected the **bert-base-uncased** architecture, a well-established variant of BERT that's specifically designed for uncased text. By making this strategic choice, we enabled our model to comprehend the subtleties of language usage, leading to enhanced accuracy and performance in genre classification.

#### Model Training in model_training.ipynb
    Our journey is documented in the model_training.ipynb notebook, where we documented each step of the training process. From preprocessing our data to configuring the model, defining the loss function, selecting optimization strategies, and monitoring training progress, the notebook serves as a comprehensive guide to our approach.

### 4. Model Evaluation:

    Here is how our model performed after training for 7 epochs:

        | Metric            | Score   |
        |----------------   |---------|
        | Accuracy Multi    | 0.87    |
        | F1 (Micro)        | 0.65    |
        | F1 (Macro)        | 0.52    |
        | ROC AUC (Micro)   | 0.77    |
        | ROC AUX (Macro)   | 0.71    |

    Refer to the model_evaluation.ipynb notebook for detailed instructions.

### 5. Convert Model to ONNX:

    Convert your trained model to the ONNX format for deployment using the convert_to_onnx.ipynb notebook.

## Model Deployment

### 1. **Hugging Face**

    The model is deployed and accessible on Hugging Face's Model Hub. You can use it for inference and predictions by visiting the following link:
    
    [Story Genre Classifier - Hugging Face Model](https://huggingface.co/spaces/dipro7/story-genre-classifier)

### 2. **Render**

    Additionally, the model is deployed and hosted on Render, allowing you to interact with it via a web interface. You can access the deployed model using the following link:
    
    [Story Genre Classifier - Render Web Interface](https://story-genre-classifier.onrender.com)

## Contributions

Contributions are welcome! If you find any issues, have suggestions for enhancements, or want to contribute new features, feel free to submit pull requests or raise issues in the repository.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for more details.

## Acknowledgments

This project is inspired by the capabilities of Hugging Face Transformers and the ease of use provided by Fastai. Special thanks to the open-source community for their valuable contributions.

---

Feel free to explore the repository, experiment with the model, and contribute to make it even better. If you have any questions or need assistance, please don't hesitate to reach out. Happy coding!
