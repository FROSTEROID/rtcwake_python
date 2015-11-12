from datetime import datetime
import sys
import os

def RTCWake(seconds):
	return(os.system("rtcwake -m mem --seconds " + str(seconds)))

if(len(sys.argv)==2):
	timeToWake = datetime.strptime(sys.argv[1], "%H:%M")
	diffTTW = timeToWake - datetime.strptime("","")
	currentTime = datetime.now()
	diffCT = datetime.strptime(str(datetime.now().hour)+":"+str(datetime.now().minute), "%H:%M") - datetime.strptime("","")
#	print(diffTTW)
#	print(diffCT)
	if(diffTTW > diffCT):
		RTCWake((diffTTW-diffCT).seconds)
	else:
		RTCWake(diffTTW.seconds + (24*60*60 - diffCT.seconds))
	
else:
	print("ERROR:\n\tDidn't get a time argument!\n")
	print("USAGE:\n\tpython rtcwake.py H:M")
	print("EXAMPLE:\n\tpython rtcwake.py 7:13\n\tThis will take the pc asleep planning to wake up at 7:13am.\n\tIt uses 24-hous format for input.")
	
