from random import randint

#this progrm demonstrates a guessing 
# game

#1.get user input
#user_name = input ("What's your name?")
#print("Hello there " + user_name +"!
#2.using a while loop
random_number = randint(10,50)
counter=0
while counter<5:
    user_number=eval(input("Enter a number: "))
    counter +=1

    if user_number<random_number:
        print("your guess is too low")
    elif user_number>random_number:
        print("your guess is too high")
    elif user_number==random_number:
        break


if user_number ==random_number:
    print("You win!" )
else:
    print("Game over! The correct number is ")
    print(random_number)    
print("The correct number was " +random_number)

#3.Get user number
#2.generate a random number

#3.check if user input is equal to generated number
#4. while using a while loop check if user input is equel to generated number

