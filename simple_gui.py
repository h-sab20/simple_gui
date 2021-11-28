import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# Variables:
key_messg = ' '
WIDTH = 500
HEIGHT = 500
ccolor = "Black"
tcolor = 'White'
cmcolor = ('Blue', 'White', 'Green')
click_counter = 0
cx = WIDTH/2
cy = HEIGHT/2


# handlers
def draw(canvas):
    canvas.draw_text(key_messg, [40, 450], 30, tcolor)
    canvas.draw_circle((cx, cy), 30, 5,"White", ccolor)

def keydown(key):
    global  key_messg, ccolor, cx, cy, tcolor
    # my_key = str(key)
    if key == simplegui.KEY_MAP["left"]:
        key_messg = "left arrow"
        tcolor = "Green"
        ccolor = "Green"
        cx = 100
        cy = 250
    elif key == simplegui.KEY_MAP['right']:
        key_messg = "right arrow"
        ccolor = "Blue"
        tcolor = "Blue"
        cx = 400
        cy = 250
    elif key == simplegui.KEY_MAP['down']:
        key_messg = "down arrow"
        ccolor = "Red"
        tcolor = "Red"
        cx = 250
        cy = 400
    elif key == simplegui.KEY_MAP['up']:
        key_messg = "up arrow"
        ccolor = "Yellow"
        tcolor = "Yellow"
        cx = 250
        cy = 100


def mouseclick(mpos):
    global cx, cy, ccolor, click_counter
    cx, cy = mpos
    ccolor = cmcolor[click_counter % 3]
    click_counter += 1

# Create Frame
frame = simplegui.create_frame("Arrow keys", WIDTH, HEIGHT)



# Register events
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_mouseclick_handler(mouseclick)


frame.start()