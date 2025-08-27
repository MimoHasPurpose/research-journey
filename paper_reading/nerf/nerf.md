- [ ] backward tracing 
- [ ] volume rendering
 

[NeRF: Neural Radiance Fields](https://www.matthewtancik.com/nerf)
[2003.08934](https://arxiv.org/pdf/2003.08934)
[Fourier Feature Networks](https://bmild.github.io/fourfeat/index.html)
[ICML Poster HyperFields: Towards Zero-Shot Generation of NeRFs from Text](https://icml.cc/virtual/2024/poster/34847)

explore related work and background from paper.

# nerf:

[krrish94/nerf-pytorch: A PyTorch re-implementation of Neural Radiance Fields](https://github.com/krrish94/nerf-pytorch/tree/master)

==A neural radiance field is a simple fully connected network (weights are ~5MB) trained to reproduce input views of a single scene using a rendering loss. The network directly maps from spatial location and viewing direction (5D input) to color and opacity (4D output), acting as the "volume" so we can use volume rendering to differentiably render new views.==

==To train a "full" NeRF model (i.e., using 3D coordinates as well as ray directions, and the hierarchical sampling procedure), first setup dependencies.==

==conda env create==

==conda activate nerf==

pip install -r requirements.txt

python train_[nerf.py](http://nerf.py) --config config/lego.yml

python train_[nerf.py](http://nerf.py) --config config/lego.yml --load-checkpoint path/to/checkpoint.ckpt

python cache_[dataset.py](http://dataset.py) --datapath cache/nerf_synthetic/lego/ --halfres False --savedir cache/legocache/legofull --num-random-rays 8192 --num-variations 50

## **(Full) NeRF on Google Colab**

A Colab notebook for the _full_ NeRF model (albeit on low-resolution data) can be accessed

[full_nerf_example.ipynb - Colab](https://colab.research.google.com/drive/1L6QExI2lw5xhJ-MLlIwpbgf7rxW7fcz3)

python eval_[nerf.py](http://nerf.py) --config pretrained/lego-lowres/config.yml --checkpoint pretrained/lego-lowres/checkpoint199999.ckpt --savedir cache/rendered/lego-lowres

convert cache/rendered/lego-lowres/*.png cache/rendered/lego-lowres.gifl

[krrish94/nerf-pytorch: A PyTorch re-implementation of Neural Radiance Fields](https://github.com/krrish94/nerf-pytorch/tree/master?tab=readme-ov-file)

[tiny_nerf_pytorch - Colab](https://colab.research.google.com/drive/1rO8xo0TemN67d4mTpakrKrLp03b9bgCX)


---

Hello, I've just read the original NeRF paper and the high-level idea of the paper seems to be pretty clear. I understood how the ray tracing works using neural networks as mappings from (x,y,z, azimuth, incline) to a color and the motivations of the equations used.

My goal is to implement this paper, and the part I'm not really clear on is, given a camera position and orientation (how to represent this?) and a desired image size, I can come up with a direction vector for each pixel on the image which I can "send into" scene to perform the ray tracing and retrieve the RGB color/density.

This gif illustrates what I'm talking about [https://imgur.com/hr4D2g2](https://imgur.com/hr4D2g2).

What are the computer vision concepts that I need to know in order to understand/implement this? Some pointers to articles/lectures/textbook chapters would be much appreciated.

I'm trying to get deeper into NeRF and Computer Vision as well. If you like we could learn together and have a chat from time to time.

About your question, there are 3 main concepts which are import in the original NeRF paper. 1) Calculating the pixel rays based on the camera parameters, 2) do the point sampling along the single rays by using the origin and direction, and 3) the accumulation of the ray colors and alpha values.

Regarding 1) I'm not very confident about this subject as of yet but I will update my comment later when I've fully understood it. Anyways, you basicallay have to use the camera parameters which discribe the position, focal length, width and height. Now you need the camera2world transformation vector to calculate the pixel rays, see [https://www.scratchapixel.com/lessons/3d-basic-rendering/ray-tracing-generating-camera-rays/generating-camera-rays](https://www.scratchapixel.com/lessons/3d-basic-rendering/ray-tracing-generating-camera-rays/generating-camera-rays)

Regarding 2), I guess you already know this. Using the camera origin and the normalized direction you can simple calculate a new point on the ray with `x_new = ray_origin + ray_direction * scalar`

And 3) is described in the paper. Let me know if you have questions about the calculation.

would love to chat more about NeRF, thanks for offering! Feel free to DM me on reddit or suggest another platform that you use.

As for your 3 concepts. I think the last two make sense to me, in 2) you essentially sample points along the line with origin `ray_origin` and direction vector `ray_direction`. In an implementation, I saw that there were some hyperparameters called `near` and `far`, which I presume to be bounds on the values that the `scalar` can take. With these sampled points, you apply positional encoding on the 5 element vector consisting of the (x,y,z, aziumuth, incline) and throw that into an MLP which spits out the density and color. Then in 3), you can simply plug that into the volume rendering equations to retrieve the color and density (these equations are integrals, but we approximate them via sums over the sampled points). I'm not super familiar with how these equations were derived, but I get the intuition behind them and understand their purposes.

The part I lack theory in is 1), this scratchapixel website was suggested in another comment as well, I am checking it out now.

  
For reference, the [paper](https://arxiv.org/abs/2003.08934).

> a camera position and orientation (how to represent this?)

Just before section 4, it talks about the MLP mapping a point _x_ and viewing direction _d_ to a color and density: FΘ : (x, d) → (c, σ)

So _d_ here is a directional vector in the global frame of the incoming ray, and _x_ is the point position.

Then, in section 4, it defines the camera ray as: _r_(_t_) = _o_ + _td_

where presumably _o_ is the camera origin and _d_ is the camera direction. So this must also be in the global frame, since _d_ is the same in both equations (I think). So, it answers your question of how the camera is represented: as a 3d position _o_ plus a directional vector _d_, where a directional vector is just a normalized vector.

Here I admit slight confusion. The paper (even the abstract) talks about representing the ray in the [spherical coordinate](https://en.wikipedia.org/wiki/Spherical_coordinate_system) space (θ,ϕ), which I guess is just for the incoming ray around the point -- the coordinates on the sphere surrounding the point, not as a 3d vector. However, this is not compatible with the ray equation given, which clearly propagates the ray using a 3d vector multiply.

What remains is to convert from a pixel position to this direction vector. But as far as I know, to get the spherical coordinates from the point of view of the _camera_, you need to apply an [inverse Gnomonic projection](https://mathworld.wolfram.com/GnomonicProjection.html), which assumes that the image is a plane tangent to a sphere.

So, having not looked at the original NeRF code, what I imagine must happen is the following transformation:

> pixel x/y coordinates → inverse gnomonic projection to get (θ,ϕ) with respect to the camera → conversion to normalized 3d direction vector → calculation of (θ,ϕ) with respect to the target point

but.. I think (θ,ϕ) in both cases might be just negatives of each other?.. if you shoot a ray from one point to another, they intersect aligned spheres with the same angles, just on opposite sides. So maybe the spherical to Cartesian conversion is not necessary, except for dealing with the ray propagation. You just need to calculate (θ,ϕ) for each pixel (a coordinate map) for input to F, which can be done once for each pixel of each image in a preprocessing stage. (Or just once if all images are the same size and taken with the same camera.) If the camera position moves (which it does, during optimization iirc), then everything rotates, but this just imposes an offset on (θ,ϕ).


---

[Math required to understand NeRF : r/computervision](https://www.reddit.com/r/computervision/comments/wpk4kn/math_required_to_understand_nerf/)


[NeRF – Representing Scenes as Neural Radiance Fields for View Synthesis | nerfss – Weights & Biases](https://wandb.ai/sweep/nerfss/reports/NeRF-Representing-Scenes-as-Neural-Radiance-Fields-for-View-Synthesis--Vmlldzo3ODIzMA)

[NeRF in 2023: Theory and Practice - It-Jim](https://www.it-jim.com/blog/nerf-in-2023-theory-and-practice/#:~:text=In%20practice%2C%20NeRF%20uses%20a,of%20a%20single%20rendered%20pixel.)
[Deep Dive into NeRF (Neural Radiance Fields)](https://dtransposed.github.io/blog/2022/08/06/NeRF/)

[Playing with NeRF | Blog | Gerry's World](https://gerry-chen.com/blog/2023-05-02_nerf.html)

[A Beginner’s 12-Step Visual Guide to Understanding NeRF: Neural Radiance Fields for Scene Representation and View Synthesis | by Aqeel Anwar | TDS Archive | Medium](https://medium.com/data-science/a-12-step-visual-guide-to-understanding-nerf-representing-scenes-as-neural-radiance-fields-24a36aef909a)
[NeRF Explosion 2020 - Frank Dellaert](https://dellaert.github.io/NeRF/)

[krrish94/nerf-pytorch: A PyTorch re-implementation of Neural Radiance Fields](https://github.com/krrish94/nerf-pytorch)





self-notes:
- neural radiance field for scene representation and view synthesis
- NeRF, short for _Neural Radiance Fields_, is a 2020 paper introducing a novel method for rendering 2D images from 3D scenes.
- Traditional approaches rely on physics-based, computationally intensive techniques such as ray casting and ray tracing.
- neRF addresses this issue by functioning as a scene compression method. It uses an overfitted multi-layer perceptron (MLP) to encode scene information, which can then be queried from any viewing direction to generate a 2D-rendered image.
- At its core, NeRF answers the following question using an MLP:

> 	_What will I see if I view the scene from this direction?_

	This question is answered by providing the viewing direction (in terms of two angles (θ, φ), or a unit vector) to the MLP as input, and MLP provides RGB (directional emitted color) and volume density, which is then processed through volumetric rendering to produce the final RGB value that the pixel sees. To create an image of a certain resolution (say HxW), the MLP is queried HxW times for each pixel’s viewing direction, and the image is created. Since the release of the first NeRF paper, numerous updates have been made to enhance rendering quality and speed. However, this blog will focus on the original NeRF paper.

-  Multi-view input images

   NeRF needs various images from different viewing angles to compress a scene. MLP learns to interpolate these images for unseen viewing directions (novel views). The information on the viewing direction for an image is provided using the camera's intrinsic and extrinsic matrices. The more images spanning a wide range of viewing directions, the better the NeRF reconstruction of the scene is. In short, the basic NeRF takes input camera images, and their associated camera intrinsic and extrinsic matrices.****
- ## **Sampling, Pixel iteration, and Ray casting**
- Each image in the input images is processed independently (for the sake of simplicity). From the input, an image and its associated camera matrices are sampled. For each camera image pixel, a ray is traced from the camera center to the pixel and extended outwards. If the camera center is defined as o, and the viewing direction as directional vector d, then the ray r(t) can be defined as r(t)=o+td where t is the distance of the point r(t) from the center of the camera.
![[Pasted image 20250819055732.png]]
Ray casting is done to identify the parts of the scene that contribute to the color of the pixel.
## **Step 5: Ray Marching**

Once the ray is cast, we sample n point along the ray. Theoretically, the ray can extend out infinitely, so to limit the ray we define a near r(t_n) and far plane r(t_f) which are t_n and t_f distance away from the camera center. These planes limit our search space. Only the space within these planes is considered for scene reconstruction, hence the planes need to be defined by the scene under consideration.

- [ ] ![[Pasted image 20250819055842.png]]
- [ ] ![[Pasted image 20250819055906.png]]
- [ ] ## **Step 6, 7: Multi layer perceptron (MLP)**

Now for each pixel in the camera image, we have a viewing direction (θ, φ — which is the same) and n number of 3D points from the scene that lie in that viewing direction ((x1, y1,z1), (x2, y2, z2), …, (xn, yn, zn)). From these parameters, we create n number of 5D vectors which is used as input to the MLP as shown above The MLP then predicts n number of 4D vectors that contain the directional emitted color c (i.e. the RGB color c=(ri, gi, bi) contributed by the 3D position xi, yi, zi towards the pixels when viewed from the direction θi, φi), and a volumetric density σ (a scalar value used to determine the probability of a ray interacting with a particular point in space). σ indicates how “opaque” a point in space is. High values of σ mean that the space is dense (e.g., part of an object), while low values indicate empty or transparent regions.

Formally the MLP F_Θ does the following

![](https://miro.medium.com/v2/resize:fit:530/1*v5Z-DIlhV530oAL_WFEumg.png)

MLP used for NeRF

where d is the viewing direction (either (θ, φ), or a 3D unit vector) of the ray, and **x =** (x, y, z) is the 3D position of the sampled point along the ray

![[Pasted image 20250819055938.png]]
## **Step 8: Pixel reconstruction**

The pixel color is reconstructed by integrating contributions along the ray that passes through the scene. For a ray parameterized as r(t)=o+td, the color C(r) of the ray (and thus the pixel) is computed using the volume rendering equation as follows

![[Pasted image 20250819055951.png]]


where sigma(r(t)) is the volumetric density of the point r(t) on the ray cast, c(r(t), d) is the directional emitted color of the point r(t), t_f and t_n are the limits defined by the near and the far plane. T(t) is the transmittance, representing the probability that light travels from the camera to depth t without being absorbed, and is calculated as follows

![[Pasted image 20250819060045.png]]
Let's first understand what transmittance is. The farther you move along the ray, the higher the probability that the ray is absorbed within the scene. Consequently, the transmittance is determined by the negative exponent of the cumulative volumetric density integrated from the near plane to the point t where the transmittance is being calculated.

## **Steps 9, 10, and 11: Image reconstruction, Loss calculation & Optimization**

After estimating the pixel color through volume rendering, the same process is repeated for all pixels in the image to reconstruct the complete image. The reconstructed image is then compared to the input image, and a pixel-wise Mean Squared Error (MSE) loss is computed as follows.
![[Pasted image 20250819060118.png]]
![[Pasted image 20250819060136.png]]


## Summary:

This article provides a visual guide to understanding NeRF for beginners. The article breaks down NeRF’s workflow into 12 simple, easy-to-follow steps. Here’s a summary:

1. **Input**: NeRF requires multi-view images of a scene, along with their corresponding camera matrices.
2. **Sampling**: Start by selecting an image and its camera matrix to begin the process.
3. **Pixel Iteration**: For each pixel in the image, repeat the following steps.
4. **Ray Casting**: Cast a ray r from the camera center through the pixel, as defined by the camera matrix.
5. **Ray Marching**: Sample n points along the ray r, between a near and a far plane.
6. **Input to the MLP**: Construct n 5D vectors, each containing the sampled position (x,y,z) and viewing direction (θ,ϕ), and feed them into the MLP.
7. **MLP Output**: The MLP predicts the color (r, g, b) and volumetric density σ for each sampled point.
8. **Pixel Reconstruction**: Use differentiable volume rendering to combine the predicted color and density of the sampled points to reconstruct the pixel’s color.
9. **Image Reconstruction**: Iterate over all pixels to predict the entire image.
10. **Loss Calculation**: Compute the reconstruction loss between the predicted image and the ground truth input image.
11. **Optimization**: Leverage the differentiable nature of all components to use backpropagation, training the MLP to overfit the scene for all input views.
12. **Rendering from Novel Viewpoints**: Query the trained MLP to generate pixel colors for a new viewpoint and reconstruct the image.


personal notes: 


