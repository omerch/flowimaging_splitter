import cv2 as cv
import numpy as np
from PIL import Image
import imutils
import os 
from os.path import isfile

class FlowImagingSplitter:
	"""FlowImagingSplitter class for splitting collage images(*.tif) from COLLAGE_DIR into 
	single images in the OUTPUT_DIR. 

	Attributes:
		collage_dir: Absolute path of the collage directory
		output_dir = Absolute path of the output directory
	"""
	def __init__(self, collage_dir, output_dir):
		self.collage_dir = collage_dir
		self.output_dir = output_dir
		# Create the paths for the data and the output
		self.collage_folder_path = os.path.join(self.collage_dir, "")
		self.output_folder_path = os.path.join(self.output_dir, "")	
	
	def select_tif_images(self, collage_path):
		# Selecting only *(.tif) image files excluding *(.bin.tif, cal_, rawfile_)
		return [tf for tf in os.listdir(collage_path) if tf.endswith(".tif") and not tf.endswith("bin.tif") and not  tf.startswith("cal_") and not tf.startswith("rawfile_")]

	def split_image(self, file_name, output_folder):
		"""Using OpenCV and countours to split the collage image files into single images. First 
		image in the collage image files will be the last image. i.e (#9_7_300_000001.tif_1)
		collage image name = #9_7_300_000001
		last image of the collage image files = .tif_1

		Args:
			file: collage image file
			output_folder: outputs directory 
		"""
		img = cv.imread(file_name, -1)
		gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
		ret,thresh1 = cv.threshold(gray,1,255,cv.THRESH_BINARY)
		contours = cv.findContours(thresh1,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
		contours = imutils.grab_contours(contours)
		i = 1
		for cnt in contours:
			x,y,w,h = cv.boundingRect(cnt)
			img2 = img[y:y+h, x:x+w]
			save_path = os.path.join(output_folder, os.path.basename(os.path.splitext(file_name)[0]) + "_"  + str(i) + ".tif")
			i += 1
			cv.imwrite(save_path,img2)

	def apply(self):
		"""Method to structure directory paths and select only *(.tif) images and not those 
		image files start or endwith *(.bin.tif, cal_, rawfile_)
		"""
		# Create output folder if it does not exists
		if not os.path.exists(self.output_folder_path):
			os.makedirs(output_folder_path)

		# Selecting only *(.tif) image files excluding *(.bin.tif, cal_, rawfile_)
		tif_files = self.select_tif_images(self.collage_folder_path)

		for file in tif_files:
			file = os.path.join(self.collage_folder_path, file)
			print(file)
			self.split_image(file, self.output_folder_path)

