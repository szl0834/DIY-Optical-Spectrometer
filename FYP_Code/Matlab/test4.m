%ploting diffration diagram 
x=-10:0.1:10;
a=2;
b=4;
y=sin(x).^2./x.^2;
y(101)=1;
plot(x,y,(x+pi),y,'LineWidth',2);
hold on;
% z = 0*ones(1,201);
% z(101)=2;
% z(132)=2;
% stem(x,z);
hold off;
axis([-3*pi 4*pi -0.1 1.1]);