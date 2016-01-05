import ephem
import datetime
import time
from datetime import datetime
# time is handled in UTC
print("-----------------------\n")
while 1:###########forever#####################
	print("Location of the Earth's Moon\n")
	# compute the position of the moon
	# would like to automate long/lat grab
	home = ephem.Observer()
	home.lon, home.lat = '-117.238646','33.905186'

	#automate time grab instead of hardcoding time

#	UTC_date = datetime.datetime.utcnow()
#	PST_time = datetime.datetime.now()
	UTC_date, PST_time = datetime.utcnow(), datetime.now()
	UTC_date = str(UTC_date)
	UTC_date = UTC_date.replace("-","/")
	home.date = UTC_date 
	PST_time = str(PST_time)
	PST_time = PST_time.replace("-","/")	

	moon = ephem.Moon()
	moon.compute(home)
	print("Altitude: %s\nAzimuth: %s" % (moon.alt, moon.az))
	print("\nDate: %s UTC" % home.date)
	# chop off fraction of seconds at end of time
	print("Date: %s PST \n" % PST_time[:-7])
	print("-----------------------\n")
	time.sleep(10)
