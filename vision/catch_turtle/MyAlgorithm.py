from sensors import sensor
import cv2
import numpy as np
import colorsys
from PIL import Image, ImageOps
import math

class MyAlgorithm():
    def __init__(self, sensor):
        self.sensor = sensor


    def execute(self):

        input_image = self.sensor.getImage()
        if input_image != None:		
		# Convert BGR to HSV
		hsv = cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)

		# define range of orange and green color in HSV

		lower_orange = np.array([108,220,69], dtype=np.uint8)
		upper_orange = np.array([120, 255,110], dtype=np.uint8)

		lower_green = np.array([20,193,65], dtype=np.uint8)
		upper_green = np.array([70, 227,100], dtype=np.uint8)

		#Do the mask
		mask = cv2.inRange(hsv, lower_orange, upper_orange)
		mask2 = cv2.inRange(hsv, lower_green, upper_green)
		maskTot = mask + mask2


		#Convert the mask to RGB for show in ColorFilter. Create a total mask(with the two colors)
		maskRGB = cv2.bitwise_and(input_image,input_image, mask= mask)
		mask2RGB = cv2.bitwise_and(input_image,input_image, mask= mask2)
		maskRGBTot = maskRGB + mask2RGB


		#
		#AQUI SACAMOS EL CENTRO DE LA IMAGEN TOTAL.
		#
		ximg = 159
		yimg = 119


		momentsgreen=cv2.moments(mask2)
		areagreen= momentsgreen['m00']

		momentsOrange = cv2.moments(mask)
		areaOrange = momentsOrange['m00']

		momentsTot = cv2.moments(maskTot)
		areaTot= momentsTot['m00']

		#if(areaTot==0 and areaOrange ==0 and areagreen ==0):
		#	self.sensor.sendCMDVel(0,0,0.5,0.3,0,0)

		if(areaTot>200 and areagreen> 0 and areaOrange > 0 ):
			#Buscamos los centros
			x = int(momentsTot['m10']/momentsTot['m00'])
			y = int(momentsTot['m01']/momentsTot['m00'])

			xOrange = int(momentsOrange['m10']/momentsOrange['m00'])
			yOrange = int(momentsOrange['m01']/momentsOrange['m00'])

			xGreen = int(momentsgreen['m10']/momentsgreen['m00'])
			yGreen = int(momentsgreen['m01']/momentsgreen['m00'])


			kernel = np.ones((3,3),np.uint8)
			maskRGBTot = cv2.dilate(maskRGBTot,kernel,iterations = 2)
			maskRGB = cv2.dilate(maskRGB,kernel,iterations = 2)
			mask2RGB = cv2.dilate(mask2RGB,kernel,iterations = 2)
			maskRGBTot = maskRGBTot - maskRGB - mask2RGB

			#Escribimos el valor de los centros
			cv2.rectangle(maskRGBTot, (x,y), (x+1,y+1),(0,0,255), 1)

			'''
			if(areaTot < 801720):
				self.sensor.sendCMDVel(-0.3*(x-ximg)/65,-0.3*(y-yimg)/65,-0.6,0,0,0)
			else:
				self.sensor.sendCMDVel(-0.1*(x-ximg)/65,-0.1*(y-yimg)/65,0,0,0,0)
			'''

			#size= 160,120
			#res = cv2.resize(maskRGBTot,(2*maskRGBTot, 2*maskRGBTot)
			res = cv2.resize(maskRGBTot,None,fx=0.3, fy=0.3, interpolation = cv2.INTER_CUBIC)
			pix = res
	
			iMin=0
			i2Min=0
			iMax=0
			i2Max=0
			

			jMin=0
			j2Min=0
			jMax=0
			j2Max=0
			for i in range(0,71):
				for j in range (0,95):
					if (pix[i,j][0] != 0 or pix[i,j][1] != 0 or pix[i,j][2] != 0):
						if(iMin ==0):
							iMin=i
							i2Min=j
						if(i<iMin):
							iMin=i
							i2Min=j
						if(iMax ==0):
							iMax=i
							i2Max=j
						if(i>iMax):
							iMax=i
							i2Max=j

						if(jMin ==0):
							jMin=j
							j2Min=i
						if(j<jMin):
							jMin=j
							j2Min=i
						if(jMax ==0):
							jMax=j
							j2Max=i
						if(j>jMax):
							jMax=j
							j2Max=i

			cv2.line(res,(i2Min,iMin),(i2Max,iMax),(0,0,255),2)
			cv2.line(res,(jMin,j2Min),(jMax,j2Max),(0,0,255),2)

			p1x= i2Max - i2Min
			p2x= iMax - iMin

			p1y= jMax - jMin
			p2y= j2Max - j2Min
		
			
			r = math.acos(((p1x*p1y)+(p2x*p2y))/(math.sqrt(p1x**2 + p2x**2)*math.sqrt(p1y**2 + p2y**2)))

			if(abs(r) < 1.70):
				print("baliza ;)", r)		

		self.sensor.setColorImage(res)
		self.sensor.setThresoldImage(maskRGBTot)

	    	'''
	        If you want show a thresold image (black and white image)
	        self.sensor.setThresoldImage(bk_image)
	        '''

