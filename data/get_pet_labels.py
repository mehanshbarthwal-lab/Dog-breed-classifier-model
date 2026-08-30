#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import listdir

def get_pet_labels(image_dir):
    results_dic = {}

    filename_list = listdir(image_dir)

    for filename in filename_list:
        if filename.startswith('.'):
            continue

        pet_label = ''
        word_list_lower = filename.lower().split('_')

        for word in word_list_lower:
            if word.isalpha():
                pet_label += word + ' '

        pet_label = pet_label.strip()

        if filename not in results_dic:
            results_dic[filename] = [pet_label]

    return results_dic
