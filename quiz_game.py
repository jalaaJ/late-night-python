print("Welcome to the quiz!")

score = 0

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

answer = input("What does the CPU stand for? ")

if answer == "Central Processing Unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("Your score is: ", score)
