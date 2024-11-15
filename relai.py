import time
import grovepi


##Relai 
# Connect the Grove Relay to digital port D4
# SIG,NC,VCC,GND
def relay():
    relay = 4

    grovepi.pinMode(relay,"OUTPUT")

    # switch on for 5 seconds
    grovepi.digitalWrite(relay,1)
    print ("on")
    time.sleep(5)

    # switch off for 5 seconds
    grovepi.digitalWrite(relay,0)
    print ("off")
    time.sleep(5)
        