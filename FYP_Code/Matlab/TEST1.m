%% caculating effective indeicent angle
d = 1000;
theta_1 = 0:0.001:pi / 2;
lambda_1 = 300;
lambda_2 = 1000;
lambda_3 = 635;
theta_2 = asin(sin(theta_1) - (lambda_1) / d);
theta_3 = asin(sin(theta_1) - (lambda_2) / d);
theta_4 = theta_2 - theta_3;
figure(1);
plot(theta_1, theta_4, 'LineWidth', 2);
xlabel("Incident Angle (rad)");
ylabel("Diffraction Angle Difference (rad)")
%% calculate diffraciton angle
m = 0:1:10;
figure(2);
theta_5 = asin(0 - (lambda_3 * m) / d);
plot(m, theta_5);
theta_6 = asin(0 - (lambda_1) / d) * 180 / pi;
theta_7 = asin(0 - (lambda_2) / d) * 180 / pi;
