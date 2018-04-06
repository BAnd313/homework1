#!/usr/bin/env python2
# license removed for brevity
import rospy, signal, sys, readchar
from std_msgs.msg import String


def sigint_callback():
    sys.exit(130)


def controller():
	pub = rospy.Publisher('controller', String, queue_size=10)
	rospy.init_node('controller', anonymous=True)
	rate = rospy.Rate(1) # 1hz
	
	#choice = raw_input("Digit a command: ")
	choice = readchar.readkey()
	
	# SIGINT handler
	if choice == '\x03':
	    sigint_callback()
	
	if choice in "enac":
	    #rospy.loginfo(choice)
	    pub.publish(choice)
	
	#rate.sleep()

if __name__ == '__main__':
    
    while True:
	    controller()
