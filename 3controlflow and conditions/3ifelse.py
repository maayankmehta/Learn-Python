#conditional statements

#if/elif/else statement

# Complete the if and elif statements!
def game_rps(input):
    if input == 1:
        return "rock"
    elif input == 2:
        return "paper"
    elif input == 3:
        return "scissors"
    else:
        return 0
      
# This should print "rock"     
print (game_rps(1))

# This should print "scissors"
print (game_rps(3))

# This should print "paper"
print (game_rps(2))

# This should print 0
print(game_rps(5))
