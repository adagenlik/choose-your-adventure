name=input("Type Your Name:")
print("Welcome", name, "to this adventure")

answer = input("you are in a dirt way. Where will you go: (left/right) ")



#left
if answer == "left":
    answer = input("You come to a river. What will you do:  (swim/walk) ")

    if answer == "swim":
        print("hungry alligator ate you, YOU LOSE")

    elif answer == "walk":
        print("You walked too much and ran out of water you died, YOU LOSE")

    else:
        print('Not valid option you lose')



#right
elif answer == "right":
    answer=input("You come to bridge cross or head back (cross/back)")

    if answer == "back":
        print("while going you saw a bear and it ate you YOU LOSE")

    elif answer == "cross":
        answer= input("you cross and saw an foreign will you speak to him  (yes/no)")

        if answer == "yes":
            print("you talked to him and he gave you gold YOU WİN")

        elif answer == "no":
            print("He got angry and punched to your face YOU LOSE")


        else:
            print('Not valid option you lose')

    else:
        print('Not valid option you lose')

else:
    print('Not valid option you lose')
