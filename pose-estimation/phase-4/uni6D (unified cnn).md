# Summary:
- SOTA approaches use different backbones to extract features for RGB and depth iamges. its done by using 2dcnn for rgb images, per pixel point cloud network for depth data and fusion network for feature fusion.
- reason for using 2 independent backbones is projection breakdown.
- depth image planes the 3d structure of physical world is preserved by 1d depth value and its built in 3d pixel coorinate (uv).
- ### Problem:
- spatial transformation (resize, flip, crop or pooling) that modifies UV, breaks the binding between pixel coordinate and uv coordinate. so 3d structure is no longer preserved by modified depth image or feature.
- real time and practical
- ### SOLUTION:
- UNI6D: explicitly takes extra UV data along with RGB-D images as input.
	D+UV-> 3d data(d,u,v) (self complete information)
- architecture is based on mask r-cnn with 2 extra heads (RT head (6d pose) and abc head (guiding network to map visible points to their coordinate in 3d model as  an auxilary module))

### where is 6d pose estimation used? 
 autonomous driving, intelligent robotic grasping, augmented reality.
data collected via RGB-D sensors.
reason we cant use single backbone lies in 3d vision projection equaltion.
 problem: spatial transformations (pooling, crop and RoI-Align) change the UV.
 and when these spatial transformations are applied to depth imae projection equation is broken.
### what was new in paper? 
1. projection problem
2. uv data to fix pp 
3. so single cnn backbone is all u need for feature extraction in rgb-d IMAGES.
4. ABC and RT method
5. experimental and ablation studies.

#  Methodology:
 masked R-CNN performs object detection , instance segmentation with parallel multi head networks.
 and RT head predict r,t and abc head does the mapping to visible points.




## Similar methods:
1. holistic methods
2. keypoint based approaches 
3. dense correspondence methods
  - used for rgb only pose estimation.
  - performance is limited by loss of geometry information.
  - so came point cloud methods.


## Results:
95.2 AUC of ADDS-0.1 on YCB video dataset 



## pre-requisites:
### Questions:
1. what does it do?
2. how does it do?
3. is it better? than who?
4. what is uv?
5. how is training done and on what?
6. how did they design the single backbone?
7. how are they using point cloud data.
.