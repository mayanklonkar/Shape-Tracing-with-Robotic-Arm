import sympy as sp
from sympy.physics.mechanics import dynamicsymbols
from sympy.matrices import Matrix, eye
from sympy import *

a,d,alpha,l1,l2,l3,theta1,theta2,theta3,theta,x,y,z=dynamicsymbols('a d alpha l1 l2 l3 theta1 theta2 theta3 theta x y z')
A=[0,50,50]
trans_matrix=sp.Matrix([[sp.cos(theta),-sp.sin(theta)*sp.cos(alpha),sp.sin(theta)*sp.sin(alpha), a*sp.cos(theta)],
    [ sp.sin(theta), sp.cos(theta)*sp.cos(alpha),-sp.cos(theta)*sp.sin(alpha),a*sp.sin(theta)],
    [0, sp.sin(alpha),sp.cos(alpha),d],
    [0,0,0,1]])

trans_0_1=trans_matrix.subs({alpha:0,a:50,d:0,theta:theta1})

trans_1_2=trans_matrix.subs({alpha:0,a:50,d:0,theta:theta2})

trans_2_3=trans_matrix.subs({alpha:0,a:50,d:0,theta:theta3})

print("\n From frame 0 to 1")
sp.pretty_print(trans_0_1)
print("\n From frame 1 to 2")
sp.pretty_print(trans_1_2)
print("\n From frame 2 to 3")
sp.pretty_print(trans_2_3)
print("\n")

A=trans_0_1*trans_1_2
B=A*trans_2_3

print("\n")


simply= trigsimp(B)
print("Final transformation matrix from 0 to 3rd frame \n")
sp.pretty_print(simply)
