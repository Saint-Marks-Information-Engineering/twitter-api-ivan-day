import time
import RPi.GPIO as GPIO
from twython import TwythonStreamer

TERMS = '#MAGA'

LED = 22

APP_KEY = 'VA4kCGDKNzBKRmp4axaErPKBk'
APP_SECRET = 'WbMM7JDnKGEGQe4MszVREuxSVn8zoV3PyriycYUKotOC1lpbnD'
OAUTH_TOKEN = '2944605690-czlhK7XsPQvcRfLIGqhXRdCx0Vsl0kUeCZxReVw'
OAUTH_TOKEN_SECRET = 'hhedqlI2hDzYdnYuoWw9XkrG61ySoRtso7zLwpEs27QN3'

class BlinkyStreamer(TwythonStreamer):
	def on_success(self, data):
		if 'text' in data:
			print(data['text'].encode('utf-8'))
			GPIO.output(LED, GPIO.HIGH)
			time.sleep(0.5)
			GPIO.output(LED, GPIO.LOW)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

try:
	stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
	stream.statuses.filter(track = TERMS)
except KeyboardInterrupt:
	GPIO.cleanup()
