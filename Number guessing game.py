print("NUMBER GUESSING GAME")
import random as r
z=True
li1=[]
guesses=0
ans=0
def mode():
    global z
    global guesses
    global ans
    ans+=r.randrange(1,100)
    while z:
        diff=input("Choose difficulty[E/M/H]: ").strip().upper()
        if diff=="E":
            guesses+=10
            z=False
        elif diff=="M":
            guesses+=5
            z=False
        elif diff=="H":
            guesses+=3
            z=False
        else:
             print("Error. please enter one of the three letters.")
    
def game():
    global guesses
    global ans
    if guesses==0:
        print("GAME OVER")

        q=input("Would you like to try again?(Y/N):").strip().upper()
        if q=="Y":
            ans=0
            mode()
            z=True
            game()
        elif q=="N":
            print("Thank you for playing!")
    else:
        inp=int(input("Guess the number: "))
        guesses-=1
        print(f"Guesses left: {guesses}")

        if inp>ans:
            print("The number is lesser")
            li1.append(inp)
            game()
        elif inp<ans:
            print("The number is greater")
            li1.append(inp)
            game()
        else:
            print("You guessed it correctly!")
            li1.append(inp)
            q=input("Would you like to try again?(Y/N):").strip().upper()
            if q=="Y":
                z=True
                ans=0
                mode()
                game()
            elif q=="N":
                print("Thank you for playing!")




mode()       
game()      



















        
            
