def game():
    state = "FOREST"
    w = input("Would you like to go North or East?")
    if w == "North":
        state = "CAVE"
        print("What is this??? TREASURE??? YOU WON!!!")
    elif w == "East":
        state = "RIVER"
        s = input("You are at a river, would you like to swim or return to the forest?")
        if s == "swim":
            print("YOU DROWNED!!! WHAT ARE YOU DOING?!?!")
        elif s == "return to forest":
            state = "FOREST"
            return game()
    else: 
        print("YOU IDIOT THERE IS A BEAR IN THAT DIRECTION!!!")
game()
