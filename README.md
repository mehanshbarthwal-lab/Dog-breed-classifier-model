# Dog Breed Classifier Using a Pre-trained CNN

## Overview
This project uses three pre-trained CNN architectures (ResNet, AlexNet, VGG) to classify pet images: it identifies whether an image is a dog or not, and if it is, predicts the breed. The goal is to find which architecture balances accuracy and speed best.

## Objectives
1. Correctly classify images as dog or not-dog.
2. Correctly identify the dog breed.
3. Compare runtime across architectures.

## Repository Structure

| File / Directory | Purpose |
|---|---|
| check_images.py | Main script. Wires all functions together, measures runtime. |
| get_input_args.py | Parses --dir, --arch, --dogfile command-line arguments. |
| get_pet_labels.py | Extracts ground-truth labels from image filenames. |
| classify_images.py | Calls the classifier and compares its output to the ground-truth label. |
| djust_results4_isadog.py | Flags each result as dog or not-dog using dognames.txt. |
| calculates_results_stats.py | Computes match percentages and counts. |
| print_results.py | Prints the summary and any misclassified cases. |
| classifier.py | **PROVIDED, NOT MODIFIED.** Pre-trained CNN wrapper (ResNet-18, AlexNet, VGG-16). |
| 	est_classifier.py | Provided smoke test for classifier.py. |
| dognames.txt | List of dog breed names used for dog/not-dog labelling. |
| data/pet_images/ | 40 evaluation images (30 dogs, 10 non-dogs). |
| data/uploaded_images/ | Custom images for supplemental evaluation. |

## Pipeline
1. Parse arguments.
2. Extract pet labels from filenames.
3. Run images through the CNN classifier.
4. Flag each label as dog or not-dog against dognames.txt.
5. Compute statistics.
6. Print results and runtime.

## Requirements
Python 3 with:
- 	orch
- 	orchvision
- Pillow

## How to Run
Run from the data/ directory.

`bash
# Default (VGG)
python check_images.py

# ResNet
python check_images.py --dir pet_images/ --arch resnet --dogfile dognames.txt

# AlexNet
python check_images.py --dir pet_images/ --arch alexnet --dogfile dognames.txt

# VGG
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
`

Replace pet_images/ with uploaded_images/ to run against the custom images.

## Results on pet_images (40 images)

| Model | % Correct Dogs | % Correct Breed | % Correct Not-Dogs | Runtime |
|---|---:|---:|---:|---:|
| VGG | 100.0% | 93.3% | 100.0% | 0:0:10 |
| AlexNet | 100.0% | 80.0% | 100.0% | 0:0:2 |
| ResNet | 100.0% | 90.0% | 90.0% | 0:0:4 |

VGG scored highest on breed accuracy (93.3%) and correctly separated dogs from non-dogs at 100%. AlexNet ran fastest at 2 seconds but dropped to 80% breed accuracy. ResNet sits in between on speed but missed 10% of non-dog images. VGG is the best overall pick when accuracy matters more than speed.

## Uploaded Image Results

Four custom images were tested: Dog_01.jpg, Dog_02.jpg, Frog_01.jpg, Coffee_mug_01.jpg.

1. **Breed for Dog_01**: All three architectures predicted golden retriever.
2. **Dog_02 vs Dog_01 consistency**: All three predicted golden retriever for Dog_02 as well.
3. **Non-dog images**: The frog was labelled 	ree frog, tree-frog and the coffee mug was labelled cup across all three models. Neither label appears in dognames.txt, so all three correctly classified them as not-dogs.
4. **Best architecture on uploaded images**: All three agreed on every prediction. AlexNet is the practical choice here because it finished fastest.

## Output Files

| File | Contents |
|---|---|
| data/resnet_pet-images.txt | ResNet terminal output on pet_images/ |
| data/alexnet_pet-images.txt | AlexNet terminal output on pet_images/ |
| data/vgg_pet-images.txt | VGG terminal output on pet_images/ |
| data/resnet_uploaded-images.txt | ResNet terminal output on uploaded_images/ |
| data/alexnet_uploaded-images.txt | AlexNet terminal output on uploaded_images/ |
| data/vgg_uploaded-images.txt | VGG terminal output on uploaded_images/ |

## Testing
All three models were run end-to-end on both image directories. Output was captured to the files above and statistics were verified against the expected project values.

## Author
Mehansh Barthwal
