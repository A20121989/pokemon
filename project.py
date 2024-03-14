import random

def create_and_shuffle_cards():
    pokemon_cards = [
        ("Pikachu", "50pts & 35hp"), ("Charmander", "65pts & 39hp"), ("Bulbasaur", "45pts & 45hp"), ("Squirtle", "60pts & 44hp"),
        ("Jigglypuff", "55pts & 115hp"), ("Meowth", "40pts & 40hp"), ("Psyduck", "52pts & 50hp"), ("Abra", "48pts & 25hp"),
        ("Gastly", "47pts & 30hp"), ("Magikarp", "30pts & 20hp"), ("Eevee", "58pts & 55hp"), ("Snorlax", "80pts & 160hp"),
        ("Mewtwo", "90pts & 106hp"), ("Mew", "85pts & 100hp"), ("Cyndaquil", "62pts & 39hp"), ("Totodile", "59pts & 50hp"),
        ("Chikorita", "54pts & 45hp"), ("Marill", "49pts & 70hp"), ("Hoothoot", "46pts & 60hp"), ("Togepi", "51pts & 35hp")
    ]
    random.shuffle(pokemon_cards)
    return pokemon_cards

def deal_cards(cards):
    player1_cards = cards[:10]
    player2_cards = cards[10:]
    return player1_cards, player2_cards

def display_cards(cards, show_power=False):
    for i, (pokemon, power) in enumerate(cards, start=1):
        if show_power:
            print(f"{i}. {pokemon} (Power: {power})")
        else:
            print(f"{i}. {pokemon}")

def choose_card(cards):
    while True:
        try:
            choice = int(input("Choose a card by number: "))
            card = cards[choice - 1]
            return card
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid card number.")

def play_round(player1_name, player2_name, player1_cards, player2_cards):
    print(f"\n{player1_name}'s turn:")
    display_cards(player1_cards)
    player1_card = choose_card(player1_cards)
    player1_cards.remove(player1_card)  # Remove the chosen card from player's deck

    print(f"\n{player2_name}'s turn:")
    display_cards(player2_cards)
    player2_card = choose_card(player2_cards)
    player2_cards.remove(player2_card)  # Remove the chosen card from player's deck

    print("\nResults:")
    print(f"{player1_name} chose {player1_card[0]}")
    print(f"{player2_name} chose {player2_card[0]}")

    print(f"{player1_name}'s card: {player1_card[0]} (Power: {player1_card[1]})")
    print(f"{player2_name}'s card: {player2_card[0]} (Power: {player2_card[1]})")

    if player1_card[1] > player2_card[1]:
        print(f"{player1_name} wins the round!")
        return 1
    elif player2_card[1] > player1_card[1]:
        print(f"{player2_name} wins the round!")
        return 2
    else:
        print("It's a tie!")
        return 0

def main():
    player1_name = input("Enter name for Player 1: ")
    player2_name = input("Enter name for Player 2: ")

    cards = create_and_shuffle_cards()
    player1_cards, player2_cards = deal_cards(cards)

    rounds_to_win = 5
    player1_score = 0
    player2_score = 0
    rounds_played = 0

    while player1_score < rounds_to_win and player2_score < rounds_to_win:
        print(f"\nRound {rounds_played + 1}:")
        result = play_round(player1_name, player2_name, player1_cards, player2_cards)

        if result == 1:
            player1_score += 1
        elif result == 2:
            player2_score += 1

        rounds_played += 1

        if not player1_cards or not player2_cards:
            print("No more cards to play!")
            break

    print("\nFinal Results:")
    print(f"{player1_name}: {player1_score} wins")
    print(f"{player2_name}: {player2_score} wins")

    if player1_score > player2_score:
        print(f"{player1_name} wins the game!")
    elif player2_score > player1_score:
        print(f"{player2_name} wins the game!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()

