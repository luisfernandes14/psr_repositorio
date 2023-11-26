#!/usr/bin/env python3

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

    frequency= rospy.get_param("/publisher/frequency",1.0)
    rate = rospy.Rate(frequency)
    while not rospy.is_shutdown():
        message_to_send = "some content"
        
        
        print_color = rospy.get_param("/highlight_text_color","MAGENTA")
        
        rospy.loginfo(getattr(Fore, print_color) + message_to_send+ Style.RESET_ALL)
        
        rospy.logwarn("I think something is up")
        
        rospy.logerr("Something went wrong")
        
        pub.publish(message_to_send)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass