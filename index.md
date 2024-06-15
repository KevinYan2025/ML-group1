# Proposal

Authors: Zhixiang Yan, Abdullah Ahmed, Jad Ahmed Helmy

## Introduction / Background

With the rise of generative AI models, we can generate artwork in a few seconds. These generated artworks challenge us to ask how they compare stylistically and formally, in terms of authenticity and coherence, to art created by humans during defined periods in art history. This project aims to use a dataset that contains a collection of artwork of the 50 most influential artists of all time[[dataset](https://www.kaggle.com/datasets/ikarus777/best-artworks-of-all-time)] to train a model to classify the style of an art piece as being from a human or an artificial intelligence (AI) artist.

## Problem Definition

Given an image, our project aims to determine whether the art is AI-generated or human-created, and, if the latter, to categorize the style of art (eg, Baroque, Impressionism), thereby classifying the label and the image. A successful model would provide an effective tool for curation of art, digitization of art, and benchmarks towards transparency of AI content creation in the art market.

## Methods

### Data augmentation

Data augmentation can enrich the variability of the dataset, which is crucial for improving the model's generalization capability.[[1](https://spotintelligence.com/2023/03/09/data-augmentation-python-image-text-nlp/#:~:text=Data%20augmentation%20is%20a%20technique%20used%20in,with%20different%20versions%20of%20the%20same%20information.)]

### Feature Extraction

Feature extraction allows us to transform raw image data into numerical features that can yield better performance.[[2](https://www.mathworks.com/discovery/feature-extraction.html#:~:text=What%20Is%20Feature%20Extraction%3F,directly%20to%20the%20raw%20data.)]

### Label Encoding

Label encoding allows us to convert categorical data into numerical data for modeling. [[3](https://saturncloud.io/glossary/label-encoding/)] 

### Supervised Learning:

Neural Networks (CNNs), Support Vector Machines (SVMs) and OpenCV. The CNNs will be fine-tuned on our dataset to classify the images into human or AI-generated categories and further classify the human-made artworks into their respective styles. OpenCV allows us to easily implement feature extraction.[[4](https://www.geeksforgeeks.org/opencv-overview/)]

### Model Evaluation:
We will use metrics such as accuracy, precision, recall, and F1-score to evaluate our model. Additionally, we will employ cross-validation techniques to ensure the robustness and generalizability of our model.
Using these techniques, we want to create a model for classifying works as authentic or AI-generated. The project will allow us to understand how AI may transform art, and provide tools to help artists navigate this new landscape of digital art creation.

## Potential Results

There are two potential labels we are attempting to use to classify a given piece of artwork: AI-generated (Two classes) & style of art (Multiclass). The most distinctive features of these classifiers could help art curators better identify exactly what it is about an artwork. [[5](http://proceedings.mlr.press/v97/zhang19d.html)]
Additionally, a robust model that can determine whether an artwork is AI-generated could be beneficial to help clear confusion between fake artwork and authentic pieces. [[6](http://proceedings.mlr.press/v48/reed16.html)]
Our goal is to create a computer vision model that can accurately classify the creator of an artwork (human or machine) and identify the style of art that the artwork falls under.
We will use the following metrics to evaluate our model:
·  	Accuracy
·  	Precision
·  	Recall
·  	F1-Score

## References

[1] Otten, N. V. (2023, October 31). How to implement data augmentation in Python [Image & Text (NLP)]. Spot Intelligence. https://spotintelligence.com/2023/03/09/data-augmentation-python-image-text-nlp/#:~:text=Data%20augmentation%20is%20a%20technique%20used%20in,with%20different%20versions%20of%20the%20same%20information. 

[2] Feature extraction explained. Explained - MATLAB & Simulink. (n.d.). https://www.mathworks.com/discovery/feature-extraction.html#:~:text=What%20Is%20Feature%20Extraction%3F,directly%20to%20the%20raw%20data.

[3] Label encoding. Saturn Cloud. (2023, April 4). https://saturncloud.io/glossary/label-encoding/

[4] GeeksforGeeks. (2024, April 15). What is opencv library? https://www.geeksforgeeks.org/opencv-overview/

[5] Zhang, H., Goodfellow, I., Metaxas, D., & Odena, A. (2019). Self-attention generative adversarial networks. Proceedings of the 36th International Conference on Machine Learning, 7354-7363. http://proceedings.mlr.press/v97/zhang19d.html

[6] Reed, S. E., Akata, Z., Yan, X., Logeswaran, L., Schiele, B., & Lee, H. (2016). Generative adversarial text to image synthesis. Proceedings of the 33rd International Conference on Machine Learning, 1060-1069. http://proceedings.mlr.press/v48/reed16.html

[[Gnatt Chart](https://gtvault-my.sharepoint.com/:x:/g/personal/aahmed325_gatech_edu/EX_WzZorNqpOsYLy_TFPWeMBmku716cK_ZE9_tpJgMufSA?e=tWEBQl)]


| Name          | Proposal Contribution |
|---------------|-----------------------------------------------------------------------------------------------------------------------------|
| Zhixiang Yan  |set up github and hosting report, creating citation,find data processing method and refine the report, complete youtube video|
| Abdullah Ahmed|team lead, delegate task and complete introduction and problem definition section                                            |
|Jad Ahmed Helmy|complete method and potential result section                                                                                 |