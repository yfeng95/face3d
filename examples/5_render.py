''' Test render speed.
'''
import os, sys
import numpy as np
import scipy.io as sio
from skimage import io
from time import time
import matplotlib.pyplot as plt

np.set_printoptions(suppress=True)

sys.path.append('..')
import face3d
from face3d import mesh
from face3d import mesh_cython
from face3d.morphable_model import MorphabelModel

# load data 
C = sio.loadmat('Data/example1.mat')
vertices = C['vertices']; colors = C['colors']; triangles = C['triangles']
colors = colors/np.max(colors)
# move center to [0,0,0]
vertices = vertices - np.mean(vertices, 0)[np.newaxis, :]
s = 200/(np.max(vertices[:,1]) - np.min(vertices[:,1]))
R = mesh.transform.angle2matrix([0, 0, 0]) 
t = [0, 0, 0]
vertices = mesh.transform.similarity_transform(vertices, s, R, t)
# h, w of rendering
h = w = 256
image_vertices = mesh.transform.to_image(vertices, h, w)

# -----------------------------------------render
# # render texture python
# st = time()
# rendering_tp = face3d.mesh.render.render_texture(vertices, triangles, texture, texcoord, triangles, h, w)
# print('----------texture python: ', time() - st)

# # render texture c++
# st = time()
# rendering_tc = face3d.mesh_cython.render.render_texture(vertices, triangles, texture, texcoord, triangles, h, w)
# print('----------texture c++: ', time() - st)

# render colors python
st = time()
rendering_cp = face3d.mesh.render.render_colors(image_vertices, triangles, colors, h, w)
print('----------colors python: ', time() - st)

# render colors python ras
st = time()
rendering_cpr = face3d.mesh.render.render_colors_ras(image_vertices, triangles, colors, h, w)
print('----------colors python ras: ', time() - st)

# render colors python c++
st = time()
rendering_cc = face3d.mesh_cython.render.render_colors(image_vertices, triangles, colors, h, w)
print('----------colors c++: ', time() - st)