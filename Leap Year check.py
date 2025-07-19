yr=input("Enter year:")

def LeapCheck(x):
    if int(x)%100==0:
        if int(x)%400==0:
            print(f"{x} is a leap year.")
        else:
            print(f"{x} is not a leap year.")
    elif int(x)%4==0:
        print(f"{x} is a leap year")
    
    else:
        print(f"{x} is not leap year")

LeapCheck(yr)