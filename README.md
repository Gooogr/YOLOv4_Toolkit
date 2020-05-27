# YOLO_toolkit
Toolkit for training custom YOLOv3 models in [Google Colab](
https://drive.google.com/open?id=1gTMES2Aj4NeNEK9YzjNdEmGEcItGsvxj).<br>

This toolkit is designed for fast learning of YOLO and Tiny YOLO neural networks, starting from data collection and up to the trained model with custom weights.

## How to create your dataset
**First way - use Open Images Dataset**

Follow [OpenImagesV4Loader.ipynb](https://github.com/Gooogr/YOLO_toolkit/blob/master/1\)OpenImagesV4Loader.ipynb)

**Second way - Kaggle dataset. Or whatever.**

There are plenty of object detection datasets on [Kaggle](https://www.kaggle.com/search?q=tag%3A%22object+detection%22+in%3Adatasets).
Some of them are ready to go with YOLO algorithms, some of them not. In this case, you will most probably face with VOC labels in XML files. You can use VOC to YOLO converter:
```
python3 VOC2YOLODatasetConverter.py -d path_to_your_VOC_dataset -c name_of_classes_that_you_need
```
By default, class indexes start with 0. You can correct labels in TXT files with the help of this script:
```
ReplaceSubStringInFile.py
```
## How to train your model
Follow [TrainCustomYOLOweights.ipynb](https://github.com/Gooogr/YOLO_toolkit/blob/master/2\)TrainCustomYOLOweights.ipynb)

### How to configure darknet files for training

**cfg files**
Links to original YOLO cfg files:
* [Tiny YOLOv3](https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov3-tiny-prn.cfg)
* [YOLOv3](https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov3.cfg)

How to configure them:
* Comment/uncomment train/test part for specifying *batch* and *subdivisions* parameters
* Minimum *maxbatches* = number_of_your_classes * 2000. Of course you can use a bigger values
* *steps* = *maxbatches* * 0.8, *maxbatches* * 0.9
* *classes* = number_of_your_classes
* *filters* = 3 * (*classes*+5)

**obj.names**

Write labels in the same way as in the classes.txt file. One class - one line. If you make a mistake in the order of the labels, the algorithm will work, but will incorrectly name the detected objects.

**yolo.data**

Specify classes amount. Check pathes to other files but they should be right by default:
valid = /mydrive/YOLO_toolkit/test.txt
names = /mydrive/YOLO_toolkit/obj.names
backup = /mydrive/YOLO_toolkit/yolo_weights
train = /mydrive/YOLO_toolkit/train.txt
