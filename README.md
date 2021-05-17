# Pick and Place using a 4DoF Robotic Manipulator
 

### Problem Statement
Create a 3-Dof/4-Dof robotic arm with a gripper from scratch and implement pick and place using MoveIt for a cube container. Assume all the required dimensions and details of the links and cube appropriately

### Assumptions 
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

### Methodology 

1. First create the parts in Fusion 360 or your desired CAD software. <br>
2. Exported the parts in .step extension so that it can be used in solidworks. <br>
3. Create a new assembly in Solidworks using the exported parts. <br>
4. Create a URDF File using the URDF plugin in solidworks. <br>
5. Upload the generated a folder on a drive so that you can use it later in Linux. <br>
 (Make sure you have ROS and MoveIt installed before this step) <br>
5. Create a setup in MoveIt using MoveIt setup Assisatant and URDF Files.<br>
6. Write a Python or C++ code for performing the pick and place operation. <br>
7. Run the rviz-MoveIt in one terminal and the python code in another terminal to see the output. <br>

### Manipulator  

### Video Output
