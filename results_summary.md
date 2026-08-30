# Final Results Summary

## Pet Images (40 images)

| Model | % Correct Dogs | % Correct Breed | % Correct Not-Dogs | Runtime |
|---|---:|---:|---:|---:|
| VGG | 100.0% | 93.3% | 100.0% | 0:0:10 |
| AlexNet | 100.0% | 80.0% | 100.0% | 0:0:2 |
| ResNet | 100.0% | 90.0% | 90.0% | 0:0:4 |

## Recommended Model: VGG

VGG is the strongest overall. It scored 100% on dog/not-dog identification and 93.3% on breed accuracy, the highest of all three. It took 10 seconds versus AlexNet's 2 and ResNet's 4, but that trade-off is worth it when breed accuracy is the priority. AlexNet ran fastest but dropped to 80% breed accuracy. ResNet fell to 90% on non-dog images, which is a meaningful miss for that category.

## Uploaded Images (4 images)

Images tested: Dog_01.jpg, Dog_02.jpg, Frog_01.jpg, Coffee_mug_01.jpg.

1. **Breed for Dog_01**: ResNet, AlexNet, and VGG all predicted golden retriever.
2. **Dog_02 consistency**: All three predicted golden retriever, matching Dog_01.
3. **Non-dog identification**: The frog was labelled 	ree frog, tree-frog and the mug was labelled cup by all three architectures. Neither term is in dognames.txt, so all three correctly scored them as not-dogs.
4. **Best architecture on uploaded images**: All three agreed on every prediction. AlexNet is the practical pick because it finished in 0 seconds versus VGG's 2.
