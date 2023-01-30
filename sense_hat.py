# TODO: Please provide a "README" file to specify how to test your code. The "README" file should also include a summary of teamwork for this assignment. 
# TODO: Header comment block
from sense_hat import SenseHat

# TODO: add functions here

if __name__ == '__main__':

    sns = SenseHat()

    red = (255,0,0)
    blue = (0,0,255)
    text = (255,255,255)
    
    # TODO: Display messages when actions. You should define the contents of the message, the color of the text, the color of the background, and the scroll speed. 
    
    while True:
        for event in sns.stick.get_events():
            if event.direction == "down":
                # 1. Display images. Define two or more images to display. 
                pass # display image one followed by image two
            elif event.direction == "left":
                # display temp with tree for hot/cold with diff colors and speeds etc
                temp = round(sns.get_temperature())
                if temp >= 24:
                    message = 'Temp: %dC'%(temp)
                    sns.show_message(message,.1,text,red)
                elif temp < 24:
                    message = 'Temp: %dC'%(temp)
                    sns.show_message(message,.1,text,blue)
            elif event.direction == "up":
                # display humidity with tree etc
                humidity = round(sns.get_humidity())
                if humidity >= 50:
                    message = 'Humidity: %d%'%(humidity)
                    sns.show_message(message,.1,text,red)
                elif humidity < 50:
                    message = 'Humidity: %d%'%(humidity)
                    sns.show_message(message,.1,text,blue)
            elif event.direction == "right":
                # display presure with tree etc
                pressure = round(sns.get_pressure())
                if pressure >= 1013:
                    message = 'Pressure: %dmbars'%(pressure)
                    sns.show_message(message,.1,text,red)
                elif pressure < 1013:
                    message = 'Pressure: %dmbars'%(pressure)
                    sns.show_message(message,.1,text,blue)
            else:
                raise ValueError("ValueError")