# Autonomous Car Camera Semantic Segmentation

This repository is an adapted version of https://github.com/aakaashjois/Autonomous-Car-Camera-Segmentation used in the task of semantic segmentation for my final year project in Data Science and Analytics.

## Dataset
The dataset used in this project consists of RGB images collected from the CARLA simulator and their corresponding semantically labelled images which act as the 'ground truth'.

## Training procedure
Two loss functions were explored, a Tversky Dice weighted cross entropy and a weighted cross entropy loss (the weights correspond to the inverse frequency of the class label).
  
## Results
### Tversky Dice Weighted Cross Entropy
Training Metrics:
![](./misc/TverskyDice/accuracy_loss.png)
Original Images:
![](./misc/TverskyDice/test-set.png)
Original Masks:
![](./misc/TverskyDice/actuals.png)
Predicted Masks:
![](./misc/TverskyDice/preds.png)

### Weighted Cross Entropy
Training Metrics:
![](./misc/CE/accloss.png)
Original Images:
![](./misc/CE/rgbs.png)
Original Masks:
![](./misc/CE/actuals.png)
Predicted Masks:
![](./misc/CE/preds.png)