#! /usr/bin/env python

import rospy                               # Import the Python library for ROS
from geometry_msgs.msg import Twist        # Import the Twist message from the geometry_msgs package

rospy.init_node('move_robot_node')         # Initiate a Node named 'move_robot_node'
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)    
                                           # Create a Publisher object, that will publish on the /cmd_vel topic
                                           # messages of type Twist
rate = rospy.Rate(2)                       # Set a publish rate of 2 Hz
Move = Twist()                            # Create a var of type Int32
Move.linear.x = 1                           # Move the robot with linear velocity in the x axis
Move.angular.z = 1                      # Move the robot with an angular velocity in the z axis

while not rospy.is_shutdown():             # Create a loop that will go until someone stops the program execution
  pub.publish(Move)                       # Publish the message within the 'count' variable
  rate.sleep()   