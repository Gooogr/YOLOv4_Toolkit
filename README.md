<p align="center">
  <img width="400" src="https://raw.githubusercontent.com/Gooogr/YOLO_Toolkit/master/page_cover.png">
</p>

This toolkit was designed for fast and easy training of YOLO v4 and Tiny YOLO v4 neural networks on the Google Colab GPU. In the beginning you only have to specify  the classes from the ImageNetV4 dataset and the samples amount. After that, script will automatically  prepare dataset, setting up framework and create most of necessary files.<br>

Toolkit covers the following stages:
* Automatic data set formation
* Darknet files preparations and model training
* Prediction generating
* Converting Darknet model to the TensorFlow format (in process)
* Providing minimal usage example with TensorFlow (in process)

The training set of V4 contains 14.6M bounding boxes for 600 object classes on 1.74M images<br>
[Dataset description](https://storage.googleapis.com/openimages/web/factsfigures_v4.html) - Overview of Open Images V4<br>
[Available image classes](https://storage.googleapis.com/openimages/2018_04/bbox_labels_600_hierarchy_visualizer/circle.html) - Classes hystoram<br>

### How to start with it
Follow this link to start in playground mode [Train_yolov4_imagenet.ipynb](https://colab.research.google.com/github/Gooogr/YOLO_Toolkit/blob/imagenet/Train_yolov4_imagenet.ipynb)<br>

## Acknowledgments
[AlexeyAB, darknet](https://github.com/AlexeyAB/darknet)<br>
[OIDv4_ToolKit](https://github.com/theAIGuysCode/OIDv4_ToolKit)<br>

