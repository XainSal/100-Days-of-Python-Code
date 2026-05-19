def turn_right():
    turn_left()
    turn_left()
    turn_left()

def check_condition():
    if front_is_clear():
        if wall_on_right():
            move()
        else:
            turn_right()
            move()
    elif wall_in_front():
        if wall_on_right():
            turn_left()
        else:
            turn_right()
            move()
            
while not at_goal():
    check_condition()