print("The Love Calculator is calculating your score...")
name1 = input("What's your name? ") # What is your name?
name2 = input("What's your lover's name? ") # What is their name?

occurrence1, occurrence2 = 0, 0

n1 = name1.lower()
n2 = name2.lower()

joint_name = n1 + n2

for i in ["t", "r", "u", "e"]:
    occurrence1 += joint_name.count(i)
for i in ["l", "o", "v", "e"]:
    occurrence2 += joint_name.count(i)
love_score = int(occurrence1 + occurrence2)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")