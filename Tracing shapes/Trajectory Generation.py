from sympy import *
import sympy as sp
from sympy import sin,cos
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import numpy as np


def invkinematics(x_f,y_f,orien):

    t_1=1.4
    t_2=1.4
    t_3=1.4
 

    f1=l1*cos(theta1)+l2*cos(theta1+theta2)+l3*cos(theta1+theta2+theta3) -x_f
    f2=l1*sin(theta1)+l2*sin(theta1+theta2)+l3*sin(theta1+theta2+theta3) -y_f
    f3=theta1+theta2+theta3-orien

    func_value=sp.Matrix(3,1,[f1,f2,f3])

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
    jacobian_inv=jacobian.inv()
    func_value1=func_value.subs({theta1:t_1,theta2:t_2,theta3:t_3})
    guess=sp.Matrix(3,1,[t_1,t_2,t_3])
    value=sp.Matrix(3,1,[0,0,0])

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
    angle=sp.Matrix(3,1,[0,0,0])
    angle[0,0]=in_range(value[0,0])
    angle[1,0]=in_range(value[1,0])
    angle[2,0]=in_range(value[2,0])

    theta_1.append(angle[0,0])
    theta_2.append(angle[1,0])
    theta_3.append(angle[2,0])
    
    print(7)
    # sp.pretty_print(angle)
    # error=sp.cos(angle[0,0]+angle[1,0]+angle[2,0])-sp.cos(orien)
    # print(error)
    return(angle)


def in_range(a):
      if(a%(2*float(sp.pi))<=float(sp.pi)):
        a=a%(2*float(sp.pi))
      else:
        a=a%(2*float(sp.pi))-(2*float(sp.pi))
      return a

def trace_line():
    x_points=np.linspace(-5,4,100)
    y_points=np.linspace(22,22,100)
    orien_line=np.linspace(2.245,1.2472,1)
    print(3)
    
    for i in range(0,100):
        invkinematics(x_points[i],y_points[i],orien_line[i])
        print(i)

def trace_rectangle():
    side_x_1=np.linspace(8,14,50)
    #y coordinate being constant =22
    side_y_1=22
    side_ori_1=1.57

    #x coordinate being constant=14
    side_x_2=14
    side_y_2=np.linspace(22,18,50)
    side_ori_2=0.75

    side_x_3=np.linspace(14,8,50)
    #y coordinate being constant =18
    side_y_3=18
    side_ori_3=1.57

    #x coordinate being constant=14
    side_x_4=8
    side_y_4=np.linspace(18,22,50)
    side_ori_4=0.75
    i=0
    for i in range (0,4):
        print(i)
        if(i==0):
            for j in range(0,50):
                invkinematics(side_x_1[j],side_y_1,side_ori_1)
        if(i==1):
            for k in range(0,50):
                invkinematics(side_x_2,side_y_2[k],side_ori_2)
        if(i==2):
            for m in range(0,50):
                invkinematics(side_x_3[m],side_y_3,side_ori_3)
        if(i==3):
            for n in range(0,50):
                invkinematics(side_x_4,side_y_4[n],side_ori_4)
        
 
if __name__=="__main__":

    theta1,theta2,theta3=sp.symbols('theta1,theta2,theta3')
    theta_1=[]
    theta_2=[]
    theta_3=[]
    l1,l2,l3=9.7,8.4,7.7  # links lengths for our planar robotic arm

    #To find Inv kinematics of a point

    # x_f=float(input("enter the x cordinate of end effector"))
    # y_f=float(input("enter the y coordinate of end effector"))
    # orien=float(input("enter the orientation of end effector"))

    # invkinematics(x_f,y_f,orien)
    
    #Tracing a line
    # trace_line()

    #Tracing a Rectangle
    trace_rectangle()
    
    print(theta_1)
    print(theta_2)
    print(theta_3)
    