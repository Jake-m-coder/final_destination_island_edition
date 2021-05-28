from turtle_game import etch_e_sketch
from pandas import DataFrame
from logo import logo


def survival_challenge():
    """The purpose of this function is to give you a short interactive survival situation."""

    def end_game():
        """"This function gives a print statement informing the user the game has ended."""
        print("You've ended this survival game.")

    def relaxation_adventure():
        relaxation = """
        You've decided to stay in and have a cozy day. You decide to have a nostalgic experience to take your mind
        off the dream. You've decided to build an etch-e-sketch program, and now get to enjoy the fruits of your
        labour.\n"""

        controls = {
            "Controls": " and Action Performed",
            "Up Arrow Key": "used to move forward",
            "Down Arrow Key": "used to move backwards",
            "Left Arrow Key": "used to move counter-clockwise",
            "Right Arrow Key": "used to move clockwise",
            "C": "used to reset the screen to it's initial state"}
        print(relaxation)
        for x, y in controls.items():
            print(x, y)
        etch_e_sketch()
        end_game()

    def solo():
        single_player = """
        You've jumped ship too early in the panic. The waves are too rough to swim and you drift further away from the
        life boat. You've fought as hard as you could but you've ran out of stamina and drowned."""
        print(single_player)

    def short_term():
        """This function provides the results of the final choice in the game when opting for a short term line of
        thinking."""

        current_scenario = """
        You've worked together to row the boat as close as possible to the island. After abandoning the boat, you 
        inspect the bag to see what items the team has left over to survive on. You ask your companion to explain the
        reasoning behind the selected items.\n"""

        results = """
        Unfortunately there is a finite number of matches, so you run out opportunities to make a fire. The beans
        take between 50-60 days to grow after being planted. Humans can only go 21-40 days without food. You and your
        companions die from starvation."""

        items_in_bag = {"First Aid Kit": "used for wounds",
                        "Flares": "to signal for rescue",
                        "Water Container": "to store fresh water",
                        "Torch": "to help see at night and explore the island",
                        "Matches": "to start a fire",
                        "Bean": "to plant and grow more",
                        "Sauce Pan": "to cook the beans",
                        "Pen-Knife": "to open the beans",
                        "Tent": "to have shelter"}

        print(current_scenario)
        for x, y in items_in_bag.items():
            print(x, y)
        print(results)

    def long_term():
        """This function provides the results of the final choice in the game when opting for a long term line of
               thinking."""

        current_scenario = """
                You've worked together to row the boat as close as possible to the island. After abandoning the boat, 
                your companions inspect the bag to see what items the team has left over to survive on. They ask you to 
                explain your choice of selection for the items.\n"""

        results = """
        You and your companions have managed to survive for a lengthy period of time on the island, and have been 
        saved by another ship. Good job on maintaining teamwork to make it to the end."""

        items_in_bag = {"First Aid Kit": "used for wounds",
                        "Flares": "to signal for rescue",
                        "Water Container": "to store fresh water",
                        "Mirror": "can be used to signal for help or make fire with sunlight",
                        "Rope": "can be used to make a net to catch fish/crustaceans, or climb trees to gather food",
                        "Hooks": "can be used with rope to make a fishing line for a continuous supply of food",
                        "Sauce Pan": "to boil bird eggs or catch water from the rain to drink",
                        "Pen-Knife": "to used to make spears for hunting or preparing fish",
                        "Tent": "to have shelter"}

        print(current_scenario)
        for x, y in items_in_bag.items():
            print(x, y)
        print(results)

    mission_statement = "Pick the best choice to survive."

    # Sinking Ship
    background_story = """
    You're on a cruise ship enjoying the holiday of your life. An announcement goes out that a
    flash storm is approaching, and warns passengers to return to their rooms. As the storm worsens, powerful winds are 
    rocking the ship, and waves are adding water to the deck forcing it lower into the water. This results in the ship
    flipping over completely. Water is now rising within the ship, and damaged electrical wiring is exposed making
    the environment deadly. To your knowledge, you're the only survivor.\n"""

    scenario_one = "Do you:\n A. Go down with the ship\n B. Try to escape"

    # Inspiration of "Final Destination"
    premonition = """ 
    You've awoken in your room, looking frantically around realising it was all a dream. A reminder is on your phone 
    stating you have to be at the docks by 12:00p.m. to go on your holiday to the Caribbean. The dream felt so surreal 
    but now you're scared to go on the cruise ship.\n"""

    scenario_two = "Do you:\n A. Go on the holiday anyway \n B. Stay home just to be on the safer side "

    # Options of resources
    background_story_two = """
    You've managed to find three other survivors, they've secured the only functional 
    emergency boat. You all band together to gather a quick provision of supplies before escaping on the emergency
    boat.\n"""

    items_gathered = ["First Aid Kit", "Flares", "Rope", "Hooks", "Water Container", "Matches", "Torch", "Sauce Pan",
                      "Pen-Knife", "Beans", "Tent", "Sleeping Bag", "Tin Cup", "Magazine", "Smart Phone",
                      "Pair of Keys", "Sun Tan Lotion", "Sunglasses", "Small Mirror", "Bottle of Rum", "Toothbrush",
                      "Backpack"]

    item = DataFrame(items_gathered, columns=["Items"])

    # Emergency Boat goes down
    background_story_three = """
    Tensions are running high in the group after the close experience with death. You point out the emergency boat has 
    been damaged and is slowly filling with water. It's only a matter of time, before the boat will sink. The storm is
    effecting the tides making them rougher. You can see a small island in the distance and you've noticed the backpack 
    can hold at most nine items.\n"""

    # Teamwork vs Independence
    scenario_three = "Do you:\n A. Declare every man for themselves and go solo \n B. Encourage teamwork for survival"

    # Trustful or Untrustworthy
    final_scenario = "Do you:\n A. Trust another survivor to back the bag \n B. Pack the bag yourself"

    death = """
    You've wasted too much time deciding on an action. The waves flip over the boat, the tides are too strong to swim 
    out of causing everyone to drown.\n"""

    print(logo)
    print(mission_statement)
    print(background_story)
    print(scenario_one)

    choice_one = input("\nInput 'A' for option one, 'B' for option two, or 'Q' to quit: ").upper()
    if choice_one == "A":
        print(f"You've accepted that a chance of survival is low, and await a peaceful but wet death.")
    elif choice_one == "B":
        print(background_story_two)
        print(item)
        print(background_story_three)
        print(scenario_three)
        choice_three = input("\nInput 'A' for option one, 'B' for option two, or 'Q' to quit: ").upper()
        if choice_three == "A":
            solo()
        elif choice_three == "B":
            print("\n")
            print(final_scenario)
            final_choice = input("\nInput 'A' for option one, 'B' for option two, or 'Q' to quit: ").upper()
            if final_choice == "A":
                short_term()
            elif final_choice == "B":
                long_term()
            elif final_choice == "Q":
                end_game()
            else:
                print(death)
        elif choice_three == "Q":
            end_game()
        else:
            print(death)
    elif choice_one == "Q":
        end_game()
    else:
        print(premonition)
        print(scenario_two)
        choice_two = input("\n Input 'A' for option one, 'B' for option two, or 'Q' to quit: ").upper()
        if choice_two == "A":
            survival_challenge()
        elif choice_two == "B":
            relaxation_adventure()
        else:
            print("\n")
            end_game()


game_on = True
print("Would you like to play a game?")
consent = input("Type 'Y' for yes or 'N' for no: ").upper()
if consent == "Y":
    while game_on:
        survival_challenge()
        print("Would you like to play again?")
        replay = input("Type 'Y' for yes or 'N' for no: ").upper()
        if replay == "N":
            game_on = False
print("Have a good day!")
