import random
print("\n---------------Hey user Welcome to the game Rock Paper Scissors!!---------------")
print("---------------0 : ROCK--------------- \n---------------1 : PAPER--------------- \n---------------2 : SCISSORS---------------\n")
num=int(input("Hey,- Pick  1 to start the Game \n    - pick 0 to exit game  :"))
game={0:"stone",1:"paper",2:"scissors"}
guss=random.randrange(0,3)
k=1
counter1=0
counter2=0
total_game=0
if num==1:
    while(k<=20):
        num = int(input("Pick a number from the given Box :"))
        if (num <= 2):
            total_game+=1
            print("you selected", game[num])
            print("Computer selected", game[guss])
            if num==0:
                if game[guss]==game[1]:
                    print("You got 0 point \n")
                    counter1+=1
                elif game[guss]==game[num]:
                    print("Try again...!")
                else:
                    print("You got 1 Point")
                    counter2 += 1
            elif num==1:
                if game[guss]==game[2]:
                    print("You got 0 point")
                    counter1 += 1
                elif game[guss]==game[num]:
                    print("Try again...!")
                else:
                    print("You got 1 Point")
                    counter2 += 1
            else:
                if game[guss]==game[0]:
                    print("You got 0 pont")
                    counter1 += 1
                elif game[guss]==game[num]:
                    print("Try again...!")
                else:
                    print("You got 1 Point")
                    counter2 += 1
        else:
            break
            # print("Hey Select any values from 0-2!")
        # num = int(input("Hey,Pick the next number from the given Box :"))
        k+=1
    print("Game ended!!")
    if counter1>counter2:
        print("Opzz!you failed...!!!! \n---------------Points---------------\n Computer got",counter1,"points.\n Number of games you have played",total_game,"\n You got",counter2,"points." )
    elif counter1<counter2:
        print("Congrats!!! You Won!! \n ---------------Points---------------\n You got",counter2,"points \n Number of games you have played",total_game,"\n Computer got",counter1,"points.")
    else:
        print("Hehhee... You and Computer got same point! ",counter1," Try again....")
elif num==0:
    print("---------------Exit---------------")
else:
    print("Opz! You entered an invalid number")

