import grovepi
import math

## capteur temperature

def temperature():
    # Connect the Grove Temperature Sensor to analog port D2
    sensor = 2
    # temp_humidity_sensor_type
    # Grove Base Kit comes with the blue sensor.
    blue = 0    # The Blue colored sensor.
    white = 1   # The White colored sensor.

    # This example uses the blue colored sensor. 
    # The first parameter is the port, the second parameter is the type of sensor.
    
    [temp,humidity] = grovepi.dht(sensor,blue)  
    if math.isnan(temp) == False and math.isnan(humidity) == False:
        print("temp = %.02f"%(temp))
        return temp

        temperature()