def turn_right():
    turn_left()
    turn_left()
    turn_left() 
    
consecutive_right_turns = 0    
    
def hurdle_jump():
    global consecutive_right_turns
    if right_is_clear() and consecutive_right_turns < 21:
        consecutive_right_turns += 1
        turn_right()
        move()
        return
    if consecutive_right_turns > 20:
        consecutive_right_turns = 0
        turn_left()
        if front_is_clear():
            move()

while not at_goal():
    while wall_on_right() and front_is_clear():
        move()
        break
    if at_goal():
        break
    if wall_in_front() and not right_is_clear() and not at_goal():
        turn_left()
        continue
    hurdle_jump()
