import readline
readline.parse_and_bind("tab: complete")

# This is far from perfect, first version of my first Python program
# I can't figure out how to get it to loop back to ask the previous question again
# Also want to add more pathways

'''
def intro():
  print("Hello, let me help you choose a cannabis strain!")
  print("To start, do you prefer to select by type (indica, sativa, hybrid), strain, or terpenes?")
  startConsult = input("> ").lower()
  if startConsult == "type":
     begin_sathybind()
  if startConsult == "strain":
     begin_strain()
  if startConsult == "terpenes":
     begin_terpenes()

def begin_strains():
    user_input = input("Enter text: ")
    keyword_responses = {
        "Kush": "Kush strains are primarily indica plants from the Hindu Kush region.",
        "Diesel": "Diesel strains come from parents like Sour Diesel and Chemdawg and are popular sativa strains.",
        "Haze": "Haze strains are sativas famous for their head buzz.",
        "Cookies": "Cookies strains were invented by Jay and Berner, and were the first hybrid strain to gain popularity.",
        "Gold": "Colombia and Acapulco Gold are famous and hard-to-find sativa landrace strains.",
        "Thai": "Thai stick strains are a rewnown indica family from Thailand.",
        "Afghan": "Afghan strains are potent indica strains from the Middle East.",
        "Blueberry": "Blueberry strains are indica-dominant and often heavy in the terpene Myrcene.",
        "Mango": "Mango strains are indica-dominant and often heavy in the terpene Myrcene.",
        "Blue Dream": "Blue Dream is a highly balanced sativa, often high in Myrcene and backed up by Pinene.",
        "Cheese": "A rare release from the UK, Cheese strains are heavy, balanced hybrid strains that often feel like indicas.",

        # Add more keywords and responses as needed
        }
    found = keyword_search(user_input, keyword_responses)
    if found:
        for keyword, response in found.items():
            print("Keyword found:", keyword)
            print("Response:", response)
    else:
        print("No keywords found.")
'''


def begin_sathybind():
    print("Hello! Let me help you pick a strain today.")
    print("What type do you prefer: indica, sativa, hybrid?")
  # figure out how to add an "explain more" option/loop
    strainType = input("> ").lower()
    if strainType == "sativa":
       sativa_strains()
    elif strainType == "indica":
       indica_strains() 
    elif strainType == "hybrid":
        hybrid_strains()
    else:
      print("Sorry, please select indica, sativa, or hybrid")

# sativa
def sativa_strains():
    print("Excellent! Let's talk about some sativa strains.")
    print("Do you prefer to feel creative, energized, or uplifted?")
    sativaFeeling = input("> ").lower()
    if sativaFeeling == "creative":
        creative_strains()
    elif sativaFeeling == "energized":
      energizing_strains()
    elif sativaFeeling == "uplifted":
      uplifting_strains()
    else:
      print("Sorry, please enter creative, energized, or uplifted.")

# effects - sativa
def creative_strains():
    print("Thank you! What sort of flavor/aroma profiles are most appealing to you?")
    print("Would you prefer a sweet, skunky, or gassy strain?")
    creativeFlavor = input("> ").lower()
    if creativeFlavor == "sweet":
        sweet_creative()
    elif creativeFlavor == "skunky":
        skunky_creative()
    elif creativeFlavor == "gassy":
        gassy_creative()
    else:
        print("Sorry, please enter sweet, skunky, or gassy.")

def energizing_strains():
    print("Thank you! What sort of flavor/aroma profiles are most appealing to you?")
    print("Would you prefer a sweet, skunky, or gassy strain?")
    energyFlavor = input("> ").lower()
    if energyFlavor == "sweet":
        sweet_energy()
    elif energyFlavor == "skunky":
        skunky_energy()
    elif energyFlavor == "gassy":
        gassy_energy()
    else:
        print("Sorry, please enter sweet, skunky, or gassy.")

def uplifting_strains():
    print("Thank you! What sort of flavor/aroma profiles are most appealing to you?")
    print("Would you prefer a sweet, skunky, or gassy strain?")
    upliftFlavor = input("> ").lower()
    if upliftFlavor == "sweet":
        sweet_uplift()
    elif upliftFlavor == "skunky":
        skunky_uplift()
    elif upliftFlavor == "gassy":
        gassy_uplift()
    else:
        print("Sorry, please enter sweet, skunky, or gassy.")

# sativa solutions

def sweet_creative():
    print("Thank you! I have a few recommendations for you!")
    print("Hawaiian Butterscotch")
    print("Tangie")
    print("Berry White")

def skunky_creative():
    print("Thank you! I have a few recommendations for you!")
    print("Super Silver Haze")
    print("Colombian Gold")
    print("AK-47")

def gassy_creative():
    print("Thank you! I have a few recommendations for you!")
    print("Chem 91")
    print("Jack Herer")
    print("Stardawg")

def sweet_uplift():
    print("Thank you! I have a few recommendations for you!")
    print("L'Orange")
    print("Pineapple Express")
    print("Maui Wowie")

def skunky_uplift():
    print("Thank you! I have a few recommendations for you!")
    print("Amnesia Haze")
    print("Capital Haze")
    print("Jacky White")

def gassy_uplift():
    print("Thank you! I have a few recommendations for you!")
    print("Sour Diesel")
    print("Chemdawg")
    print("Thor's Hammer")

def sweet_energy():
    print("Thank you! I have a few recommendations for you!")
    print("Super Lemon Haze")
    print("Lemon Cake")
    print("Pineapple OG")

def skunky_energy():
    print("Thank you! I have a few recommendations for you!")
    print("Outer Space")
    print("Kauau'i Electric")
    print("Trainwreck")

def gassy_energy():
    print("Thank you! I have a few recommendations for you!")
    print("Sour Jack")
    print("Ghost Train Haze")
    print("Green Crack")

# hybrids start here
def hybrid_strains():
    print("Excellent! Let's talk about some hybrid strains.")
    print("Do you prefer to feel chill or social?")
    hybridFeeling = input("> ").lower()
    if hybridFeeling == "chill":
        chill_strains()
    elif hybridFeeling == "social":
        social_strains()
    else:
      print("Sorry, please enter either chill or social.")

# effect - hybrids
def chill_strains():
    print("Thank you! What sort of flavor/aroma profiles are most appealing to you?")
    print("Would you prefer a sweet, skunky, or gassy strain?")
    chillFlavor = input("> ").lower()
    if chillFlavor == "sweet":
        sweet_chill()
    elif chillFlavor == "skunky":
        skunky_chill()
    elif chillFlavor == "gassy":
        gassy_chill()
    else:
        print("Sorry, please enter sweet, skunky, or gassy.")

def social_strains():
    print("Thank you! What sort of flavor/aroma profiles are most appealing to you?")
    print("Would you prefer a sweet, skunky, or gassy strain?")
    socialFlavor = input("> ").lower()
    if socialFlavor == "sweet":
        sweet_social()
    elif socialFlavor == "skunky":
        skunky_social()
    elif socialFlavor == "gassy":
        gassy_social()
    else:
        print("Sorry, please enter sweet, skunky, or gassy.")

# solutions - hybrids

def sweet_social():
    print("Thank you! I have a few recommendations for you!")
    print("Runtz")
    print("Rainbow Beltz")
    print("Banana Dream")

def skunky_social():
    print("Thank you! I have a few recommendations for you!")
    print("Appalachia")
    print("Deadhead OG")
    print("Love Triangle")

def gassy_social():
    print("Thank you! I have a few recommendations for you!")
    print("Copper Chem")
    print("Sour Diesel")
    print("Jet Fuel")

def sweet_chill():
    print("Thank you! I have a few recommendations for you!")
    print("Wedding Cake")
    print("Animal Cookies")
    print("Alien Rock Candy")

def skunky_chill():
    print("Thank you! I have a few recommendations for you!")
    print("Bubba Fett")
    print("GG #4")
    print("Casino Kush")

def gassy_chill():
    print("Thank you! I have a few recommendations for you!")
    print("Copper Chem")
    print("Sour Diesel")
    print("Jet Fuel")

# indicas start here
def indica_strains():
    print("Excellent! Let's talk about some indica strains.")
    print("Do you prefer to feel relaxed, hungry, or do you want to manage pain?")
    indicaFeeling = input("> ").lower()
    if indicaFeeling == "relaxed":
        relax_strains()
    elif indicaFeeling == "hungry":
        hungry_strains()
    elif indicaFeeling == "manage pain":
        pain_strains()
    else:
        print("Sorry, please enter relaxed, hungry, or manage pain.")

# effects - indica
def relax_strains():
    print("Thank you! What sort of flavor/aroma profiles are most appealing to you?")
    print("Would you prefer a sweet, skunky, or gassy strain?")
    relaxFlavor = input("> ").lower()
    if relaxFlavor == "sweet":
        sweet_relax()
    elif relaxFlavor == "skunky":
        skunky_relax()
    elif relaxFlavor == "gassy":
        gassy_relax()
    else:
        print("Sorry, please enter sweet, skunky, or gassy.")

def hungry_strains():
    print("Thank you! What sort of flavor/aroma profiles are most appealing to you?")
    print("Would you prefer a sweet, skunky, or gassy strain?")
    hungryFlavor = input("> ").lower()
    if hungryFlavor == "sweet":
        sweet_hungry()
    elif hungryFlavor == "skunky":
        skunky_hungry()
    elif hungryFlavor == "gassy":
        gassy_hungry()
    else:
        print("Sorry, please enter sweet, skunky, or gassy.")

def pain_strains():
    print("Thank you! What sort of flavor/aroma profiles are most appealing to you?")
    print("Would you prefer a sweet, skunky, or gassy strain?")
    painFlavor = input("> ").lower()
    if painFlavor == "sweet":
        sweet_pain()
    elif painFlavor == "skunky":
        skunky_pain()
    elif painFlavor == "gassy":
        gassy_pain()
    else:
        print("Sorry, please enter sweet, skunky, or gassy.")

# solutions - indica
def sweet_pain():
    print("Thank you! I have a few recommendations for you!")
    print("Blueberry Kush")
    print("Shishkaberry")
    print("Kryptonite")

def skunky_pain():
    print("Thank you! I have a few recommendations for you!")
    print("Head Cheese")
    print("Hindu Skunk")
    print("Star Master Kush")

def gassy_pain():
    print("Thank you! I have a few recommendations for you!")
    print("Super Bud")
    print("Anonymous OG")
    print("Ape Diesel")

def sweet_hungry():
    print("Thank you! I have a few recommendations for you!")
    print("Mango Kush")
    print("Grape Ape")
    print("Blackberry Kush")

def skunky_hungry():
    print("Thank you! I have a few recommendations for you!")
    print("Pot Of Gold")
    print("LA Confidential")
    print("Afghan Skunk")

def gassy_hungry():
    print("Thank you! I have a few recommendations for you!")
    print("Titty Sprinkles")
    print("Tyson")
    print("Chronic Thunder")

def sweet_relax():
    print("Thank you! I have a few recommendations for you!")
    print("Granddaddy Purp")
    print("Blueberry")
    print("Grape Ape")

def skunky_relax():
    print("Thank you! I have a few recommendations for you!")
    print("Death Star")
    print("God's Breath")
    print("Triangle Kush")

def gassy_relax():
    print("Thank you! I have a few recommendations for you!")
    print("Purple Octane")
    print("Snoop Dogg OG")
    print("Wifi 43")

raw_input('Press ENTER to exit')

