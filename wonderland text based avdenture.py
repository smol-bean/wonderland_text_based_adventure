from time import sleep


def clear_output():
    for i in range(100):
        print("\n")


while True:
    print("start game")
    print("----------------------------------")
    print("1: yes")
    print("2: no")
    answer = input()
    if answer == "1":
        clear_output()
        print("your name is (insert name) and you are walking the streets of london at midnight and you come across a strange man.")
        print("he looks oddly like a rabbit but you cant figure out why.")
        print("you think about following him.")
        print("do you...")
        print("---------------------------------------------------------------------------------------------------------------------")
        print("1: follow him")
        print("2: go home its late")
        print("3: exit")
        answer = input()
    elif answer == "2":
        clear_output()
        print("then why boot up the game?")
        sleep(3)
        break
    if answer == "2":
        clear_output()
        print("you go home and go to bed")
        sleep(4)
        clear_output()
        print("game end")
        sleep(5)
        continue
    elif answer == "1":
        clear_output()
        print("you follow the strange man and as you follow him he turns a corner.")
        print("you turn the corner as well and you are suddenly falling.")
        print("soon you end up on the ground unharmed from the fall")
        print("you sit up to see you are in what seems to be a garden.")
        print("do you...")
        print("-----------------------------------------------------------------------------------------------------------------")
        print("1: sit there and wonder how you got there")
        print("2: get up and look around")
        print("3: exit")
        answer = input()
    if answer == "1":
        print(" you sit down and ponder how you got here.")
        print(" you then realize that sitting there wont help and get up.")
        print("you take a look around and see that there is a long table in the middle.")
        print("the table has different colors on it.")
        print("one half is red and the other is black.")
        print("")
    if answer == "3":
        break
clear_output()
print("do come back soon")
sleep(3)
clear_output()
sleep(3)
print("game end")
sleep(5)
