''' Simple example of pipeline
3D obj(process) --> 2d image
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

# ------------------------------ 1. load mesh data
# -- mesh data consists of: vertices, triangles, color(optinal), texture(optional)
# -- here use colors to represent the texture of face surface
C = sio.loadmat('Data/example1.mat')
vertices = C['vertices']; colors = C['colors']; triangles = C['triangles']
colors = colors/np.max(colors)

# ------------------------------ 2. modify vertices(transformation. change position of obj)
# -- change the position of mesh object in world space
# scale. target size=180 for example
s = 180/(np.max(vertices[:,1]) - np.min(vertices[:,1]))
# rotate 30 degree for example
R = mesh.transform.angle2matrix([0, 30, 0]) 
# no translation. center of obj:[0,0]
t = [0, 0, 0]
transformed_vertices = mesh.transform.similarity_transform(vertices, s, R, t)

# ------------------------------ 3. modify colors/texture(add light)
# -- add point lights. light positions are defined in world space
# set lights
light_positions = np.array([[-128, -128, 300]])
light_intensities = np.array([[1, 1, 1]])
lit_colors = mesh.light.add_light(transformed_vertices, triangles, colors, light_positions, light_intensities)

# ------------------------------ 4. modify vertices(projection. change position of camera)
# -- transform object from world space to camera space(what the world is in the eye of observer). 
# -- omit if using standard camera
camera_vertices = mesh.transform.lookat_camera(transformed_vertices, eye = [0, 0, 200], at = np.array([0, 0, 0]), up = None)
# -- project object from 3d world space into 2d image plane. orthographic or perspective projection
projected_vertices = mesh.transform.orthographic_project(camera_vertices)

# ------------------------------ 5. render(to 2d image)
# set h, w of rendering
h = w = 256
# change to image coords for rendering
image_vertices = mesh.transform.to_image(projected_vertices, h, w)
# render 
rendering =  mesh.render.render_colors(image_vertices, triangles, lit_colors, h, w)

# ---- show rendering
# plt.imshow(rendering)
# plt.show()
save_folder = 'results/pipeline'
if not os.path.exists(save_folder):
    os.mkdir(save_folder)
io.imsave('{}/rendering.jpg'.format(save_folder), rendering)

# ---- show mesh
# mesh.vis.plot_mesh(camera_vertices, triangles)
# plt.show()
