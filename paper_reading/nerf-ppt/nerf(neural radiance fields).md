[tiny-nerf-code](https://colab.research.google.com/github/bmild/nerf/blob/master/tiny_nerf.ipynb)


![[78472235-d1010d80-7769-11ea-9be9-51365180e063.gif]]
## 1/10 
### prerequisites
* world coordinate frame
* camera coordinate frame
* coordinate transformation
* projective transformation

## 2/10
### previous work and dataset

## 3/10
### broad views
## 4/10
### marching camera rays through the scene
**Input**: A set of camera poses {xc,yc,zc,γc,θc}n{xc​,yc​,zc​,γc​,θc​}n​

**Output**: A bundle of rays for every pose {vo,vd}H×W×n{vo​,vd​}H×W×n​


![[Pasted image 20250827100702.png]]
![[Pasted image 20250827100727.png]]
## 5/10
### collecting query points

**Input**: A bundle of rays for every pose {vo,vd}H×W×n{vo​,vd​}H×W×n​

**Output**: A set of 3D query points {xp,yp,zp}n×m×H×W{xp​,yp​,zp​}n×m×H×W​

![[Pasted image 20250827100751.png]]
## 6/10
### projecting query points to high dimensional space

**Input**: A set of 3D query points {xp,yp,zp}n×m×H×W{xp​,yp​,zp​}n×m×H×W​

**Output**: A set of query points embedded into dd-dimensional space {x1,x2,...,xd}n×m×H×W{x1​,x2​,...,xd​}n×m×H×W​
## 7/10
### neural network inference and volume rendering

#### nn inference:

**Input** A set of 3D query points (after positional encoding) {x1,x2,...,xd}n×m×H×W{x1​,x2​,...,xd​}n×m×H×W​

**Output** RGB colour and volume density for every query point {RGB,σ}n×m×H×W{RGB,σ}n×m×H×W​


#### volume rendering
**Input** A set of 3D query points (after positional encoding) + their volume profile + RGB value {x1,x2,...,xd,RGB,σ}n×m×H×W{x1​,x2​,...,xd​,RGB,σ}n×m×H×W​

**Output** A set of rendered images (one per pose) {H,W}n{H,W}n
## 8/10
### computing the loss
**Input** A set of rendered images (one per pose) {H,W}n{H,W}n​ and a set of ground truth images (one per pose) {H,W}ngt{H,W}ngt​

**Output** L2 loss between the inputs, a single scalar {l}n{l}n​
![[Pasted image 20250827101016.png]]
![[Pasted image 20250827101033.png]]


![[6p4i6y.gif]]
## 9/10
## 10/10


references:
1. [original nerf paper](https://arxiv.org/pdf/2003.08934)
2. [Deep Dive into NeRF (Neural Radiance Fields)](https://dtransposed.github.io/blog/2022/08/06/NeRF/)
3. [Computer Graphics and Deep Learning with NeRF using TensorFlow and Keras: Part 1 - PyImageSearch](https://pyimagesearch.com/2021/11/10/computer-graphics-and-deep-learning-with-nerf-using-tensorflow-and-keras-part-1/)
4. [NeRF Part 1. Prerequisite: Theory | by M(A)C | Medium](https://medium.com/@chengmu/nerf-part-1-prerequisite-theory-1d5395389f99)
5. [NeRF Part 2. Paper Details. This is my study note for this… | by M(A)C | Medium](https://medium.com/@chengmu/nerf-part-2-paper-details-65cb4b2d899a)
6. [NeRF in 2023: Theory and Practice - It-Jim](https://www.it-jim.com/blog/nerf-in-2023-theory-and-practice/)**
7. [A Beginner’s 12-Step Visual Guide to Understanding NeRF: Neural Radiance Fields for Scene Representation and View Synthesis | by Aqeel Anwar | TDS Archive | Medium](https://medium.com/data-science/a-12-step-visual-guide-to-understanding-nerf-representing-scenes-as-neural-radiance-fields-24a36aef909a)
8. [Creating Full Body Deepfakes by Combining Multiple NeRFs - Unite.AI](https://www.unite.ai/creating-full-body-deepfakes-by-combining-multiple-nerfs/)**
9. [Paper Summary: “BlockNeRF: Scalable Large Scene Neural View Synthesis” | Document My Data Science Journey](https://riven314.github.io/alexlauwh314/paper/computer-graphics/2022/03/06/BlockNeRF.html)
10. [38  Representing Images and Geometry – Foundations of Computer Vision](https://visionbook.mit.edu/homogeneous_coordinates.html)
11. https://developer.nvidia.com/blog/getting-started-with-nvidia-instant-nerfs/

implementation: 
12. [NVlabs/instant-ngp: Instant neural graphics primitives: lightning fast NeRF and more](https://github.com/NVlabs/instant-ngp)
13. [Instant Neural Graphics Primitives with a Multiresolution Hash Encoding](https://nvlabs.github.io/instant-ngp/)

14. [CS5670 Project 5 -- NeRF](https://www.cs.cornell.edu/courses/cs5670/2022sp/projects/pa5/)
