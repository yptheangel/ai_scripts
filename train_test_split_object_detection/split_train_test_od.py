#!/usr/bin/env python
# coding: utf-8

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
images=[]
for root, dirs, files in os.walk(dataset_folder, topdown=False):
    for file in files:
        if file.endswith(".jpg"):
            images.append(file)
    filelist=np.asarray(images)
    train_split_num= int((train / 100) * len(filelist))
    shuffled=np.random.choice(filelist,train_split_num,replace=False)
    trainSplit=set(shuffled)
    fullDataset=set(filelist)
    testSplit = fullDataset.difference(trainSplit)
    print(f"Total train images: {len(trainSplit)}, Total test images: {len(testSplit)}")
                    
    trainSplit=list(trainSplit)
    testSplit=list(testSplit)
    
    dst = osp.join("train")
    os.makedirs(dst,exist_ok=False)
    for img in trainSplit:          
        copyfile(osp.join(root,img), osp.join(dst,img))
        copyfile(osp.join(root,img[:-4]+".xml"), osp.join(dst,img[:-4]+".xml"))
        
    dst = osp.join("test")
    os.makedirs(dst,exist_ok=False)
    for img in testSplit:          
        copyfile(osp.join(root,img), osp.join(dst,img))
        copyfile(osp.join(root,img[:-4]+".xml"), osp.join(dst,img[:-4]+".xml"))
