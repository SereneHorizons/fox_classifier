import urllib.request
import cv2
import numpy as np
import os

def create_neg_bg():
    for file in ['../negatives']:
        for img in os.listdir(file):
            line = 'negatives/' + img + '\n'
            with open('bg_5000.txt', 'a') as f:
                f.write(line)

def resize_files():
    for file in ['../negatives']:
        for img in os.listdir(file):
            line = 'negatives/' + img + '\n'
            with open('bg_5000.txt', 'a') as f:
                f.write(line)
