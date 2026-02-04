# pvnet:

- works under severe occlusion or truncation.
    
- occlusion: blockage
    
- truncation: shorten
    
- recent approach : 2 stage : detect keypoints then solves a pnp problem. for pose estimation.
    
- pixel vise voting network.
    
    - ==what are keypoints?==
        
    - ==wha is pnp problem and algorithm?==
        
- to regress pixel-wise unit vectors pointing to the keypoints and use these vectors to vote for keypoint locations using RANSAC
    
- **==what is RANSAC?==**
    
- **==pixel-wise unit vectors?==**
    
- This creates a flexible representation for localizing occluded or truncated keypoints.
    
- Another important feature of this representation is that it provides uncertainties of keypoint locations that can be further leveraged by the PnP solver.
    
- Experiments show that the proposed approach outperforms the state of the art on the LINEMOD, Occlusion LINEMOD and YCB-Video datasets by a large margin, while being efficient for real-time pose estimation
    
- . We further create a ==Truncation LINEMOD dataset to validate the robustness of our approach against truncation.==
    

## Introduction:

- Object pose estimation aims to detect objects and esti mate their orientations and translations relative to a canon ical frame
    
- ==what is orientation and translation ?==
    
- ==what is canonical form?==
    
- recent methods use cnn to regress 2d keypoints, and compute 6d pose parameers using pnp algorithm.
    

- ![](https://r2.noteddy.com/images/e5fb684c-e4b8-4c15-9f06-eb04cb4aaad3.png)
    
- nstead of directly regressing image coordinates of keypoints, **PVNet predicts unit vectors that represent directions from each pixel of the object towards the keypoints.** **These directions then vote for the keypoint locations based on RANSAC [12]**
    
- This voting scheme is motivated from a property of rigid objects that once we see some local parts, we are able to infer the relative directions to other parts.
    
- We propose a novel framework for 6D pose estimation using a pixel-wise voting network (PVNet), which l**earns a vector-field representation for robust 2D key point localization and naturally deals with occlusion and truncation.**
    
- We propose to utilize an uncertainty-driven PnP algorithm to account for uncertainties in 2D keypoint local izations, based on the dense predictions from PVNet.
    
- We demonstrate significant performance improvements of our approach compared to the state of the art on benchmark datasets (ADD: 86.3% vs. 79% and 40.8% vs. 30.4% on LINEMOD and OCCLUSION, respectively). We also create a new dataset for evaluation on truncated objects.
    

## Related work:

Instead of directly obtaining the pose from an image, **keypoint-based methods adopt a two-stage pipeline: they first predict 2D keypoints of the object and then compute the pose through 2D-3D correspondences with a PnP algorithm.**


## Proposed approach:

- Specifically, 6D pose is represented by a rigid transformation (R;t) from the object coordinate system to the camera coordinate system, where R represents
    
    the 3D rotation and t represents the 3D translation
    
- we estimate the object pose using a two-stage pipeline: we first de tect 2D object keypoints using CNNs and then compute 6D pose parameters using the PnP algorithm. **Our innovation is in a new representation for 2D object keypoints as well as a modified PnP algorithm for pose estimation.**
    
- Specifically, our method uses a Pixel-wise Voting Network (PVNet) to detect 2D keypoints in a RANSAC-like fashion, which robustly handles occluded and truncated objects. The RANSAC-based voting also gives a spatial probability dis tribution of each keypoint, allowing us to estimate the 6D pose with an uncertainty-driven PnP.
    

### **voting based keypoint localization:**

PVNet predicts pixel wise object labels and unit vectors that represent the direc tion from every pixel to every keypoint.

Given the direc tions to a certain object keypoint from all pixels belong ing to that object, we generate hypotheses of 2D locations for that keypoint as well as the confidence scores through RANSAC-based voting

. Based on these hypotheses, we es timate the mean and covariance of the spatial probability distribution for each keypoint.

More specifically, PVNet performs two tasks: seman tic segmentation and vector-field prediction. For a pixel p, PVNet outputs the semantic label that associates it with a specific object and the unit vector vk(p) that represents the direction from the pixel p to a 2D keypoint xk of the object. The vector vk(p) is defined as

![](https://r2.noteddy.com/images/0e90b306-e298-4ec6-9342-6240ced33bfa.png)

Specifically, the voting score wk, i of a hypothesis hk i is defined as

some

![](https://r2.noteddy.com/images/51da5f47-461f-4f98-9d0d-6d8001bc2462.png)

### **voting based keypoint localization:**

### Uncertainity driven PnP:

## Implementation details:

We use a **pretrained ResNet-18 [**16] as the backbone network, and we make three revisions on it. First, when the **feature map of the network has the size H8 W8, we do not downsample the feature map anymore by discarding the subsequent pooling layers.**

Second, t**o keep the receptive fields unchanged, the subsequent convolutions are replaced with suitable dilated convolutions** [45].

Third, the fully connected layers in the original ResNet-18 are replaced with **convolution layers**. Then, we repeatedly perform skip con nection, convolution and upsampling on the feature map, until its size reaches H W, as shown in Figure 2(b)

![](https://r2.noteddy.com/images/11b10a7a-f695-42a4-a06c-87041cb6a029.png)

- We implement hypothesis generation, pixel-wise voting and density estimation using CUDA. The EPnP [24] used to initialize the pose is implemented in OpenCV [5]. To obtain the final pose, we use the iterative solver Ceres [1] to mini mize the Mahalanobis distance (5). For symmetric objects, there are ambiguities of keypoint locations. To eliminate the ambiguities, we rotate the symmetric object to a canonical pose during training, as suggested by [33]
    

## Training:

![](https://r2.noteddy.com/images/3fb1e631-eeda-48df-a9ea-3d7500e52561.png)

- where w represents the parameters of PVNet, vk is the pre dicted vector, vk is the ground truth unit vector, and vkx and vky represent the two elements of vk, respec tively. For training semantic labels, a softmax cross-entropy loss is adopted. Note that during testing, we do not need the predicted vectors to be unit because the subsequent processing uses only the directions of the vectors.
    

To prevent overfitting, we add synthetic images to the training set. For each object, we render 10000 images whose viewpoints are uniformly sampled. We further syn thesize another 10000 images using the “Cut and Paste” strategy proposed in [10]. The background of each synthetic image is randomly sampled fromSUN397[44]. Wealsoap ply online data augmentation including random cropping, resizing, rotation and color jittering during training. We set the initial learning rate as 0.001 and halve it every 20 epochs. All models are trained for 200 epochs

## Experiments:

1. Datasets:
    
    - LINMOD
        
    - Occlusion LINE
        
    - truncation LINEMOD
        
    - YCB-Video
        

**metrics**: 2d projection metric and average 3d distance of model points (add) metric.

Ablation studies We conduct ablation studies to compare different key point detection methods, keypoint selection schemes, num bers of keypoints and PnP algorithms, on the Occlusion LINEMODdataset. Table 1 summarizes the results of abla tion studies.

## Conclusion:


## Doubts:
vector field representations and voting
- world frame
- camera frame
- image frame
- pixel frame
- canonical frame
- RANSAC: **ANSAC (RANdom SAmple Consensus) is an iterative outlier detection algorithm.** Its goal is to find the best fit for data that's full of noise or errors. For this, it picks random samples, makes a mathematical model, and checks how many points fit that model. The model with the most good fits is chosen as the best solution.
- See how the line fitting would have been impacted negatively if we had to consider the red points as part of our equation.

So this is the point of RANSAC: to find **outliers**, and more importantly: **inliers**.

1. **Start** with the input data
2. **Pick** random samples
3. **Fit** a mathematical model (line, curve, 3d shape, ...)
4. **Compute** a cost by checking how many points fit the model
5. **Repeat** until you found the model with the lowest cost
![[Pasted image 20250813140643.png]]


**MSAC** (M-estimator SAmple Consensus)

Now let's see...
- PNP algorithm

![[Pasted image 20250813133732.png]]


![[Pasted image 20250813133813.png]]

![[Pasted image 20250813133832.png]]
![[Pasted image 20250813141644.png]]
![[Pasted image 20250813141756.png]]

## Conclusion:

- Given a 480 640 image, our method runs at 25 fps on a desktop with an Intel i7 3.7GHz CPU and a GTX 1080 Ti GPU, which is efficient for real-time pose estima tion. Specifically, our implementation takes 10.9 ms for data loading, 3.3 ms for network forward propagation, 22.8 ms for the RANSAC-based voting scheme, and 3.1 ms for the uncertainty-driven PnP.
## main idea: 

PVNet predicts unit vectors that represent directions from each pixel of the object towards the keypoints. **These directions then vote for the keypoint locations based on RANSAC [12]**
- [Perspective-n-Point: P3P](https://jingnanshi.com/blog/pnp_minimal.html)
- [The Ultimate Guide to the RANSAC Algorithm](https://www.thinkautonomous.ai/blog/ransac-algorithm/)
- [Camera Conventions, Transforms, and Conversions](https://blog.mkari.de/posts/cam-transform/)
- [lecture12.pdf](https://www.cse.psu.edu/~rtc12/CSE486/lecture12.pdf)
- [CS6320 3D Computer Vision](https://www.sci.utah.edu/~gerig/CS6320-S2015/CS6320_3D_Computer_Vision.html)



