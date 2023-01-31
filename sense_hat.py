'''
Authors:     Brandon, Carson, Jack
Instructor:  Dr. Zhang
Course:      CPSC 341-01 IoT
Institution: Gonzaga University, Spokane, WA 99258
Date:        30 January 2023
Description: A file for practice with the basic functionality of Sense Hat with
             Raspberry Pi.
'''

from sense_hat import SenseHat

if __name__ == '__main__':

    sns = SenseHat()

    red = (255,0,0)
    blue = (0,0,255)
    text = (255,255,255)
        
    while True:
        for event in sns.stick.get_events():
            if event.direction == "down":
                # 1. Display images. Define two or more images to display. 
                pass # display image one followed by image two
            elif event.direction == "left":
                # display temp with tree for hot/cold with diff colors and speeds etc
                temp = round(sns.get_temperature())
                if temp >= 24: # higher than 24C show red background and display 
                    message = 'Temp: %dC'%(temp)
                    sns.show_message(message,.1,text,red)
                elif temp < 24: # lower than 24C show blue background asnd display
                    message = 'Temp: %dC'%(temp)
                    sns.show_message(message,.1,text,blue)
            elif event.direction == "up":
                # display humidity with tree etc
                humidity = round(sns.get_humidity())
                if humidity >= 50: # higher than 50% show red background and display 
                    message = 'Humidity: %d%'%(humidity)
                    sns.show_message(message,.1,text,red)
                elif humidity < 50: # lower than 50% show blue background asnd display
                    message = 'Humidity: %d%'%(humidity)
                    sns.show_message(message,.1,text,blue)
            elif event.direction == "right":
                # display presure with tree etc
                pressure = round(sns.get_pressure())
                if pressure >= 1013: # lower than 1013 mbars show blue background asnd display
                    message = 'Pressure: %dmbars'%(pressure)
                    sns.show_message(message,.1,text,red)
                elif pressure < 1013: # higher than 1013 mbars show red background and display 
                    message = 'Pressure: %dmbars'%(pressure)
                    sns.show_message(message,.1,text,blue)
            else:
                raise ValueError("ValueError")