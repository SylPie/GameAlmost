import random

def findValue(value, percentRange):
    minValue = value - (percentRange / 100) * value
    maxValue = value + (percentRange / 100) * value
    return random.randint(minValue, maxValue)
w = 0
gold_held = 0
you_meet_chests = ['yes', 'no']
types_of_chests = ['green', 'orange', 'violet', 'gold(legendary)']
movement = 5
print("|--->-->->Welcome in chamber<-<--<---| \n")
while (movement > 0):
    make_a_movement = input("Do you want to go ahead? If you want, enter yes: ")
    print(" \n")

    if(make_a_movement == 'yes'):
        if_you_meet_chests = random.choices(you_meet_chests, [60, 40], k = 1)
        movement -= 1
        
        if(if_you_meet_chests == ['yes']):
            print("GOOD JOB! You found the chests.")

            types_of_chests2 = random.choices(types_of_chests, [75 , 20, 4, 1], k = 1)


            if(types_of_chests2 == ['green']):
                print("Your chest is green. \n")
                w = findValue(1000, 10)
                gold_held += w
                print("YEAH! There is", w, "gold in it. \n")
                
            if(types_of_chests2 == ['orange']):
                print("Your chest is orange. \n")
                w = findValue(4000, 10)
                gold_held += w
                print("YEAH! There is", w, "gold in it. \n")
                
            if(types_of_chests2 == ['violet']):
                print("Your chest is violet. \n")
                w = findValue(9000, 10)
                gold_held += w
                print("YEAH! There is", w, "gold in it. \n")

            if(types_of_chests2 == ['gold(legendary)']):
                print("Your chest is gold(legendary). \n")
                w = findValue(16000, 10)
                gold_held += w
                print("YEAH! There is", w, "gold in it. \n")

        else:
            print("Sorry guy, there is nothing here ;( \n")

    elif(make_a_movement == 'no'):
        print("This chamber is not for cowards, so you can only go ahead!! \n")

    else:
        print("This chamber is not for cowards, so you can only go ahead!! \n")

    


if(gold_held == 0):
    print("Fucking seriously, there was nothing there?")
    
elif(gold_held > 1000 and gold_held < 4000):
    print("You earned", gold_held, "gold , applause.")

elif(gold_held > 4000 and gold_held < 9000):
    print("For", gold_held, "gold you can go on a nice vacation")

elif(gold_held > 9000 and gold_held < 16000):
    print("Oh yeah, you collected", gold_held, "gold. I knew you could handle it")
elif(gold_held > 16000):
    print("Finds", gold_held, "gold you broke the bank. Maybe you want to visit another room?")

return(0)