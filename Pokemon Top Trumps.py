import requests
import random


# define function to get  Pokemon's data from the API
def get_pokemon(pokemon_id):


    url = "https://pokeapi.co/api/v2/pokemon/{}".format(pokemon_id)

    response = requests.get(url)

    pokemon = response.json()
    # Extract and return the relevant details in a new dictionary
    return {
        "name": pokemon["name"],
        "id": pokemon["id"],
        "height": pokemon["height"],
        "weight": pokemon["weight"]
    }


# Function to play the game
def play_game():

    print("Welcome to Pokemon Top Trumps!")

    # Generate random Pokemon IDs for the player and the opponent
    player_pokemon_one = random.randint(1,151)
    player_pokemon_two = random.randint(1,151)
    opponent_pokemon = random.randint(1,151)


    # Get Pokemon data for the player and opponent
    player_pokemon_first = get_pokemon(player_pokemon_one)
    player_pokemon_second = get_pokemon(player_pokemon_two)
    opponent_pokemon = get_pokemon(opponent_pokemon)


    # Display the player's first Pokemon details
    print("Your first Pokemon is: {}".format(player_pokemon_first["name"]))
    print("Stats:")
    print("ID: {}".format(player_pokemon_first["id"]))
    print("Height: {}".format(player_pokemon_first["height"]))
    print("Weight: {}".format(player_pokemon_first["weight"]))

    #Display the player's second pokemon details
    print("\nYour second Pokemon is: {}".format(player_pokemon_second["name"]))
    print("Stats:")
    print("ID: {}".format(player_pokemon_second["id"]))
    print("Height: {}".format(player_pokemon_second["height"]))
    print("Weight: {}".format(player_pokemon_second["weight"]))


    #Ask the player which pokemon they want to use

    first = player_pokemon_first
    second = player_pokemon_second
    print("\nDo you want to play with your first or second pokemon?")
    pokemon_choice = input ("Enter your choice:").lower()
    if pokemon_choice == 'first':
        player_pokemon = player_pokemon_first
        print("You picked {}! Great choice".format(player_pokemon_first["name"]))
    else:
        player_pokemon = player_pokemon_second
        print("You chose {}! Great choice".format(player_pokemon_second["name"]))


  # Ask the player which stat they want to use
    print("\nWhich stat do you want to use? (id/height/weight)")
    chosen_stat = input("Enter your choice: ").lower()



    # Display the opponent's Pokemon details
    print("\nYour opponent's Pokemon is: {}".format(opponent_pokemon["name"]))
    print("Opponent's {}: {}".format(chosen_stat, opponent_pokemon[chosen_stat]))

    # Compare the chosen stat between the player's and opponent's Pokemon

    player_stat = player_pokemon[chosen_stat]
    opponent_stat = opponent_pokemon [chosen_stat]

    # Determine the winner based on the chosen stat
    if player_stat > opponent_stat:
        print("\nCongratulations! You win! Your {} ({}) is higher than the opponent's {} ({}).".format(
            chosen_stat, player_stat, chosen_stat, opponent_stat))
    elif player_stat < opponent_stat:
        print("\nYou lose! The opponent's {} ({}) is higher than your {} ({}).".format(
            chosen_stat, opponent_stat, chosen_stat, player_stat))
    else:
        print("\nIt's a tie! Both your {} and the opponent's {} are equal ({}).".format(
            chosen_stat, chosen_stat, player_stat))


play_game()

