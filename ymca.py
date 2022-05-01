# Author: Emil Gomez
# Course: CSc 120
# Description: This program draws stick figures dancing to the YMCA song. It
# uses time to have some figures put their hands up at a certain moment.
import graphics

def main():
    '''
    In the main function a window is created and functions that draw
    each character are called. To make sure that each stick figure
    puts their hands up at the right time we have a counter, that
    also resets to 0. At each interval put the other stick figure
    puts their hands up.
    :return:
    This function returns the drawing of all the stick figures dancing
    to YMCA.
    '''
    # Create the window and counter
    win = graphics.graphics(500, 400, 'YMCA')
    i = 0
    # Have a while loop to keep running as long as the window is up.
    # Call each function at the start, and then set intervals for
    # each other figure to put their hands up.
    while not win.is_destroyed():
        win.clear()
        background(win)
        y_guy(win, i)
        m_guy(win, i)
        c_guy(win, i)
        a_guy(win, i)
        if i >= 6:
            y_guy_y(win, i)
        if i >= 8:
            m_guy_m(win, i)
        if i >= 10:
            c_guy_c(win, i)
        if i >= 12:
            a_guy_a(win, i)
        # Lower frame update to adjust speed of dancing
        win.update_frame(2)
        if i >= 20:
            i = 0
        i += 1
def background(win):
    '''
    This is the grey background for the window
    :param win: This is the window.
    :return: Returns a grey background
    '''
    win.rectangle(0, 0, 500, 400, 'Light gray')
def y_guy(win, i):
    '''
    This is the function that draws the first guy on the left.
    He is made up of lines and a circle.
    :param win: The graphics window
    :param i: The counter so we can draw the squatting figure
    only when there is an even counter.
    :return:
    This function returns a stick figure squatting up and down.
    '''
    # Only draw the squatting figure when the counter is even
    if i % 2 == 0:
            win.line(50, 400, 60, 350, width=2)
            win.line(130, 400, 120, 350, width=2)
            win.line(60, 350, 90, 320, width=2)
            win.line(120, 350, 90, 320, width=2)
            win.line(90, 320, 90, 200, width=2)
            win.line(90, 220, 50, 320, width=2)
            win.line(90, 220, 130, 320, width=2)
            win.ellipse(90, 180, 50, 40, 'black')
            win.ellipse(90, 180, 45, 35, 'light gray')
    # Draw the standing figure every other time.
    else:
        win.line(50, 400, 90, 300, width=2)
        win.line(130, 400, 90, 300, width=2)
        win.line(90, 300, 90, 180, width=2)
        win.line(90, 200, 50, 310, width=2)
        win.line(90, 200, 140, 310, width=2)
        win.ellipse(90, 160, 50, 40, 'black')
        win.ellipse(90, 160, 45, 35, 'light gray')
def y_guy_y(win, i):
    '''
    This function draws the figures arms to create a Y.
    :param win: Graphics window
    :param i: counter to draw at an even counter.
    :return: This returns the first stick figure with
    its arms as a y
    '''
    # Draw over the previous arms and draw new ones
    if i % 2 == 0:
        win.line(90, 220, 50, 320, 'light grey', 2)
        win.line(90, 220, 130, 320, 'light grey', 2)
        win.line(90, 220, 50, 120, width=2)
        win.line(90, 220, 130, 120, width=2)
        win.line(90, 320, 90, 200, width=2)
    else:
        win.line(90, 200, 50, 310, 'light grey', 2)
        win.line(90, 200, 140, 310, 'light grey', 2)
        win.line(90, 200, 50, 90, width=2)
        win.line(90, 200, 140, 90, width=2)
        win.line(90, 300, 90, 180, width=2)
def m_guy(win, i):
    '''
    This function draws the second figure who is assaigned to M.
    He is also made up of lines and a circle head.
    :param win: Graphics window
    :param i: Counter to draw when the counter is at an even
    number.
    :return: This returns the second figure squatting up and
    down.
    '''
    # Draw the figure squatting whenever the counter is even
    if i % 2 == 0:
        win.line(140, 400, 150, 350, width=2)
        win.line(220, 400, 210, 350, width=2)
        win.line(150, 350, 180, 320, width=2)
        win.line(210, 350, 180, 320, width=2)
        win.line(180, 320, 180, 200, width=2)
        win.line(180, 220, 140, 320, width=2)
        win.line(180, 220, 220, 320, width=2)
        win.ellipse(180, 180, 50, 40, 'black')
        win.ellipse(180, 180, 45, 35, 'light gray')
    # Draw the figure standing every other time
    else:
        win.line(140, 400, 180, 300, width=2)
        win.line(220, 400, 180, 300, width=2)
        win.line(180, 300, 180, 180, width=2)
        win.line(180, 200, 140, 310, width=2)
        win.line(180, 200, 220, 310, width=2)
        win.ellipse(180, 160, 50, 40, 'black')
        win.ellipse(180, 160, 45, 35, 'light gray')
def m_guy_m(win, i):
    '''
    This function draws the arms that from an m for
    the figure. It covers the older arms and draws new
    ones.
    :param win: Graphics window
    :param i: Counter so we can draw whenever its at an
    even number
    :return: This function returns the arms as an M
    instead of them being on the side.
    '''
    # Draw over the older arms and draw the new ones
    if i % 2 == 0:
        win.line(180, 220, 150, 180, width=2)
        win.line(180, 220, 210, 180, width=2)
        win.line(150, 180, 180, 150, width=2)
        win.line(210, 180, 180, 150, width=2)
        win.line(180, 220, 140, 320, 'light grey', 2)
        win.line(180, 220, 220, 320, 'light grey', 2)
        win.line(180, 320, 180, 200, width=2)

    else:
        win.line(180, 200, 150, 160, width=2)
        win.line(180, 200, 210, 160, width=2)
        win.line(150, 160, 180, 130, width=2)
        win.line(210, 160, 180, 130, width=2)
        win.line(180, 200, 140, 310, 'light grey', 2)
        win.line(180, 200, 220, 310, 'light grey', 2)
        win.line(180, 300, 180, 180, width=2)

def c_guy(win, i):
    '''
    This function is for the third figure who is assaigned to C.
    This figure is also made up of lines and a circle head.
    :param win: Graphics window
    :param i: Counter so we can draw when the number is even.
    :return: This returns the third figure squatting up and down
    in sync with the other figures.
    '''
    # Draw the figure squatting when the counter is even.
    if i % 2 == 0:
        win.line(240, 400, 250, 350, width=2)
        win.line(320, 400, 310, 350, width=2)
        win.line(250, 350, 280, 320, width=2)
        win.line(310, 350, 280, 320, width=2)
        win.line(280, 320, 280, 200, width=2)
        win.line(280, 220, 240, 320, width=2)
        win.line(280, 220, 320, 320, width=2)
        win.ellipse(280, 180, 50, 40, 'black')
        win.ellipse(280, 180, 45, 35, 'light gray')
    # Draw it standing every other time.
    else:
        win.line(240, 400, 280, 300, width=2)
        win.line(320, 400, 280, 300, width=2)
        win.line(280, 300, 280, 180, width=2)
        win.line(280, 200, 240, 310, width=2)
        win.line(280, 200, 320, 310, width=2)
        win.ellipse(280, 160, 50, 40, 'black')
        win.ellipse(280, 160, 45, 35, 'light gray')
def c_guy_c(win, i):
    '''
    This function is to draw the arms in a C shape.
    :param win: Graphics window
    :param i: Counter to draw at an even number
    :return: Returns the arms in a C shape instead of
    on the sides.
    '''
    # Draw over the older arms and draw the new C arms.
    if i % 2 == 0:
        win.line(280, 220, 240, 320, 'light grey', 2)
        win.line(280, 220, 320, 320, 'light grey', 2)
        win.line(280, 320, 280, 200, width=2)
        win.line(280, 220, 320, 140, width=2)
        win.line(280, 220, 320, 300, width=2)

    else:
        win.line(280, 200, 240, 310, 'light grey', 2)
        win.line(280, 200, 320, 310, 'light grey', 2)
        win.line(280, 300, 280, 180, width=2)
        win.line(280, 200, 320, 120, width=2)
        win.line(280, 200, 320, 280, width=2)

def a_guy(win, i):
    '''
    This function is for the last figure and it is
    assaigned to hold up the A. It is also made up
    of lines and a circle head.
    :param win: Graphics window
    :param i: Counter to draw whenever the counter is
    even
    :return: This returns the final figure squatting up
    and down with the other figures.
    '''
    # Draw the figure squatting whenever the counter is even.
    if i % 2 == 0:
        win.line(340, 400, 350, 350, width=2)
        win.line(420, 400, 410, 350, width=2)
        win.line(350, 350, 380, 320, width=2)
        win.line(410, 350, 380, 320, width=2)
        win.line(380, 320, 380, 200, width=2)
        win.line(380, 220, 340, 320, width=2)
        win.line(380, 220, 420, 320, width=2)
        win.ellipse(380, 180, 50, 40, 'black')
        win.ellipse(380, 180, 45, 35, 'light gray')
    else:
        win.line(340, 400, 380, 300, width=2)
        win.line(420, 400, 380, 300, width=2)
        win.line(380, 300, 380, 180, width=2)
        win.line(380, 200, 340, 310, width=2)
        win.line(380, 200, 420, 310, width=2)
        win.ellipse(380, 160, 50, 40, 'black')
        win.ellipse(380, 160, 45, 35, 'light gray')
def a_guy_a(win, i):
    '''
    This function draws the A arms for the last figure.
    :param win: Graphics window
    :param i: Counter to draw whenever the number is even.
    :return: Returns the arms at a given interval to make
    an A.
    '''
    # Cover the older arms and draw new ones.
    if i % 2 == 0:
        win.line(380, 220, 340, 320, 'light grey', 2)
        win.line(380, 220, 420, 320, 'light grey', 2)
        win.line(380, 220, 340, 180, width=2)
        win.line(380, 220, 420, 180, width=2)
        win.line(340, 180, 370, 150, width=2)
        win.line(420, 180, 390, 150, width=2)
        win.line(380, 320, 380, 200, width=2)
    else:
        win.line(380, 200, 340, 160, width=2)
        win.line(380, 200, 420, 160, width=2)
        win.line(340, 160, 370, 130, width=2)
        win.line(420, 160, 390, 130, width=2)
        win.line(380, 200, 340, 310, 'light grey', 2)
        win.line(380, 200, 420, 310, 'light grey', 2)
        win.line(380, 300, 380, 180, width=2)

main()