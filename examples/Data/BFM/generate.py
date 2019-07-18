#!/usr/bin/env python
# encoding: utf-8

import scipy.io as sio
import numpy as np
import shutil
import os

# 0. load all data
bfm = sio.loadmat('raw/01_MorphableModel.mat',matlab_compatible=True)
model_info = sio.loadmat('3ddfa/model_info.mat',matlab_compatible=True)
model_expr = sio.loadmat('3ddfa/Model_Expression.mat',matlab_compatible=True)
model_tri_mouth = sio.loadmat('3ddfa/Model_tri_mouth',matlab_compatible=True)
model_face_contour_trimed = sio.loadmat('3ddfa/Model_face_contour_trimed.mat',matlab_compatible=True)
modelplus_nose_hole = sio.loadmat('3ddfa/Modelplus_nose_hole.mat',matlab_compatible=True)
modelplus_parallel = sio.loadmat('3ddfa/Modelplus_parallel.mat',matlab_compatible=True)
bfm_uv = sio.loadmat('stn/BFM_UV.mat',matlab_compatible=True)


Model = {}
ModelInfo = {}

# 1. model_info
trimIndex = model_info["trimIndex"].astype(np.int32)
trimIndex_f = np.concatenate([3 * trimIndex-3, 3 * trimIndex -2, 3 * trimIndex - 1], axis = 1)
trimIndex_f = trimIndex_f.reshape(-1, )

Model["shapeMU"] = bfm["shapeMU"][trimIndex_f]
Model["shapePC"] = bfm["shapePC"][trimIndex_f]
Model["shapeEV"] = bfm["shapeEV"]
Model["texMU"] = bfm["texMU"][trimIndex_f]
Model["texPC"] = bfm["texPC"][trimIndex_f]
Model["texEV"] = bfm["texEV"]
Model["tri"] = model_info["tri"]
Model["kpt_ind"] = model_info["keypoints"]

ModelInfo["kpt_ind"] = model_info["keypoints"]
ModelInfo["trimIndex"] = model_info["trimIndex"]
ModelInfo["symlist"] = model_info["symlist"]
ModelInfo["symlist_tri"] = model_info["symlist_tri"]
ModelInfo["segbin"] = model_info["segbin"][trimIndex.reshape(-1,) - 1].T
ModelInfo["segbin_tri"] = model_info["segbin_tri"].T


# 2. model_expr
Model["expMU"] = model_expr["mu_exp"]
Model["expPC"] = model_expr["w_exp"]
Model["expEV"] = model_expr["sigma_exp"]


# 3. model_tri_mouth
Model["tri_mouth"]      = model_tri_mouth["tri_mouth"]
ModelInfo["tri_mouth"] = model_tri_mouth["tri_mouth"]

# 4. model_face_contour_trimed

ModelInfo["face_contour"]= model_face_contour_trimed["face_contour"]
ModelInfo["face_contour_line"]= model_face_contour_trimed["face_contour_line"]
ModelInfo["face_contour_front"]= model_face_contour_trimed["face_contour_front"]
ModelInfo["face_contour_front_line"]= model_face_contour_trimed["face_contour_front_line"]

# 5. modelplus_nose_hole
ModelInfo["nose_hole"] = modelplus_nose_hole["nose_hole"]
ModelInfo["nose_hole_right"] = modelplus_nose_hole["nose_hole_right"]
ModelInfo["nose_hole_left"] = modelplus_nose_hole["nose_hole_left"]

# 6. modelplus_parallel
ModelInfo["parallel"] = modelplus_parallel["parallel"]
ModelInfo["parallel_face_contour"] = modelplus_parallel["parallel_face_contour"]

# 7. pncc (skip)
# copyfile('3ddfa/vertex_code.mat', 'Out/pncc_code.mat')

# 8. bfm_uv
uv_coords = bfm_uv["UV"][trimIndex.reshape(-1,) - 1].T
bad_ind = np.array([10032, 10155, 10280])
round1 = np.array([10033, 10158])
round2 = np.array([10534, 10157, 10661] )
round3 = np.array([10916, 10286])
uv_coords[:, bad_ind[0]-1] = np.mean(uv_coords[:, round1-1], axis = 1)
uv_coords[:, bad_ind[1]-1] = np.mean(uv_coords[:, round2-1], axis = 1)
uv_coords[:, bad_ind[2]-1] = np.mean(uv_coords[:, round3-1], axis = 1)
ModelInfo["uv_coords"] = uv_coords.T
uv_coords = ModelInfo["uv_coords"]


tm_inner = Model["tri_mouth"]
tm_inner_add = np.array([[6420, 6542, 6664],
                         [6420, 6294, 6167],
                         [6167, 6297, 6420],
                         [6167, 6297, 6296],
                         [6167, 6296, 6295],
                         [6167, 6295, 6039],
                         [6168, 6295, 6039]]).T

ind_bad = 38
all_ind = np.array(range(1,tm_inner.shape[1] + 1))
tm_inner = tm_inner[:, np.setdiff1d(all_ind, bad_ind) - 1]
tm_inner = np.concatenate([tm_inner, tm_inner_add], axis = 1)
ModelInfo["tri_mouth"] = tm_inner
Model["tri_mouth"] = tm_inner

dst_dir = 'Out'
if not os.path.exists(dst_dir):
    os.mkdir(dst_dir)

sio.savemat(os.path.join(dst_dir, "BFM.mat"), {"model":Model})
sio.savemat(os.path.join(dst_dir, "BFM_info.mat"), {"model_info":ModelInfo})
sio.savemat(os.path.join(dst_dir, "BFM_UV.mat"), {"UV":uv_coords})
shutil.copyfile('3ddfa/vertex_code.mat', os.path.join(dst_dir, 'pncc_code.mat') )
