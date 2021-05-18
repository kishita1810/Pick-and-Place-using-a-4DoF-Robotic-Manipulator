# Pick and Place using a 4DoF Robotic Manipulator
 

## Problem Statement
Create a 3-Dof/4-Dof robotic arm with a gripper from scratch and implement pick and place using MoveIt for a cube container. Assume all the required dimensions and details of the links and cube appropriately

## Assumptions 
Base: 
Diameter = 800 mm,
Thickness = 200 mm

Link_1:
Length = 800 mm, 
Width = 400 mm,
Thickness = 200 mm

Link_2:
Length = 900 mm, 
Width = 300 mm,
Thickness = 200 mm

Link_3:
Length = 750 mm, 
Width = 250 mm,
Thickness = 200 mm

Vacuum Gripper:
Outer Radius = 200 mm,
Inner Radius = 100 mm


Assuming the box is placed on certain height and not on ground.<br>
Assuming a cube of 400 mm is to be picked.

## Methodology 

You can download all the files and skip to step 6.

1. First create the parts in Fusion 360 or your desired CAD software. <br>
2. Export the parts in .step extension so that it can be used in solidworks. <br>
3. Create a new assembly in Solidworks using the exported parts. <br>
4. Create a URDF File using the URDF plugin in solidworks. <br>
5. Upload the generated a folder on a drive so that you can use it later in Linux. <br>
 (Make sure you have ROS and MoveIt installed before this step) <br>
6. Create a catkin workspace (internship) and build it.<br>
7. Add the generated urdf folder (robot_final_urdf) in the src folder of the workspace.  <br>
9. Create a package (pkg_internship_bot) and a folder called scripts to store the code files. <br>
10. Build the workspace once again. <br>
11. Create a setup in MoveIt using MoveIt setup Assisatant and URDF Files.<br>
12. Save the generated package (pkg_moveit_robot) in the src folder of the workspace. <br>
13. Once again build the workspace. <br>
14. Write a Python or C++ code for performing the pick and place operation and save it in the scripts folder. <br>
15. Run the rviz-MoveIt in one terminal and the python code in another terminal to see the output. <br>

### Command to open MoveIt setup Assistant:<br>
roslaunch moveit_setup_assistant setup_assistant.launch


### Command to launch rviz-MoveIt:<br>
roslaunch pkg_moveit_robot demo.launch


### Command to run python code:<br>
rosrun pkg_internship_bot internship.py


## Manipulator  

#### Image:
![image](https://user-images.githubusercontent.com/78917282/118496328-a7266280-b741-11eb-9ed5-3050d23e9dde.png)

#### Video:
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/-NfOZPfUFLA/0.jpg)](https://www.youtube.com/watch?v=-NfOZPfUFLA)


## Video Output

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/bBtZ40Qu28w/0.jpg)](https://www.youtube.com/watch?v=bBtZ40Qu28w)

## Google Drive Link with all the files

https://drive.google.com/drive/folders/1pgNGCP11WMNUuV7l_mr3C8NVQqc5NLha?usp=sharing
