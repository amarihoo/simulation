#!/usr/bin/env python

# import roslib
# roslib.load_manifest('my_package')
import sys

import cv2
from cv_bridge import CVBridge, CVBridgeError

import rospy

# ROSPY NODE meant to get camera feed from image_raw topic, 
# find block with CV, and send coordinates to 

class imagery:
 
    def __init__(self):
        self.cv_image = None
        
        self.pub = rospy.Publisher("block_location", String)

        self.bridge = CVBridge()
        self.image_sub = rospy.Subscriber("image_raw", Image, self.callback)
 
    def callback(self, data):
        try:
            self.cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")

        except CVBridgeError as error:
            print(error)

        cv2.imshow("Image window", cv_image)
        cv2.waitKey(3)

        pose = analyze(cv_image)

        pub.publish(pose)

    def analyze(self, img):
        continue
        print("TODO")

    def test():
        rospy.loginfo("Success!!!!! $$$$$$$$$$$")


def main():
    print("initialize node... ")
    rospy.init_node('imagery', anonymous=True)

    ip = imagery()

    ip.test()

    
    try:
        rospy.spin()
    except KeyboardInterrupt:
       print("Shutting down")

    cv2.destroyAllWindows()

if __name__ == '__main__':
main()