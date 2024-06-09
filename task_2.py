import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    koch_curve(t, order, size)
    t.right(120)
    koch_curve(t, order, size)
    t.right(120)
    koch_curve(t, order, size)

    window.mainloop()


def main():
    while True:
        order_level = input('Type order level for Koch snowflake:\n')

        if not order_level.isnumeric():
            print('Order level should be a number greater than or equal 0!')
        else:
            draw_koch_snowflake(int(order_level))
            break
    
    print('\nGoodbye!')
          

if __name__ == '__main__':
    main()
