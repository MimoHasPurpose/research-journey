### paper : challenges for monocular 6-d object pose estimation

main website: [BOP](https://bop.felk.cvut.cz/home/)
bop paper: [link](https://arxiv.org/pdf/1808.08319)

- common datasets
- survey of robot specific challenges
### datasets:

1. TUD-L: [link](https://bop.felk.cvut.cz/datasets/#TUD-L) three moving objects under eight lighting conditions.

2. IC-BIN:  [link 1. ](https://bop.felk.cvut.cz/datasets/#IC-BIN)[link 2. ](https://rkouskou.gitlab.io/research/6D_NBV.html)  images of two objects from IC-MI, in multiple locations with heavy occlusion , bin-picking scenario.

3. Homebrewed-Database [link 1.](https://bop.felk.cvut.cz/datasets/#HB) 33 objects (17 toy, 8 household and 8 industry-relevant objects) captured in 13 scenes 
	-  The dataset 
		- Primesense Carmine 1.09 
		-  Microsoft Kinect 2. 
   

4. HOPE: [link ](https://bop.felk.cvut.cz/datasets/#HOPE) NVIDIA Household Objects for Pose Estimation)
	 28 toy grocery objects , 50 scenes from 10 household/office environments. 
	 Up to 5 lighting variations are captured for each scene
	  - including backlighting 
	  - angled direct lighting with cast shadows.
	   Scenes are cluttered with varying levels of occlusion.

5.  T-LESS: [link](https://bop.felk.cvut.cz/datasets/#T-LESS)
	- 30 industry-relevant objects with no significant texture or discriminative color.
	- The objects exhibit symmetries and mutual similarities in shape and/or size, and a few objects are a composition of other objects.
	
6. ITODD [link](https://bop.felk.cvut.cz/datasets/#ITODD)
	- 28 objects captured in realistic industrial setups with a high-quality Gray-D sensor.

	

7. MP6D [link](https://ieeexplore.ieee.org/document/9722997)

	 - 6D pose estimation of Metal Parts in industrial environments. 
	 - The dataset consists of 20 metal parts made of aluminum alloy material which are commonly used in factories.
	 - first dataset of metal parts with simultaneous multi-target, occluded, and illumination changes.
	 - The color homogeneity, textureless and light-reflecting properties raise great challenges for estimating the pose of the objects.

8. ClearPose: [link](https://arxiv.org/pdf/2203.03890): 
	- Transparent objects are ubiquitous in household settings and
	- pose distinct challenges for visual sensing and perception systems.
	- The optical properties of transparent objects leave conventional 3D sensors
	    alone unreliable for object depth and pose estimation. 
	- large-scale real-world RGB-Depth transparent object dataset
		dataset contains over 350K labeled real-world RGB-Depth frames and 5M instance annotations covering 63 household objects.commonly used in daily life under various lighting and occluding conditions as well as challenging test scenarios
	
9.  NOCS: [link](https://geometry.stanford.edu/projects/NOCS_CVPR2019/):  
	- To handle different and unseen object instances in a given category, we introduce Normalized Object Coordinate Space (NOCS)—a shared canonical representation for all possible object instances within a category. 
	- region-based neural network is then trained to directly infer the correspondence from observed pixels to this shared object representation (NOCS) along with other object information such as class label and instance mask. These predictions can be combined with the depth map to jointly estimate the metric 6D pose and dimensions of multiple objects in a cluttered scene. 
10. PhoCal: [link](https://arxiv.org/pdf/2205.08811):
	-  mul-timodal dataset for category-level object pose estimation
		with photometrically challenging objects 
	- PhoCaL comprises 60 high quality 3D models of household
		objects over 8 categories including highly reflective, trans-
		parent and symmetric objects. 
11. DREDS: [link. ](https://arxiv.org/pdf/2208.03792)
	- large-scale synthetic dataset that contains 130K photorealistic RGB im-
		ages along with their simulated depths carrying realistic sensor noises. 
	- To evaluate depth restoration methods, a real-world dataset,
		STD,  30 cluttered scenes composed of 50 ob-
		jects with different materials from specular, transparent, to diffuse. 
	
12. KeyPose: [link](https://sites.google.com/view/keypose/)
	 - 15 clear objects in 5 classes, with 48k 3D-keypoint labeled images. 
	 
13. TransCG: [link](https://arxiv.org/pdf/2202.08471) 
	-  a large-scale real-world
		dataset for transparent object depth completion
	-  contains 57,715 RGB-D images from 130 different scenes. 
		first large-scale, real-world dataset that provides ground
		truth depth, surface normals, transparent masks in diverse and
		cluttered scenes. 
	-  The full dataset at: [link](www.graspnet.net/transcg.)

14. HouseCat6d: [link](https://sites.google.com/view/housecat6d)
	-  addresses annotation quality and pose variety
	
15. GraspNet/SuctionNet-1 billion:

	-  [graspnet website]( https://graspnet.net/publications.html)
	-  dataset has scenes, models, densePointClouds, seal-label, wrench-label, suction collision label and each scene folder has objects id, rs_wrt_kn.npy, kinect folder having( rgb image, depth, label, annotations, meta, rect) camera inrinsics, camera_poses, camwrttable (camera pose wrt to table), realsense folder same as kinect.
	-  [paper](https://openaccess.thecvf.com/content_CVPR_2020/papers/Fang_GraspNet-1Billion_A_Large-Scale_Benchmark_for_General_Object_Grasping_CVPR_2020_paper.pdf)


## Ongoing research problems:
1.
2.
3.
4.
5.
6.
7.
8.
9.
11.
12.

## Ongoing research problems:
1. refinement: iterative refinement approach is used
2. symmetry handling: easy to handle with template based approaches
	- finding semantically important object locations that enable direct grasping.
3. category level training: 
4. novel objects: instance and category level dont generalize so solution for novel objects is a research problem. solution via, support view, template matching, foundational models. future research would be finding view of novel objects without template matching.
5. challenging material properties: 


## Future challenges
1. object ontology
2. deformable and articulated objects
3. scene level consistency
4. benchmark realism
5. environmental impact
6. generalist object manipulation


---


