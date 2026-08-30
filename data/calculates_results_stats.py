#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calculates_results_stats(results_dic):
    results_stats_dic = {}

    n_images = len(results_dic)
    n_dogs_img = 0
    n_notdogs_img = 0
    n_match = 0
    n_correct_dogs = 0
    n_correct_notdogs = 0
    n_correct_breed = 0

    for filename in results_dic:
        if results_dic[filename][2] == 1:
            n_match += 1
            if results_dic[filename][3] == 1:
                n_correct_breed += 1

        if results_dic[filename][3] == 1:
            n_dogs_img += 1
            if results_dic[filename][4] == 1:
                n_correct_dogs += 1
        else:
            n_notdogs_img += 1
            if results_dic[filename][4] == 0:
                n_correct_notdogs += 1

    results_stats_dic['n_images'] = n_images
    results_stats_dic['n_dogs_img'] = n_dogs_img
    results_stats_dic['n_notdogs_img'] = n_notdogs_img
    results_stats_dic['n_match'] = n_match
    results_stats_dic['n_correct_dogs'] = n_correct_dogs
    results_stats_dic['n_correct_notdogs'] = n_correct_notdogs
    results_stats_dic['n_correct_breed'] = n_correct_breed

    results_stats_dic['pct_match'] = (n_match / n_images) * 100.0 if n_images > 0 else 0.0
    results_stats_dic['pct_correct_dogs'] = (n_correct_dogs / n_dogs_img) * 100.0 if n_dogs_img > 0 else 0.0
    results_stats_dic['pct_correct_breed'] = (n_correct_breed / n_dogs_img) * 100.0 if n_dogs_img > 0 else 0.0
    results_stats_dic['pct_correct_notdogs'] = (n_correct_notdogs / n_notdogs_img) * 100.0 if n_notdogs_img > 0 else 0.0

    return results_stats_dic
