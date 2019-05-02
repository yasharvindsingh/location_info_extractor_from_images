import numpy as np
import pandas as pd 
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

import sys, os
# import piexif

filename = "images/DJI_0004.JPG"

# im = Image.open(filename)
# exif_dict = piexif.load(im.info["exif"])
# print(exif_dict)

class ImageMetaData():
	exif_data = None
	image = None

	def __init__(self,img_path):
		self.image = Image.open(img_path)
		self.get_exif_data()

	def get_exif_data(self):
		exif_data={}
		info = self.image._getexif()

		if info:
			for tag,value in info.items():
				decoded = TAGS.get(tag, tag)
				if decoded == "GPSInfo":
					gps_data = {}
					for t in value:
						sub_decoded = GPSTAGS.get(t,t)
						gps_data[sub_decoded] = value[t]

					exif_data[decoded] = gps_data
				else:
					exif_data[decoded] = value

		self.exif_data = exif_data

		return exif_data


	def get_if_exist(self, data, key):
		if key in data:
			return data[key]
		return None

	def convert_to_degrees(self, value):
		d0 = value[0][0]
		d1 = value[0][1]

		d = float(d0)/float(d1)

		m0 = value[1][0]
		m1 = value[1][1]

		m = float(m0)/float(m1)

		s0 = value[2][0]
		s1 = value[2][1]

		s = float(s0)/float(s1)

		return d+(m/60.0) + (s/3600.0)


	def get_lat_lng(self):
		lat = None
		lng = None

		exif_data = self.get_exif_data()

		if "GPSInfo" in exif_data:
			gps_info = exif_data["GPSInfo"]

			gps_latitude = self.get_if_exist(gps_info,"GPSLatitude")
			gps_latitude_ref = self.get_if_exist(gps_info, 'GPSLatitudeRef')
			gps_longitude = self.get_if_exist(gps_info, 'GPSLongitude')
			gps_longitude_ref = self.get_if_exist(gps_info, 'GPSLongitudeRef')

			if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
				lat = self.convert_to_degrees(gps_latitude)
				if gps_latitude_ref != "N":
					lat = -1*lat

				lng = self.convert_to_degrees(gps_longitude)
				if gps_longitude_ref != "E":
					lng = -1*lng

		return lat,lng

meta_data = ImageMetaData(filename)

latlng = meta_data.get_lat_lng()

print("Latitude and Longi: ",latlng)


img_list = os.listdir("images/")

img_lat_lng = []
for name in img_list:
	if ".JPG" in name:
		path = "images/"+name
		meta_data = ImageMetaData(path)
		lat,lng = meta_data.get_lat_lng()
		img_lat_lng.append([name,lat,lng])

labels = ['image','latitude','longitude']

df = pd.DataFrame(img_lat_lng,columns = labels)

df.to_csv("img_gps_info.csv",index = False)