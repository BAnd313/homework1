#!/usr/bin/env python2
# license removed for brevity
import rospy
from homework1.msg import Student

message = Student()


def setMessage() :
	# This is an example with only one student
	message.name = "Andrea"
	message.age = 21
	message.major = "Laurea in Informatica"


def talker():
	pub = rospy.Publisher('/publisher', Student, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(1) # 1hz

	while not rospy.is_shutdown():
		setMessage()
		rospy.loginfo(message)
		pub.publish(message)
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
