import xml.etree.ElementTree as ET
import os
import argparse 
import shutil
import random
import string
from PIL import Image


N = 20 # Length of random string name for txt and jpg files.
damage_counter = 0 # Global counter of damaged xml files 


def img2jpg(img_file_path):
	'''
	Convert and replace any supported PIL image by JPG
	Alpha channel in png problem: https://github.com/python-pillow/Pillow/issues/2609#issuecomment-313922483
	'''
	image = Image.open(img_file_path)
	fill_color = 255  #Background color of alpha channel
	if image.mode in ('RGBA', 'LA'):
		background = Image.new(image.mode[:-1], image.size, fill_color)
		background.paste(image, image.split()[-1])
		image = background
		
	jpg_file_path = img_file_path.split('.')[0] + '.jpg'
	os.remove(img_file_path) 
	image.save(jpg_file_path, quality=95)
	

def scale_bndbox(width, height, limits):
	'''
	Helper function that convert absulte coordinates of boundary box (VOC format) 
	to the relative (YOLO format) <x>, <y>, <width>, <height>.
	Atention: <x> <y> - are center of rectangle (are not top-left corner).
	'''
	xmin, ymin, xmax, ymax = limits
	dw = 1./width
	dh = 1./height
	x = (xmin + xmax)/2.0
	y = (ymin + ymax)/2.0
	w = xmax - xmin
	h = ymax - ymin
	x = x*dw
	w = w*dw
	y = y*dh
	h = h*dh
	return (x,y,w,h)

def create_annotation(file_path, yolo_labels_dir):
	'''
	Read xml annotation file and extract from it index labels (encoded object names) 
	and there boundary boxes in YOLO format
	'''
	global damage_counter
	
	tree = ET.parse(file_path)
	root = tree.getroot()
	size = root.find('size')
	width = int(size.find('width').text)
	height = int(size.find('height').text)
	
	# Check that xml file have normal shape parameters
	if width == 0 or height == 0:
		damage_counter += 1
		print('File with corrrapted size was detected')
		return None
		
	# Check that corresponded jpg file exists
	print(file_path.split('.')[0] + '.jpg')
	if not os.path.exists(file_path.split('.')[0] + '.jpg'):
		print('JPG file doean`t exist, skip xml file')
		return None
			
	# create file for yolo label
	file_name = file_path.split('/')[-1].split('.')[0]
	generated_name = ''.join(random.sample(string.ascii_uppercase + string.digits, k=N))
	f= open(os.path.join(yolo_labels_dir, (generated_name + ".txt")),"w+")
	
	for obj in root.iter('object'):
		difficult = int(obj.find('difficult').text)
		name = obj.find('name').text
		if (name in classes) and (difficult == 0):  #check that we have non-problematic image
			
			src = file_path.split('.')[0] + '.jpg'
			dst = os.path.join(yolo_labels_dir, (generated_name + ".jpg"))
			shutil.copyfile(src, dst)
			
			# encode label name
			idx_name = classes.index(name) + 2   # HARDCODED LABEL EDITING
			# convert boundary box to YOLO format
			bndbox = obj.find('bndbox')
			xmin, ymin, xmax, ymax =  float(bndbox.find('xmin').text), float(bndbox.find('ymin').text),\
										float(bndbox.find('xmax').text), float(bndbox.find('ymax').text)
			yolo_bndbox = scale_bndbox(width, height, (xmin, ymin, xmax, ymax))
			f.write(str(idx_name) + " " + " ".join([str(a) for a in yolo_bndbox]) + '\n')
		else:
			damage_counter += 1
			continue
	f.close()
			


def main(classes, working_dir):
	# Create folder for new yolo labels
	try:
		yolo_labels_dir = os.path.join(working_dir, 'yolo_set')
		os.mkdir(yolo_labels_dir)
	except:
		pass
	
	for filename in os.listdir(working_dir):
		# If image - convert it to jpg format
		try:
			img_path = os.path.join(os.path.abspath(working_dir), filename)
			img2jpg(img_path)
		except:
			pass
			
		if '.xml' in filename:
			create_annotation(os.path.join(os.path.abspath(working_dir), filename), yolo_labels_dir)
	print('Pictures in dataset: {}, Skipped: {}'. format('#####', damage_counter))
	
	
if __name__ == "__main__":
	

	parser = argparse.ArgumentParser(description = 'Say hello')
	parser.add_argument("-d", "--dir", type=str,
						help="VOC dataset directory with jpg images and xml files")
	parser.add_argument("-c", "--classes", type=str,
						help="Detector classes. Type across the comma without spaces.")
	args = parser.parse_args()
	
	classes = args.classes.split(',')
	working_dir = args.dir
	
	main(classes, working_dir)
	
			
	
