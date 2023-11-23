#!/usr/bin/env python3

import argparse
import rospy
from std_msgs.msg import String
from colorama import Fore,Back,Style

def main():

    # -------------------------------------------
    # Initialization
    # -------------------------------------------
    # Setup ROS
    pub = rospy.Publisher("topic_name", String, queue_size=10)

    rospy.init_node('publisher', anonymous=True)

    print_color = rospy.get_param("/highlight_text_color","MAGENTA")

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        message_to_send = "some content"

        rospy.loginfo(Fore.RED + message_to_send+ Style.RESET_ALL)
        pub.publish(message_to_send)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass