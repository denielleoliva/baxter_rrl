#!/usr/bin/python3

import rospy
import sensor_msgs

current_joint_state = None

def record_joint_state(msg):
    global current_joint_state
    current_joint_state = msg

if __name__ == '__main__':
    rospy.init_node("joint_state_get")
    rospy.Subscriber("robot/joint_states", sensor_msgs.JointState, record_joint_state)

    while (current_joint_state == None):
        print("waiting for joint_state")
    print(current_joint_state)