%calculate linear distance
C = 0;
d = 1e-6;
center = 1920;
pixel_w = 6.4/3840;
focal_l = 3.6;
lambda1 = 300e-9;
lambda2 = 1000e-9;
theta = 0:0.0001:(pi / 2);
x1 = (asin(lambda1 / d) + theta) * focal_l / pixel_w + center;
x2 = (asin(lambda2 / d) + theta) * focal_l / pixel_w + center;
dx = x2 - x1;
plot(theta, dx);
