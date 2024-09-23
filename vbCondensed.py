def begin_sathybind():
    print("Hello! Let me help you pick a strain today.")
    print("What type do you prefer: indica, sativa, or hybrid?")
    strainType = input("> ").lower()
    if strainType: "sativa"
        sat_strains(strainType)
    elif strainType: "indica"
        ind_strains(strainType)
    elif strainType: "hyrbid"
        hyb_strains(strainType)
    else:
        print("Sorry, please select indica, sativa, or hybrid.")

def sat_strains(strainType):
    print(f"Excellent! Let's talk about some {strainType} strains.")
    print("Do you prefer to feel creative, energized, or uplifted?")
    feeling = input("> ").lower()
    if feeling in ["creative", "energized", "uplifted"]:
        sat_effects(feeling)
    else:
        print("Sorry, please enter creative, energized, or uplifted.")

def sat_effects(flavor):
    print("Thank you! What sort of flavor/aroma profiles are most appealing to you?")
    print("Would you prefer a sweet, skunky, or gassy strain?")
    flavor = input("> ").lower()
    if flavor in ["sweet", "skunky", "gassy"]:
        sat_recommendations(feeling, flavor)
    else:
        print("Sorry, please enter sweet, skunky, or gassy.")

def sat_recommendations(feeling, flavor):
    print("Thank you! I have a few recommendations for you!")
    if feeling == "creative":
        if flavor == "sweet":
            print("Hawaiian Butterscotch, Tangie, Berry White")
        elif flavor == "skunky":
            print("Super Silver Haze, Colombian Gold, AK-47")
        elif flavor == "gassy":
            print("Chem 91, Jack Herer, Stardawg")
    elif feeling == "energized":
        if flavor == "sweet":
            print("Super Lemon Haze, Lemon Cake, Pineapple OG")
        elif flavor == "skunky":
            print("Outer Space, Kauau'i Electric, Trainwreck")
        elif flavor == "gassy":
            print("Sour Jack, Ghost Train Haze, Green Crack")
    elif feeling == "uplifted":
        if flavor == "sweet":
            print("L'Orange, Pineapple Express, Maui Wowie")
        elif flavor == "skunky":
            print("Amnesia Haze, Capital Haze, Jacky White")
        elif flavor == "gassy":
            print("Sour Diesel, Chemdawg, Thor's Hammer")

def hyb_strains(strainType):
    print(f"Excellent! Let's talk about some {strainType} strains.")
    print("Do you prefer to feel chilll or social?")
    feeling = input("> ").lower()
    if feeling in ["creative", "energized", "uplifted"]:
        hyb_effects(feeling)
    else:
        print("Sorry, please enter creative, energized, or uplifted.")

def hyb_effects(flavor):
    print("Thank you! What sort of flavor/aroma profiles are most appealing to you?")
    print("Would you prefer a sweet, skunky, or gassy strain?")
    flavor = input("> ").lower()
    if flavor in ["sweet", "skunky", "gassy"]:
        hyb_recommendations(feeling, flavor)
    else:
        print("Sorry, please enter sweet, skunky, or gassy.")

def hyb_recommendations(feeling, flavor):
    print("Thank you! I have a few recommendations for you!")
    if feeling == "chill":
        if flavor == "sweet":
            print("Wedding Cake, Animal Cookies, Alien Rock Candy")
        elif flavor == "skunky":
            print("Bubba Fett, GG4, Casino Kush")
        elif flavor == "gassy":
            print("Gassy Taffy, V Kush, Wild Cherry")
    elif feeling == "social":
        if flavor == "sweet":
            print("Runtz, Rainbow Beltz, Banana Dream")
        elif flavor == "skunky":
            print("Appalachia, Deadhead OG, Love Triangle")
        elif flavor == "gassy":
            print("Copper Chem, Sour Diesel, Jet Fuel")

def ind_strains(strainType):
    print(f"Excellent! Let's talk about some {strainType} strains.")
    print("Do you prefer to feel relaxed, hungry, or do you want to manage pain?")
    feeling = input("> ").lower()
    if feeling in ["relaxed", "hungry", "manage pain"]:
        sat_effects(feeling)
    else:
        print("Sorry, please enter relaxed, hungry, or manage pain.")

def ind_effects(flavor):
    print("Thank you! What sort of flavor/aroma profiles are most appealing to you?")
    print("Would you prefer a sweet, skunky, or gassy strain?")
    flavor = input("> ").lower()
    if flavor in ["sweet", "skunky", "gassy"]:
        ind_recommendations(feeling, flavor)
    else:
        print("Sorry, please enter sweet, skunky, or gassy.")

def ind_recommendations(feeling, flavor):
    print("Thank you! I have a few recommendations for you!")
    if feeling == "relaxed":
        if flavor == "sweet":
            print("Granddaddy Purp, Grape Ape, Blueberry")
        elif flavor == "skunky":
            print("Death Star, Triangle Kush, God's Breath")
        elif flavor == "gassy":
            print("Purple Octane, Snoopp Dogg OG, Wifi OG")
    elif feeling == "hungry":
        if flavor == "sweet":
            print("Mango Kush, Grape Ape, Blackberry Kush")
        elif flavor == "skunky":
            print("Pot O'Gold, LA Confidential, Afghan Skunk")
        elif flavor == "gassy":
            print("Titty Sprinkles, Tyson, Chronic Thunder")
    elif feeling == "manage pain":
        if flavor == "sweet":
            print("Blueberry Kush, Kryptonite, Shishkaberry")
        elif flavor == "skunky":
            print("Head Cheese, Hindu Skunk, Star Master Kush")
        elif flavor == "gassy":
            print("Superbud, Anonymous OG, Ape Diesel")




begin_sathybind()

if __name__ == "__main__":
    while True:
        begin_sathybind()

        restart = input("Do you want to start again? (yes/no): ").lower()
        if restart != "yes":
            break  # Exit the loop

    input("Press Enter to exit...")  # Wait for user input before closing
