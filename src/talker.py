#!/usr/bin/env python2
# license removed for brevity
import rospy
from homework1.msg import Template

message = Template()


def setMessage() :
	message.name = "Andrea"
	message.age = 100
	message.major = "Bachelor's degree in Computer Science "


def talker():
	pub = rospy.Publisher('/chatter', Template, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(1) # 1hz

	while not rospy.is_shutdown():
		setMessage()
		#rospy.loginfo(message)
		pub.publish(message)
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
