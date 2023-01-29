

# As a group, work on this assignment by interacting with the Sense HAT board. Write up your program(s) to cover the components below: 
# 1. Display images. Define two or more images to display. 
# 2. Display a message. You should define the contents of the message, the color of the text, the color of the background, and the scroll speed. 
# 3. Sense the environment. Read data from temprature, humidity, and presure. Define some "action(s)" based on analyzing the sensing data.
# 4. Use the joystick. Define "actions" for each direction of pushing the joystick.


# 3.Please provide a "README" file to specify how to test your code. The "README" file should also include a summary of teamwork for this assignment. 


from sense_hat import SenseHat


if __name__ == '__main__':

    sns = SenseHat()
    
    while True:
        for event in sns.stick.get_events():
            if event.direction == "down":
                pass # display image one followed by image two
            elif event.direction == "left":
                pass # display temp with tree for hot/cold with diff colors and speeds etc
            elif event.direction == "up":
                pass # displ humidity with tree etc
            elif event.direction == "right":
                pass # displ presure with tree etc
            else:
                raise ValueError("ValueError")