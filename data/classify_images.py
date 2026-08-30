#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from classifier import classifier
import os

def classify_images(images_dir, results_dic, model):
    for filename in results_dic:
        full_path = os.path.join(images_dir, filename)

        classifier_label = classifier(full_path, model)
        classifier_label = classifier_label.lower().strip()

        pet_label = results_dic[filename][0]

        if pet_label in classifier_label:
            results_dic[filename].extend([classifier_label, 1])
        else:
            results_dic[filename].extend([classifier_label, 0])
