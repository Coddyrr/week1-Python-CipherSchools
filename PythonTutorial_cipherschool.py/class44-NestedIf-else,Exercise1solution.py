# EXERCISE SOLUTION
winnning_number = 27
user_input = input("guess a number b/w 1 and 100 : ")
user_input = int(user_input)
if user_input == winnning_number:
    print("YOU WIN !!!")
else:   # nested if-else
    if user_input<winnning_number:
        print("too low")
    else:
        print("too high")