%this code is for estimation algorithm for linear callibration
L = [532 632.8 808 532];
b = L / 1000;
PP = [827 1179 1919 827];
k = abs(PP - 1920) * 6.4/3840;
a = 0:0.1:3;
a = a * pi / 180;

q = zeros(3, 31);

for i = 1:3

    for j = 1:31
        q(i, j) = (k(i) * asin(b(i + 1) - sin(a(j))) - k(i + 1) * (asin(b(i) - sin(a(j))))) / (asin(b(i + 1) - sin(a(j))) - asin(b(i) - sin(a(j))));
    end

end

Variance = zeros(1, 31);

for j = 1:31
    Variance(j) = var(q(:, j));
end

[min_value, min_position] = min(Variance);
q_estimation = q(:, min_position);
q_mean = sum(q_estimation) / 3;

F = zeros(1, 3);

for i = 1:3
    F(i) = (q_mean - k(i)) / asin(b(i) - sin(a(min_position)));
end

F_mean = mean(F);
phi = q_mean / F_mean;
