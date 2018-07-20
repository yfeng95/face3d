% addpath(genpath(pwd))
% --> model

%% load raw BFM models
load('raw/01_MorphableModel.mat');

%% load 3ddfa data
% 1. load bfm information. trim 
load('3ddfa/model_info.mat');
trimIndex_f = [3*trimIndex-2, 3*trimIndex-1, 3*trimIndex]';
trimIndex_f = trimIndex_f(:);

model.shapeMU = shapeMU(trimIndex_f,:);
model.shapePC = shapePC(trimIndex_f, :);
model.shapeEV = shapeEV;
model.texMU = texMU(trimIndex_f, :);
model.texPC = texPC(trimIndex_f, :);
model.texEV = texEV;
model.tri = tri;
model.kpt_ind = keypoints;

model_info.kpt_ind = keypoints;
model_info.trimIndex = trimIndex;
model_info.symlist = symlist;
model_info.symlist_tri = symlist_tri;
%segbin: nose eyes mouth rest
model_info.segbin = segbin(trimIndex, :)';
model_info.segbin_tri = segbin_tri';

% 2. load expression
load('3ddfa/Model_Expression.mat');
model.expMU = mu_exp;
model.expPC = w_exp;
model.expEV = sigma_exp;

% 3. load mouth tri
load('3ddfa/Model_tri_mouth');
model.tri_mouth = tri_mouth;
model_info.tri_mouth = tri_mouth;

% 4. face contour 
load('3ddfa/Model_face_contour_trimed.mat');
model_info.face_contour = face_contour;
model_info.face_contour_line = face_contour_line;
model_info.face_contour_front = face_contour_front;
model_info.face_contour_front_line = face_contour_front_line;

% 5. nose hole
load('3ddfa/Modelplus_nose_hole.mat');
model_info.nose_hole = nose_hole;
model_info.nose_hole_right = nose_hole_right;
model_info.nose_hole_left = nose_hole_left;

% 6. parallel for key points
load('3ddfa/Modelplus_parallel')
model_info.parallel = parallel;
model_info.parallel_face_contour = parallel_face_contour;

% 7. pncc
copyfile('3ddfa/vertex_code.mat', 'Out/pncc_code.mat')

%% load 3DMMasSTN UV coords
load('stn/BFM_UV.mat');
uv_coords = UV(trimIndex, :)';

% modify bad vers
bad_ind = [10032, 10155, 10280];
round1 = [10033, 10158 ];
round2 = [10534, 10157, 10661];
round3 = [10916, 10286];
uv_coords(:, bad_ind(1)) = mean(uv_coords(:, round1), 2);
uv_coords(:, bad_ind(2)) = mean(uv_coords(:, round2), 2);
uv_coords(:, bad_ind(3)) = mean(uv_coords(:, round3), 2);

model_info.uv_coords = uv_coords';
UV = model_info.uv_coords;

% modify tri mouth
tm_inner = model.tri_mouth;
tm_inner_add =[6420 6542 6664;  %% add inner mouth triangles
                        6420 6294 6167;
                        6167 6297 6420;
                        6167 6297 6296;
                        6167 6296 6295;
                        6167 6295 6039;
                        6168 6295 6039];   
ind_bad = 38;
all_ind = 1:size(tm_inner, 2);
tm_inner = tm_inner(:, setdiff(all_ind, bad_ind));
tm_inner = [tm_inner tm_inner_add'];
model_info.tri_mouth = tm_inner;
model.tri_mouth = tm_inner;

% save
clearvars -except model model_info UV

save 'Out/BFM.mat' model
save 'Out/BFM_info.mat' model_info
save 'Out/BFM_UV.mat' UV
copyfile('3ddfa/pncc_code.mat', 'Out/pncc_code.mat')