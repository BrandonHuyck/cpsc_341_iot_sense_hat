# TODO: Please provide a "README" file to specify how to test your code. The "README" file should also include a summary of teamwork for this assignment. 
# TODO: Header comment block
from sense_hat import SenseHat

# TODO: add functions here

if __name__ == '__main__':

    sns = SenseHat()

    g = (0, 255, 0) #Green
    b = (1, 1, 1) #Black
    w = (255, 255, 255) #White

    # Image 1: Frog
    img_1 = [
        w, g, g, g, w, g, g, g,
        w, g, b, g, w, g, b, g,
        g, g, g, g, g, g, g, g,
        g, b, b, b, b, b, b, b,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, w, g, g, g, w, g,
    ]

    r = (255, 0, 0) #Red
    bl = (0, 0, 255) #Blue
    t = (210, 180, 140) #Tan
    c = (116, 55, 71) #Crimson
    gy = (128, 128, 128) #Grey
    o = (255, 165, 0) #Orange
    k = (0,0,0) #Clear/Off

    #Image 2: Superman
    img_2 = [
        k, k, k, k, b, t, k, k,
        k, k, k, k, t, t, k, k,
        k, k, r, bl, r, o, r, k,
        r, r, bl, bl, bl, r, bl, k,
        c, c, t, c, bl, bl, b, t,
        k, c, c, c, r, c, k, k,
        k, k, k, b, gy, b, gy, k,
        k, k, k, r, k, k, r, k,
    ]
    
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