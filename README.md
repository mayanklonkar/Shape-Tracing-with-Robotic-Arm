# Shape Tracing with Robotic Arm

## Description



In this project, we created a serial manipulator with 3 degrees of freedom that can draw shapes. The Arduino Mega is used to control the robotic arm, and Python is used to implement it.

<p align="center">
<image src="https://user-images.githubusercontent.com/108993449/197596223-350a1840-f1d7-459b-b260-47adfec11647.png" width="350" height="250">
  </p>

The main methods used during implementation of this project are-

- Forward Kinematics
- Inverse Kinematics
- Trajectory generation


##  Forward kinematics
In this section, we converted the joint angles (theta1, theta2, and theta3) to the end effector coordinate. For that, we took the following actions:

- Found the Denavit–Hartenberg parameters of 3 Dof manipulators.
- Using sympy (Symbolic python) created generalised homogeneous matrix and then substituited DH parameters to obtain the transform from frame three to frame zero.
- Obtained the equations of x and y in terms of joint angles and other parameters which will be further used for inverse kinematics.
<p align="center">
<image align="centre" src="https://user-images.githubusercontent.com/108993449/197388420-f2e78226-776f-4065-b925-2b68d35d149c.png" width ="500" height="300" >
  </p>
  
## Inverse Kinematics

We determined the joint angles necessary to move the end effector to a specific coordinate using inverse kinematics. To do that, we approximated using the Newton-Ralphson method.

- Used the two equations obtained from Forward kinmatics and third equation regarding the orientation of the end effector.
- Initial guesses were made for theta1, theta2, and theta3.
- Using a first-guess calculation and the Newton-Raphson equation, the function value matrix and Jacobian matrix were obtained and hence obtaining joint angle values for a   specific coordinate.
  
   <p float="left">
  <image src="https://user-images.githubusercontent.com/108993449/197811121-ad1f64e9-3854-4908-a465-049475868b55.png" width="350" height="300" />
  <image src="https://user-images.githubusercontent.com/108993449/197811059-eb77233b-4949-4b29-91eb-9f2f60a66e84.png" width="350" height="300" />
  </p>







## Trajectory Generation

Now, a trajectory must be created in order to trace shapes.

- Taking a simple line trajectory into consideration, we divided the line into a significant number of points, say 100.
- By doing this we obtained a straight line between 2 consecutive point instead of a arc.

The trajectory for various shapes, such as square, rectangle, and elipse, can be calculated using the same methodology as the line.

## Results-
  Following results were obtained -
  
  - Tracing a Line 
  <p float="left">
  <image src="https://user-images.githubusercontent.com/108993449/197814044-d463bc68-66a5-4228-83be-ac1eca8b7280.gif" width="350" height="300" />
  <image src="https://user-images.githubusercontent.com/108993449/197770862-09606c4b-78ee-4f71-bd50-0889e7a02df7.png" width="350" height="300" />
  </p>
  
  - Tracing a Rectangle
  <p float="left">
  <image src="https://user-images.githubusercontent.com/108993449/197806583-c9955128-aab8-4acd-9d82-a9241e00960f.gif" width="350" height="300" />
  <image src="https://user-images.githubusercontent.com/108993449/197806092-1db77428-1a5b-4b84-a474-aaedc0168a7d.png" width="350" height="300" />
  </p>
  
  - Tracing a Ellipse

<p float="left">
  <image src="https://user-images.githubusercontent.com/108993449/197807668-5c0c62b9-a8f3-44a7-b249-16c622de3707.gif" width="350" height="300" />
  <image src="https://user-images.githubusercontent.com/108993449/197809988-c352a60b-c43c-4a04-9a98-c9e1481790e3.png" width="350" height="300" />
  </p>
  
  - Tracing IvLabs
  <p align="center">
  <image align="centre" src="https://user-images.githubusercontent.com/108993449/197814860-974e0c4e-571a-4105-8171-3eaf3165e893.gif" width ="400" height="400" >
   </p>
  
