% verification of linear callibration 
C = 0;
d = 1e-6;
center = 1920;
pixel_w = 6.4/3840;
focal_l = 3.6;
angle_1 = 53.725/180 * pi;
x = 0:3839;
angle_2 = (x - center) * pixel_w / focal_l + angle_1;
lambda = C + d * sin((x - center) * pixel_w / focal_l + angle_1);
plot(x, lambda);
