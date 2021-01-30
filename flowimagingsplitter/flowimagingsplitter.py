'''
	...This module will split the FlowCam collage images from COLLAGE_DIR... 
	...into single images with the same directory structure in OUTPUT_DIR... 
'''
import cv2
import numpy as np
import imutils
import os

def tif_files(collage_folder_path):
	'''Select only .t if files'''
	return [tf for tf in os.listdir(collage_folder_path) if tf.endswith('.tif') and not tf.endswith('bin.tif') and not tf.startswith('cal_') and not tf.startswith('rawfile_')]

def split_image(file_name, output_folder):
	'''Using OpenCV retreiving and saving single images from collage'''
	global i
	# reading image using OpenV
	img = cv2.imread(file_name)
	# convert image to gray scale and later apply thresholding 
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	ret,thresh1 = cv2.threshold(gray,1,255,cv2.THRESH_BINARY)
	# find contours after thresholding
	contours = cv2.findContours(thresh1,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
	contours = imutils.grab_contours(contours)
	# Sort contours from left to right and top-to-bottom of collage images
	sorted_contours = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[0] + cv2.boundingRect(ctr)[1] * img.shape[1])

	for cnt in sorted_contours:
		# Getting boundary box (x, y) cordinates followed by the width and height 
		x,y,w,h = cv2.boundingRect(cnt)
		# Reconstruct image with boundary box cordinates 
		img2 = img[y:y+h, x:x+w]
		# Getting filename without .tif ext
		# file_name = os.path.splitext(file_name)[0]
		save_path = os.path.join(output_folder, str(i) + ".jpg")
		i += 1
		# save image in output directory
		cv2.imwrite(save_path,img2)

def main(folder_name):
	'''Split particles collage images collected from flowCam and flowCam nano similar structure to its algorithm
	'''
	# Create the paths for the data and the output
	collage_folder_path = os.path.join(COLLAGE_DIR, folder_name)
	output_folder_path = os.path.join(OUTPUT_DIR, folder_name)

	# Create the output folder if it does not exists
	if not os.path.exists(output_folder_path):
		os.makedirs(output_folder_path)
	# indexing to start image number
	global i
	i = 1
	for file in tif_files(collage_folder_path):
		file = os.path.join(collage_folder_path, file)
		split_image(file, output_folder_path)
		
if __name__ == '__main__':
	# absolute directory of collage images
	COLLAGE_DIR = r''
	# output directory of single images
	OUTPUT_DIR = r''
	main("")
		
	print('Program Finished')
	