'''
test light
'''
import os, sys
import numpy as np
import scipy.io as sio
from skimage import io
from time import time
import subprocess

sys.path.append('..')
import face3d
from face3d import mesh

def light_test(vertices, light_positions, light_intensities, h = 256, w = 256):
	lit_colors = mesh.light.add_light(vertices, triangles, colors, light_positions, light_intensities)
	image_vertices = mesh.transform.to_image(vertices, h, w)
	rendering = mesh.render.render_colors(image_vertices, triangles, lit_colors, h, w)
	rendering = np.minimum((np.maximum(rendering, 0)), 1)
	return rendering

# --------- load mesh data
C = sio.loadmat('Data/example1.mat')
vertices = C['vertices']; 
global colors
global triangles
colors = C['colors']; triangles = C['triangles']
colors = colors/np.max(colors)
# move center to [0,0,0]
vertices = vertices - np.mean(vertices, 0)[np.newaxis, :]
s = 180/(np.max(vertices[:,1]) - np.min(vertices[:,1]))
R = mesh.transform.angle2matrix([0, 0, 0]) 
t = [0, 0, 0]
vertices = mesh.transform.similarity_transform(vertices, s, R, t) # transformed vertices

# save settings
save_folder = 'results/light'
if not os.path.exists(save_folder):
    os.mkdir(save_folder)
options = '-delay 12 -loop 0 -layers optimize' # gif. need ImageMagick.

# ---- start
# 1. fix light intensities. change light positions.
# x axis: light from left to right
light_intensities = np.array([[1, 1, 1]])
for i,p in enumerate(range(-200, 201, 40)): 
	light_positions = np.array([[p, 0, 300]])
	image = light_test(vertices, light_positions, light_intensities) 
	io.imsave('{}/1_1_{:0>2d}.jpg'.format(save_folder, i), image)
# y axis: light from up to down
for i,p in enumerate(range(200, -201, -40)): 
	light_positions = np.array([[0, p, 300]])
	image = light_test(vertices, light_positions, light_intensities) 
	io.imsave('{}/1_2_{:0>2d}.jpg'.format(save_folder, i), image)
# z axis: light near down to far
for i,p in enumerate(range(100, 461, 40)): 
	light_positions = np.array([[0, 0, p]])
	image = light_test(vertices, light_positions, light_intensities) 
	io.imsave('{}/1_3_{:0>2d}.jpg'.format(save_folder, i), image)
subprocess.call('convert {} {}/1_*.jpg {}'.format(options, save_folder, save_folder + '/position.gif'), shell=True)


# 2. fix light positions. change light intensities.
light_positions = np.array([[0, 0, 300]])
for k in range(3):
	for i,p in enumerate(np.arange(0.4,1.1,0.2)): 
		light_intensities = np.array([[0, 0, 0]], dtype = np.float32)
		light_intensities[0,k] = p
		image = light_test(vertices, light_positions, light_intensities) 
		io.imsave('{}/2_{}_{:0>2d}.jpg'.format(save_folder, k, i), image)
subprocess.call('convert {} {}/2_*.jpg {}'.format(options, save_folder, save_folder + '/intensity.gif'), shell=True)

# -- delete jpg files
print('gifs have been generated, now delete jpgs')
subprocess.call('rm {}/*.jpg'.format(save_folder), shell=True)
