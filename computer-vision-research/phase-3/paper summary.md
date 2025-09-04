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

rgb contains rich color and texture info  which facilitates network to extract coarse and fine features of image+
#### Coordinate correspondence-based methods:

ccbo maps b/w 2d images and 3d space.
(dense or sparse correspondance)



#### feature-based methods:





#### template-based methods





## pose estimation of unseen objects and articulated objects


## data and evaluation :
	1. datasets
	2. metrics
	3. data optimization


## Datasets:
datasets having different pose changes, complex backgrounds , occlusions and noise

## Instance level dataset:

1. linemod dataset
2. occlusion lineMod
3. T-less
4. YCB-video
5. 

## Category level:
1. CAMERA25
2. real275
3. Wild6D


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
10. 

Note: category level approaches focus more on evaluating translational and angular errors.







## New concepts:

