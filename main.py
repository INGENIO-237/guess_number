from random import randint

print("*****************************************************")
print("**                                                 **")
print("**                GUESS NUMBER                     **")
print("**                                                 **")
print("*****************************************************")

cntinue = True

while(cntinue):
    to_guess = randint(1,100)
    user_number: int = None
    try:
        while(user_number != to_guess):
            user_number = int(input("Guess the number chosen between 1-100 chosen by the computer\n"))
            if(user_number > to_guess):
                print("Lesser\n\n")
            elif(user_number < to_guess):
                print("Greater\n\n")
            else:
                print("You got it !")

        response: int = None
        while(response!=0 and response!=1):
            response = int(input("Do you wish to continue the game ? enter 0 for 'No' and 1 for 'Yes'\n"))

        if response == 0:
            cntinue = False
        
    except TypeError:
        print("You must enter an integer ! Retry !!")
        break
