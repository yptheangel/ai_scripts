#!/usr/bin/env python
# coding: utf-8

# # Create train and test split for image dataset
# Folder structure is targeted towards Deeplearning4j's Image DatasetIterator, tf.keras's ImageGenerator, Pytorch's ImageFolder and fastai.

# ### Why this?
# Online tutorials mostly do the split on the fly before going for training. In my opinion, it's not very practical. Yes, you can reproduce the train test split using a random seed, but imagine if you want to switch and compare the results between different deep learning frameworks.
# 
# Then this script will be useful for you to presplit the image dataset to train and test splits.


import os
import numpy as np
from shutil import copyfile
import os.path as osp
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--folder", type=str, default="None")
parser.add_argument("-t", "--train", type=int, default=80)
args = parser.parse_args()
print("Your dataset folder: {}".format(args.folder))
print("Your train split percentage over full dataset: {}".format(args.train))

dataset_folder = args.folder
train = args.train

# Why convert to set type? set does not allow duplicates, you can perform operations between 2 sets and it is faster than list
# Set random seed if you wan reproduce results of your random sampling, but most of the time.. No

# rng_seed = 000
# np.random.seed(rng_seed)
for root, dirs, files in os.walk(dataset_folder, topdown=False):
    if (len(root)) > (len(dataset_folder)):
        filelist=np.asarray(files)
        
        train_split_num= int((train / 100) * len(filelist))
        shuffled=np.random.choice(filelist,train_split_num,replace=False)
        trainSplit=set(shuffled)
        fullDataset=set(filelist)
        testSplit = fullDataset.difference(trainSplit)
        print("Label: {}, Total train images: {}, Total test images: {}".format(osp.basename(root), len(trainSplit), len(testSplit)))
                      
        trainSplit=list(trainSplit)
        testSplit=list(testSplit)
        
        dst = osp.join("train",osp.basename(root))
        os.makedirs(dst,exist_ok=False)
        for img in trainSplit:          
            copyfile(osp.join(root,img), osp.join(dst,img))
            
        dst = osp.join("test",osp.basename(root))
        os.makedirs(dst,exist_ok=False)
        for img in testSplit:          
            copyfile(osp.join(root,img), osp.join(dst,img))

