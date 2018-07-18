addpath(genpath(pwd))
load 'Out/BFM.mat'
load 'Out/BFM_info.mat' 

% test model
vertices = model.shapeMU + model.expMU;
vertices = reshape(vertices, 3, length(vertices)/3);
vertices = double(vertices);
tex = model.texMU/255.;
tex = reshape(tex, 3, length(tex)/3);
tri = model.tri;

% keypoints 
% tex(:, model_info.parallel{2}) = 0;
% tex(:, face_contour) = 0;
% tex(2, face_contour) = 1;

% show
figure
subplot(221)
tri = [tri model.tri_mouth];
patch('Vertices', vertices',  'FaceVertexCData', tex', 'Faces', tri', 'FaceColor', 'interp', 'EdgeColor', 'none', 'EdgeLighting', 'none', 'LineWidth', 1);

% mouth triangles
% edgeColor = 'red';
% patch('Vertices', vertices', 'Faces', model.tri_mouth', 'FaceColor', 'green', 'EdgeColor', edgeColor, 'EdgeLighting', 'none', 'LineWidth', 1);

% % stitch triangles
% edgeColor = 'yellow';
% patch('Vertices', vertices', 'Faces', trif_stitch', 'FaceColor', 'none', 'EdgeColor', edgeColor, 'EdgeLighting', 'none', 'LineWidth', 1);
axis equal;

%% project
s = 128;
uv_coords = model_info.uv_coords * (s -1) + 1;
uv_vertices = [uv_coords; zeros(1, size(uv_coords, 2))];
subplot(222);
patch('Vertices', uv_vertices',  'FaceVertexCData', tex', 'Faces', tri', 'FaceColor', 'interp', 'EdgeColor', 'none', 'EdgeLighting', 'none', 'LineWidth', 1);
% patch('Vertices', uv_vertices', 'Faces', model.tri_mouth', 'FaceColor', 'green', 'EdgeColor', edgeColor, 'EdgeLighting', 'none', 'LineWidth', 1);

hold on

plot(uv_vertices(1, model.kpt_ind), uv_vertices(2, model.kpt_ind), 'bx');
plot(uv_vertices(1, model_info.face_contour_front), uv_vertices(2, model_info.face_contour_front), 'g.');
plot(uv_vertices(1, model_info.parallel{1}), uv_vertices(2, model_info.parallel{1}), 'k.');

axis equal;


%% segbin
ver1_nose = vertices(:, boolean(model_info.segbin(1,:)));
ver2_eye = vertices(:, boolean(model_info.segbin(2,:)));
ver3_mouth = vertices(:, boolean(model_info.segbin(3,:)));
ver4_rest = vertices(:, boolean(model_info.segbin(4,:)));

subplot(223)
plot(vertices(1,:), vertices(2,:), 'k.');
hold on
plot(ver1_nose(1,:), ver1_nose(2,:), 'r.');
hold on
plot(ver2_eye(1,:), ver2_eye(2,:), 'b.');
hold on
plot(ver3_mouth(1,:), ver3_mouth(2,:), 'g.');
hold on
plot(ver4_rest(1,:), ver4_rest(2,:), 'm.');



