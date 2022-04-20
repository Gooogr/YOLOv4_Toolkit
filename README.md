<p align="center">
  <img width="400" src="https://raw.githubusercontent.com/Gooogr/YOLO_Toolkit/master/page_cover.png">
</p>

This toolkit was designed for fast and easy training of YOLO v4 and Tiny YOLO v4 neural networks on the Google Colab GPU. In the beginning you only have to specify  the classes from the ImageNetV4 dataset and the samples amount. After that, script will automatically  prepare dataset, setting up framework and create most of necessary files.<br>

Toolkit covers the following stages:
* [Train_yolov4_imagenet.ipynb](https://github.com/Gooogr/YOLO_Toolkit/blob/master/Train_yolov4_imagenet.ipynb):
  * Automatic data set formation
  * Darknet files preparations and model training
* [Predict_yolov4.ipynb](https://github.com/Gooogr/YOLO_Toolkit/blob/master/Predict_yolov4.ipynb):
  * Prediction generating

The training set of Imagenet V4 contains 14.6M bounding boxes for 600 object classes on 1.74M images<br>
[Dataset description](https://storage.googleapis.com/openimages/web/factsfigures_v4.html) - Overview of Open Images V4<br>
[Available image classes](https://storage.googleapis.com/openimages/2018_04/bbox_labels_600_hierarchy_visualizer/circle.html) - Classes hystoram<br>

### How to start with it
Follow this link to start in playground mode [Train_yolov4_imagenet.ipynb](https://colab.research.google.com/github/Gooogr/YOLO_Toolkit/blob/imagenet/Train_yolov4_imagenet.ipynb)<br>

Could be useful:<br>
[External data: Local Files, Drive, Sheets, and Cloud Storage](https://colab.research.google.com/notebooks/io.ipynb#scrollTo=eikfzi8ZT_rW) - How to upload your external data to Google Colab notebook <br>
[Connection pushers](https://stackoverflow.com/questions/57113226/how-to-prevent-google-colab-from-disconnecting) - How to prevent Google Colab from disconnect during the training.

## Acknowledgments
[Darknet](https://github.com/AlexeyAB/darknet) - AlexeyAB's version of the Darknet framework <br>
[OIDv4_ToolKit](https://github.com/theAIGuysCode/OIDv4_ToolKit) - ImagenetV4 dataset downloader <br>
[tensorflow-yolov4-tflite](https://github.com/hunglc007/tensorflow-yolov4-tflite) - Weights converter

