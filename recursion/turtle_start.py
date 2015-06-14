import turtle

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(40)
        tree(branchLen-15,t)
        t.left(80)
        tree(branchLen-15,t)
        t.right(40)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(120,t)
    myWin.exitonclick()

main()
