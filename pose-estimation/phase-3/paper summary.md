paper:  visual understanding to 6d pose reconstruction:
- CNN, Resnet and DGCNN to extract features
- from rgb images, rgb-d images or point cloud data.
- paper analyzes these methods based on diff input data types focusing on rgb images, rgb-d 
- provides detailed summary of implementation methods, advantages & disadvantages and problem these methods aim to solve.

> [!NOTE]
> depending on different modalities of the input data, 
>  the implementations, application domains, training paradigms, network architectures, and their strengths and weaknesses of the deep learning-based object position estimation methods is highlighted.


## Introduction:
early research focuseed on geometric methods
and feature point matching.(rely on correspondance b/w image and model to compute pose)

application: industrial automation, augmented reality, and human computer interaction.

system applies pose estin tech to analayze and understand orientation of ojbect in space.
then align virtual objects with real world objects.

traditional methods for object pose estimation correspond the extracted feature points to the feature points in 3d model and pnp algorithm to solve for the cooridinates of target under camera coordinate system.
  

>[!NOTE]
>map object contour in 2d image and 3d model to compute object pose.
>edge and contour based use edge detection algo to extract edges then match edge with projecgtions of 3d model.
>(have advantages in dealiwth with local features geometric transformation)
>but complexity and dependence on cad model.

>[!Note]
>based on whether res use objects cad model we classify object pose into
>instance level ope
>category level ope(estimate pose without need for object models)


high quality training data provies rich feature inforn and reduces noise and bias.
paper also explores reln b/w data quality and model performance.

ways to optimize data:
data preprocessing
data augmentation
shape deformation teh

## papers contribution:
* high impact cv paper on dl-object pose estn 
* 2 main direction (instance, categoy and unseen/articlate)
* sumary of dataset. and analysis.
* esisting challenges in field and future development diren of objects.



2 methods:
1. instance level  object pose estimation methods
		  - based on rgb images
			* coordinate correspondance based methods
			* feature based methods
			* tempate based methods
		   - based on rgb-d images
			* voting based or refinement methods
			* direct regression based methods
		* based on depth or point cloud data


2. category-level  object pose estimation methods.


# Instance level object pose estimation:

 use cnn, ResNet, DGCNN
TO extract features from rgb images , rgb-d, point cloud data.
implementation/advantages/disadvantes/problems they solve.

## RGB-BASED input image methods:

rgb contains rich color and texture info  which facilitates network to extract coarse and fine features of image and enhance networks perception.
- 
#### Coordinate correspondence-based methods:
![[Pasted image 20250904214018.png]]
ccbo maps b/w 2d images and 3d space.
(dense or sparse correspondance)
by training deep network to predict 3d spatial location of pixel points in image.
target pose is computed using RANSAC and PnP algo.

#### pix2pose:
2019
pose est for poorly textured objects
by mappin b/w coordinates.
utilizes codec structure to extract coarse and delicate features.
uses jump connection during decoding 

#### PVNET
method for occlusions or truncation of objects in a image.
pixel-level vectors pointing to keypoints
allows network 
doesn't propose a method to deal with symmetric objects.


#### Hybrid-pose algorithm
intermediate feature prediction network and a pose regression network
not only uses keypoints as intermediate representations but incorporates edge vectors and symmetry correspondance to capture richer geometric info.

- designs an optimization submodule that uses gm robust norms to enhance robustness of estiamtion.
- practical me: requires generating keypiont and symmetry labels and providing segmentation templts and pvnet data.


#### NERF pose:
REPRESENTS objects 3d shape and color as implicity function and optimizing it via multi-view image training.
due to this robust in processing complex scenes.
volume rendering required resources.


##### SOPOSE:
enhances representation by self-obscuration info
and a two layer observer centered representation structure.
doubt:

The first layer deals with the correspondence between visible points and their projections, and the second layer utilizes a self-attention mechanism [29] to gen- erate a self-obscuring perceptual map to integrate the occlusion in- formation
doubt: 
SO-Pose introduces a cross-layer consistency loss term to align the self-obscuring, the correspondence field, and the 6D pose to improve the accuracy and robustness of the pose estima- tion. H

##### Efficient pose:
balances computational efficiency with performance by scaling depth, width, and resolution.
it adds sub-networks to efficientNet.
to predict object rotation and translation to recover rotation and translation information.
utilizes: pose loss and feature loss.

##### CosyPose:
reconstructs before regressiong.
generates pose hypotheses from a single view then matches these hypotheses across different images to jiontly estimae camerea viewpoint and ojbect pose.
uses shared encoder and 2 seperarte decoder to predict self-occlusion info and 2d-3d point correspondences.
###### improved single view and multi-view 6d pose estimation on YCB video and T-LESS datasets.


##### DPOD
focuses more on estimating and refining the pose of individual objects using deep learning to compute 6d posees throught 2d-3d correspondence maps.
- uses online data generation, background enhancement. 
- ##### creates a bidirectional mapping through correspondence texture mapping.

#### CheckerPose

improves matching accuracy of corresponding ponits in 2d images by sampling critical points on surface of 3d objects using GNN.



#### feature-based methods:


![[Pasted image 20250904214032.png]]

classical and widely used technique (utilizes pre-defined object templates)





#### template-based methods

![[Pasted image 20250904214052.png]]


#### vitPose

#### OSOP
#### PoseRBPF

#### GSPOSE

## pose estimation of unseen objects and articulated objects


## data and evaluation :
	1. datasets
	2. metrics
	3. data optimization


## Datasets:
datasets having different pose changes, complex backgrounds , occlusions and noise

## Instance level dataset:

1. linemod dataset
	- Standardized benchmark dataset for task of object pose estimation.
	- covering 15 common everyday objects.
	- each of which has 3d model , rgb-d images from multiple viewpoints.
	- partially occluded objects , complex backgrounds.
	- unified benchmark for comparision and evaluation of algos.
	-
2. occlusion lineMod: 
     - extension of linemod, designed for occlusion.
     - 8 classes.
     
3. T-less:
	- task of pose estimation of untextured industrial objects 
	- 20 obj
	- rgb-d imaeg data
	- diff lightining condition
	- higly symmetric 
	- weakly textured
	- good for industrial setups
	
4. YCB-video
	- 21 obj
	- from ycb(yale, cmu, berkley) objects and models set
	- caputres multi-view pose changes of obj in a variety of backgrounds, lightning conditions and occlusions.
	
 

## Category level:
1. CAMERA25:
	- used for training and evaluation of synthetic data.
	- synthetic images: 25obj.
	- initial training
2. real275
	- 275 3d object models of diff classes.
	- multi-view images and corresponding real 5d object poselabels 
	
3. Wild6D
	- pose estimation of unlabeled obj in ral world scenes.
	- lareg number of ral images : capture multiple views of objets.
	- 

## Unseen object datasets:
1. OnePose: large amount of robot data, through AR tools, (robots center position, dimensions around z-axis, rotation angle, camera pose information, dataset contains high resolution images take from multiple viewpoints also, reconstruced sparse point clouds and 2d keypoints)

2. MOPED:
	designed specifically for multi-object pose estimation tasks.
	rgb and depth image data.
	 detailed annotation information : (object location, pose and category labels)
3. SAPIEN :
 for 6d object estimation and scene understanding.
 

## Metrics:
1. average distance
2. translation error
3. rotation error
4. intersection over union
5. maximum symmetry aware surface distance
6. Average Recall
7. VSD
8. MSSD
9. MSPD


Note: category level approaches focus more on evaluating translational and angular errors.







## New concepts:

