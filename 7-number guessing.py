import random
number = random.randint(1,100)
# hint
print(f"nubmer is {number}")

 
while True: 
    user_input = int(input("Enter The Number: "))
    try:
        if user_input >= 100 or user_input < 0:
          raise ValueError("Number must be in range [1, 100].")
        
        else:
            if user_input == number :
                print("correct")
                break
            elif user_input > number:
                print("you are higher")
            elif user_input < number :
                print("you are lower")
    except ValueError as ve:
        print(ve)
    except:
        print("error!")
