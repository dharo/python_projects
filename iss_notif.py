import requests
import time
import datetime
from twilio.rest import TwilioRestClient




# let import.io grab data and make json

# display purpoe and get user input for zipcode and telephone number
print("This program will track the ISS and notify via text when there is\na visible pass.")
print("Please enter your zip code: ")
zip_code = input(">>")
zip_code = str(zip_code)	# format to string
print("Please enter your phone number: ")
phone = input(">>")
phone = str(phone)		# format to string

# get dates
# the purpose of this is to display todays and tomorrow's flybys
today = datetime.date.today()
tmrw_date = today + datetime.timedelta(days=1)
# format dates, API pulls dates in mm/dd/yyyy
# while datetime uses yyyy/mm/dd
tmrw_date = tmrw_date.strftime("%m/%d/%Y") # capital Y gives 4 digit year
tmrw_date = str(tmrw_date)
today = today.strftime("%m/%d/%Y")         # capital Y gives 4 digit year
today = str(today)

print "Today is: %s" % today
print "Tomorrow is: %s" % tmrw_date

# Update api_string for specific zip_code entered by user
api_string = 'https://api.import.io/store/connector/b6466e29-6877-468c-8a92-5705fb5dbce4/_query?input=webpage/url:http%3A%2F%2Fspaceweather.com%2Fflybys%2Fsearch_results_printable.php%3Fzip%3D{}&&_apikey=3070b43a2e804e0cbb247b9ad7c7e66444bbd949e237fd3a2c95e08f9707469e84f0d0c970a3de9bb5795e254af0d179e2161ea62ad4565cd64c6912bbb1ed88e15e3b10ed4f1c7b800e4a70f7d0a756'.format(zip_code)
print("-" * 30)  # do a line
print("Tracking ISS")
while 1:
    # grab data
    r = requests.get(api_string)
    a = r.json()
    text = "-----\n"
    # print type(a)

    # sift through data and display only needed info (ISS specific)
    for i in a['results']:
        if 'ISS' in i['satellite_value']:
	        if today  in i['date_value']:
                # prints to console, also creates string to be sent as text
		        print ("-" * 30)
		        # Satellite name
          		print("Satellite name: {} ".format(i['satellite_value']))
		        text += "Satellite name: {}\n".format(i['satellite_value'])
		
		        # Visibility date
                	print("Visible date:  {}".format(i['date_value']))
		        text += "Visible date:  {}\n".format(i['date_value'])
		
		        # Visibility time
                	print("Visible time: {}".format(i['risetime_value']))
		        text += "Visible time: {}\n".format(i['risetime_value'])

		        # Direction that satellite will come from
	                print("Direction of Rise (Compass): {}".format(i['directionto_value']))
		        text += "Direction of Rise (Compass): {}\n".format(i['directionto_value'])

		        # Elevation above the horizon
        	        print("Elevation in degrees: {}".format(i['maxelevation_number']))
		        text += "Elevation in degrees: {}\n".format(i['maxelevation_number'])
		
		        # Brightness, negative numbers indicate brighter object
                	print("Magnitude (Lower is better): {}".format(i['magnitude_number']))
		        text += "Magnitude (Lower is better): {}\n".format(i['magnitude_number'])
			text += "-----\n"
		if tmrw_date in i['date_value']:
                	# prints to console, also creates string to be sent as text
		        print ("-" * 30)
		        # Satellite name
          		print("Satellite name: {} ".format(i['satellite_value']))
		        text += "Satellite name: {}\n".format(i['satellite_value'])
		
		        # Visibility date
                	print("Visible date:  {}".format(i['date_value']))
		        text += "Visible date:  {}\n".format(i['date_value'])
		
		        # Visibility time
                	print("Visible time: {}".format(i['risetime_value']))
		        text += "Visible time: {}\n".format(i['risetime_value'])

		        # Direction that satellite will come from
	                print("Direction of Rise (Compass): {}".format(i['directionto_value']))
		        text += "Direction of Rise (Compass): {}\n".format(i['directionto_value'])

		        # Elevation above the horizon
        	        print("Elevation in degrees: {}".format(i['maxelevation_number']))
		        text += "Elevation in degrees: {}\n".format(i['maxelevation_number'])
		
		        # Brightness, negative numbers indicate brighter object
                	print("Magnitude (Lower is better): {}".format(i['magnitude_number']))
		        text += "Magnitude (Lower is better): {}\n".format(i['magnitude_number'])
    

    # for the purpose of knowing when data is grabbed
    current_time = datetime.datetime.now()  # get time
    current_time = str(current_time)  # make to a string to format
    print("\nData Grab date: %s" % current_time[:-7])  # print time, chop off fraction of second
    print "\n%s" % text
    text = str(text)
    client = TwilioRestClient()
    message = client.messages.create(to="+1"+phone, from_="+19518015143", body=text)
    time.sleep(604800)  # repeat every 7 days


