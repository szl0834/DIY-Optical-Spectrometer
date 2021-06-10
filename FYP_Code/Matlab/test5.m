%this is for finding pixel number of spectrum lines
a = x532laser(1080,:,:);
b = x632laser(1080,:,:);
c = x650laser(1080,:,:);
figure();
plot(a(1,:,1));
figure();
plot(b(1,:,1));
figure();
plot(c(1,:,1));