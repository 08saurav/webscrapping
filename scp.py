import wget
import codecs
import os
fi=codecs.open("output.csv","a+",encoding='utf-8')
#f=fi.read()
#fi.close()
#f=f.split("\n")
stra="http://flights.makemytrip.com/makemytrip/search/O/O/E/1/0/0/S/"
url="https://www.makemytrip.com/flight/search?itinerary=JDH-BLR-18/02/2020_BLR-JDH-20/02/2020&tripType=R&paxType=A-1_C-0_I-0&intl=false&cabinClass=E"
files = wget.download(url,out="dump/myfile.txt")
fa=codecs.open("./dump/myfile.txt","r",encoding='utf-8')
f=fa.read()
fa.close()
os.remove("./dump/myfile.txt")
f=f.split("\n")
for i in f:
	if "var minfare =" in i:
		print i
