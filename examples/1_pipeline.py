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
from face3d import mesh_cython

# ------------------------------ 1. load mesh data
C = sio.loadmat('Data/example1.mat')
vertices = C['vertices']; colors = C['colors']; triangles = C['triangles']
colors = colors/np.max(colors)

# ------------------------------ 2. modify vertices(transformation. change position of obj)
# scale. target size=180 for example
s = 180/(np.max(vertices[:,1]) - np.min(vertices[:,1]))
# rotate 30 degree for example
R = mesh.transform.angle2matrix([0, 30, 0]) 
# no translation. center of obj:[0,0]
t = [0, 0, 0]
transformed_vertices = mesh.transform.similarity_transform(vertices, s, R, t)

# ------------------------------ 3. modify colors/texture(add light)
# set lights
light_positions = np.array([[-128, -128, 300]])
light_intensities = np.array([[1, 1, 1]])
lit_colors = mesh.light.add_light(transformed_vertices, triangles, colors, light_positions, light_intensities)

# ------------------------------ 4. modify vertices(projection. change position of camera)
projected_vertices = mesh.transform.lookat_camera(transformed_vertices, eye = [0, 0, 200], at = np.array([0, 0, 0]), up = None)

# ------------------------------ 5. render(to 2d image)
# set h, w of rendering
h = w = 256
# change to image coords for rendering
image_vertices = mesh.transform.to_image(projected_vertices, h, w)
rendering = face3d.mesh_cython.render.render_colors(image_vertices, triangles, lit_colors, h, w)

# ---- show
plt.imshow(rendering)
plt.show()

