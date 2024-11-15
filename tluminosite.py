import grovepi

## capteur luminosite - light sensor
# jusqu'à 200 -
# jusqu'a 500 +
# jusqu'a 800 ++

def luminosite():
    # Connect the Grove Light Sensor to analog port A1
    light_sensor = 1

    # Get sensor value
    sensor_value = grovepi.analogRead(light_sensor)

    # Calculate resistance of sensor in K
    resistance = (float)(1023 - sensor_value) * 10 / sensor_value

    print("sensor_value = %d resistance = %.2f" %(sensor_value,  resistance))
    return sensor_value
#plus la resistance est basse plus la luminosité est forte
    
