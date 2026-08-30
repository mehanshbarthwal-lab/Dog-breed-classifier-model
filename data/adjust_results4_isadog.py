#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def adjust_results4_isadog(results_dic, dogfile):
    dognames_dic = {}
    with open(dogfile, 'r') as f:
        for line in f:
            name = line.rstrip('\n')
            if name not in dognames_dic:
                dognames_dic[name] = 1

    for filename in results_dic:
        pet_label = results_dic[filename][0]
        classifier_label = results_dic[filename][1]

        # Check if pet label is a dog
        is_pet_dog = 1 if pet_label in dognames_dic else 0

        # Check if classifier label is a dog
        # Classifier labels might contain multiple comma-separated terms
        is_classifier_dog = 0
        classifier_terms = [term.strip() for term in classifier_label.split(',')]
        for term in classifier_terms:
            if term in dognames_dic:
                is_classifier_dog = 1
                break

        results_dic[filename].extend([is_pet_dog, is_classifier_dog])
