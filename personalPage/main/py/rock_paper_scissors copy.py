print("Enter \"done\" to end game.")
game = True

while game == True:
    player_1 = input("Player one, rock, paper, or scissors?")
    player_2 = input("Player two, rock, paper, or scissors?")

    if player_1 == player_2:
        print("It looks like you don't know how to play...")
        break

    if player_1.lower() == "rock" and player_2.lower() == "scissors":
        print("Player one wins")
        new_game = input("Play another game? y/n: ")
        if new_game == "y":
            continue
        else:
            break
    if player_1.lower() == "scissors" and player_2.lower() == "paper":
        print("Player one wins")
        new_game = input("Play another game? y/n: ")
        if new_game == "y":
            continue
        else:
            break

    if player_1.lower() == "paper" and player_2.lower() == "rock":
        print("Player one wins")
        new_game = input("Play another game? y/n: ")
        if new_game == "y":
            continue
        else:
            break

    if player_2.lower() == "rock" and player_1.lower() == "scissors":
        print("Player two wins")
        new_game = input("Play another game? y/n: ")
        if new_game == "y":
            continue
        else:
            break

    if player_2.lower() == "scissors" and player_1.lower() == "paper":
        print("Player two wins")
        new_game = input("Play another game? y/n: ")
        if new_game == "y":
            continue
        else:
            break

    if player_2.lower() == "paper" and player_1.lower() == "rock":
        print("Player two wins")
        new_game = input("Play another game? y/n: ")
        if new_game == "y":
            continue
        else:
            break

    if player_1.lower() or player_2.lower() == "done":
        game = False

    else:
        continue
