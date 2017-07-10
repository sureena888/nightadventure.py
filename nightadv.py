import time
variable = "no"

while variable == "no":
    print("You and your five friends are in the woods.")
    time.sleep(2)
    print("The time is 11 pm. Since you are so immersed inside of the tranquility of the night hike, you are unaware of how late it has gotten and where exactly your group is...")
    time.sleep(4)
    print("CRAAASHHH!!!!!!")
    time.sleep(1)
    print("What was that??! You wave your arms around, trying desperately to find one of your friends in the darkness, but you are alone.")
    time.sleep(4)

    scare = input("Are you scared?")
    if scare == "yes":
        print("You hear a bear grumble.")
        time.sleep(1)
        flashlight = input("Do you want to turn on your flashlight?")
        if flashlight == "yes":
            print("You see the bear's face and faint from shock.")
            print("The End")
        elif flashlight == "no":
            print("Run as fast as you can!")
            time.sleep(1)
            print("You escape and live the rest of your life in the woods and become Tarzan.")
            print("The End")
        else:
            print("invalid input")
    elif scare == "no":
        print("You hear a voice.")
        time.sleep(3)
        voice = input("Do you follow the voice?")
        if voice == "yes":
            print("You trip and fall into the arms of your true love.")
            print("The End")
        elif voice == "no":
            print("You keep walking, and find yourself and caught in the light of a police car.")
            time.sleep(1)
            print("The police arrest you for the murder of your six friends.")
            print("The End")
        else:
            print("invalid input")
    else:
        print("invalid input")
    variable = input("Would you like to end the program (yes/no) ")
