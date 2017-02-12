#!/usr/bin/env python
# coding=UTF-8
import cv2
import numpy as np

class test:
    def __init__(self, name, image):
        self.name = name
        self.image = image
        self.height = image.shape[0]
        self.width = image.shape[1]
        self.togray()
    def togray(self):
    	self.gray=cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
    	return self.gray
    def tobw(self, thresh):
        self.bw = cv2.threshold(self.gray, thresh, 255, cv2.THRESH_BINARY)[1]
        return self.bw
    def tobw_otsu(self):
        (self.bw_thresh, self.bw) = cv2.threshold(self.gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        #print self.bw_thresh
        return self.bw
    def calhistogram(self):
    	self.histogram = cv2.calcHist([self.gray],[0],None,[256],[0,256])
    	return self.histogram
    def calhistogram2(self):
    	bins = range(0,257)
    	self.histogram = np.histogram(self.gray, bins)
    	return self.histogram
    def calotsu(self):
    	hist = self.calhistogram2() #[v1, v2,....]   <-- hist[0][:]
    	                            #[0,1,2,..256]   <-- hist[1][:]
    	#h_val = [None] * len(h)
    	sumT = 0
    	#total = self.width*self.height
    	total = 1
    	h_val = [None] * 257
    	for i in range(0,256):
    		h_val[i] = hist[0][i] / float(self.width*self.height)
    	for i in range(0,256):
			sumT += i * h_val[i]
        weightB, weightF = 0, 0
        sumB,sumF = 0,0
        meanB,meanF = 0,0
        varBetween = 0.0
        current_max = 0
        threshold = 0
        for i in range(0,256):
            weightB += h_val[i]
            weightF = total - weightB
            if weightB == 0:
            	continue
            if weightF == 0:
                break
            sumB += i*h_val[i]
            sumF = sumT - sumB
            meanB = sumB/weightB
            meanF = sumF/weightF
            varBetween = weightB * weightF
            varBetween *= (meanB-meanF)*(meanB-meanF)
            if varBetween > current_max:
                current_max = varBetween
                threshold = i
        return threshold
    def find_corner(self):
    	y = 0
    	x = 0
    	wind_sz = 5
    	wind_bnd = (wind_sz - 1) / 2
        ptr = np.array([wind_sz, wind_sz], dtype=np.int)
    	#ptr = [None] * wind_sz
    	index = 0
    	sum_b = 0
        for k in range(0-wind_bnd,wind_bnd+1):
            for l in range(0-wind_bnd,wind_bnd+1):
            	ptr[0][0] = 1
                #ptr[k+wind_bnd][l+wind_bnd] = self.gray[y+k][x+l]
            #print ptr[index]
            index += 1
        for i in range(0,wind_sz):
            if ((i==0) or (i==(wind_sz-1))):
                print i
                for j in range(0-wind_bnd,wind_bnd+1):
                    print j
                    #if(ptr[i][x+j] == 0):
                    #    sum += 1
                    #else:
                    #    continue
            #if((i == 0) || (i==(wind_sz-1)))
                #for (int j = (0-wind_bnd); j <= wind_bnd; ++j)
    	#for w in range(0,self.width):
        #    for h in range(0,self.height):
        #    	print self.gray[w][h]



    def __str__(self):
    	return 'This is neo test class: {0} {1}x{2}'.format(self.name,self.width,self.height)
