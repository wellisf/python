import turtle

def drawSquare(temp):
    
    for x in range(0, 4):
        temp.forward(100)
        temp.right(90)
         
window = turtle.Screen()
window.bgcolor("beige")  

brad = turtle.Turtle()
brad.shape("turtle")
brad.color("forest green")
brad.speed(3)

for x in range(0,36):
    drawSquare(brad)
    brad.right(10)

window.exitonclick()
