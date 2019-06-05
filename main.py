import turtle

tiny = turtle.Turtle()
window = tiny.getscreen()
window.reset()
window.bgcolor("olive drab")
tiny.color("white")
penup()
forward(250)

#Speed of drawing
tiny.speed(0.5)


#inside of track (Square)
tiny.penup()
tiny.forward(60)
tiny.pendown()
tiny.fillcolor("green")
tiny.begin_fill()
tiny.left(90)
tiny.backward(30)
tiny.forward(50)
tiny.left(90)
tiny.forward(120)
tiny.left(90)
tiny.forward(50)
tiny.left(90)
tiny.forward(120)
tiny.end_fill()
tiny.backward(120)

#start of outline
tiny.right(90)
tiny.penup()
tiny.forward(20)
tiny.left(90)
tiny.pendown()
tiny.forward(120)
tiny.pendown()


#start of outline curve around inside field
tiny.circle(45,180)
tiny.forward(120)


tiny.circle(45,180)
tiny.forward(120)

#positions the start of the first lane
tiny.penup()
tiny.left(180)
tiny.fillcolor("firebrick")
tiny.begin_fill()
tiny.pendown()
tiny.forward(120)
tiny.left(90)

#Start of 1std lane 
tiny.forward(20)
tiny.left(90)
tiny.forward(120)
tiny.left(90)
tiny.forward(20)
tiny.end_fill()
tiny.backward(20)
tiny.right(90)

tiny.backward(120)

tiny.left(90)

#line across field
tiny.forward(20)
tiny.penup()
tiny.forward(90)
tiny.pendown()


# fill im algorithm color for lane
tiny.fillcolor("firebrick")
tiny.begin_fill()
tiny.forward(20)
tiny.right(90)
tiny.forward(120)
tiny.right(90)
tiny.forward(20)
tiny.end_fill()
tiny.penup()
tiny.forward(90)
tiny.pendown()
tiny.forward(20)
tiny.left(90)

#Start of 2nd lane
tiny.circle(65,180)
tiny.forward(120)
tiny.circle(65,180)

#start of 2nd lane
tiny.right(90)
tiny.fillcolor("firebrick")
tiny.begin_fill()
tiny.forward(20)
tiny.left(90)
tiny.forward(120)
tiny.left(90)
tiny.forward(20)
tiny.end_fill()
tiny.backward(20)
tiny.right(90)
tiny.circle(85,180)


tiny.fillcolor("firebrick")
tiny.begin_fill()
tiny.forward(120)
tiny.left(90)
tiny.forward(20)
tiny.left(90)
tiny.forward(120)
tiny.left(90)
tiny.forward(20)
tiny.end_fill()

tiny.left(90)
tiny.forward(120)

tiny.circle(85,180)

#Start of 3rd lane
tiny.right(90)
tiny.fillcolor("firebrick")
tiny.begin_fill()
tiny.forward(20)
tiny.left(90)
tiny.forward(120)
tiny.left(90)
tiny.forward(20)
tiny.end_fill()
tiny.backward(20)
tiny.right(90)
tiny.circle(105,180)

tiny.fillcolor("firebrick")
tiny.begin_fill()
tiny.forward(120)
tiny.left(90)
tiny.forward(20)
tiny.left(90)
tiny.forward(120)
tiny.left(90)
tiny.forward(20)
tiny.end_fill()

tiny.left(90)
tiny.forward(120)


tiny.circle(105,180)

#start of the 4th lane
tiny.right(90)
tiny.fillcolor("firebrick")
tiny.begin_fill()
tiny.forward(20)
tiny.left(90)
tiny.forward(120)
tiny.left(90)
tiny.forward(20)
tiny.end_fill()
tiny.backward(20)
tiny.right(90)

tiny.fillcolor("firebrick")
tiny.begin_fill()

tiny.circle(125,180)
tiny.left(90)
tiny.forward(20)
tiny.right(90)
tiny.circle(105,-180)
tiny.end_fill()

tiny.begin_fill()
tiny.circle(105,180)
tiny.left(90)
tiny.forward(20)
tiny.right(90)
tiny.circle(85,-180)
tiny.end_fill()

tiny.begin_fill()
tiny.circle(85,180)
tiny.left(90)
tiny.forward(20)
tiny.right(90)
tiny.circle(65,-180)
tiny.end_fill()

tiny.begin_fill()
tiny.circle(65,180)
tiny.left(90)
tiny.forward(20)
tiny.right(90)
tiny.circle(45,-180)
tiny.end_fill()

tiny.penup()
tiny.left(90)
tiny.forward(170)
tiny.left(90)
tiny.pendown()


tiny.fillcolor("firebrick")
tiny.begin_fill()
tiny.forward(120)
tiny.left(90)
tiny.forward(20)
tiny.left(90)
tiny.forward(120)
tiny.left(90)
tiny.forward(20)
tiny.end_fill()

tiny.left(90)
tiny.forward(120)



tiny.fillcolor("firebrick")
tiny.begin_fill()

tiny.circle(125,180)
tiny.left(90)
tiny.forward(20)
tiny.right(90)
tiny.circle(105,-180)
tiny.end_fill()

tiny.begin_fill()
tiny.circle(105,180)
tiny.left(90)
tiny.forward(20)
tiny.right(90)
tiny.circle(85,-180)
tiny.end_fill()

tiny.begin_fill()
tiny.circle(85,180)
tiny.left(90)
tiny.forward(20)
tiny.right(90)
tiny.circle(65,-180)
tiny.end_fill()

tiny.begin_fill()
tiny.circle(65,180)
tiny.left(90)
tiny.forward(20)
tiny.right(90)
tiny.circle(45,-180)
tiny.end_fill()

tiny.penup()
tiny.forward(300)



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Start of the go0od stuff
import random

announcer = turtle.Turtle()
announcer.color("light blue")
announcer.shape("classic")
announcer.penup()
announcer.hideturtle()
announcer.setheading(90)
announcer.forward(150)
announcer.left(90)
announcer.forward(135)
announcer.setheading(90)



cc = input ("Enter a color for your athelete: ")
fname = input("What's your atheletes name: ")

flash = turtle.Turtle()
flash.color(cc)
flash.penup()
flash.right(90)
flash.forward(60)
flash.left(90)
flash.backward(50)
flash.write(fname, move=False, align="left", font=("comic sans",10, "normal"))
flash.forward(110)




black = turtle.Turtle()
black.color("black")

black.penup()
black.right(90)
black.forward(80)
black.left(90)
black.backward(50)
black.write("Usain Bolt", move=False, align="left", font=("comic sans", 10, "normal"))
black.forward(110)


white = turtle.Turtle()
white.color("cyan")
white.penup()
white.right(90)
white.forward(100)
white.left(90)
white.backward(50)
white.write("Jaden Frazier", move=False, align="left", font=("comic sans",10, "normal"))
white.forward(110)

blue = turtle.Turtle()
blue.color("gold")
blue.penup()
blue.right(90)
blue.forward(120)
blue.left(90)
blue.backward(50)
blue.write("The Flash", move=False, align="left", font=("comic sans",10, "normal"))
blue.forward(110)

print "What event would you like to run Today? "
start = input("Enter 100m,200m, or 400m: ")
if (start == "200m"):
    flash.setposition(-45,50)
    black.setposition(-45,70)
    white.setposition(-45,90)
    blue.setposition(-45,110)
elif(start == "100m"):
    flash.backward(120)
    black.backward(120)
    white.backward(120)
    blue.backward(120)

#path 
running = True

lastlapf = False
lastlapb = False
lastlapw = False
lastlape = False
announced = False
winner = ""

def wins():
    global lastlapf
    global lastlapb
    global lastlapw
    global lastlape
    global announced
    global winner
    
    if(flash.xcor() < 0):
        lastlapf = True
    if(black.xcor() < 0):
        lastlapb = True
    if(white.xcor() < 0):
        lastlapw = True
    if(blue.xcor() < 0):
        lastlape = True
    
    if(announced == False):
        if(flash.xcor() > 60 and lastlapf):
            winner = fname
            announced = True
        if(black.xcor() > 60 and lastlapb):
            winner = "Usain Bolt"
            announced = True
        if(white.xcor() > 60 and lastlapw):
            winner = "Jaden Frazier"
            announced = True
        if(blue.xcor() > 60 and lastlape):
            winner = "The Flash"
            announced = True
        if(announced):
            announcer.write(winner + " wins!", move=False, align="left", font=("Arial", 30, "normal"))


def run(): 
    if running:
        if (flash.xcor() >= 60 or flash.xcor() <= -60):
            flash.forward(4.6)
            flash.left(5)
        if (black.xcor() >= 60 or black.xcor() <= -60):
                black.forward(5.05679012346)
                black.left(3.998024691353)
        if (white.xcor() >= 60 or white.xcor() <= -60):
                 white.forward(5.61872592593)
                 white.left(3.40631703704)
        if (blue.xcor() >= 60 or blue.xcor() <= -60):
                blue.forward(6.888)
                blue.left(3.5112)
            
    
    # straight path
    
        if(flash.xcor() > -60 and flash.xcor() < 60):
            if(flash.ycor() > 0):
                flash.setheading(180)
                x = random.randint(2,5)
                flash.forward(x)
            else:
                flash.setheading(0)
                x = random.randint(2,5)
                flash.forward(x)
        if(black.xcor() > -60 and black.xcor() < 60):
            if(black.ycor() > 0):
                black.setheading(180)
                x = random.randint(4,6)
                black.forward(x)
            else:
                black.setheading(0)
                x = random.randint(3,6)
                black.forward(x)
        if(white.xcor() > -60 and white.xcor() < 60):
            if(white.ycor() > 0):
                white.setheading(180)
                x = random.randint(7,8)
                white.forward(x)
            else:
                white.setheading(0)
                x = random.randint(6,10)
                white.forward(x)
        if(blue.xcor() > -60 and blue.xcor() < 60):
            if(blue.ycor() > 0):
                blue.setheading(180)
                x = random.randint(3,7)
                blue.forward(x)
            else:
               blue.setheading(0)
               x = random.randint(9,13)
               blue.forward(x)
               
        wins()
        window.ontimer(run,30)

def run1():
    if running:
        if (flash.xcor() >= 60 or flash.xcor() <= -60):
            flash.forward(4.6)
            flash.left(5)
        if (black.xcor() >= 60 or black.xcor() <= -60):
                black.forward(5.05679012346)
                black.left(3.998024691353)
        if (white.xcor() >= 60 or white.xcor() <= -60):
                 white.forward(5.61872592593)
                 white.left(3.40631703704)
        if (blue.xcor() >= 60 or blue.xcor() <= -60):
                blue.forward(6.888)
                blue.left(3.5112)
            
    
    # straight path
    
        if(flash.xcor() > -60 and flash.xcor() < 60):
            if(flash.ycor() > 0):
                flash.setheading(180)
                x = random.randint(3,5)
                flash.forward(x)
            else:
                flash.setheading(0)
                x = random.randint(3,6)
                flash.forward(x)
        if(black.xcor() > -60 and black.xcor() < 60):
            if(black.ycor() > 0):
                black.setheading(180)
                x = random.randint(4,6)
                black.forward(x)
            else:
                black.setheading(0)
                x = random.randint(3,6)
                black.forward(x)
        if(white.xcor() > -60 and white.xcor() < 60):
            if(white.ycor() > 0):
                white.setheading(180)
                x = random.randint(7,8)
                white.forward(x)
            else:
                white.setheading(0)
                x = random.randint(6,10)
                white.forward(x)
        if(blue.xcor() > -60 and blue.xcor() < 60):
            if(blue.ycor() > 0):
                blue.setheading(180)
                x = random.randint(3,7)
                blue.forward(x)
            else:
               blue.setheading(0)
               x = random.randint(9,13)
               blue.forward(x)
               
        wins()
        window.ontimer(run,30)

def run2():
    if running:
        if (flash.xcor() >= 60 or flash.xcor() <= -60):
            flash.forward(9.2)
            flash.left(10)
        if (black.xcor() >= 60 or black.xcor() <= -60):
                black.forward(10.1135802469)
                black.left(7.99604938271)
        if (white.xcor() >= 60 or white.xcor() <= -60):
                 white.forward(11.2374518519)
                 white.left(6.81263407408)
        if (blue.xcor() >= 60 or blue.xcor() <= -60):
                blue.forward(13.776)
                blue.left(7.0224)
            
    
    # straight path
    
        if(flash.xcor() > -60 and flash.xcor() < 60):
            if(flash.ycor() > 0):
                flash.setheading(180)
                x = random.randint(3,5)
                flash.forward(x)
            else:
                flash.setheading(0)
                x = random.randint(3,6)
                flash.forward(x)
        if(black.xcor() > -60 and black.xcor() < 60):
            if(black.ycor() > 0):
                black.setheading(180)
                x = random.randint(4,6)
                black.forward(x)
            else:
                black.setheading(0)
                x = random.randint(3,6)
                black.forward(x)
        if(white.xcor() > -60 and white.xcor() < 60):
            if(white.ycor() > 0):
                white.setheading(180)
                x = random.randint(7,8)
                white.forward(x)
            else:
                white.setheading(0)
                x = random.randint(6,10)
                white.forward(x)
        if(blue.xcor() > -60 and blue.xcor() < 60):
            if(blue.ycor() > 0):
                blue.setheading(180)
                x = random.randint(3,7)
                blue.forward(x)
            else:
               blue.setheading(0)
               x = random.randint(9,13)
               blue.forward(x)
               
        wins()
        window.ontimer(run,30)
 
def run3():
    if running:
        if (flash.xcor() >= 60 or flash.xcor() <= -60):
            flash.forward(4.6)
            flash.left(5)
        if (black.xcor() >= 60 or black.xcor() <= -60):
                black.forward(5.05679012346)
                black.left(3.998024691353)
        if (white.xcor() >= 60 or white.xcor() <= -60):
                 white.forward(5.61872592593)
                 white.left(3.40631703704)
        if (blue.xcor() >= 60 or blue.xcor() <= -60):
                blue.forward(6.888)
                blue.left(3.5112)
            
    
    # straight path
    
        if(flash.xcor() > -60 and flash.xcor() < 60):
            if(flash.ycor() > 0):
                flash.setheading(180)
                x = random.randint(3,5)
                flash.forward(x)
            else:
                flash.setheading(0)
                x = random.randint(3,6)
                flash.forward(x)
        if(black.xcor() > -60 and black.xcor() < 60):
            if(black.ycor() > 0):
                black.setheading(180)
                x = random.randint(4,6)
                black.forward(x)
            else:
                black.setheading(0)
                x = random.randint(3,6)
                black.forward(x)
        if(white.xcor() > -60 and white.xcor() < 60):
            if(white.ycor() > 0):
                white.setheading(180)
                x = random.randint(7,8)
                white.forward(x)
            else:
                white.setheading(0)
                x = random.randint(6,10)
                white.forward(x)
        if(blue.xcor() > -60 and blue.xcor() < 60):
            if(blue.ycor() > 0):
                blue.setheading(180)
                x = random.randint(3,7)
                blue.forward(x)
            else:
               blue.setheading(0)
               x = random.randint(9,13)
               blue.forward(x)
               
        wins()
        window.ontimer(run,30)
 
x = random.randint(0,3)



if(x == 0):
    run()
elif(x==1):
    run2()
elif(x==2):
    run2()
else:
    run3()

run()