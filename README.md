# Useful scripts for Computer Vision
Collection of useful and practical scripts used for Computer Vision

1. Presplit Image Classification Dataset to train and test split. 
<br>Suitable for DL4J's Image DatasetIterator, Pytorch's ImageFolder, tf.keras's ImageGenerator and fastai ImageDataBunch.from_folder.
<br>Do not rely on sklearn or DL framework's splitter and shuffler. 

2. Presplit  Object Detection dataset
<br>Supports Pascal VOC, randomly samples and copies the images and annotation files(.xml).
<br>Modify accordingly for your own scenario
