import pandas as pd 
import numpy as np

file = open("videos/DJI_0301.SRT")

lines = file.readlines()

i=1
count_s=1
temp = lines[i].split("-->")[1].split(",")[0].split(":")[2]
lat_lng_list=[]

while i < len(lines):
	s = lines[i].split("-->")[1].split(",")[0].split(":")[2]
	if temp == s:
		ln,l,_ = lines[i+1].split(",")
		lat,lng = float(l),float(ln)
		lat_lng_list.append([count_s,lat,lng])
	else:
		l,ln,_ = lines[i+1].split(",")
		lat,lng = float(l),float(ln)
		lat_lng_list.append([count_s,lat,lng])
		count_s+=1
		temp = s
	i+=4
# print(lat_lng_list)

labels = ['seconds','latitude','longitude']

df = pd.DataFrame(lat_lng_list,columns = labels)
print(df.head())
df.to_csv("video_gps_info.csv",index = False)
