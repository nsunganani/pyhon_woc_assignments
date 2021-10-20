#GUESSING GAME ASSIGNMENT

#First initialise and declare the mystery number
answer = 7

#Initial prompt for user to enter their guess
guess=int(input("Guess the number between within 1-9 range: "))

#Create a loop that prompts user to keep guessing until the guess is correct
while guess > 0:
    #Proceed to check the guess if guess is within range
    if guess in range (1,10):
    #If guess is not correct, prompt user to try again
        if answer != guess:
            guess=int(input("Wrong. Guess again: "))
    #If guess is correct, inform user and end game                
        else:
             print("Well guessed!")
             break
    #Prompt user to enter their guess again within the correct range
    else:
        print("Number out of range")
        guess=int(input("Enter a guess number between within the 1-9 range: "))

