# Dog Breed Classifier Using a Pre-trained CNN

## Project Overview
This project uses a provided pre-trained image classifier to identify whether an image contains a dog or not, and if it does, it predicts the dog's breed. The project compares the performance of three different Convolutional Neural Network (CNN) architectures—ResNet, AlexNet, and VGG—by evaluating their accuracy and runtime on a dataset of pet images.

## Project Objectives
The main classification objectives are:
1. **Correct Dog vs. Not-Dog Identification**: Accurately classifying whether an image is a dog or a non-dog entity.
2. **Correct Dog-Breed Identification**: Accurately identifying the specific breed of the dog.

An additional consideration for evaluating the models is **runtime** efficiency, balancing the trade-off between computational speed and classification accuracy.

## Repository Structure
- \check_images.py\: The main script that wires all functions together, tracks runtime, and drives the entire classification pipeline.
- \get_input_args.py\: Parses command-line arguments including the image directory, CNN architecture, and the dog names file.
- \get_pet_labels.py\: Extracts the true identity of the pets from the filenames in the image directory to create the ground truth labels.
- \classify_images.py\: Uses the provided classifier to label the images and compares the predictions against the true labels.
- \djust_results4_isadog.py\: Adjusts the results dictionary to indicate whether the true label and the classifier's label correspond to a dog or a non-dog.
- \calculates_results_stats.py\: Computes the final statistics (counts and percentages) for matches, correct dogs, correct non-dogs, and correct breeds.
- \print_results.py\: Outputs a formatted summary of the statistics and conditionally lists incorrectly classified dogs or breeds.
- \classifier.py\: **(PROVIDED — NOT MODIFIED)** The pre-trained image classifier module that wraps PyTorch's pre-trained CNN models.
- \	est_classifier.py\: A provided testing script to verify the basic functionality of \classifier.py\.
- \dognames.txt\: A text file containing a comprehensive list of dog breeds used to determine if a label corresponds to a dog.
- \data/pet_images/\: The primary dataset containing 40 images (30 dogs, 10 non-dogs) used for evaluating the models.
- \data/uploaded_images/\: A directory intended for custom uploaded images for further model evaluation.

## How It Works
The processing pipeline operates in the following sequence:
1. Parse command line arguments.
2. Extract ground truth **pet labels** from the image filenames.
3. Pass images through the **CNN classifier** to get predictions.
4. Perform **dog/not-dog classification** by comparing labels against the known dog names dictionary.
5. Calculate comprehensive **statistics** (percentages and counts).
6. Output **printed results** and total elapsed runtime.

## Requirements / Environment
This project requires a Python 3 environment. The dependencies identified based on the implementation of the pre-trained classifier and core logic are:
- \	orch\ (PyTorch)
- \	orchvision\
- \Pillow\ (PIL)

## How to Run
To run the classifier on the primary dataset, use the following commands from the \data/\ directory:

**Default run (defaults to VGG):**
\\\ash
python check_images.py
\\\

**ResNet:**
\\\ash
python check_images.py --dir pet_images/ --arch resnet --dogfile dognames.txt
\\\

**AlexNet:**
\\\ash
python check_images.py --dir pet_images/ --arch alexnet --dogfile dognames.txt
\\\

**VGG:**
\\\ash
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
\\\

*Note: Equivalent commands for \uploaded_images/\ follow the same structure (e.g., \python check_images.py --dir uploaded_images/ --arch resnet --dogfile dognames.txt\).*

## Results
The actual results obtained from running the three architectures on the 40 provided images in \pet_images/\ are as follows:

| Model   | % Correct Dogs | % Correct Breed | % Correct Not-Dogs | Runtime |
|---------|---------------:|----------------:|-------------------:|--------:|
| VGG     | 100.0%         | 93.3%           | 100.0%             | 0:0:10  |
| AlexNet | 100.0%         | 80.0%           | 100.0%             | 0:0:2   |
| ResNet  | 100.0%         | 90.0%           | 90.0%              | 0:0:4   |

*VGG achieved the highest accuracy across all metrics, perfectly classifying dogs and non-dogs while maintaining a 93.3% breed accuracy. AlexNet was the fastest but had the lowest breed accuracy. ResNet performed well but struggled slightly with the non-dog classification (90.0%). Overall, VGG is the best performing model for this dataset, despite the slightly longer runtime.*

## Uploaded Image Results
Based on the newly provided four custom images (\Dog_01.jpg\, \Dog_02.jpg\, \Frog_01.jpg\, \Coffee_mug_01.jpg\), here are the findings:

1. **Did all three architectures agree on the breed for Dog_01?**
   Yes. ResNet, AlexNet, and VGG all classified \Dog_01.jpg\ as a \golden retriever\.

2. **Did each architecture classify Dog_02 as the same breed it gave Dog_01?**
   Yes. All three models also classified \Dog_02.jpg\ as a \golden retriever\, remaining perfectly consistent despite any image manipulation.

3. **Did all three correctly identify the animal image and object image as not-dogs?**
   Yes. All three models identified the frog as a \	ree frog, tree-frog\ and the coffee mug as a \cup\. Neither of these terms are in the dog names list, so all models scored 100% for correct not-a-dog classification.

4. **Which architecture performed best on the uploaded images and why?**
   All three architectures performed identically well on the uploaded images, achieving 100% accuracy on the dog/not-dog classification and agreeing precisely on the specific classes (\golden retriever\, \	ree frog\, and \cup\). Since their accuracy was completely tied, **AlexNet** could be considered the best for this specific tiny batch purely because it has the fastest runtime.

## Output Files
The repository contains raw output files capturing the complete terminal outputs from the actual model runs:
- \data/resnet_pet-images.txt\: Captured output of the ResNet model on the pet images.
- \data/alexnet_pet-images.txt\: Captured output of the AlexNet model on the pet images.
- \data/vgg_pet-images.txt\: Captured output of the VGG model on the pet images.
- \data/resnet_uploaded-images.txt\: Captured output of the ResNet model on the uploaded images.
- \data/alexnet_uploaded-images.txt\: Captured output of the AlexNet model on the uploaded images.
- \data/vgg_uploaded-images.txt\: Captured output of the VGG model on the uploaded images.

## Testing
The following checks were executed to validate the project:
- Tested dependencies and the \classifier.py\ component to verify PyTorch inference execution.
- Extracted exact text outputs by executing all three models against the \pet_images\ folder end-to-end to ensure the pipeline executes without error and correctly computes statistics.

## Author
Mehansh Barthwal
