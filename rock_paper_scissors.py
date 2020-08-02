import random
random.seed()

player = {}
player["name"] = input("Enter your name: ")
print(f"Hello, {player['name']}")

f = open("rating.txt", "r")
for line in f:
    line = line.rstrip()
    # print(line)
    p_name, score = line.split(" ")
    if p_name == player["name"]:
        player["score"] = score
        break
    else:
        player["score"] = 0

options = input().split(",")
# print(options)
if options == ['']:
    options = ["rock", "paper", "scissors"]
print("Okay, let's start")

def gameplay(user, comp):
    if comp == user:
        print(f"There is a draw ({comp})")
        player["score"] += 50
    elif comp in win:
        print(f"Sorry, but computer chose {comp}") 
    else:
        print(f"Well done. Computer chose {comp} and failed")
        player["score"] += 100

while True:
    user = input()
    if user in ["!exit", "!rating"] + options:
        if user == "!exit":
            print("Bye!")
            break
        elif user == "!rating":
            print(f"Your rating: {player['score']}")    
        else:
            comp = random.choice(options)
            win = []
            for i in range(1, (len(options) - 1) // 2 + 1):
                win.append(options[(options.index(user) + i) % len(options)])
            # print(win)
            gameplay(user, comp)
    else:
        print("Invalid input")

f.close()
