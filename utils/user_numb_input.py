print("\n\n")

def number_input():
    while True:
        user_numb_input = input("Write number divisible by two: ")
        try:
            user_numb_input = int(user_numb_input)
        except:
            print("Write only integer number!\n")
            continue
        if user_numb_input % 2 == 0:
            return "Your number: " + str(user_numb_input) + " is divisible by two."
        else:
            print("Try another number...\n")

print("the end")
