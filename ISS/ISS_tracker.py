import ephem
import time
from datetime import datetime
# location of ISS
print("--------------------------\n")
while 1:############forever#################
	print("Location of International Space Station\n")
	#home coordinates, please automate
	home = ephem.Observer()
	home.lon, home.lat = '-117.238646','33.905186'

	# get times UTC and PST
	UTC_date, PST_time = datetime.utcnow(), datetime.now()
	UTC_date = str(UTC_date)
	UTC_date = UTC_date.replace("-","/")
	home.date = UTC_date
	PST_time = str(PST_time)
	PST_time = PST_time.replace("-","/")

	# two line data for ISS
	# pulled from here:
	# http://spaceflight.nasa.gov/realdata/sightings/SSapplications/Post/JavaSSOP/orbit/ISS/SVPOST.html
	
	line1 = "ISS"
	line2 = "1 25544U 98067A   16002.56941713  .00016717  00000-0  10270-3 0  9013"
	line3 = "2 25544  51.6406 169.0160 0008342 351.6259   8.4754 15.55218639 19064"
	iss = ephem.readtle(line1,line2,line3)
	# get that data!
	iss.compute(home)
	print("Azimuth: %s Altitude: %s\n" % (iss.az, iss.alt))
	print("\nDate: %s UTC" % home.date)
	# chop off fraction of seconds at end of time
	print("Date: %s PST \n" % PST_time[:-7])
	print("-----------------------\n")
	time.sleep(10)

