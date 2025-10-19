print("NUMBER GUESSING GAME")
import random as r
z=True
li1=[]
guesses=0
ans=0
def mode():


    print("\n------------------------------------------------------------------------------------------------------------ \n")
    print("Welcome!!")
    print("INSTRUCTIONS")
    print("1) Choose game difficulty=>\n\t E - easy - 10 guesses \n\t M - medium - 5 guesses \n\t H - hard - 3 guesses")
    print("2) Guess a number between 1 - 100 and user shall recieve a hint depending on the number they've guessed")
    print("3) Inputs such as strings or floats shall not be counted ")
    print("\n------------------------------------------------------------------------------------------------------------ \n")



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
    global z


    if guesses==0:
        print("GAME OVER")
        print(f"Your guesses \n {li1}")

        q=input("Would you like to try again?(Y/N):").strip().upper()
        if q=="Y":
            z=True
            ans=0
            mode()
            game()
        elif q=="N":
            print("Thank you for playing!")
        else:
            print("Invalid input!! Taking it as a 'NO' and EXITING THE GAME. Thank you for playing!!!")


    else:
        try:
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
            elif inp == ans:
                print("Congratulations!! You guessed it correctly!")
                li1.append(inp)

                print(f"\n Your guesses \n {li1}")

                q=input("Would you like to try again?(Y/N):").strip().upper()
                if q=="Y":
                    z=True
                    ans=0
                    mode()
                    game()
                elif q=="N":
                    print("Thank you for playing!")
                else:
                    print("Invalid input!! Taking it as a 'NO' and EXITING THE GAME. Thank you for playing!")

        except ValueError:
            print("Invalid input!! Try again.")
            game()




mode()       
game()      



















        
            
