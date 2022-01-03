import turtle


win = turtle.Screen()
win.title("Pong by Rebecca")
win.bgcolor("blue")
win.setup(width=800, height=600)
win.tracer(0) #stops the window from updating

#Main game loop
while True:
    win.update() #everytime the loop runs it updates the screen