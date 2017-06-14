import sys
from picamera import PiCamera
from time import sleep
import RPi.GPIO as IO
import RPi.GPIO as GPIO
import time
import pin_funcs
import show_img
import tweepy
import os
   # print("Modules cannot be loaded!")
   # print("\nFolgender Fehler ist aufgetreten:")
   # print("Unexpected error: ", sys.exc_info()[0])
   # exit()
camera = PiCamera()
DISPLAY = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x67]            # string of characters storing PORT values for each digit.

# Consumer keys and access tokens, used for OAuth
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

IO.setwarnings(False)
IO.setmode(IO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

IO.setup(13,IO.OUT)
IO.setup(6,IO.OUT)
IO.setup(16,IO.OUT)
IO.setup(20,IO.OUT)
IO.setup(21,IO.OUT)
IO.setup(19,IO.OUT)
IO.setup(26,IO.OUT)
IO.setup(12,IO.OUT)

os.system("killall lxpanel");

def main():
    buttonState = True
    camera.start_preview()
    while(buttonState):
        if(GPIO.input(18) == False):
            buttonState = False
    counter = 5
    for x in range(6):          # execute the loop ten times incrementing x value from zero to nine
        time.sleep(1) #Am Anfang, damit bei 0 sofort ausgelöst wird.
        pin = DISPLAY[counter]        # assigning value to 'pin' for each digit
        pin_funcs.PORT(pin);              # showing each digit on display
        counter = counter-1
        #time.sleep(1)
    camera.capture('/home/pi/image.jpg')
    camera.stop_preview()
    decision = show_img.showWindow()
    if(decision == False):
        return
    else:
        #api.update_status('Hello Python Central!')
        api.update_with_media("/home/pi/image.jpg","Greetings from #Glarnermesse")

while(True):
#    try:
    main()
#    except:
#        print("Unexpected error: ", sys.exc_info()[0])
