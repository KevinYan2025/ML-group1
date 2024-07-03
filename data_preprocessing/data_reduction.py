import numpy as np
import os
class Data_reduction:
    def __init__(self, sampling_size):
        self.sampling_size = sampling_size
    
    def random_sampling(self, dataset_path):
        """
        Randomly sample the data, and delete the rest of the iamges in the dataset
        :param dataset_path: path to the dataset to be sampled

        """
        #get all image in the dataset
        images = os.listdir(dataset_path)
        #if the number of images is less than the sampling size, return
        print(len(images))
        if len(images) <= self.sampling_size:
            print("The number of images is less than the sampling size")
            return
        sampled_images = np.random.choice(images, self.sampling_size, replace=False)
        sampled_images_set = set(sampled_images)
        for image in images:
            if image not in sampled_images_set:
                print(f"Removed image {image}")
                os.remove(os.path.join(dataset_path, image))
        print(f"Finished sampling {dataset_path}")
        
    
    
# Data_reduction = Data_reduction(200)
# Data_reduction.random_sampling('ai_generated_images/')
# Data_reduction.random_sampling('human_generated_images/')