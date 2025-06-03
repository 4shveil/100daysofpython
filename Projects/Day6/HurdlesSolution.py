def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def hurdle_jump():
    if right_is_clear():
        turn_right()
        move()
        return
    if not is_facing_north() and not front_is_clear():
        turn_left()

while not at_goal():
    while wall_on_right() and front_is_clear():
        move()
        break
    hurdle_jump()
