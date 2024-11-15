from driverI2C import *

## ecran 
def arrose():
    setText("Plante arrosee")
    setRGB(0,255,0)
    
def parrose():
    setText("Plante non arrosee")
    setRGB(255,0,0)

def pasplante():
    setText("il n'y a pas de plante")
    setRGB(0,0,0)