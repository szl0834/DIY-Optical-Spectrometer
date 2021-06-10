
fun=@root4d;
x0=[3.6,0.9376];
options = optimoptions('fsolve','Display','none','PlotFcn',@optimplotfirstorderopt);
x=fsolve(fun,x0);