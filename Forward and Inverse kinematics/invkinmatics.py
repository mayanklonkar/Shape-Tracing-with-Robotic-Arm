from sympy import *
import sympy as sp
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np



x,y,z,theta1,theta2,theta3=sp.symbols('x y z theta1 theta2 theta3')

x_f=float(input("enter the x cordinate of end effector"))
y_f=float(input("enter the y coordinate of end effector"))
orientation=float(input("enter the orientation of end effector"))

f1=5*(sp.cos(theta1)+sp.cos(theta1+theta2)+sp.cos(theta1+theta2+theta3)- x_f)
f2=5*(sp.cos(theta1)+sp.sin(theta1+theta2)+sp.sin(theta1+theta2+theta3)-y_f)
f3=sp.cos(theta1+theta2+theta3)-sp.cos(orientation)

t_1=float(input("enter intial guess of theta1 "))
t_2=float(input("enter intial guess of theta2"))
t_3=float(input("enter intial guess of theta3"))


# Differentiating to find jacobian
j_00=sp.diff(f1,theta1)
j_01=sp.diff(f1,theta2)
j_02=sp.diff(f1,theta3)

j_10=sp.diff(f2,theta1)
j_11=sp.diff(f2,theta2)
j_12=sp.diff(f2,theta3)

j_20=sp.diff(f3,theta1)
j_21=sp.diff(f3,theta2)
j_22=sp.diff(f3,theta3)

jacobian=sp.Matrix(3,3,[j_00,j_01,j_02,j_10,j_11,j_12,j_20,j_21,j_22])
sp.pretty_print(jacobian)
jacobian_inv=jacobian.inv()
sp.pretty_print(jacobian_inv)

t_10=0
t_20=0
t_30=0
func_value=sp.Matrix(3,1,[f1,f2,f3])
func_value1=func_value.subs({theta1:t_1,theta2:t_2,theta3:t_3})
guess=sp.Matrix(3,1,[t_1,t_2,t_3])
value=sp.Matrix(3,1,[t_10,t_20,t_30])

for i in range(0,50):
    func_value1=func_value.subs({theta1:t_1,theta2:t_2,theta3:t_3})
    #sp.pretty_print(func_value1)
    jacobian_inv1=jacobian_inv.subs({theta1:t_1,theta2:t_2,theta3:t_3})
    #sp.pretty_print(jacobian_inv1)
    diff=jacobian_inv1*func_value1
    value=guess-diff

   
    diff1=abs(value[0,0]-guess[0,0])
    diff2=abs(value[1,0]-guess[1,0])
    guess[0]=value
    guess[0, 0] = value[0, 0]
    guess[1, 0] = value[1, 0]
    guess[2, 0] = value[2, 0]
    
sp.pretty_print(value)
theta_1=value[0,0]
theta_2=value[1,0]
theta_3=value[2,0]

#Resucing the angles below 360 degrees
j=0
while j==0:
    if(theta_1>float(np.pi) or theta_2>float(np.pi) or theta_3>float(np.pi)):
        if(theta_1%(2*np.pi)<=np.pi):
            theta_1=theta_1%(2*np.pi)
        else:
            theta_1=theta_1%(2*np.pi)-(2*np.pi)

        if(theta_2%(2*np.pi)<=np.pi):
            theta_2=theta_2%(2*np.pi)
        else:
            theta_2=theta_2%(2*np.pi)-(2*np.pi)

        if(theta_3%(2*np.pi)<=np.pi):
            theta_3=theta_3%(2*np.pi)
        else:
            theta_3=theta_3%(2*np.pi)-(2*np.pi)
    if(theta_1<float(np.pi) or theta_2<float(np.pi) or theta_3<float(np.pi)):
        j=1

a=sp.cos(theta_1+theta_2+theta_3)-sp.cos(orientation)
print(a)
# Convering the values above 0 degrees
k=0
while k==0:
    if(theta_1 < float(-np.pi) or theta_2 < float(-np.pi) or theta_3 < float(-np.pi)):
        if(theta_1< float(-np.pi)):
            theta_1=theta_1+float(2*pi)
        else:
            theta_1 = theta_1
        if(theta_2< float(-np.pi)):
            theta_2 = theta_2+float(2*pi)
        else:
            theta_2 = theta_2
        if(theta_3< float(-np.pi)):
            theta_3 = theta_3+float(2*pi)
        else:
            theta_3 = theta_3
    if(theta_1 >= float(-np.pi) and theta_2 >=float(-np.pi) and theta_3 >= float(-np.pi)):
        k=1

final_angles=sp.Matrix(3,1,[theta_1,theta_2,theta_3])
sp.pretty_print(final_angles)

fig=plt.figure()
axis=plt.axes(xlim=(-15,15),ylim=(-15,15))
link1,=axis.plot([],[],lw=1,marker='o')
link2=axis.plot([],[],lw=1,marker='o')
link3=axis.plot([],[],lw=1,marker='o')

r1 =-1.2926
r2 =0.95865
r3 =0.57049 

l1,l2,l3=5,5,5
if(r1>=0):
    d1=np.linspace(0,r1,int(30*r1))
else:
    d1=np.linspace(0,abs(r1),int(30*abs(r1)))
    d1=d1*-1
if(r2>=0):
    d2=np.linspace(0,r2,int(30*r2))
else:
    d2=np.linspace(0,abs(r2),int(30*abs(r2)))
    d2=d2*-1
if(r3>=0):
    d3=np.linspace(0,r3,int(30*r3))
else:
    d3=np.linspace(0,abs(r3),int(30*abs(r3)))
    d3=d3*-1
l_d1,l_d2,l_d3=len(d1),len(d2),len(d3)
# 
l=l_d1+l_d2+l_d3
l1_xmax,l2_xmax=l1*np.cos(d1[l_d1-1]),l2*np.cos(d1[l_d1-1]+d2[l_d2-1])
l1_ymax,l2_ymax=l1*np.sin(d1[l_d1-1]),l2*np.sin(d1[l_d1-1]+d2[l_d2-1])

def animate(i):
    if(i<l_d1):
        x1=0
        y1=0
        x2=l1*np.cos(d1[i])
        y2=l1*np.sin(d1[i])
        x3=(l1+l2)*np.cos(d1[i])
        x4=(l1+l2+l3)*np.cos(d1[i])
        y3=(l1+l2)*np.sin(d1[i])
        y4=(l1+l2+l3)*np.sin(d1[i]) 
        link1.set_data([x1,x2,x3,x4],[y1,y2,y3,y4])
        return link1,
    if(i>=l_d1 and i<l_d1+l_d2):
        x1=0
        y1=0
        x2=l1_xmax
        y2=l1_ymax
        x3=l1_xmax+l2*np.cos(d1[l_d1-1]+d2[i-l_d1])
        x4=l1_xmax+(l2+l3)*np.cos(d1[l_d1-1]+d2[i-l_d1])
        y3=l1_ymax+l2*np.sin(d1[l_d1-1]+d2[i-l_d1])
        y4=l1_ymax+(l2+l3)*np.sin(d1[l_d1-1]+d2[i-l_d1])
        link1.set_data([x1,x2,x3,x4],[y1,y2,y3,y4])
        return link1
    elif(i<l and i>=l_d1+l_d2):
         x1=0
         y1=0
         x2=l1_xmax
         y2=l1_ymax
         x3=l1_xmax+l2_xmax
         x4=l1_xmax+l2_xmax+l3*np.cos(d1[l_d1-1]+d2[l_d2-1]+d3[i-l_d1-l_d2])
         y3=l1_ymax+l2_ymax
         y4=l1_ymax+l2_ymax+l3*np.sin(d1[l_d1-1]+d2[l_d2-1]+d3[i-l_d1-l_d2])
         link1.set_data([x1,x2,x3,x4],[y1,y2,y3,y4])
         return link1

anim =animation.FuncAnimation(fig, animate,frames = l, interval = 120)
fig.suptitle('Inverse Kinematics', fontsize=14)
plt.show()
