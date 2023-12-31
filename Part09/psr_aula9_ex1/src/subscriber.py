#!/usr/bin/env python3
import argparse
import rospy
from std_msgs.msg import String
from colorama import Fore,Style

def callback(message_received):
    print_color = rospy.get_param("/highlight_text_color","MAGENTA")
    rospy.loginfo(getattr(Fore, print_color) + message_received.data + Style.RESET_ALL)

def main():

    # -------------------------------------------
    # Initialization
    # -------------------------------------------

    # Setup of argparse
    # Setup ROS
    rospy.init_node('subscriber', anonymous=True)    

    rospy.Subscriber("topic_name", String, callback)


    # -------------------------------------------
    # Execution
    # -------------------------------------------
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

    # -------------------------------------------
    # Termination
    # -------------------------------------------

if __name__ == '__main__':
    main()