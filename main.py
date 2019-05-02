import numpy as np 
import pandas as pd
from math import sin, cos, sqrt, atan2, radians

df = pd.read_csv("video_gps_info.csv")
# print(df.info())

tf = pd.read_csv("img_gps_info.csv")
tf = tf[['image','latitude','longitude']]
tf.dropna(inplace = True)
# print(tf.columns)

dist = 35.0
R = 6373.0

def get_dist(lat1,lng1,lat2,lng2):
	lat1 = radians(lat1)
	lon1 = radians(lng1)
	lat2 = radians(lat2)
	lon2 = radians(lng2)

	dlon = lon2 - lon1
	dlat = lat2 - lat1 

	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))
	
	distance = (R * c) * 1000.0
	return distance


geofence_list = {}

for index_vid,row_vid in df.iterrows():
	lat = row_vid['latitude']
	lng = row_vid['longitude']
	s = row_vid['seconds']

	if s not in geofence_list.keys():
		geofence_list[s]=[]

	for index_img,row_img in tf.iterrows():
		calc = get_dist(row_img['latitude'],row_img['longitude'],lat,lng)
		# print(calc)
		if calc <= dist:
			l = geofence_list[s]
			set_l = set(l)
			set_l.add(row_img['image'])
			l = list(set_l)
			geofence_list[s] = l

final_list=[]
for i in geofence_list.keys():
	final_list.append([i,geofence_list[i]])

rf = pd.DataFrame(final_list,columns = ['seconds','img_list'])
rf.to_csv("sub.csv",index = False)