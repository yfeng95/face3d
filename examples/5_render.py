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
from face3d import mesh_numpy
from face3d.morphable_model import MorphabelModel

# load data 
C = sio.loadmat('Data/example1.mat')
vertices = C['vertices']; colors = C['colors']; triangles = C['triangles']
colors = colors/np.max(colors)
# transform
vertices = vertices - np.mean(vertices, 0)[np.newaxis, :]
s = 180/(np.max(vertices[:,1]) - np.min(vertices[:,1]))
R = mesh.transform.angle2matrix([0, 0, 0]) 
t = [0, 0, 0]
vertices = mesh.transform.similarity_transform(vertices, s, R, t)
# h, w of rendering
h = w = 256
image_vertices = mesh.transform.to_image(vertices, h, w)

# -----------------------------------------render colors
# render colors python numpy
st = time()
rendering_cp = mesh_numpy.render.render_colors(image_vertices, triangles, colors, h, w)
print('----------colors python: ', time() - st)

# render colors python ras numpy
st = time()
rendering_cpr = mesh_numpy.render.render_colors_ras(image_vertices, triangles, colors, h, w)
print('----------colors python ras: ', time() - st)

# render colors python c++
st = time()
rendering_cc = mesh.render.render_colors(image_vertices, triangles, colors, h, w)
print('----------colors c++: ', time() - st)

# ----------------------------------------- render texture(texture mapping)
# when face texture is saved as texture map, this method is recommended.
# load texture
texture = io.imread('Data/uv_texture_map.jpg')/255.
tex_h, tex_w, _ = texture.shape
# load texcoord(uv coords)
uv_coords = face3d.morphable_model.load.load_uv_coords('Data/BFM/Out/BFM_UV.mat') # general UV coords: range [0-1]
# to texture size
texcoord = np.zeros_like(uv_coords) 
texcoord[:,0] = uv_coords[:,0]*(tex_w - 1)
texcoord[:,1] = uv_coords[:,1]*(tex_h - 1)
texcoord[:,1] = tex_h - texcoord[:,1] - 1
texcoord = np.hstack((texcoord, np.zeros((texcoord.shape[0], 1)))) # add z# render texture python
# tex_triangles
tex_triangles = triangles 

# render texture python
st = time()
rendering_tp = face3d.mesh_numpy.render.render_texture(image_vertices, triangles, texture, texcoord, tex_triangles, h, w)
print('----------texture python: ', time() - st)

# render texture c++
st = time()
rendering_tc = face3d.mesh.render.render_texture(image_vertices, triangles, texture, texcoord, tex_triangles, h, w)
print('----------texture c++: ', time() - st)

# plot
# plt.subplot(2,2,1)
# plt.imshow(rendering_cp)
# plt.subplot(2,2,2)
# plt.imshow(rendering_cc)
# plt.subplot(2,2,3)
# plt.imshow(rendering_tp)
# plt.subplot(2,2,4)
# plt.imshow(rendering_tc)
# plt.show()


## --------------------------- write obj
# mesh.vis.plot_mesh(vertices, triangles)
# plt.show()
save_folder = os.path.join('results', 'io')
if not os.path.exists(save_folder):
    os.mkdir(save_folder)

vertices, colors, uv_coords = image_vertices.astype(np.float32).copy(), colors.astype(np.float32).copy(), uv_coords.astype(np.float32).copy()

st = time()
mesh_numpy.io.write_obj_with_colors_texture(os.path.join(save_folder, 'numpy.obj'), vertices, triangles, colors, texture, uv_coords)
print('----------write obj numpy: ', time() - st)

st = time()
mesh.io.write_obj_with_colors_texture(os.path.join(save_folder, 'cython.obj'), vertices, triangles, colors, texture, uv_coords)
print('----------write obj cython: ', time() - st)
