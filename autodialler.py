#!/usr/bin/python
import sched, time
from twilio.twiml.voice_response import Play, VoiceResponse, Say
from twilio.rest import Client

def main():

	# Consts
	START_TIME = time.time()
	NUM_TIMES = 20
	ct   = 0
	TO   = "+1234567890"  # Scammer's number
	FROM = "+1234567890" # Your account's phone number

	#DAY RUINER V1
	while ct < NUM_TIMES:#True:

		# Account + Client Setup
		account_sid = "your_account_sid"
		auth_token = "your_auth_token"
		client = Client(account_sid, auth_token)

		call = client.calls.create(
		    to=TO,
		    from_=FROM,
		    url="http://your.com/xml/file.xml"
		)
		ct = ct+1
		time.sleep(60.0 - ((time.time() - START_TIME) % 60.0))

if __name__ == '__main__':
	print("Calling...")
	main()
