''' 
Generate 2d uv maps representing different attributes(colors, depth, image position, etc)
: render attributes to uv space.
'''
import os, sys
import numpy as np
import scipy.io as sio
from skimage import io
import skimage.transform
from time import time
import matplotlib.pyplot as plt

sys.path.append('..')
import face3d
from face3d import mesh
from face3d.morphable_model import MorphabelModel

def process_uv(uv_coords, uv_h = 256, uv_w = 256):
    uv_coords[:,0] = uv_coords[:,0]*(uv_w - 1)
    uv_coords[:,1] = uv_coords[:,1]*(uv_h - 1)
    uv_coords[:,1] = uv_h - uv_coords[:,1] - 1
    uv_coords = np.hstack((uv_coords, np.zeros((uv_coords.shape[0], 1)))) # add z
    return uv_coords


# --load mesh data
C = sio.loadmat('Data/example1.mat')
vertices = C['vertices']; colors = C['colors']; triangles = C['full_triangles']; 
colors = colors/np.max(colors)
# --modify vertices(transformation. change position of obj)
s = 180/(np.max(vertices[:,1]) - np.min(vertices[:,1]))
R = mesh.transform.angle2matrix([-10, -35, 20]) 
t = [0, 0, 0]
transformed_vertices = mesh.transform.similarity_transform(vertices, s, R, t)
# --load uv coords
uv_coords = face3d.morphable_model.load.load_uv_coords('Data/BFM/Out/BFM_UV.mat') 

# -- start
save_folder = 'results/uv_map'
if not os.path.exists(save_folder):
    os.mkdir(save_folder)

uv_h = uv_w = 256
image_h = image_w = 256
uv_coords = process_uv(uv_coords, uv_h, uv_w)

#-- 1. uv texture map
attribute = colors
uv_texture_map = mesh.render.render_colors(uv_coords, triangles, attribute, uv_h, uv_w, c=3)
io.imsave('{}/uv_texture_map.jpg'.format(save_folder), np.squeeze(uv_texture_map))

#-- 2. uv position map in 'Joint 3D Face Reconstruction and Dense Alignment with Position Map Regression Network'
#--   for face reconstruction & alginment(dense correspondences)
# To some extent, when uv space is regular, position map is a subclass of geometry image(recording geometry information in regular image)
# Notice: position map doesn't exit alone, it depends on the corresponding rendering(2d facical image). 
# Attribute is the position with respect to image coords system.
projected_vertices = transformed_vertices.copy() # use standard camera & orth projection here
image_vertices = mesh.transform.to_image(projected_vertices, image_h, image_w) 
position = image_vertices.copy()
position[:,2] = position[:,2] - np.min(position[:,2]) # translate z 
attribute = position
# corresponding 2d facial image
image = mesh.render.render_colors(image_vertices, triangles, colors, image_h, image_w, c=3)
uv_position_map = mesh.render.render_colors(uv_coords, triangles, attribute, uv_h, uv_w, c=3)
io.imsave('{}/image.jpg'.format(save_folder), np.squeeze(image))
np.save('{}/uv_position_map.npy'.format(save_folder), uv_position_map)
io.imsave('{}/uv_position_map.jpg'.format(save_folder), (uv_position_map)/max(image_h, image_w)) # only for show

# - verify
# import cv2
# uv_texture_map_rec = cv2.remap(image, uv_position_map[:,:,:2].astype(np.float32), None, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT,borderValue=(0))
# io.imsave('{}/uv_texture_map_rec.jpg'.format(save_folder), np.squeeze(uv_texture_map_rec))

#-- 3. general geometry image. attribute = vertices or transformed_vertices
# TODO 
#-- 4. attribute = normals
# TODO

