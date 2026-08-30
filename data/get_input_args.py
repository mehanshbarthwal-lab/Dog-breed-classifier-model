#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

def get_input_args():
    parser = argparse.ArgumentParser(description='Get input arguments for the dog breed classifier')
    parser.add_argument('--dir', type=str, default='pet_images/', help='Path to the folder of pet images')
    parser.add_argument('--arch', type=str, default='vgg', help='CNN Model Architecture')
    parser.add_argument('--dogfile', type=str, default='dognames.txt', help='Text file with dog names')
    return parser.parse_args()
