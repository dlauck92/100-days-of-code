# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")

# greet_with(location="nowhere", name="Drew Lauck")  

print("Welcome to Treasure Isaland.")
print("Your mission is to find the treasure.")
choice1 = input("Go left or right?\n").lower()
if choice1 == "left":
    choice2 = input("Wait or Swim?").lower()
    if choice2 == "swim":
        choice3 = input("Choose the Red, Blue or Yellow door to walk through").lower()
        if choice3 == "yellow":
            print("you found the treasure gj")
        elif choice3 == "red":
            print("Game Over")
        else:
            print("Game Over")
    else:
        print("Game Over")    
else:
    print("Game Over")