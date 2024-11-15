import grovepi
import chumidite as h
import ctemperature as t
import tluminosite as l
import bouton as b
import relai as r
import ecran as ecran
import LED as LED


# humidite      A0
# temperature   D2
# luminosite    A1
# relai         D4
# ecran         I2C1
# led           D3


## Fonctionnement 

if h.humidite()==0:
    ecran.pasplante()
elif h.humidite()<300:
    LED.led()
    r.relay()
    ecran.arrose()
    LED.ledstop()
elif 300<h.humidite()<=800:
    if t.temperature()<=15:
        ecran.parrose()
    elif 15<t.temperature()<=20:
        if l.luminosite()<=200:
            ecran.parrose()
        elif 200<l.luminosite()<=500:
            ecran.parrose()
        else :
            LED.led()
            r.relay()
            ecran.arrose()
            LED.ledstop()
    else :
        LED.led()
        r.relay()
        ecran.arrose()
        LED.ledstop()
else :
    ecran.parrose()