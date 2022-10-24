# Shape Tracing with Robotic Arm

## Description


This project was part of Summer Intern Program at IvLabs, the AI and Robotics lab of VNIT.

<image src="https://user-images.githubusercontent.com/108993449/197596223-350a1840-f1d7-459b-b260-47adfec11647.png" width="400" height="300">

In this project we have made a 3 link robotic arm which can draw shapes . We have used a Arduino Mega to control the Robotic arm.

The two main methods used during implementation of this project are-

1) Forward Kinematics
2) Inverse Kinematics


## 1. Forward kinematics
In this part we have transformed the given joint angles (theta1,theta2,theta3) to the coordinate of the end effector.For that we deployed following steps-

- Found the DH paramter of our 3 link robot.
- Obtained a generalised Homogeneous Matrix using sympy (Symbolic Python)
- Substituited the DH parmeter value and obtained transform for 3rd frame to 0th frame.
- Obtained the equations of x and y in terms of joint angles and other parameters which will be used for inverse kinematics.


<image src="https://user-images.githubusercontent.com/108993449/197388420-f2e78226-776f-4065-b925-2b68d35d149c.png" width ="500" height="300">

## 2. Inverse Kinematics

Using Inverse Kinematics we obtained the joint angles required to move end effector to a particular coordinate . For that we used Newton Ralphson Method of Approximation.

- Used the two equations obtained from Forward kinmatics and third equation regarding the orientation of the end effector.
- Took intial guess of theta1,theta2 and theta3.
- Obtained function value matrix and Jacobian matrix at intial guess and used the following equation of Newton Raphson.



- Obatained values of joint amgles for a particular coordinate.






## Trajectory Generation

Now , to trace shapes it is important to make a trajectory.

- Consider a simple line trajectory,we divide the line into large number of points say 100 .
- This is done to obtain straight line between two points instead of arc.

Following same concept as line ,trajectory for other shapes like square ,rectangle , elipse can be obtained.
