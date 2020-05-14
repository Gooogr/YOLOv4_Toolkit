# YOLO_toolkit
Toolkit for training custom YOLOv3 models in Google Colab.

Links to original YOLO cfg files:
* [Tiny YOLOv3](https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov3-tiny-prn.cfg)
* [YOLOv3](https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov3.cfg)
How to configure them:
* Comment/uncomment train/test part for specifying *batch* and *subdivisions* parameters
* Minimum *maxbatches* = number_of_your_classes * 2000. Of course you can use a bigger values
* *steps* = *maxbatches* * 0.8, maxbatches* * 0.9
* *classes* = number_of_your_classes
* filters* = 3*(*classes*+5)

