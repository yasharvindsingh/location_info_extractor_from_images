f = open("video_kml.kml","w")
s = open("videos/DJI_0301.SRT")

lines = s.readlines()
i=0

f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
while i < len(lines):
	f.write('\t<Placemark>\n')
	f.write("".join(['\t\t<name>',lines[i],' </name>\n']))
	f.write('\t\t<description>' + lines[i+1] + ' </description>\n')
	f.write('\t\t<Point>\n')
	f.write('\t\t\t<coordinates>' + lines[i+2] + ' </coordinates>\n')
	f.write('\t\t</Point>\n')
	f.write('\t</Placemark>\n')	
	i+=4

f.write('</kml>')
f.close()
