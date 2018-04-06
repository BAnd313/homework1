#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String
from homework1.msg import Template


choice = ''


def printout(data):
	string = "\nDati studente\n"
	
	if choice == 'a':
		string += "Nome: %s\nEtà: %s\nCorso di laurea: %s\n" % (data.name, data.age, data.major)
	elif choice == 'n':
		string += "Nome: %s" % (data.name)
	elif choice == 'e':
		string += "Età: %s" % (data.age)
	elif choice == 'c':
		string += "Corso di laurea: %s" % (data.major)
	
	#rospy.loginfo(string)
	print(string)
		

def selectcontent(data):
    global choice
    
    choice = data.data
    

def listener():

	# In ROS, nodes are uniquely named. If two nodes with the same
	# node are launched, the previous one is kicked off. The
	# anonymous=True flag means that rospy will choose a unique
	# name for our 'listener' node so that multiple listeners can
	# run simultaneously.
	rospy.init_node('listeners', anonymous=True)

	rospy.Subscriber("chatter", Template, printout)
	rospy.Subscriber("controller", String, selectcontent)

	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()


if __name__ == '__main__':
    listener()
