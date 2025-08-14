# posenet:

## Introduction:

We present a robust and real-time monocular six de gree of freedom relocalization system

Our system trains a convolutional neural network to regress the 6-DOF cam era pose from a single RGB image in an end-to-end man ner with no need of additional engineering or graph op timisation.

We show that the PoseNet localizes from high level features and is robust to difficult lighting, motion blur and different camera intrinsics where point based SIFT reg istration fails.

This pa per addresses the lost or kidnapped robot problem by intro ducing a novel relocalization algorithm

Our proposed sys tem, PoseNet, takes a single 224x224 RGB image and re gresses the camera’s 6-DoF pose relative to a scene

Our main contribution is the deep convolutional neural network camera pose regressor.

Our second main contribution is towards understanding the representations that this convnet generates. We show that the system learns to compute feature vectors which are easily mapped to pose, and which also generalize to unseen scenes with a few additional training samples

Simultaneous localization and mapping (SLAM) is a traditional solution to this problem. We introduce a new framework for localization which removes several issues faced by typical SLAM pipelines, such as the need to store densely spaced keyframes, the need to maintain sep arate mechanisms for appearance-based localization and landmark-based pose estimation, and a need to establish frame-to-frame feature correspondence.

## Related work

There are generally two approaches to localization: met ric and appearance-based. Metric SLAM localizes a mobile robot by focusing on creating a sparse [13, 11] or dense [16, 7] map of the environment. Metric SLAM estimates the camera’s continuous pose, given a good initial pose es timate. Appearance-based localization provides this coarse estimate by classifying the scene among a limited number of discrete locations

## Model for deep regression of camera pose

In this section we describe the convolutional neural net work (convnet) we train to estimate camera pose directly from a monocular image, I. Our network outputs a pose vector p, given by a 3D camera position x and orientation represented by quaternion q:

**p =[x,q]**

![](https://r2.noteddy.com/images/620d9030-1fa6-4c1c-94b3-6d7029d80a07.png)

Where isascale factor chosen to keep the expected value of position and orientation errors to be approximately equal.

We found that training individual networks to regress position and orientation separately performed poorly com pared to when they were trained with full 6-DOF pose la bels (f

## Architectecture:

GoogLeNet is a 22 layer convolutional net work with six ‘inception modules’ and two additional in termediate classifiers which are discarded at test time. Our model is a slightly modified version of GoogLeNet with 23 layers (counting only the layers with trainable parameters)

- Replace all three softmax classifiers with affine regres sors. The softmax layers were removed and each final fully connected layer was modified to output a pose vector of 7-dimensions representing position (3) and orientation (4).
    
- Insert another fully connected layer before the final re gressor of feature size 2048. This was to form a local ization feature vector which may then be explored for generalisation.
    
- At test time we also normalize the quaternion orienta tion vector to unit length.
    

It was trained using stochastic gradient de scent with a base learning rate of 10 5, reduced by 90% every 80 epochs and with momentum of 0.9. Using one half of a dual-GPU card (NVidia Titan Black), training took an hour using a batch size of 75. For reasons of time, we did not explore multi-GPU training, although it is reason able to expect better results from using double the through put and memory. We subtracted a separate image mean for each scene as we found this to improve experimental per formance

--

We show that PoseNet is able to effectively localize across both the indoor 7 Scenes dataset and outdoor Cam bridge Landmarks dataset

## Importance of transfer learning:

n general convnets require large amounts of training data. We sidestep this problem by starting our pose train ing from a network pretrained on giant datasets such as Im ageNet and Places.

t-SNE [26] is an algorithm for embedding high dimensional data in a low dimensional space, in a way that tries to preserve Euclidean distances.

- Fig. 13 compares system performance of PoseNet on a modern desktop computer. Our network is very scalable, as it only takes 50 MB to store the weights, and 5ms to com
    

pute each pose, compared to the gigabytes and minutes for metric localization with SIFT. These values are independent of the number of training samples in the system while met ric localization scales O(n2) with training data size

- We have demonstrated that one can sidestep the need for millions of training images by use of transfer learning from networks trained as classifiers. We showed that such networks preserve ample pose informa tion in their feature vectors, despite being trained to produce pose-invariant outputs. Our method tolerates large baselines that cause SIFT-based localizers to fail sharply.
    

- In future work, we aim to pursue further uses of mul tiview geometry as a source of training data for deep pose regressors, and explore probabilistic extensions to this algo rithm [12]. It is obvious that a finite neural network has an upper bound on the physical area that it can learn to localize within.