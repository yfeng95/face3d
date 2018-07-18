# Prepare BFM data

1. Download raw BFM model 
    website: https://faces.cs.unibas.ch/bfm/index.php?nav=1-0&id=basel_face_model.
    copy 01_MorphabelModel.mat to raw/

2. Download extra BFM information from 3DDFA(Face Alignment Across Large Poses: A 3D Solution).
    website: http://www.cbsr.ia.ac.cn/users/xiangyuzhu/projects/3DDFA/main.htm
    copy  *.mat to 3ddfa/

3. Download UV coordinates fom STN
    website: https://github.com/anilbas/3DMMasSTN/blob/master/util/BFM_UV.mat
    copy BFM_UV.mat to stn/

run generate.m in Matlab

files will be saved in Out/



Note: you need mkdir folders yourself, since I can not  upload empty folder in github.



  

