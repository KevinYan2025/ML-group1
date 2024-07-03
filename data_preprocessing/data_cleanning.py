import os
from PIL import Image,UnidentifiedImageError
from PIL.Image import DecompressionBombError
import imagehash

class Data_cleanning:
    def __init__(self):
    # Initialize instance variables here
        self.image_count = 0
    def get_image_hash(self,image_file_path):
        """
        Get image hash using phash algorithem from ImageHash library
        :param image_path: path to the image
        :return: image hash
        """
        image = Image.open(image_file_path)
        return imagehash.phash(image)
    def resize_image(self,image_path):
        """
        Resize the image to 256,256
        :param image_path: path to the image
        """
        image = Image.open(image_path)
        image = image.resize((256, 256))
        # Convert image to RGB if it's not
        if image.mode != 'RGB':
            image = image.convert('RGB')
        image.save(image_path)

    def remove_duplicated_image(self,image_directory_path):
        """
        Remove duplicated images from the directory
        :param image_directory: path to the directory containing images
        """
        #store all vistied image hash
        image_hash_dict = {}
        for image_name in os.listdir(image_directory_path):
            image_path = os.path.join(image_directory_path, image_name)
            try:
                #remove the image if it is not jpg
                if not image_name.endswith('.jpg'):
                    os.remove(image_path)
                    print(f"Removed image {image_path}")
                    print(f'checking image number {self.image_count} ')
                    self.image_count += 1
                else:
                    self.resize_image(image_path)

                    image_hash = self.get_image_hash(image_path)
                    print(f'checking image number {self.image_count} ')
                    self.image_count += 1
                    #remove the image if it is similar to other iamge' hash
                    if image_hash in image_hash_dict:
                        os.remove(image_path)
                        print(f"Removed duplicate image {image_path}")
                    else:
                        image_hash_dict[image_hash] = image_path
            except DecompressionBombError:
                # if the image is too larget to hash we can simply remove it
                print(f"DecompressionBombError: {image_path}")
                os.remove(image_path)
                print(f"Removed image {image_path}")
            except UnidentifiedImageError:
                # if the image is not valid image we can simply remove it
                print(f"UnidentifiedImageError: {image_path}")
                os.remove(image_path)
                print(f"Removed image {image_path}")


data_cleanning = Data_cleanning()
data_cleanning.remove_duplicated_image('ai_generated_images/')
data_cleanning.remove_duplicated_image('human_generated_images/')