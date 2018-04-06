#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# license removed for brevity
import rospy, signal, sys, readchar
import tty, termios, select
from std_msgs.msg import String

lastchoice = ''

def sigint_callback():
    rospy.signal_shutdown("Ctrl+C detected")
    sys.exit(0)


def controller():
    rate = rospy.Rate(1) # 1hz
    global lastchoice

    choice = readchar.readkey()

    # SIGINT handler
    if choice == '\x03':
        sigint_callback()

    if choice in "enac":
        if choice != lastchoice:
            rospy.loginfo("HAI SELEZIONATO %s" % choice)
            lastchoice = choice

        pub.publish(choice)

    #rate.sleep()

if __name__ == '__main__':
    pub = rospy.Publisher('controller', String, queue_size=10)
    rospy.init_node('controller', anonymous=True)

    string = """\n\r
Digita la tua scelta:\n\r
- 'a': stampa tutti i dati
- 'n': stampa il nome dello studente
- 'e': stampa l'età dello studente
- 'c': stampa il corso di laurea dello studente\n\r
Ctrl+C per terminare
    """

    rospy.loginfo(string)

    while True:
        controller()
