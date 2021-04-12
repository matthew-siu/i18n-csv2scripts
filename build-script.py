import sys
import csv
import numpy as np
from numpy import genfromtxt
from datetime import datetime
import os

# read csv into 2d array
def read_csv(filepath, i):
	with open(filepath, 'rb') as f:
		reader = csv.reader(f)
		data = []
		for row in reader:
			data.append([row[i],row[i+1],row[i+2],row[i+3]])
		return data

def write_iOS(data, filepath):
	txt = "/* Localizable.strings */\n\n"
	for row in data:
		_id = row[0]
		val = row[1]
		if _id == "" : 
			txt += "\n"
		elif (_id != "" and val == "") :
			if _id[0] != "/" : 
				print("WARNING: detected invalid comment or id: "+_id)
				txt += "// " + _id + "\n"
			else:
				txt += _id + "\n"
		elif (_id != "" and val != "") : 
			txt += "\""+_id+"\" = \"" + val + "\";\n"
	
	with open(filepath, 'wb') as iOSfile:
		print("writing "+filepath+"...")
		iOSfile.write(txt)
		iOSfile.close()

def write_aOS(data, filepath):
	txt = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<resources>\n"
	for row in data:
		_id = row[0]
		val = row[1]
		if _id == "" : 
			txt += "\n"
		elif (_id != "" and val == "") :
			if _id[0] != "<!" : 
				print("WARNING: detected invalid comment or id: "+_id)
				txt += "    <!-- " + _id + " -->\n"
			else: 
				txt += _id + "\n"
		elif (_id != "" and val != "") : 
			txt += "    <string name=\""+_id+"\">"+val+"</string>\n"
	txt += "</resources>"
	
	with open(filepath, 'wb') as iOSfile:
		print("writing "+filepath+"...")
		iOSfile.write(txt)
		iOSfile.close()

def build_script_iOS(data):
	dataEN = np.delete(data, [2,3], axis=1)
	dataTC = np.delete(data, [1,3], axis=1)
	dataCN = np.delete(data, [1,2], axis=1)

	dateTimeObj = datetime.now()
	timestampStr = dateTimeObj.strftime("%Y-%m-%d %H_%M_%S")
	print("create directory: " + timestampStr)
	timestampStr = "iOS " + timestampStr
	os.mkdir(timestampStr)

	write_iOS(dataEN, os.path.join(timestampStr, "en.txt"))
	write_iOS(dataTC, os.path.join(timestampStr, "tc.txt"))
	write_iOS(dataCN, os.path.join(timestampStr, "cn.txt"))
	print("Completed!")

def build_script_aOS(data):
	dataEN = np.delete(data, [2,3], axis=1)
	dataTC = np.delete(data, [1,3], axis=1)
	dataCN = np.delete(data, [1,2], axis=1)

	dateTimeObj = datetime.now()
	timestampStr = dateTimeObj.strftime("%Y-%m-%d %H_%M_%S")
	print("create directory: " + timestampStr)
	timestampStr = "aOS " + timestampStr
	os.mkdir(timestampStr)

	write_aOS(dataEN, os.path.join(timestampStr, "en.xml"))
	write_aOS(dataTC, os.path.join(timestampStr, "tc.xml"))
	write_aOS(dataCN, os.path.join(timestampStr, "cn.xml"))
	print("Completed!")

def export_iOS(filepath):
	print("export iOS")

	# iOS csv
	# index: 4 = id , 5 = EN , 6 = TC , 7 = CN
	raw_data = read_csv(filepath, 4)
	# remove first 2 row
	data = np.delete(raw_data, [0,1], axis=0)
	build_script_iOS(data)

def export_aOS(filepath):
	print("export Android")

	# android csv
	# index: 0 = id , 1 = EN , 2 = TC , 3 = CN
	raw_data = read_csv(filepath, 0)
	# remove first 2 row
	data = np.delete(raw_data, [0,1], axis=0)
	build_script_aOS(data)



if __name__ == "__main__":

    if len(sys.argv) != 3:
    	print("cmd error: python [.py file] [.csv filepath] [-a,-i]")
    	print("-a: export for Android \n-i: export for iOS")
    	sys.exit()

    # get filepath
    filepath = sys.argv[1]

    # get osVersion
    osVersion = sys.argv[2]
    if (osVersion == "-a" or osVersion == "-i"): pass
    else: 
    	print("args error: 2nd argment must be either -a or -i")
    	sys.exit()

    print(filepath, osVersion)

    if (osVersion == "-a"): export_aOS(filepath)
    else: export_iOS(filepath)
    