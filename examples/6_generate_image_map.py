''' 
Generate 2d maps representing different attributes(colors, depth, pncc, etc)
: render attributes to image space.
'''
import os, sys
import numpy as np
import scipy.io as sio
from skimage import io
from time import time
import matplotlib.pyplot as plt

sys.path.append('..')
import face3d
from face3d import mesh

# ------------------------------ load mesh data
C = sio.loadmat('Data/example1.mat')
vertices = C['vertices']; colors = C['colors']; triangles = C['triangles']
colors = colors/np.max(colors)

# ------------------------------ modify vertices(transformation. change position of obj)
# scale. target size=200 for example
s = 180/(np.max(vertices[:,1]) - np.min(vertices[:,1]))
# rotate 30 degree for example
R = mesh.transform.angle2matrix([0, 30, 0]) 
# no translation. center of obj:[0,0]
t = [0, 0, 0]
transformed_vertices = mesh.transform.similarity_transform(vertices, s, R, t)

# ------------------------------ render settings(to 2d image)
# set h, w of rendering
h = w = 256
# change to image coords for rendering
image_vertices = mesh.transform.to_image(transformed_vertices, h, w)

## --- start
save_folder = 'results/image_map'
if not os.path.exists(save_folder):
    os.mkdir(save_folder)

## 0. color map
attribute = colors
color_image = mesh.render.render_colors(image_vertices, triangles, attribute, h, w, c=3)
io.imsave('{}/color.jpg'.format(save_folder), np.squeeze(color_image))

## 1. depth map
z = image_vertices[:,2:]
z = z - np.min(z)
z = z/np.max(z)
attribute = z
depth_image = mesh.render.render_colors(image_vertices, triangles, attribute, h, w, c=1)
io.imsave('{}/depth.jpg'.format(save_folder), np.squeeze(depth_image))

## 2. pncc in 'Face Alignment Across Large Poses: A 3D Solution'. for dense correspondences 
pncc = face3d.morphable_model.load.load_pncc_code('Data/BFM/Out/pncc_code.mat')
attribute = pncc
pncc_image = mesh.render.render_colors(image_vertices, triangles, attribute, h, w, c=3)
io.imsave('{}/pncc.jpg'.format(save_folder), np.squeeze(pncc_image))

## 3. uv coordinates in 'DenseReg: Fully convolutional dense shape regression in-the-wild'. for dense correspondences
uv_coords = face3d.morphable_model.load.load_uv_coords('Data/BFM/Out/BFM_UV.mat') #
attribute = uv_coords # note that: original paper used quantized coords, here not
uv_coords_image = mesh.render.render_colors(image_vertices, triangles, attribute, h, w, c=2) # two channels: u, v
# add one channel for show
uv_coords_image = np.concatenate((np.zeros((h, w, 1)), uv_coords_image), 2)
io.imsave('{}/uv_coords.jpg'.format(save_folder), np.squeeze(uv_coords_image))

