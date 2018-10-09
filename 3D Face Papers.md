# 3D Face

## Surveys & Doctoral Thesis

- Face Image Analysis using a Multiple Features Fitting Strategy(2005, Basel)

- 3D Face Modelling for 2D+3D Face Recognition(2007, Surrey)

- Image Based 3D Face Reconstruction: A Survey(IJIG2009, Georgios Stylianou, Andreas Lanitis, EUC, CUT) 

  `early 3D facial acquisition approaches`

- animation reconstruction of deformable surfaces(2010, Hao Li, ETHz)

- Inverse Rendering of Faces with a 3D Morphable Model(2012, Oswald Aldrian, York)

- Digital Geometry Processing Theory and Applications(2012, Kun Zhou, Zhengjiang, 中文)

- ***State of the Art on Monocular 3D Face Reconstruction, Tracking, and Applications*** 

  **State of the Art on 3D Reconstruction with RGB-D Cameras**(EG2018, MZ, CT, MPI, Stanford, TUM, Disney, Technicolor, UEN) [[talks]](http://web.stanford.edu/~zollhoef/papers/EG18_FaceSTAR/page.html)

  

## Papers & Codes

### Reconstruction&3D Alignment&Correspondences

#### 1998 - 2015


- A Morphable Model For The Synthesis Of 3D Faces

     (SIGGRAPH1998, [V Blanz](https://scholar.google.com.hk/citations?user=jYCidWgAAAAJ&hl=zh-CN&oi=sra), [T Vetter](https://scholar.google.com.hk/citations?user=HKLgZpYAAAAJ&hl=zh-CN&oi=sra) , MPI) 

     `3dmm,analysis-by-synthesis(cascaded, coarse to fine, using texture information), mid-detail `

- Efficient, Robust and Accurate Fitting of a 3D Morphable Model

     (ICCV2003, S Romdhani, [T Vetter](https://scholar.google.com.hk/citations?user=HKLgZpYAAAAJ&hl=zh-CN&oi=sra) , Basel) 

     `3dmm, fitting Algorithm needs: Efficient, Robust, Accurate, Automatic. Mid-detail`

- Estimating 3D Shape and Texture Using Pixel Intensity, Edges, Specular Highlights, Texture Constraints and a Prior

   (CVPR2005, S Romdhani, [T Vetter](https://scholar.google.com.hk/citations?user=HKLgZpYAAAAJ&hl=zh-CN&oi=sra) , Basel)

   `3dmm, multiple features`

- A 3D Face Model for Pose and Illumination Invariant Face Recognition

  (AVSS2009, Paysan, P., Knothe, R., Amberg, B., Romdhani, S., & Vetter, T. , Basel) [[data](BFM)](https://faces.cs.unibas.ch/bfm/)

- 3D Face Reconstruction from a Single Image Using a Single Reference Face Shape

     (TPAMI2011, [I Kemelmacher-Shlizerman](https://scholar.google.com.hk/citations?user=P97vI1EAAAAJ&hl=zh-CN&oi=sra), Basri R, UW)

     `template, sfs, texture information, mid-detail`

- Face Reconstruction in the Wild

     (ICCV2011, Kemelmacher-Shlizerman I, Seitz S M , UW)

     `collection, sparse correspondence, warp template,  low-rank approximation(photometric stereo, for expression normalization), mid-detail `

- A FACS Valid 3D Dynamic Action Unit Database with Applications to 3D Dynamic Morphable Facial Modeling

     (ICCV2011, Cosker D, Krumhuber E, Hilton A. , UofSurrey)

     `aam, expression`

- Viewing Real-World Faces in 3D

     (ICCV2013, [T Hassner](https://scholar.google.com.hk/citations?user=ehe5pyIAAAAJ&hl=zh-CN&oi=sra), Open U Israel)

     `template, sparse correspondence, pose adjustment, depth optimization(SIFT)  ` 

- Improving 3D Face Details based on Normal Map of Hetero-source Images

  (CVPRW2014, Yang, C., Chen, J., Su, N., & Su, G. , Tsinghua University)

- Total Moving Face Reconstruction

   (LNCS2014, Suwajanakorn S, Kemelmacher-Shlizerman I, Seitz S M. , Washington)

   `video(collections), template, average shape, pose estimation, 3d flow(correspondence), refinement, high-detail `

- FaceWarehouse: a 3D Facial Expression Database for Visual Computing

  (VCG2014, Cao, C., Weng, Y., Zhou, S., Tong, Y., & Zhou, K., Zhejiang) [[data]]()

- Intrinsic Face Image Decomposition with Human Face Priors

  (ECCV2014, Li C, Zhou K, Lin S , Zhejiang)

- Fitting 3D Morphable Models using Local Features

  (ICIP2015, Huber, P., Feng, Z. H., Christmas, W., Kittler, J., & Ratsch, M, Surrey)

   `sparse correspondence, 3dmm, regression`

- What Makes Tom Hanks Look Like Tom Hanks

  (ICCV2015, Suwajanakorn S, Seitz S M, Kemelmacher-Shlizerman I. , Washington)

  `collection, template, average model, 3D flow, correspondence, deformation vector, TPS, expression sililarity weighted, high-frequency details, Laplacian pyramid      `

- Unconstrained Realtime Facial Performance Capture

  (CVPR2015, Hsieh, P. L., Ma, C., Yu, J., & Li, H. , USC)

  `video,image collections, occlusion, segmentation, landmarks `

- Unconstrained 3D Face Reconstruction

  (CVPR2015, Roth, J., Tong, Y., & Liu, X, MSU)

  `collection, sparse correspondence(landmarks), template, photometric stereo(SVD), matrix completion,  `

- Pose-Invariant 3D Face Alignment

  (ICCV2015, Jourabloo, A., & Liu, X., MSU)

  `alignment, dense correspondence, visibility, cascaded regressor, 3DPDM. `

- Discriminative 3D Morphable Model Fitting

  (CVPR2015)



#### 2016 

**#CVPR**

* Large-pose Face Alignment via CNN-based Dense 3D Model Fitting

  (CVPR2016, Jourabloo, A., & Liu, X., MSU)

   `alignment, 3dmm `

* Automated 3D Face Reconstruction from Multiple Images using Quality Measures

  (CVPR2016, Piotraschke, M., & Blanz, V , Siegen)

* A Robust Multilinear Model Learning Framework for 3D Faces

  (CVPR2016, Bolkart, T., & Wuhrer, S., Saarland)

* Face Alignment Across Large Poses: A 3D Solution

  (CVPR2016, Zhu, X., Lei, Z., Liu, X., Shi, H., & Li, S. Z. , MSU, CASIA)

* Adaptive 3D Face Reconstruction from Unconstrained Photo Collections

  (CVPR2016, Roth, J., Tong, Y., & Liu, X, MSU)

   `landmarks, 3dmm, coarse-to-fine,photometric stereo, time: 7 minutes  `

* Augmented Blendshapes for Real-time Simultaneous 3D Head Modeling and Facial Motion Capture

  (CVPR2016, Thomas, D., & Taniguchi, R. I. , Kyushu University)

* A 3D Morphable Model learnt from 10,000 faces

  (CVPR2016, Booth, J., Roussos, A., Zafeiriou, S., Ponniah, A., & Dunaway, D., ICL)

**#ECCV**

* Joint Face Alignment and 3D Face Reconstruction

  (ECCV2016, Liu, F., Zeng, D., Zhao, Q., & Liu, X, MSU, Sichuan U) 

  `alignment, landmarks`

* Real-Time Facial Segmentation and Performance Capture from RGB Input

  (ECCV2016, Saito, S., Li, T., & Li, H. , USC)

   `occlusions, tracking` 

**#Others**

- 3D Face Reconstruction by Learning from Synthetic Data

  (3DV2016, Richardson, E., Sela, M., & Kimmel, R, IIT)

   `3dmm, cnn, regress 3dmm parameters, sfs`

- Face Reconstruction on Mobile Devices Using a Height Map Shape Model and Fast Regularization

  (3DV2016, Maninchedda, F., Häne, C., Oswald, M. R., & Pollefeys, M., ETH)

- A Multiresolution 3D Morphable Face Model and Fitting Framework  [[code]](https://github.com/patrikhuber/eos)

  (IJCV2016, Huber, P., Hu, G., Tena, R., Mortazavian, P., Koppen, P., Christmas, W. J., ... & Kittler, J. ，Surrey)

- Rapid Photorealistic Blendshape Modeling from RGB-D Sensors

  (2016, USC)

- 3D Face Reconstruction with Region Based Best Fit Blending Using Mobile Phone for Virtual Reality Based Social Media

  (2016, Anbarjafari, G., Haamer, R. E., Lusi, I., Tikk, T., & Valgma, L. , Turkey)

  `landmarks, uv texture, region`



#### 2017

**#CVPR**

* 3D Face Morphable Models “In-the-Wild”  

  (CVPR2017, Booth, J., Antonakos, E., Ploumpis, S., Trigeorgis, G., Panagakis, Y., & Zafeiriou, S., ICL)

   `3dmm, register, UV`

* Face Normals “in-the-wild” using Fully Convolutional Networks

  (CVPR2017, Trigeorgis, G., Snape, P., Kokkinos, I., & Zafeiriou, S. , ICL)

* Regressing Robust and Discriminative 3D Morphable Models with a very Deep Neural Network

  (CVPR2017, Tran, A. T., Hassner, T., Masi, I., & Medioni, G. , USC)

* Fast 3D Reconstruction of Faces with Glasses

  (CVPR2017, Maninchedda, F., Oswald, M. R., & Pollefeys, M., ETH)

* DenseReg: Fully Convolutional Dense Shape Regression In-the-Wild

  (CVPR2017, Güler, R. A., Trigeorgis, G., Antonakos, E., Snape, P., Zafeiriou, S., & Kokkinos, I. , ICL)

  `dense correspondence, uv`

* Learning Detailed Face Reconstruction from a Single Image

  (CVPR2017, Richardson, E., Sela, M., Or-El, R., & Kimmel, R. , Washington)

* End-to-end 3D face reconstruction with deep neural networks

  (CVPR2017, Dou, P., Shah, S. K., & Kakadiaris, I. A., UofHouston)

  `3dmm, dl, directly learn 3dmm parameters`

* A Generative Model for Depth-based Robust 3D Facial Pose Tracking

  (CVPR2017, Cai, L. S. J., Pavlovic, T. J. C. V., & Ngan, K. N. , CUHK) 

   `occlusions` 

**#ICCV**

* 3D Morphable Models as Spatial Transformer Networks

   (ICCV2017, Bas, A., Huber, P., Smith, W. A., Awais, M., & Kittler, J. , York, Surrey )

   `dl, cnn, uv texture, landmarks, stn, 3dmm`

* Faster Than Real-time Facial Alignment: A 3D Spatial Transformer Network Approach in Unconstrained Poses

  (ICCV2017, Bhagavatula, C., Zhu, C., Luu, K., & Savvides, M., CMU)

* Pose-Invariant Face Alignment with a Single CNN

  (ICCV2017, Jourabloo, A., Ye, M., Liu, X., & Ren, L. , MSU)

  `alignment, 3dmm, dl, cnn`

* Large Pose 3D Face Reconstruction from a Single Image via Direct Volumetric CNN Regression [code](https://github.com/AaronJackson/vrn)

  (ICCV2017, Jackson, A. S., Bulat, A., Argyriou, V., & Tzimiropoulos, G. , Nottingham)

  `end-to-end, 3dmm, dl, cnn, landmarks, voxel  ` 

* Unrestricted Facial Geometry Reconstruction Using Image-to-Image Translation

  (ICCV2017, Sela, M., Richardson, E., & Kimmel, R. , IIT)

* MoFA: Model-based Deep Convolutional Face Autoencoder for Unsupervised Monocular Reconstruction

   (ICCV2017, Tewari, A., Zollhöfer, M., Kim, H., Garrido, P., Bernard, F., Pérez, P., & Theobalt, C. , MPI)

* Dense Face Alignment [code](http://cvlab.cse.msu.edu/project-pifa.html)

   (ICCVW2017, Liu, Y., Jourabloo, A., Ren, W., & Liu, X. , MSU)

* Realtime Dynamic 3D Facial Reconstruction for Monocular Video In-the-Wild

   (ICCVW2017) 

* Learning Dense Facial Correspondences in Unconstrained Images

  (ICCV2017, Yu, R., Saito, S., Li, H., Ceylan, D., & Li, H.  , USC)

  `dense correspondence`

**#others**

* Large Scale 3D Morphable Models [[data](LSFM)](https://faces.cs.unibas.ch/bfm/)

  (IJCV2017, Booth, J., Roussos, A., Ponniah, A., Dunaway, D., & Zafeiriou, S. , ICL) 

  `for alignment, template, cnn, dl, sparse correspondence, landmarks, tps warping `

* What does 2D geometric information really tell us about 3D face shape?  (2017, Bas, A., & Smith, W. A )

  `shape from landmarks, shape from contours`

* Pix2Face: Direct 3D Face Model Estimation

   (2017)

   `dense correspondence, 3dmm`

* 3D Face Reconstruction with Geometry Details from a Single Image

   (TIP2017, Jiang, L., Zhang, J., Deng, B., Li, H., & Liu, L. , USC, USTC)

   `coarse-to-fine, landmarks, corrective deformatio, sfs  `

   

#### 2018

**#CVPR**

* Unsupervised Training for 3D Morphable Model Regression  [code](https://github.com/google/tf_mesh_renderer)

  (CVPR2018, Genova, K., Cole, F., Maschinot, A., Sarna, A., Vlasic, D., & Freeman, W. T , Google)

- 4DFAB: A Large Scale 4D Database for Facial Expression Analysis and Biometric Applications  [data]( )

  (CVPR2018, Cheng, S., Kotsia, I., Pantic, M., & Zafeiriou, S., ICL) 

- Sparse Photometric 3D Face Reconstruction Guided by Morphable Models

  (CVPR2018, Cao, X., Chen, Z., Chen, A., Chen, X., Li, S., & Yu, J.  , shanghaitech)

  `5 input images, 3dmm, shadow processing, light calibration, photometric stereo, denoising `

- Disentangling Features in 3D Face Shapes for Joint Face Reconstruction and Recognition

  (CVPR2018, Liu, F., Zhu, R., Zeng, D., Zhao, Q., & Liu, X. , MSU, Sichuan)

- Mesoscopic Facial Geometry Inference Using Deep Neural Networks

  (CVPR2018, Hao Li, USC)

  `high-detail, dl, scan, uv texture, displacement `

- Self-supervised Multi-level Face Model Learning for Monocular Reconstruction at over 250 Hz

  (CVPR2018, Tewari, A., Zollhöfer, M., Garrido, P., Bernard, F., Kim, H., Pérez, P., & Theobalt, C., MPI)

- SfSNet : Learning Shape, Reflectance and Illuminance of Faces in the Wild

  (CVPR2018, Sengupta, S., Kanazawa, A., Castillo, C. D., & Jacobs, D.  , Maryland, UCB )

- Probabilistic Joint Face-Skull Modelling for Facial Reconstruction

  (CVPR2018, Madsen, D., Lüthi, M., Schneider, A., & Vetter, T. , Basel)

- Alive Caricature from 2D to 3D

  (CVPR2018, Wu, Q., Zhang, J., Lai, Y. K., Zheng, J., & Cai, J, USTC)

- Nonlinear 3D Face Morphable Model

  (CVPR2018, Tran, L., & Liu, X. , MSU)

- InverseFaceNet: Deep Monocular Inverse Face Rendering

  (CVPR2018, Kim, H., Zollhöfer, M., Tewari, A., Thies, J., Richardt, C., & Theobalt, C. , MPI)

  `Self-Supervised Bootstrapping`

- Extreme 3D Face Reconstruction: Looking Past Occlusions

  (CVPR2018, Tran, A. T., Hassner, T., Masi, I., Paz, E., Nirkin, Y., & Medioni, G. , USC)

- Total Capture: A 3D Deformation Model for Tracking Faces, Hands, and Bodies

  (CVPR2018, best student paper, Joo, H., Simon, T., & Sheikh, Y. , CMU)

- Modeling Facial Geometry using Compositional VAEs

  (CVPR2018, Bagautdinov, T., Wu, C., Saragih, J., Fua, P., & Sheikh, Y., EPEL, FRL )

**#ECCV**

* 3D Face Reconstruction from Light Field Images: A Model-free Approach

   (ECCV2018, Feng, M., Gilani, S. Z., Wang, Y., & Mian, A., Western Australia, Hunan)

   `epopolar plane images`

* Generating 3D Faces using Convolutional Mesh Autoencoders [[code]](https://github.com/anuragranj/coma)

   (ECCV2018, Ranjan, A., Bolkart, T., Sanyal, S., & Black, M. J., MPI)

* Joint 3D Face Reconstruction and Dense Alignment with Position Map Regression Network [[code]](https://github.com/YadiraF/PRNet)

   (ECCV2018, Feng, Y., Wu, F., Shao, X., Wang, Y., & Zhou, X., SJTU)

**#others**

* Morphable Face Models - An Open Framework

   (FG2018, Gerig, T., Morel-Forster, A., Blumer, C., Egger, B., Luthi, M., Schönborn, S., & Vetter, T. , Basel)

* CNN-based Real-time Dense Face Reconstruction with Inverse-rendered Photo-realistic Face Images [[data&code]](https://github.com/Juyong/3DFace)

   (TPAMI2018, Yudong Guo, Juyong Zhang, Jianfei Cai, Boyi Jiang, Jianmin Zheng, USTC)

* Multilinear Autoencoder for 3D Face Model Learning(WACV 2018,  Universite Grenoble Alpes (LJK), France)

   `3d scan to registered mesh. dl. height map  `

* On Face Segmentation, Face Swapping, and Face Perception(AFGR,2018, HT)

* Evaluation of Dense 3D Reconstruction from 2D Face Images in the Wild(FG2018) [data]( )

**#arxiv**

* Joint Face Alignment and 3D Face Reconstruction with Application to Face Recognition(2017, Feng Liu, Xiaoming Liu)

* Convolutional Point-set Representation: A Convolutional Bridge Between a Densely Annotated Image and 3D Face Alignment(20180317)

* Unsupervised Depth Estimation, 3D Face Rotation and Replacement(20180325)




### Production-level Reconstruction

> more in computer graphics  

- High-Quality Single-Shot Capture of Facial Geometry(TOG2010, ETHZ, Disney)

   `cg, high-detail,stereo system, calibration, surface refinement, normal direction, mesoscopic  `

- Multiview Face Capture using Polarized Spherical Gradient Illumination(TOG2011)

   `image collecitons`

- High-Quality Passive Facial Performance Capture using Anchor Frames(SIGGRAPH2011, ETHZ, Disney)

   `cg, stereo,anchor frame, tracking, mesh progration, physical movement, motion estimation, refinement `

- Lightweight binocular facial perfor- mance capture under uncontrolled lighting(TOG2012, MPI)

   `cg, high-detail, stereo, template,flow,data term, geometry term, smoothness term, mesh tracking, motion refinement, shape refinement, sfs  `

- Reconstructing Detailed Dynamic Face Geometry from Monocular Video(TOG2013,  MPI)

   `cg, dynamic, high-detail, blend model, sparse correspondence, dense correspondence(appearance matching, LBP), pose estimation , shape refinement, sfs   `

- 3D Shape Regression for Real-time Facial Animation(TOG2013, ZJU)

- Real-Time High-Fidelity Facial Performance Capture (TOG2015, ZJU)

   `cg, landmarks, optical flow, train a regressor to learn detail  `

- Dynamic 3D Avatar Creation from Hand-held Video Input(TOG2015,  EPEL)

   `cg, dynamic, mobile, high-detail, avatar, 3dmm,sparse correspondence, eye mesh, tracking, refinement, sfs, detail map     ` 

- Reconstruction of Personalized 3D Face Rigs from Monocular Video(TOG2016,  MPI)

   `parametric shape prior, coarse-scale reconstruction, fine-scale(sfs), coase->medium->fine, 3dmm, corrective   `

- Production-Level Facial Performance Capture Using Deep Convolutional Neural Networks（ASCA2017,  USC)

- Multi-View Stereo on Consistent Face Topology(EG2017, USC)

   `cg, high-detail, landmarks, template, pose estimation, refinement`

- Avatar Digitization From a Single Image For Real-Time Rendering(SIGGRAPH Asia 2017, USC)

   `cg, avatar, segmentation, head, hair, 3DMM, landmarks, texture completion   `

- Learning a model of facial shape and expression from 4D scans(TOG2017, USC, MPI)

- DeepSketch2Face: A Deep Learning Based Sketching System for 3D Face and Caricature Modeling(SIGGRAPH2017)  

- High-Fidelity Facial Reflectance and Geometry Inference From an Unconstrained Image(SIGGRAPH2018, USC)

     

### Texture

> 3D-aid texture generation/ UV texture completion  
> Keys: GAN

- Face Synthesis from Facial Identity Features(CVPR2017, google)

   `3dmm, dl, landmarks`

- Photorealistic Facial Texture Inference Using Deep Neural Networks(CVPR2017, Hao Li, USC)

   `texture completion`

- UV-GAN: Adversarial Facial UV Map Completion for Pose-invariant Face Recognition(CVPR2018, SZ, ICL)

   `gan, 3dmm, uv texture completion`

- Multi-Attribute Robust Component Analysis for Facial UV Maps(2017, SZ, ICL)

- Realistic Dynamic Facial Textures from a Single Image using GANs(CVPR2017, Hao Li, USC, DeepMind)

- Semi-supervised Adversarial Learning to Generate Photorealistic Face Images of New Identities from 3D Morphable Model(2018)

- Side Information for Face Completion: a Robust PCA Approach(20180120, SZ, ICL)

  ​    

### Transfer&Reenactment(Applications)

- Face Transfer with Multilinear Models (SIGGRAPH2005)

   `Cartesian product(ID x EX x VI)`

- Online Modeling For Realtime Facial Animation(TOG2013)

   `rgbd, blendshape, corrective field `

- Displaced Dynamic Expression Regression for Real-time Facial Tracking and Animation(SIGGRAPH2014)

- Real-time Expression Transfer for Facial Reenactment(SIGGRAPH AISA 2015)

- Face2Face: Real-time Face Capture and Reenactment of RGB Videos(CVPR2016)

   `capture, transfer, 3dmm, landmarks, texture, expression, mouth retrieval `

- Synthesizing Obama: Learning Lip Sync from Audio(SIGGRAPH2017)

- Deep Video Portrait(SIGGRAPH2018)

- HeadOn: Real-time Reenactment of Human Portrait Videos(SIGGRAPH2018)



### 3D-aid 2D face recognition

- Tom-vs-Pete Classifiers and Identity-Preserving Alignment for Face Verification(ECCV2012, Columbia University)

- Face Recognition from a Single Training Image under Arbitrary Unknown Lighting Using Spherical Harmonics(PAMI2006)

- 3D-aided face recognition robust to expression and pose variations (CVPR2014)

- Effective 3D based Frontalization for Unconstrained Face Recognition(ICPR2016, MICC, Florence)

- Effective Face Frontalization in Unconstrained Images(CVPR2015, TH, Israel)

- Do We Really Need to Collect Millions of Faces for Effective Face Recognition(ECCV2016, TH, USC, Israel)

- High-Fidelity Pose and Expression Normalization for Face Recognition in the Wild(CVPR2015)

- When 3D-Aided 2D Face Recognition Meets Deep Learning: An extended UR2D for Pose-Invariant Face Recognition(2017)

- Towards Large-Pose Face Frontalization in the Wild    

- Fully Automatic Pose-Invariant Face Recognition via 3D Pose Normalization   (ICCV2011, Cambridge, MA, USA)




### 3D face recognition

- Face Identification across Different Poses and Illuminations with a 3D Morphable Model(Automatic Face and Gesture Recognition2002, VB&TV)

- Preliminary Face Recognition Grand Challenge Results(2006)

- expression Invariant 3D Face Recognition with a Morphable Model(FG2008, TV, Basel)

- Bosphorus Database for 3D Face Analysis(2008)[data]()

- Robust Learning from Normals for 3D face recognition(ECCV2012, SZ, ICL)

- Static and dynamic 3D facial expression recognition: A comprehensive survey(IVC2012, SZ, LijunYin)

- Deep 3D Face Identification(2017, USC)

- Robust Face Recognition with Deeply Normalized Depth Images (2018)

   `depth image(front&neural)`

- Learning from Millions of 3D Scans for Large-scale 3D Face Recognition(CVPR2018, Western Australia) 

