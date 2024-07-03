import numpy as np
import os
from PIL import Image
class Data_labeling:
    def __init__(self):
        self.output_images_array = []
        self.label = []
    
    # Labeling the images
    # input_image_directory: path to the directory containing images
    # label: the label of the images, eg: we can label 'ai' as 0 and 'human' as 1
    # return: images array of size N * D and its label array of size N
    def labeling(self, input_image_directory, label):
        for image in os.listdir(input_image_directory):
            image_path = os.path.join(input_image_directory, image)
            image = Image.open(image_path)
            image_array = np.array(image)
            self.output_images_array.append(image_array)
            self.label.append(label)
            print(image_array)
        return np.array(self.output_images_array), np.array(self.label)

ai_data_labeling = Data_labeling()
ai_images, ai_label = ai_data_labeling.labeling('ai_generated_images/', 0)
human_data_labeling = Data_labeling()
human_images, human_label = human_data_labeling.labeling('human_generated_images/', 1)
print(ai_images.shape) #(2999, 256, 256, 3)
print(ai_label.shape) #(2999,)
print(human_images.shape)#(2999, 256, 256, 3)
print(human_label.shape)#(2999,)
np.save('ai_images.npy', ai_images)
np.save('ai_label.npy', ai_label)
np.save('human_images.npy', human_images)
np.save('human_label.npy', human_label)
