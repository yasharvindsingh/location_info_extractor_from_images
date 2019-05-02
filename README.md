Overview:    

Extracting location information from geotagged images.

Task 1): For every second in the video,create a list of all the images that lie within 35 metres of the drone position.     
Task 2): Another file (assets.csv) is provided with some GPS coordinates for which create a list all images within 50 metres of the drone position.    
Task 3): Creating a KML file for the SRT file of the video provided.


images - contains geo-tagged images   
video - contains GPS coordinates of aerial images stored in a SRT file format   
main.py - python code for detecting all images within 35 metres (Task 1).    
mian_assets.py - python code for detecting all images within 50 metres (Task 2).    
create_kml.py - python code for creating a KML file from the SRT file (Task 3).    
sub.csv - Solution for Task 1.    
sub_assets.csv - Solution for Task 2.   
gis_info.py - preprocessing for extracting the information from the images.   
video_pro.py - preprocessing on the SRT file.    
img_gps_info.csv - preprocessed file contaning information about the images.    
video_gps_info.csv - preprocessed file containing information about the SRT file of video.   
video_kml.kml - KML file (Task 3).    
