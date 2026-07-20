def adventure ():
    
    print ("You are currently standing at a fork in your path")
    choice = input ("Do you choose to go left or go right: ")

    if choice == "left":
        print ("You encounter a friendly dragon \n" )
        second = input ("Do you talk to the dragon or choose to walk away? ")
        if second == "talk":
            print ("The dragon has given you a map")
        elif second == "walk away":
            print ("You start making your way back home feeling dissapointed")
        else:
            print ("The dragon flies away because you hesistated too long")

    elif choice == "right":
        print ("You encounter a water Kelpie")
        
    else:
        print ("You get lost in the woods")
        
adventure ()
