#Rock,Paper,Sissor game
import random
userpoint=0
comppoint=0

print("How many round you have to play")
round=int(input("Enter number of rounds : "))
for i in  range(round):
    print("R for Rock")
    print("P for Paper")
    print("S for Sissor")
    choice=input("Enter your choise : ").upper()
    if(choice=="R" or choice=="P" or choice=="S"):
        pos=["R", "P", "S"]
        ca=random.choice(pos)
        print("Computer Choice :",ca)
        print(i+1," Round  finished")
        print()
        if(choice==ca):
         userpoint+=0
         comppoint+=0
         print("Tie")
        elif (choice=="R" and ca=="P") or (choice=="P" and ca=="R") or (choice=="S" and ca=="P"):

          userpoint+=1
          print("point for user")
    
        else:
         comppoint+=1
         print("point for Computer")
    else:
       print("invalid choice and game is ended")
       break
       
       

if(userpoint>comppoint):
    print("********User Won the Match********")
    print("At the  end of game")
    print()
    print("User Point :",userpoint)
    print("Computer Point :",comppoint)
    print()
elif(userpoint<comppoint):
    print("Computer WON the Match")
    print("At the  end of game")
    print()
    print("User Point :",userpoint)
    print("Computer Point :",comppoint)
    print()
# elif(userpoint==comppoint):
#     print("********TIE********")


