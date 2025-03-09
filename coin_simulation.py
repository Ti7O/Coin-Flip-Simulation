import random

possibilities = ["Heads", "Tails"]

win_phrases = [
    "You're a winner!", "Congratulations, you've won!", "Victory is yours!",
    "You've triumphed!", "Well done, you came out on top!", "You're the champion!",
    "Hooray, you've won!", "You've earned this win!", "A resounding victory!",
    "You've proven victorious!", "You're on fire!", "Winner, winner, chicken dinner!",
    "You smashed it!", "You've conquered!", "You've achieved victory!", "You're a legend!",
    "You've prevailed!", "You're the best!", "You've taken the crown!", "You've emerged victorious!"
]

lose_phrases = [
    "Better luck next time!", "You'll get 'em next time!", "Don't give up!",
    "That's a tough loss.", "Try again!", "It's not over yet!", "You were so close!",
    "You fought well!", "Chin up, you'll win soon!", "That's just how the cookie crumbles.",
    "The wheel turns.", "You live and you learn.", "It's all part of the game.",
    "Fortune wasn't on your side this time.", "You almost had it!", "Keep your head up!",
    "You'll bounce back!", "It was a valiant effort.", "Onward and upward!", "Every loss is a lesson."
]

tie_phrases = [
    "It's a draw!", "A tie game!", "Nobody wins, nobody loses.",
    "It's a stalemate.", "A perfectly even match!", "It's a dead heat!",
    "You're equally matched!", "It's a split decision.", "A balanced outcome.", "It's a wash."
]

set_score = {"Heads": 0, "Tails": 0}

def character_select():
    player_1_name = input("Player one, What is your character's Name?: ")
    confirm_player_one_name = input(f"[CONFIRMATION] Player One, Do you want to confirm: {player_1_name} as your name? [Y/N]: ").upper()
    if confirm_player_one_name == "Y":
        player_1 = player_1_name

    player_2_name = input("Player two, What is your character's Name?: ")
    confirm_player_two_name = input(f"[CONFIRMATION] Player Two, Do you want to confirm: {player_2_name} as your name? [Y/N]: ").upper()
    if confirm_player_two_name == "Y":
        player_2 = player_2_name

    return player_1_name, player_2_name

def assign_coin():
    player_one_chosen_coin = input("Player one, do you want Heads or Tails?: ").capitalize()
    if player_one_chosen_coin in ["Heads", "Tails"]:
        player_one_coin = player_one_chosen_coin
        player_two_coin = "Tails" if player_one_coin == "Heads" else "Heads"
        return player_one_coin, player_two_coin
    else:
        print("Invalid input. Player one is assigned Heads, player two is assigned Tails.")
        return "Heads", "Tails"

def determine_winner(player_1_name, player_2_name, player_1_coin, player_2_coin):
    if set_score["Heads"] > set_score["Tails"]:
        winner_coin = "Heads"
    elif set_score["Heads"] < set_score["Tails"]:
        winner_coin = "Tails"
    else:
        return "Tie", random.choice(tie_phrases)

    if winner_coin == player_1_coin:
        return player_1_name, random.choice(win_phrases)
    else:
        return player_2_name, random.choice(win_phrases)

def coin_flip():
    player_1_name, player_2_name = character_select()
    player_1_coin, player_2_coin = assign_coin()

    continue_flip_coin = input("Do you want to flip a coin? [Y/N]: ").upper()
    if continue_flip_coin == "Y":
        play_again = True
        while play_again:
            coin_result = random.choice(possibilities)
            if coin_result == "Heads":
                set_score["Heads"] += 1
            else:
                set_score["Tails"] += 1
            flip_again = input("Your outcome was: " + coin_result + " Do you want to flip again? [Y/N]: ").upper()

            if flip_again == "N":
                winner_name, win_phrase = determine_winner(player_1_name, player_2_name, player_1_coin, player_2_coin)
                if winner_name == "Tie":
                    print(win_phrase)
                else:
                    print(f"{winner_name}: {win_phrase}")
                print(f"Final Score: {player_1_name} ({player_1_coin}): {set_score['Heads']}, {player_2_name} ({player_2_coin}): {set_score['Tails']}")
                play_again = False
                break

coin_flip()
