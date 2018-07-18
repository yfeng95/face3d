tex = model.texMU/255.;
tex = reshape(tex, 3, length(tex)/3);
tri = model.tri;

uv_coords = model_info.uv_coords';
% modify bad vers
bad_ind = [10032, 10155, 10280];
round1 = [10033, 10158 ];
round2 = [10534, 10157, 10661];
round3 = [10916, 10286];
uv_coords(:, bad_ind(1)) = mean(uv_coords(:, round1), 2);
uv_coords(:, bad_ind(2)) = mean(uv_coords(:, round2), 2);
uv_coords(:, bad_ind(3)) = mean(uv_coords(:, round3), 2);
model_info.uv_coords = uv_coords;

vertices = [uv_coords; zeros(1, size(uv_coords, 2))];

% vertices = model.shapeMU + model.expMU;% + model.expPC*randn(29, 1);
% vertices = reshape(vertices, 3, length(vertices)/3);
% vertices = double(vertices);

figure
tex(:, model.kpt_ind) = 0;

tri_mouth_ind = model_info.segbin_tri(3,:);
tri_mouth = tri(:, boolean(tri_mouth_ind));
patch('Vertices', vertices',  'FaceVertexCData', tex', 'Faces', tri_mouth', 'FaceColor', 'interp', 'EdgeColor', 'none', 'EdgeLighting', 'none', 'LineWidth', 1);

% axis equal;
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
save 'me/BFM.mat' model
save 'me/BFM_info.mat' model_info

% show
vm_inner = unique(tm_inner(:));

edgeColor = 'red';
patch('Vertices', vertices', 'Faces', tm_inner', 'FaceColor', 'green', 'EdgeColor', edgeColor, 'EdgeLighting', 'none', 'LineWidth', 1);

tm = tri_mouth;
vm = unique(tm(:));
hold on
plot(vertices(1,vm), vertices(2,vm), 'bx');

plot(vertices(1,bad_ind), vertices(2,bad_ind), 'ro');

plot(vertices(1,vm_inner), vertices(2,vm_inner), 'g.');

for i = 1:length(vm)
    ind = vm(i);
    text(vertices(1,ind), vertices(2,ind), num2str(ind));
end


% for i = 1:size(model.tri_mouth, 2)
%     patch('Vertices', vertices', 'Faces', model.tri_mouth(:,i)', 'FaceColor', 'green', 'EdgeColor', edgeColor, 'EdgeLighting', 'none', 'LineWidth', 1);
% end