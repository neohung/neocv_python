#!/usr/bin/env python2.7
import numpy as np
import cv2
from matplotlib import pyplot as plt

import neo

def main():
        """ Main behaviour """
        print("test")
        
        image = cv2.imread("lena.png")
        #image = cv2.imread("original-kps.jpg")
        #image = cv2.imread("threshold.jpg")
        #image = cv2.imread("otsu_test.png")
        
        n = neo.test("t1",image)
        print n
        #gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#        fast = cv2.FastFeatureDetector_create()
#        keypoints = fast.detect(gray,None)
#        image2 = cv2.drawKeypoints(gray, keypoints, image, color=(255,0,0))
        #should be 163
        #otsu = n.calotsu()
        #otsu = n.caltest()
        #plt.plot(h,color = 'b')
        #plt.xlim([0,256])
        #plt.show()
        n.find_corner()
        cv2.imshow("Image",n.tobw(n.calotsu()))
        #cv2.imshow("Image",n.tobw_otsu())
#        np_pts = np.asarray([kp.pt for kp in keypoints])
#        print(np_pts[0])
#        index = []
#        for point in keypoints:
#          temp = (point.pt, point.size, point.angle, point.response, point.octave, point.class_id)
#          index.append(temp)
#        print(index[0])
        #kps = []
        #for point in index:
        #  temp = cv2.KeyPoint(x=point[0][0],y=point[0][1],_size=point[1], _angle=point[2], _response=point[3], _octave=point[4], _class_id=point[5])
        #  kps.append(temp)
        #image3 = cv2.drawKeypoints(gray, kps, image, color=(0,0,255))
        #-------------------------------------------------
        #cv2.imwrite('fast_false.png',image2)
        cv2.waitKey(0)

if __name__ == "__main__":
        main()
