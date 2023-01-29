# TODO: Please provide a "README" file to specify how to test your code. The "README" file should also include a summary of teamwork for this assignment. 
# TODO: Header comment block
from sense_hat import SenseHat

# TODO: add functions here

if __name__ == '__main__':

    sns = SenseHat()
    
    # TODO: Display messages when actions. You should define the contents of the message, the color of the text, the color of the background, and the scroll speed. 
    
    while True:
        for event in sns.stick.get_events():
            if event.direction == "down":
                # 1. Display images. Define two or more images to display. 
                pass # display image one followed by image two
            elif event.direction == "left":
                pass # display temp with tree for hot/cold with diff colors and speeds etc
            elif event.direction == "up":
                pass # displ humidity with tree etc
            elif event.direction == "right":
                pass # displ presure with tree etc
            else:
                raise ValueError("ValueError")