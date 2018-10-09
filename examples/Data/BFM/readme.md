# Prepare BFM data

1. Download raw BFM model   

    website: https://faces.dmi.unibas.ch/bfm/main.php?nav=1-2&id=downloads 

    copy 01_MorphabelModel.mat to raw/  

    

2. Download extra BFM information from 3DDFA(Face Alignment Across Large Poses: A 3D Solution)  and HFPE(High-Fidelity Pose and Expression Normalization for Face Recognition in the Wild)

    website: http://www.cbsr.ia.ac.cn/users/xiangyuzhu/projects/3DDFA/main.htm  

    download [Face Profiling] and [3DDFA]

    website:  http://www.cbsr.ia.ac.cn/users/xiangyuzhu/projects/HPEN/main.htm

    download [HPEN]

    copy  *.mat to 3ddfa/  

    

3. Download UV coordinates fom STN  

    website: https://github.com/anilbas/3DMMasSTN/blob/master/util/BFM_UV.mat  

    copy BFM_UV.mat to stn/  

    

4. run generate.m in Matlab  



Files will be saved in Out/  

Note: 

you need mkdir folders yourself, since I can not  upload empty folder to github.



  

