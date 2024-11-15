import time
import grovepi

## LED
def led():
    # Connect the Grove LED to digital port D4
    led = 3

    grovepi.pinMode(led,"OUTPUT")
    time.sleep(1)

    #Blink the LED
    grovepi.digitalWrite(led,1)		# Send HIGH to switch on LED
    print ("LED ON!")


## LED
def ledstop():
    # Connect the Grove LED to digital port D4
    led = 3

    grovepi.pinMode(led,"OUTPUT")
    time.sleep(1)

    #Blink the LED
    grovepi.digitalWrite(led,0)		# Send HIGH to switch on LED
    print ("LED OFF!")

ledstop()