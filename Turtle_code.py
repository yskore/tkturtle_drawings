# a4.py
# YOUR NAME(S) AND NETID(S) HERE
# DATE COMPLETED HERE
"""Module to draw cool shapes with the Tk Turtle.

The module can be run as a script to show off the various functions.
Unimplemented functions will do nothing."""
import tkturtle
import colormodel
import math


################# Helpers for Precondition Verification #################

def is_number(x):
    """Returns: True if value x is a number; False otherwise.
    
    Parameter x: the value to check
    Precondition: NONE (x can be any value)"""
    return type(x) in [float, int]


def is_window(w):
    """Returns: True if w is a tkturtle Window; False otherwise.
    
    Parameter w: the value to check
    Precondition: NONE (w can be any value)"""
    return type(w) == tkturtle.Window


def is_valid_color(c):
    """Returns: True c is a valid turtle color; False otherwise
    
    Parameter c: the value to check
    Precondition: NONE (c can be any value)"""
    return (type(c) == colormodel.RGB or type(c) == colormodel.HSV or
            (type(c) == str and c in colormodel._TK_COLOR_MAP))


def is_valid_speed(sp):
    """Returns: True if sp is an int in range 0..10; False otherwise.
    
    Parameter sp: the value to check
    Precondition: NONE (sp can be any value)"""
    return (type(sp) == int and 0 <= sp and sp <= 10)


def is_valid_length(side):
    """Returns: True if side is a number >= 0; False otherwise.
    
    Parameter side: the value to check
    Precondition: NONE (side can be any value)"""
    return (is_number(side) and 0 <= side)


def is_valid_iteration(n):
    """Returns: True if n is an int >= 1; False otherwise.
    
    Parameter n: the value to check
    Precondition: NONE (n can be any value)"""
    return (type(n) == int and 1 <= n)


def is_valid_depth(d):
    """Returns: True if d is an int >= 0; False otherwise.
    
    Parameter d: the value to check
    Precondition: NONE (d can be any value)"""
    return (type(d) == int and d >= 0)


def is_valid_turtlemode(t):
    """Returns: True t is a Turtle with drawmode True; False otherwise.
    
    Parameter t: the value to check
    Precondition: NONE (t can be any value)"""
    return (type(t) == tkturtle.Turtle and t.drawmode)


def is_valid_penmode(p):
    """Returns: True t is a Pen with fill False; False otherwise.
    
    Parameter p: the value to check
    Precondition: NONE (p can be any value)"""
    return (type(p) == tkturtle.Pen and not p.fill)


def report_error(message, value):
    """Returns: An error message about the given value.
    
    This is a function for constructing error messages to be used in
    assert statements.  We find that students often introduce bugs into
    their assert statement messages, and do not find them because they
    are in the habit of not writing tests that violate preconditions.
    
    The purpose of this function is to give you an easy way of making
    error messages without having to worry about introducing such bugs.
    Look at the function draw_two_lines for the proper way to use it.
    
    Parameter message: The error message to display
    Precondition: message is a string
    
    Parameter value: The value that caused the error
    Precondition: NONE (value can be anything)"""
    return message+': '+`value`




#################### DEMO: Two lines ####################


def draw_two_lines(w,sp):
    """Draws two lines on to window w.
    
    In the middle of the window w, this function draws a green line 100
    pixels to the west, and then a red line 200 pixels to the south.  It
    uses a new turtle that moves at speed sp, 0 <= sp <= 10, with 1 being
    slowest and 10 fastest (and 0 being "instant").
    
    Parameter w: The window to draw upon.
    Precondition: w is a tkturtle Window object.
    
    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed."""
    # Assert the preconditions
    assert is_window(w), report_error('w is not a valid window',w)
    assert is_valid_speed(sp), report_error('sp is not a valid speed',sp)
    
    t = tkturtle.Turtle(w)
    t.speed = sp
    t.color = 'green'
    t.forward(100) # draw a line 100 pixels in the current direction
    t.left(90)     # add 90 degrees to the angle
    t.color = 'red'
    t.forward(200)


#################### TASK 1: Triangle ####################

def draw_triangle(t, s, c):
    """Draws an equilateral triangle of side s and color c at currenct position.
    
    The direction of the triangle depends on the current facing of the turtle.
    If the turtle is facing west, the triangle points up and the turtle starts
    and ends at the east end of the base line.
    
    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED:
    position (x and y, within round-off errors), heading, color, and drawmode.
    If you changed any of these in the function, you must change them back.
    
    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.
    
    Parameter s: The length of each triangle side
    Precondition: s is a valid side length (number >= 0)
    
    Parameter c: The triangle color
    Precondition: c is a valid turtle color (see the helper function above)"""
    # Assert the preconditions
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(s), report_error('Invalid side length', s)
    assert is_valid_color(c), report_error('Invalid color', c)
    
    # Hint: each angle in an equilateral triangle is 60 degrees.
    # Note: In this function, DO NOT save the turtle position and heading
    # in the beginning and then restore them at the end. The turtle moves
    # should be such that the turtle ends up where it started and facing
    # in the same direction, automatically.
    
    # Also, 3 lines have to be drawn. Does this suggest a for loop that
    # processes the range 0..2?

    start_color = t.color
    t.color = c
    for x in range(3):
        t.forward(s)
        t.right(120)
        
    t.color = start_color    
        

#################### TASK 2: Hexagon ####################

def draw_hex(t, s):
    """Draws six triangles using the color 'orange' to make a hexagon.
    
    The triangles are equilateral triangles, using draw_triangle as a helper.
    The drawing starts at the turtle's current position and heading. The
    middle of the hexagon is the turtle's starting position.
    
    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED:
    position (x and y, within round-off errors), heading, color, and drawmode.
    If you changed any of these in the function, you must change them back.
    
    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.
    
    Parameter s: The length of each triangle side
    Precondition: s is a valid side length (number >= 0)"""
    # Assert the preconditions
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(s), report_error('Invalid side length', s)

    # Note: Do not save any of the turtle's properties and then restore them
    # at the end. Just use 6 calls on procedures drawTriangle and t.left. Test
    # the procedure to make sure that t's final location and heading are the
    # same as t's initial location and heading (except for roundoff error).
    
    # The procedure is supposed to draw 6 triangles. Does that suggest a loop
    # that processes the integers in 0..5?
    
    start_color = t.color
    for x in range(6):
        draw_triangle(t,s,'orange')
        t.left(60)
        
    t.color = start_color    


#################### Task 3A: Spirals ####################

def draw_spiral(w, side, ang, n, sp):
    """Draws a spiral using draw_spiral_helper(t, side, ang, n, sp)
    
    This function clears the window and makes a new turtle t.  This turtle
    starts in the middle of the canvas facing east (NOT the default west).
    It then calls draw_spiral_helper(t, side, ang, n, sp). When it is done,
    the turtle is left hidden (visible is False).
    
    Parameter w: The window to draw upon.
    Precondition: w is a tkturtle Window object.
    
    Parameter side: The length of each spiral side
    Precondition: side is a valid side length (number >= 0)
    
    Parameter ang: The angle of each corner of the spiral
    Precondition: ang is a number
    
    Parameter n: The number of edges of the spiral
    Precondition: n is a valid number of iterations (int >= 1)
    
    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed."""
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_window(w), report_error('w is not a valid window',w)
    assert is_valid_length(side), report_error('side is not a valid length',side)
    assert is_valid_iteration(n), report_error('n is not a valid number of iterations',side)
    assert is_valid_speed(sp), report_error('sp is not a valid speed',sp)
    assert is_number(ang), report_error('ang is not a valid angle',ang)
    
    # HINT: w.clear() clears window.
    # HINT: set the turtle's visible attribute to False at the end.
    
    w.clear()
    t = tkturtle.Turtle(w)
    draw_spiral_helper(t, side, ang, n, sp)
    t.visible = False
    


def draw_spiral_helper(t, side, ang, n, sp):
    """Draws a spiral of n lines at the current position and heading.
    
    The spiral begins at the current turtle position and heading, turning ang
    degrees to the left after each line.  Line 0 is side pixels long. Line 1
    is 2*side pixels long, and so on.  Hence each Line i is (i+1)*side pixels
    long. The lines alternate between red, blue, and green, in that order, with
    the first one red.  The turtle draws at speed sp.
    
    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED:
    color, speed, visible, and drawmode. However, the final position and
    heading may be different. If you changed any of these four in the function,
    you must change them back.
    
    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.
    
    Parameter side: The length of each spiral side
    Precondition: side is a valid side length (number >= 0)
    
    Parameter ang: The angle of each corner of the spiral
    Precondition: ang is a number
    
    Parameter n: The number of edges of the spiral
    Precondition: n is a valid number of iterations (int >= 1)
    
    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed."""
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(side), report_error('side is not a valid length',side)
    assert is_valid_iteration(n), report_error('n is not a valid number of iterations',side)
    assert is_valid_speed(sp), report_error('sp is not a valid speed',sp)
    assert is_number(ang), report_error('ang is not a valid angle' ,ang)

    # NOTE: Since n lines must be drawn, use a for loop on a range of integers.
    
    start_color = t.color
    start_speed = t.speed
    t.right(180)
    for x in range(n):
        if x%3 == 0:
            t.color = 'red'
        elif x%3 ==1:
            t.color = 'blue'
        else:
            t.color = 'green'
        t.speed = sp        
        t.forward(side*(x+1))
        t.left(ang)
    
    t.color = start_color
    t.speed = start_speed


#################### TASK 3B: Polygons ####################


def multi_polygons(w, side, k, n, sp):
    """Draws polygons using multi_polygons_helper(t, side, k, n, sp)

    This function clears the window and makes a new turtle t.  This turtle
    starts in the middle of the canvas facing north (NOT the default west).
    It then calls multi_polygons_helper(t, side, k, n, sp). When it is done,
    the turtle is left hidden (visible is False).
    
    Parameter w: The window to draw upon.
    Precondition: w is a tkturtle Window object.
    
    Parameter side: The length of each polygon side
    Precondition: side is a valid side length (number >= 0)
    
    Parameter k: The number of polygons to draw
    Precondition: k is an int >= 1
    
    Parameter n: The number of sides of each polygon
    Precondition: n is an int >= 3
    
    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed."""
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_window(w), report_error('w is not a valid window',w)
    assert is_valid_length(side), report_error('side is not a valid length',side)
    assert is_valid_speed(sp), report_error('sp is not a valid speed',sp)
    assert type(k) == int and k >= 1, report_error('k is not a valid number of polgons',k)
    assert type(n) == int and n >= 3, report_error('n is not a valid number of sides' ,n)
    
    # HINT: w.clear() clears window.
    # HINT: set the turtle's visible attribute to False at the end.
    
    w.clear()
    t = tkturtle.Turtle(w)
    t.heading = 90
    
    multi_polygons_helper(t, side, k, n, sp)
    
    t.visible = False


def multi_polygons_helper(t, side, k, n, sp):
    """Draws k n-sided polygons of side length s.
    
    The polygons are drawn by turtle t, starting at the current position.
    The turtles alternate colors between red and green. Each polygon is drawn
    starting at the same place (within roundoff errors), but t turns left
    360.0/k degrees after each polygon. The turtle draws at speed sp.
    
    At the end, ALL ATTRIBUTES of the turtle are the same as they were in the
    beginning (within roundoff errors).  If you change any attributes of the
    turtle. then you must restore them.  Look at the helper draw_polygon for
    more information.
    
    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.
    
    Parameter side: The length of each polygon side
    Precondition: side is a valid side length (number >= 0)
    
    Parameter k: The number of polygons to draw
    Precondition: k is an int >= 1
    
    Parameter n: The number of sides of each polygon
    Precondition: n is an int >= 3
    
    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed."""
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(side), report_error('side is not a valid length',side)
    assert is_valid_speed(sp), report_error('sp is not a valid speed',sp)
    assert type(k) == int and n >= 1, report_error('k is not a valid number of polgons',k)
    assert type(n) == int and n >= 3, report_error('n is not a valid number of sides' ,n)
    
    # HINT:  make sure that upon termination, t's color and speed are restored
    # HINT: since k polygons should be drawn, use a for-loop on a range.
    
    start_color = t.color
    start_speed = t.speed
    
    t.speed = sp
    for x in range(k):
        if x%2 == 0:
            t.color ='red'
        else:
            t.color ='green'
            
        draw_polygon(t, side, n, sp)
        t.left(360.0/k)
        
    t.color = start_color
    t.speed= start_speed


# DO NOT MODIFY
def draw_polygon(t, side, n, sp):
    """Draw an n-sided polygon using of side length side.
    
    The polygon is drawn with turtle t using speed sp.
    
    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED:
    position (x and y, within round-off errors), heading, color, speed,
    visible, and drawmode.  There is no need to restore these.

    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.
    
    Parameter side: The length of each polygon side
    Precondition: side is a valid side length (number >= 0)
    
    Parameter n: The number of sides of each polygon
    Precondition: n is an int >= 3
    
    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed."""
    # Assert the preconditions
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(side), report_error('side is not a valid length',side)
    assert (type(n) == int and n >= 3), report_error('n is an invalid # of poly sides',n)
    assert is_valid_speed(sp), report_error('sp is not a valid speed',sp)
    
    # Remember old speed
    oldspeed = t.speed
    t.speed = sp
    ang = 360.0/n # exterior angle between adjacent sides
    
    # t is in position and facing the direction to draw the next line.
    for _ in range(n):
        t.forward(side)
        t.left(ang)
    
    # Restore the speed
    t.speed = oldspeed





def radiate(w, side, n, sp):
    """Draw n straight radiating lines using radiate_helper(t, side, n, sp)
    
    This function clears the window and makes a new turtle t.  This turtle
    starts in the middle of the canvas facing east (NOT the default west).
    It then calls radiate_helper(t, side, n, sp). When it is done, the
    turtle is left hidden (visible is False).
    
    Parameter w: The window to draw upon.
    Precondition: w is a tkturtle Window object.
    
    Parameter side: The length of each radial line
    Precondition: side is a valid side length (number >= 0)
    
    Parameter n: The number of lines to draw
    Precondition: n is an int >= 2
    
    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed."""
    
    assert is_window(w), report_error('w is not a valid window',w)
    assert is_valid_length(side), report_error('side is not a valid length',side)
    assert is_valid_speed(sp), report_error('sp is not a valid speed',sp)
    assert type(n) == int and n>= 2, report_error('n is not a valid number of lines',n)
   
    
    w.clear()
    t = tkturtle.Turtle(w)
    t.heading = 0
    
    radiate_helper(t, side, n, sp)
    
    t.visible = False


def radiate_helper(t, side, n, sp):
    """Draws n straight radiating lines of length s at equal angles.
    
    This lines are drawn using turtle t with the turtle moving at speed sp.
    A line drawn at angle ang, 0 <= ang < 360 has HSV color (ang % 360.0, 1, 1).
    
    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED:
    color, speed, visible, and drawmode. However, the final position and
    heading may be different. If you changed any of these four in the function,
    you must change them back.
    
    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.
    
    Parameter side: The length of each radial line
    Precondition: side is a valid side length (number >= 0)
    
    Parameter n: The number of lines to draw
    Precondition: n is an int >= 2
    
    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed."""
    
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(side), report_error('side is not a valid length',side)
    assert is_valid_speed(sp), report_error('sp is not a valid speed',sp)
    assert type(n) == int and n>= 2, report_error('n is not a valid number of lines',n)
        

    
    start_color = t.color
    start_speed = t.speed
    ang = 360.0/n
    t.speed = sp
    
    for x in range(n):
        t.color = colormodel.HSV(t.heading%360.0, 1, 1)
        t.forward(side)
        t.backward(side)
        t.left(ang)

    t.speed = start_speed
    t.color = start_color
    



def cantor(w, side, hght, d):
    """Draws a Cantor Stool of dimensions side x hght, and depth d.
    
    This function clears the window and makes a new graphics pen p.  This
    pen starts in the middle of the canvas at (0,0). It draws by calling
    the function cantor_helper(p, 0, 0, side, hght, d). The pen is visible
    during drawing and should be set to hidden at the end.
    
    The pen should have a fill color of red and a line color of black.
    
    Parameter w: The window to draw upon.
    Precondition: w is a tkturtle Window object.
    
    Parameter side: The width of the Cantor stool
    Precondition: side is a valid side length (number >= 0)
    
    Parameter hght: The height of the Cantor stool
    Precondition: hght is a valid side length (number >= 0)
    
    Parameter d: The recursive depth of the stool
    Precondition: d is a valid depth (int >= 0)"""
   
    assert is_window(w), report_error('w is not a valid window',w)
    
  
    
    w.clear()
    p = tkturtle.Pen(w)
    p.visible = True
    p.pencolor = 'black'
    p.fillcolor = 'red'
    cantor_helper(p, 0, 0, side, hght, d)
    p.visible = False
    
def cantor_helper(p, x, y, side, hght, d):
    """Draws a stool of dimensions side x hght, and depth d centered at (x,y)
    
    The stool is draw with the current pen color and visibility attribute.
    Follow the instructions on the course website to recursively draw the
    Cantor stool.
    
    Parameter p: The graphics pen
    Precondition: p is a Pen with fill attribute False.
    
    Parameter x: The x-coordinate of the stool center
    Precondition: x is a number
    
    Parameter y: The y-coordinate of the stool center
    Precondition: y is a number
    
    Parameter side: The width of the Cantor stool
    Precondition: side is a valid side length (number >= 0)
    
    Parameter hght: The height of the Cantor stool
    Precondition: hght is a valid side length (number >= 0)
    
    Parameter d: The recursive depth of the stool
    Precondition: d is a valid depth (int >= 0)"""
    
    assert is_valid_penmode(p), report_error('Invalid pen mode', p)
    assert type(x) == int or float, report_error('invalid x-coordinate', x)
    assert type(y) == int or float, report_error('invalid y-coordinate', y)
    assert type(side) == int or float and side >= 0, report_error('invalid side length', side)
    assert type(hght) == int or float and hght >= 0, report_error('invalid height', hght)
    assert type(d) == int and d >= 0, report_error('invalid depth',d)                                                     
   
    
    if d == 0:
        fill_rect(p, x, y, side, hght)
        
    elif d>0:
        fill_rect(p,x, y+hght/4.0, side, hght/2.0)
        cantor_helper(p,x-side/3.0,y-hght/4.0,side/3.0,hght/2.0,d-1)
        cantor_helper(p, x+side/3.0, y-hght/4.0,side/3.0, hght/2.0, d-1)
        
def fill_rect(p, x, y, side, hght):
    """Fill a rectangle of lengths side, hght with center (x, y) using pen p.
    
    Parameter p: The graphics pen
    Precondition: p is a Pen with fill attribute False.
    
    Parameter x: The x-coordinate of the rectangle center
    Precondition: x is a number
    
    Parameter y: The y-coordinate of the rectangle center
    Precondition: y is a number
    
    Parameter side: The width of the rectangle
    Precondition: side is a valid side length (number >= 0)
    
    Parameter hght: The height of the rectangle
    Precondition: hght is a valid side length (number >= 0)"""
   
    
    # Move to the center and draw
    p.move(x - side/2.0, y - hght/2.0)
    p.fill = True
    p.drawLine(    0,  hght)
    p.drawLine( side,     0)
    p.drawLine(    0, -hght)
    p.drawLine(-side,     0)
    p.fill = False
    p.move(x - side/2.0, y - hght/2.0)





def sierpinski(w, side, d):
    """Draws a Sierpinski Triangle of side length and depth d.
    
    This function clears the window and makes a new graphics pen p.  This
    pen starts in the middle of the canvas at (0,0). It draws by calling
    the function sierpinski_helper(p, 0, 0, side, d). The pen is hidden during
    drawing and left hidden at the end.
    
    The pen should have both a 'magenta' fill color and a 'magenta' line color.
    
    Parameter w: The window to draw upon.
    Precondition: w is a tkturtle Window object.
    
    Parameter side: The side-length of the t-square
    Precondition: side is a valid side length (number >= 0)
    
    Parameter d: The recursive depth of the t-square
    Precondition: d is a valid depth (int >= 0)"""
   
    assert is_window(w), report_error('w is not a valid window',w)
    
    
    w.clear()
    p = tkturtle.Pen(w)
    p.visible = True
    p.pencolor = 'magenta'
    p.fillcolor = 'magenta'
    sierpinski_helper(p, 0, 0, side, d)
    p.visible = False


def sierpinski_helper(p, x, y, side, d):
    """Draws a Sierpinski triangle with side length and depth d anchored at (x, y).
    
    The (x,y) defines the lower left corner of the Sierpinksi triangle (NOT
    the middle as you might want to do). 
    
    The triangle is draw with the current pen color and visibility attribute.
    Follow the instructions on the course website to recursively draw the
    Sierpinski triangle.
    
    Parameter p: The graphics pen
    Precondition: p is a Pen with fill attribute False.
    
    Parameter x: The x-coordinate of the lower-left corner of the triangle
    Precondition: x is a number
    
    Parameter y: The y-coordinate of the lower-left corner of the triangle
    Precondition: y is a number
    
    Parameter side: The side-length of the triangle
    Precondition: side is a valid side length (number >= 0)
    
    Parameter d: The recursive depth of the triangle
    Precondition: d is a valid depth (int >= 0)"""
   
    assert is_valid_penmode(p), report_error('Invalid pen mode', p)
    assert is_number(x), report_error('invalid x co-ordinate', x)
    assert is_number(y), report_error('invalid y co-ordinate', y)
    assert is_valid_length(side), report_error('side is not a valid side-length', side)
    assert is_valid_depth(d), report_error('d is an invalid depth', d)
    
   
    if d == 0:
        fill_triangle(p, side)
        
    elif d > 0:
        fill_triangle(p, side/2.0)
        sierpinski_helper(p, x+side/4.0, y+side/2.0, side/2.0, d-1 )
#if pen returns to original postion(bottom left of first triangle)
        sierpinski_helper(p, x+side/2.0, y, side/2.0, d-1)
        


# Useful helper function
def fill_triangle(p, side):
    """Fill the equilateral triangle of side length side using pen p.
    
    The left point of the triangle base is at the current position of p. 
    In addition, the triangle is pointing up. When done, the position of Pen p 
    should be as it was initially.
    
    Parameter p: The graphics pen
    Precondition: p is a Pen with fill attribute False.
    
    Parameter side: The side length of the triangle
    Precondition: side is a valid side length (number >= 0)"""
    h = side * math.sqrt(0.75)
    p.fill = True
    p.drawLine(side, 0)
    p.drawLine(-side/2.0, h)
    p.drawLine(-side/2.0, -h)
    p.fill = False




def branches(w, hght, d):
    """Draws a three-branches tree with height hght and depth d.
    
    This function clears the window and makes a new turtle t.  This turtle
    starts at the bottom of the tree facing north (NOT the default west).
    Since the tree should be centered at (0,0), this means the turtle is
    positioned at (0,-hght/2).  This function calls branches_helper(t,hght,d),
    which does all the drawing. When it is done, the turtle is left hidden
    (visible is False).
    
    The turtle color is 'blue'.  The Turtle is visible when drawing and
    hidden at the end.
    
    Parameter w: The window to draw upon.
    Precondition: w is a tkturtle Window object.
    
    Parameter hght: The height of the three-branches tree
    Precondition: side is a valid side length (number >= 0)
    
    Parameter d: The recursive depth of the three-branches tree
    Precondition: n is a valid depth (int >= 0)"""
    
    assert is_window(w), report_error('w is not a valid window',w)
    
   
    pass


def branches_helper(t, hght, d):
    """Draws a tree of height hght and depth d at the current position
    
    The tree is draw with the current turtle color, and assuming that the
    current turtle position is the bottom of the tree. The up-direction
    of the tree is the current direction of the turtle.
    
    At the end, ALL ATTRIBUTES of the turtle are the same as they were in the
    beginning (within roundoff errors).  If you change any attributes of the
    turtle. then you must restore them.
    
    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.
    
    Parameter hght: The height of the three-branches tree
    Precondition: side is a valid side length (number >= 0)
    
    Parameter d: The recursive depth of the three-branches tree
    Precondition: n is a valid depth (int >= 0)"""
  
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    
   
    pass


################ Test Function #################

def str_to_int(s):
    """Returns: int equivalent to s if possible; -1 otherwise.
    
    Parameter s: the string to convert
    Precondition: s is a string"""
    try:
        return int(s.strip())
    except:
        return -1


def main():
    """Run each of the functions, allowing user to skip functions."""
    w = tkturtle.Window()
    
    ans = raw_input('Call draw_two_lines? [y/n]: ')
    if ans.strip().lower() == 'y':
        draw_two_lines(w,5)
    
    ans = raw_input('Call draw_triangle? [y/n]: ')
    if ans.strip().lower() == 'y':
        w.clear()
        turt = tkturtle.Turtle(w)
        draw_triangle(turt,50,'blue')
    
    ans = raw_input('Call draw_hex? [y/n]: ')
    if ans.strip().lower() == 'y':
        w.clear()
        turt = tkturtle.Turtle(w)
        draw_hex(turt,50)
    
    ans = raw_input('Call draw_spiral? [y/n]: ')
    if ans.strip().lower() == 'y':
        draw_spiral(w, 1, 24, 64, 0)
    
    ans = raw_input('Call multi_polygons? [y/n]: ')
    if ans.strip().lower() == 'y':
        multi_polygons(w, 100, 5, 6, 0)
    
    ans = raw_input('Call radiate? [y/n]: ')
    if ans.strip().lower() == 'y':
        radiate(w, 150, 45, 0)
    
    ans = raw_input('Cantor depth [-1 to skip]: ')
    d = str_to_int(ans)
    if d >= 0:
        cantor(w, 200, 100, d)
    
    ans = raw_input('Sierpinski depth [-1 to skip]: ')
    d = str_to_int(ans)
    if d >= 0:
        sierpinski(w, 150, d)
    
    ans = raw_input('3-Branches depth [-1 to skip]: ')
    d = str_to_int(ans)
    if d >= 0:
        branches(w, 250, d)
    
    # Pause for the final image
    raw_input('Press <return>')


# Application code
if __name__ == '__main__':
    main()
