#! /usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

#making an object of class move_group
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial',
                anonymous=True)

robot = moveit_commander.RobotCommander()

#setting the planning scence
scene = moveit_commander.PlanningSceneInterface()

group_name = "robot_planning_group"
group = moveit_commander.MoveGroupCommander(group_name)

display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                               moveit_msgs.msg.DisplayTrajectory,
                                               queue_size=20)


#printing the relevant robot information
planning_frame = group.get_planning_frame()
print "============ Reference frame: %s" % planning_frame


eef_link = group.get_end_effector_link()
print "============ End effector: %s" % eef_link

group_names = robot.get_group_names()
print "============ Robot Groups:", robot.get_group_names()

print "============ Printing robot state"
print robot.get_current_state()
print ""

#adding the box in the planning scence 
box_pose = geometry_msgs.msg.PoseStamped()
box_pose.header.frame_id = "base_link"
box_pose.pose.position.x = 0.72
box_pose.pose.position.y = -1.15
box_pose.pose.position.z = -1.70
box_pose.pose.orientation.x = -0.226801
box_pose.pose.orientation.y = -0.607593
box_pose.pose.orientation.z = 0.754102
box_pose.pose.orientation.w = -0.103549
box_name = "container_cube"
scene.add_box(box_name, box_pose, size=(0.45, 0.45, 0.45))


#setting the joint values of the robot to the start position
joint_goal = group.get_current_joint_values()
joint_goal[0] = 0
joint_goal[1] = -pi/6
joint_goal[2] = 0
joint_goal[3] = 0

#calling the go method
group.go(joint_goal, wait=True)

# Calling ``stop()`` ensures that there is no residual movement
group.stop()

#setting the joint values of the robot to the pick position
joint_goal = group.get_current_joint_values()
joint_goal[0] = 0
joint_goal[1] = pi/6
joint_goal[2] = pi/3
joint_goal[3] = 0

group.go(joint_goal, wait=True)

group.stop()

#attching the box to the end effector(vaccum gripper) [Plicking the cube container]
grasping_group = 'end_effector'
touch_links = robot.get_link_names(group=grasping_group)
scene.attach_box(eef_link, box_name, touch_links=touch_links)

#setting the joint values of the robot to the drop position:
joint_goal = group.get_current_joint_values()
joint_goal[0] = -pi/2
joint_goal[1] = pi/6
joint_goal[2] = pi/3
joint_goal[3] = -pi/6

group.go(joint_goal, wait=True)

group.stop()

#detaching the box from the end effector(vaccum gripper) [Placing the cube container]
scene.remove_attached_object(eef_link, name=box_name)

#setting the joint values of the robot to the home position: [Going to the start position]
joint_goal = group.get_current_joint_values()
joint_goal[0] = 0
joint_goal[1] = -pi/6
joint_goal[2] = 0
joint_goal[3] = 0

group.go(joint_goal, wait=True)

group.stop()

rospy.sleep(5)

#removing the box from the planning scence 
scene.remove_world_object(box_name)

rospy.sleep(5)

#deleting the object and closing the program
moveit_commander.roscpp_shutdown()