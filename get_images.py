import urllib.request
import cv2
import numpy as np
import os

NEG_IMG_SIZE = (100, 100)
NEG_IMG_FILEPATH = 'negative_images'
UNCLEAN_IMG_FILEPATH = 'unclean_images'

# took 4694.201s to run store_raw_images() with link
# 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'
# 844 total images
# [Finished in 4694.201s]
def store_raw_images():
    neg_images_link = 'http://image-net.org/' + \
                      'api/text/imagenet.synset.geturls?wnid=n00523513'
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()

    if (not os.path.exists(NEG_IMG_FILEPATH)):
        os.makedirs(NEG_IMG_FILEPATH)

    picture_num = 1

    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            filename = NEG_IMG_FILEPATH + '/' + str(picture_num) + '.jpg'
            urllib.request.urlretrieve(i, filename)
            img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img, NEG_IMG_SIZE)
            cv2.imwrite(filename, resized_image)
            picture_num += 1

        except Exception as e:
            print(str(e))

def find_bad_images():
    for file_type in [NEG_IMG_FILEPATH]:
        for img in os.listdir(file_type):
            for unclean in os.listdir(UNCLEAN_IMG_FILEPATH):
                try:
                    current_img_path = str(file_type) + '/' + str(img)
                    unclean = cv2.imread(UNCLEAN_IMG_FILEPATH + '/' + \
                              str(unclean))
                    current_img = cv2.imread(current_img_path)

                    if (unclean.shape == current_img.shape) and \
                       not(np.bitwise_xor(unclean, current_img).any()):
                        print('Unclean data:', current_img_path)
                        os.remove(current_img_path)

                except Exception as e:
                    print(str(e))

def create_pos_and_neg_imgs():
    for file in [NEG_IMG_FILEPATH]:
        for img in os.listdir(file):
            if file == NEG_IMG_FILEPATH:
                line = file + '/' + img + '\n'
                with open('bg.txt', 'a') as f:
                    f.write(line)

# store_raw_images()
# find_bad_images()
create_pos_and_neg_imgs()
