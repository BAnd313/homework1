#!/usr/bin/env python2
# license removed for brevity
import rospy
from homework1.msg import Template

def talker():
	pub = rospy.Publisher('/chatter', Template, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(1) # 10hz
	message = Template()
	while not rospy.is_shutdown():
		message.name = "Andrea"
		message.age = 100
		message.major = "Bachelor's degree in Computer Science "
		#rospy.loginfo(hello_str)
		pub.publish(message)
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
