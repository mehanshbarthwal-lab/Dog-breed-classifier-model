# Final Results Summary

## Model Performance on Pet Images

Based on the actual executions of the three CNN architectures on the 40 images in the \pet_images/\ dataset, the results are as follows:

| Model   | % Correct Dogs | % Correct Breed | % Correct Not-Dogs | Runtime |
|---------|---------------:|----------------:|-------------------:|--------:|
| VGG     | 100.0%         | 93.3%           | 100.0%             | 0:0:10  |
| AlexNet | 100.0%         | 80.0%           | 100.0%             | 0:0:2   |
| ResNet  | 100.0%         | 90.0%           | 90.0%              | 0:0:4   |

## Overall Model Recommendation

When considering dog/not-dog accuracy, breed accuracy, and runtime, **VGG** is the recommended model for this classification task. 

While VGG took the longest to run (10 seconds compared to AlexNet's 2 seconds and ResNet's 4 seconds), it was the only model to achieve 100% accuracy in both dog and not-a-dog identification while simultaneously delivering the highest breed accuracy (93.3%). AlexNet was the fastest but suffered a significant drop in breed accuracy (80.0%). ResNet struggled slightly with non-dog images, achieving only 90.0% in that category. For a classification task where accuracy is prioritized, VGG's superior performance across all three metric categories justifies its marginally longer runtime.

## Uploaded Image Questions
Based on the newly provided four custom images, here are the findings:

1. **Breed agreement for Dog_01:**
   ResNet, AlexNet, and VGG all classified \Dog_01.jpg\ as a \golden retriever\. They were in 100% agreement.

2. **Consistency between Dog_01 and Dog_02:**
   All three models classified \Dog_02.jpg\ as a \golden retriever\. They were perfectly consistent with their predictions for Dog_01.

3. **Correct not-dog identification:**
   Yes. All three models identified the frog as a \	ree frog, tree-frog\ and the coffee mug as a \cup\. Because these terms are not in the dog names list, all models successfully identified them as not-dogs.

4. **Best performing architecture on uploaded images:**
   All three architectures performed identically well on the uploaded images, achieving 100% accuracy on dog/not-dog classifications and agreeing exactly on the breeds and objects. Since accuracy is tied, **AlexNet** is the best choice for this specific subset simply because it is the fastest.
