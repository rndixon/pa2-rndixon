# Programmers: Richard Dixon
# Course: CS151, Professor Franceshci
# Date: 10/2/17
# Programming Assigment 2
# Making an adventure game
# Data in: Input, if, else, elif
# Data Out: Print Statements

#Tell backstory
print("In the mail you receive an invitation to spend a week at a really nice resort, and you get to stay at an expense paid luxury mansion. At first you are pumped, but after you get there the mansion is not what was advertised. An eerie voice wakes you up in the middle of the night and says, that you have 24 hours to find a way out or you will die. All the exits are locked, and it is up to you to find a way out")
#User inputs their name
name = input ("Enter your name ")
print("Hello", name)
#Story Part 1
print("After scouring the whole building you realize that every door is locked except for a red door and a green door.")
#User chooses what color door they want to go through
door_color = input("What door will you go through ")
#Change into strings
red = "red"
green = "green"

#if they chose red then the part 2 (red) storyline is followed
if door_color == "red":
    print("You procede through the red door")
#Story part 2(red)
    print("You walked through the door, and are jogging through the hallway when you accidently step on a trap panel. What trap attacks you?")
    number = input("Enter a number between 1 and 14 to select a punishment ")
    str_number = int(number)
    if str_number <= 5:
        print("arrows")
    elif str_number > 6 and str_number <= 10:
        print("rocks")
    elif str_number > 10 and str_number <= 14:
        print("nothing")
if door_color == "green":
    print("You go through the green door")
#Story part 2(green)
    print("You have ran for a while, and come upon a nice room. Since you have been in danger all day you take this oppurtunity to rest. Then out of no where you see a man creep up in the corner of your eye. He has a weapon; you only have mere seconds to dodge. What does he hit.")
    str_x = input("Enter a number between 1 and 3 to see your injury ")
    str_x = int(str_x)
    if str_x == 1:
        print("You receive a nasty gash to the side")
    elif str_x == 2:
        print("He cuts you on your eye")
    elif str_x == 3:
        print("Unfortunately you were not quick enough as a result he cut off your hand")
#Story part 3
print("Battered and bruised you have finally gotten to the last room. There is a door with a electronic lock on it. The voice comes back and says congratulations on making it this far, but in order to escape you have to give a value to put into this equation.")
final = input("What number should be substituted for x to make this expression true. x >= .0568 * 6")
final = float(final)
if final == .5 * 6:
    print("Wow you are CORRECT")
    print("The door opens and you escape to the outside world where your family surrounded by a bunch of police are waiting for your safe return.")
else:
    print("You are INCORRECT")
    print("A darkness starts filling the room, and the last thing you see is something leap out at you. As the creature leaps darkness prevails, and everything goes dark. Thus you were never seen or heard from again.")



