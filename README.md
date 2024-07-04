# Project Title
Given an image, our project aims to determine whether the art is AI-generated or human-created. A successful model would provide an effective tool for curation of art, digitization of art, and benchmarks towards transparency of AI content creation in the art market.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

python 12    
git 

### Installing

A step by step series of examples that tell you how to get a development environment running.  

1. Clone the repository     
git clone https://github.com/KevinYan2025/ML-group1.git   
2. Navigate to the project directory    
cd yourprojectdirectory   
3. Create a virtual environment on Mac    
python3 -m venv venv --prompt="env-name"   
4. Activate the virtual environment   
replace venv with your env-name    
On Mac/Linux: source venv/bin/activate    
On Windows: venv\Scripts\activate    
  
5. Install the required packages   
pip install ImageHash    
pip install notebook  

6. Create .gitignore file  
git ignore env-name  ai_generated_images   human_generated_images  

## Description

- **`/data_preprocessing/`**: This directory contain all the data preprocessing method    
- **`/data_preprocessing/data_reduction.py`**: This file using random sampling to reduce the number of image in our dataset, which help us to balance the number AI-generated images and the number human-generated images by randomly selecting certain number of AI-genereated to improve performance of our model     
- **`/data_preprocessing/data_cleanning.py`**: This file allow us to remove duplication or similar image by using  PIL libary to hash the image. we also remove all the image that are not jpg format to improve model performance. it also resize all image to 256,256 and RGB mode to ensure all images is consistent      
- **`/data_preprocessing/data_labeling.py`**: This file will convert all image to numpy array and label it with value and which output ai_images.npy,ai_label.npy,human_images.npy,human_label.npy      
- **`/ai_images.npy`**: this file contain the preprocessed ai generated image as numpy array     
- **`/ai_label.npy`**: This file contain the preprocessed ai generated image label as numpy array    
- **`/human_images.npy`**: This file contain the preprocessed human generated image as numpy array    
- **`/human_label.npy`**: this file contain the preprocessed human generated image label as numpy array   
- **`/notebook.ipynb`**: this is jupyter notebook that can be use to run our data preprocessing and train the model



## Deployment

Add additional notes about how to deploy this on a live system.

## Built With

* [Python](https://www.python.org/) - The programming language used.

## Contributing

Please read [CONTRIBUTING.md](https://yourprojectlink/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://yourprojectlink/tags).

## Authors

* **Zhixiang Yan** - *Initial work* - [kevinYan2025](https://github.com/KevinYan2025)

See also the list of [contributors](https://yourprojectlink/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments