# Final

Authors: Zhixiang Yan, Abdullah Ahmed, Jad Ahmed Helmy

## Introduction / Background

With the rise of generative AI models, we can generate artwork in a few seconds. These generated artworks challenge us to ask how they compare stylistically and formally, in terms of authenticity and coherence, to art created by humans during defined periods in art history. This project aims to use a dataset that contains a collection of human-generated artworks and a collection of AI-generated artworks[[dataset](https://www.kaggle.com/datasets/superpotato9/dalle-recognition-dataset?select=real)] to train a model to classify art as being created by a human or an artificial intelligence (AI) artist.

## Problem Definition

Given an image, our project aims to determine whether the art is AI-generated or human-create. A successful model would provide an effective tool for curation of art, digitization of art, and benchmarks towards transparency of AI content creation in the art market.

## Methods

### Data Cleanning

We use PIL libary to hash the image and then remove image that has the same hash which in turn remove all duplicate and similar image. and we reize the image to 256,256 and covert all image to RGB mode which ensures consistency within our dataset and help us achieve reliable results.[[1](https://emeritus.org/in/learn/data-science-data-cleaning/)]

### Data Reduction 

Since our the number of AI-genereated images outnumber the number of human-generated images, we use random sampling technique to reduce the number of AI-generated images to ensure equal representation.[[2](https://towardsdatascience.com/data-preprocessing-e2b0bed4c7fb)]

### Data Labeling

Label each image to create label dataset so that we can use supervise learnning method. [[3](https://aws.amazon.com/what-is/data-labeling/)] 

### Supervised Learning:

Neural Networks (CNNs), Support Vector Machines (SVMs) and OpenCV. The CNNs will be fine-tuned on our dataset to classify the images into human or AI-generated categories and further classify the human-made artworks into their respective styles. Random Forest Classifier helps our model by aggregating prediction from multiple decision trees to improve classification accuracy. OpenCV allows us to easily implement feature extraction.[[4](https://www.geeksforgeeks.org/opencv-overview/)]

### Model Evaluation:
We will use metrics such as accuracy, precision, recall, and F1-score to evaluate our model. Additionally, we will employ cross-validation techniques to ensure the robustness and generalizability of our model.
Using these techniques, we want to create a model for classifying works as authentic or AI-generated. The project will allow us to understand how AI may transform art, and provide tools to help artists navigate this new landscape of digital art creation.

## Potential Results

There are two potential labels we are attempting to use to classify a given piece of artwork: AI-generated (Two classes) & style of art (Multiclass). The most distinctive features of these classifiers could help art curators better identify exactly what it is about an artwork. [[5](http://proceedings.mlr.press/v97/zhang19d.html)]
Additionally, a robust model that can determine whether an artwork is AI-generated could be beneficial to help clear confusion between fake artwork and authentic pieces. [[6](http://proceedings.mlr.press/v48/reed16.html)]
Our goal is to create a computer vision model that can accurately classify the creator of an artwork (human or machine) and identify the style of art that the artwork falls under.
We will use the following metrics to evaluate our model:
·  	Accuracy
·  	Precision
·  	Recall
·  	F1-Score

## References

[1] Samarth, V. (2023, December 14). Why data cleaning is a significant step for accurate data analysis?. Emeritus India. https://emeritus.org/in/learn/data-science-data-cleaning/. 

[2] Singh, H. (2020, May 24). Data preprocessing. Medium. https://towardsdatascience.com/data-preprocessing-e2b0bed4c7fb 

[3] What is data labeling? - data labeling explained - AWS. (n.d.). https://aws.amazon.com/what-is/data-labeling/ 

[4] GeeksforGeeks. (2024, April 15). What is opencv library? https://www.geeksforgeeks.org/opencv-overview/

[5] Zhang, H., Goodfellow, I., Metaxas, D., & Odena, A. (2019). Self-attention generative adversarial networks. Proceedings of the 36th International Conference on Machine Learning, 7354-7363. http://proceedings.mlr.press/v97/zhang19d.html

[6] Reed, S. E., Akata, Z., Yan, X., Logeswaran, L., Schiele, B., & Lee, H. (2016). Generative adversarial text to image synthesis. Proceedings of the 33rd International Conference on Machine Learning, 1060-1069. http://proceedings.mlr.press/v48/reed16.html

[[Gnatt Chart](https://gtvault-my.sharepoint.com/:x:/g/personal/aahmed325_gatech_edu/EX_WzZorNqpOsYLy_TFPWeMBmku716cK_ZE9_tpJgMufSA?e=tWEBQl)]


| Name          | Final Contribution |
|---------------|-----------------------------------------------------------------------------------------------------------------------------|
| Zhixiang Yan  |Complete three data preprocessing method, complete data sourcing, complete a supervised learning models,complete proposal presentation            |
| Abdullah Ahmed|complete introduction and problem definition and complete result analysis and model selection                                 |
|Jad Ahmed Helmy|Complete Final Presentation and two supervised learning models                                                          |

We change our origin dataset becuase it was not suitable for what we want to implement and change all three preprocessing method to accommodating that