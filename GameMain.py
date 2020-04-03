# This is the main logic and outputs in the game
from GameClass import *
import time

# Welcome introduction of the game
print(f"{bcolors.BOLD}{bcolors.UNDERLINE}{bcolors.OKBLUE}Welcome to 31-CARD GAME!!!{bcolors.ENDC}")
if input("Do You Know The Basic Rules Of This Game(Y/ N):").upper() == "N":
    print("Rules And Objectives of 31 CARD GAME".center(100, "_") + "\n")
    print("""
    The Basic game is played by four players but in this game you can play this game with any number 
    of players How ever the recommended number is four
    You can even play this game with the computer but it will be too easy if you are a pro ; )
    
    This game is played with a single card deck and what our objective is to collect cards in a
    single suit(Clubs, Diamonds, Hearts, Spades) which give the total value of 31,
    
    And here are the values of the cards
    
    A : Ace - 11
    K : King - 10
    Q : Queen - 10
    J : Jack - 10
    Other : Value of the card
    
    In this game we represent,
    H : Heart
    S : Spade
    C : Club
    D : Diamond
    
    each player can keep 3 cards in there hands and they have three lives at the beginning all players
    them self three cards and the what left in the deck is kept on the table and the top card is shown
    When each player playing their hand they they can either take the card shown on the table or they
    can take the top card from the deck and replace a card with you,
    How ever you should keep only 3 cards.
    
    If a player is satisfied with the value of card they have they can 'Knock'
    when he does every other player get a chance to get a card in either way mention above after all
    other players got their chance,
        1. The person who has the lowest cards will lose a life
        2. If the person who had knock has the lowest value he will lose two lives
        3. If two people have same lowest value then both of them will lose a life 
           
    How ever if a player got 31 in his hand in same suit he will win instantly and it is called blitZ
    
    every player can pass their hand without taking the card on the table or looking at the top card on 
    the deck. But if a player see the top card on the deck  he has to replace it or place it on the top
    of the discard cards on the table.
    
    So This is hove The Game Goes The Program Will Lead You through out the game
    So Enjoy ;-)""")

# This is a decoration
else:
    print(f"{bcolors.WARNING}" + "_"*100 + f"{bcolors.ENDC}")
    print("Lets get started then,")


# These are some basic things a player should know to play this game
print("\n"
      "There are few things you need to know\n"
      "You may use following method to enter the names of cards\n"
      " CA : clubs ace\n"
      " h10: heart 10\n"
      " s2: spades 2\n"
      "Case does not matter but please use the method.\n"
      "You should use the given number for the command you wish to take.")

print(f"{bcolors.WARNING}" + "_"*100 + f"{bcolors.ENDC}")


# commonly used functions in this code
def common_cmd():
    """
    We use this function to take input for following common commands
        1. Exchange the table card
        2. See the deck card
        3. Knock
        4. Pass
    """
    while True:
        command = input("What do you want to do(Enter the number of the command): ")
        if command in ["1", "2", "3", "4"]:
            return command
        else:
            print("Invalid input please enter the number of the command!!!")


def max_total(cards_hand):
    """
    This will return the total value of a list of card list
    :param cards_hand: list of cards
    :return: max value of a single suit cards
    """
    card_sum = {"S": 0, "C": 0, "H": 0, "D": 0}
    pack_value = {"A": 11, "K": 10, "Q": 10, "J": 10, "10": 10, "9": 9,
                  "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}

    # This loop will get the total of each suit
    for card in cards_hand:
        suit = card[0]
        if suit == "S":
            card_sum["S"] += pack_value[card[1:]]
        elif suit == "C":
            card_sum["C"] += pack_value[card[1:]]
        elif suit == "D":
            card_sum["D"] += pack_value[card[1:]]
        elif suit == "H":
            card_sum["H"] += pack_value[card[1:]]

    return max(list(card_sum.values()))


def is_blitz(cards_hand):
    """
    This is a function defined to check whether there is a blitz
    :param cards_hand: hand that want be checked
    :return: True if it is a blitz
    """
    if max_total(cards_hand) == 31:
        return True
    else:
        return False


def rearrange(number_list, start):
    """
    arrange a list starting from a given number and reading clockwise
    :param number_list: list that we want to arrange
    :param start: The staring value of the new list
    :return: arranged list
    """
    new_list = number_list[number_list.index(start):] + number_list[:number_list.index(start)]
    return new_list


def pack_end(card_pack):
    """
    To check whether a given list of cards in a card pack is empty
    :param card_pack: list of cards
    :return: True if list is empty
    """
    if len(card_pack) == 0:
        print("Card pack is over, End of the round")
        return True
    else:
        return False


def gen_name(name_list):
    rand_name = random.choice(name_list)
    name_list.remove(rand_name)
    return rand_name


# This is the main game function
def main():
    try:
        # We use the exception for any non integer values that user input
        # number of players that playing the game at the beginning
        num_players = int(input("Enter the number of players you want to play this game: "))
        if num_players <= 0:
            raise ValueError
        num_npc = int(input("Enter the number of NPCs(Non-Character-Player) you want to get (0 for None) :"))

        if num_npc < 0:
            raise ValueError

    except ValueError:
        print("Invalid input please enter a valid number of players!!")
        main()
    else:

        # Total Number of players should belongs to (1, 10)
        if not 10 > num_players + num_npc > 1:
            print("There should be more than 1 players and maximum of 10 players to play this game")
            main()

        # Player variables are player_n (n in number_players)
        # In this code we take the names from the users and welcome each of them to the game
        for i in range(1, num_players + 1):
            vars()[f"player_{i}"] = Player(input(f"Enter player_{i} name: "))
            print(f"Hello {eval(f'player_{i}').name} you have {eval(f'player_{i}').lives} lives")

            print("*"*50)

        npc_list = []
        names = ['Lara Croft', 'Sweet', 'Carl Jonson', 'Lit. Soap', 'Cpt. Price', 'Logan', 'Lance', 'Hancock',
                 'Lucifer', 'Woods', 'Mason', 'Agent Prophet', 'Big Smoke']
        print("NPCs in the game:")
        for x in range(num_players + 1, num_players + num_npc + 1):
            vars()[f"player_{x}"] = NPC(gen_name(names))
            print(f"\t{eval(f'player_{x}').name} you have {eval(f'player_{x}').lives} lives")
            npc_list.append(x)

        print("*" * 50)

        # These are the variables that are needed through out the game
        player_list = list(range(1, num_players + num_npc + 1))
        # These are the place holders that we need in the game
        last_player_knocked = None
        not_in_game = []
        table_card = None
        pack = None
        knocked_player = None
        user_command = None
        # These are boolean values at the beginning of the game
        new_round = True
        card_pack_end = False
        blitz = False
        first_knock = False
        result_check = False
        knock = False

        # This is the main game loop : MAIN LOOP
        while True:

            # These are the code that are needed to be executed at the beginning of a round
            if new_round:
                # This is the construction of the card pack cards which is denoted by 'pack'
                pack_suit = ["H", "C", "S", "D"]
                pack_value = {"A": 11, "K": 10, "Q": 10, "J": 10, "10": 10, "9": 9,
                              "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
                pack = list_permutations(pack_suit, list(pack_value.keys()))

                # This is the loop which distribute card hands to each player
                # And check each hand have a blitz at the beginning
                for i in player_list:
                    eval(f'player_{i}').get_hand(pack)
                    blitz = is_blitz(eval(f'player_{i}').hand)

                table_card = see_deck_card(pack)
                new_round = False

                for x in npc_list:
                    eval(f"player_{x}").hot_round = True

            # This is the loop for each players hand in a game round - PLAYER LOOP
            for player in player_list:

                current_player = eval(f"player_{player}")  # We created this variable because it is easy to use

                # This is the condition for having a blitz at the very beginning
                # As now all the hands have distributed We don't need to continue the loop
                if blitz:
                    result_check = True
                    break  # breaking from the PLAYER LOOP

                # This is the code if the player is a npc
                if player in npc_list:
                    print(f"{bcolors.FAIL}{current_player.name} is playing...{bcolors.ENDC}")
                    time.sleep(random.randint(1, 6))

                    old_max_suit = max_total(current_player.hand)
                    best_from_table = current_player.card_collection(table_card)
                    new_max_suit = max_total(best_from_table)

                    if old_max_suit > 20 and current_player.hot_round:
                        knock = True

                    # This runs if knock is a good choice
                    if old_max_suit > 25 and not knock:
                        knock = True

                    # This runs if table card is not a good choice
                    elif old_max_suit == new_max_suit:
                        table_card = see_deck_card(pack)
                        best_from_deck = current_player.card_collection(table_card)

                        # This runs if pack is over
                        if pack_end(pack):
                            result_check = True

                        # This runs if deck card is a good choice
                        elif old_max_suit < max_total(best_from_deck):
                            table_card = current_player.get_collection(best_from_deck)
                            blitz = is_blitz(current_player.hand)

                    # This code run if table card is a good choice
                    elif old_max_suit < new_max_suit:
                        table_card = current_player.get_collection(best_from_table)
                        blitz = is_blitz(current_player.hand)

                    current_player.hot_round = False

                    # we have to use like this because we can't use continue because npc also can knock and
                    # it cause for every player
                    next_player = True

                # This is the code if the player is not npc
                else:
                    print(f"{bcolors.WARNING}" + "_" * 100 + f"{bcolors.ENDC}")
                    # This is the code where player get chance to see his hand and card on the table at the moment
                    print(f"{current_player.name} is playing: \n")
                    print(f"Your Hand: {' '.join(current_player.hand)}")
                    print(f"Table Card: {table_card}")

                    # This is for let other players know if there is a knock
                    if knock:
                        print(f"{eval(f'player_{player_list[last_player_knocked]}').name} has knocked!!!")

                    # list of Commands that player can have at this point
                    print("""
                        1. Exchange the table card
                        2. See the deck card
                        3. Knock
                        4. Pass""")

                    user_command = common_cmd()  # we are taking the user command from a function
                    next_player = False  # used to stop the game until this player enter a valid command next

                # This is a loop to make user input correct secondary command - COMMAND 1 LOOP
                # Because we have to keep the user asking for input until he insert the correct input
                while not next_player:

                    # This code will execute if the command is 1
                    # After taking this option taking an another option is acceptable
                    if user_command == "1":
                        # in case we decided to chose another option as user command
                        print("Enter 'X' if you want to chose another option")

                        ex_card = input("Enter the card you want to exchange: ").upper()  # card we want to exchange

                        # This code will execute if the user need to take another option
                        if ex_card == "X":
                            print("*"*50)
                            user_command = common_cmd()

                        # In this code the card on the table will be replaced with an another card in hand
                        elif ex_card in current_player.hand:
                            current_player.get_card(table_card, ex_card)  # func to exchange the card
                            table_card = ex_card  # card we discarded goes to the table

                            # decoration with players updated hand
                            print()
                            print(f'Your hand is: {" ".join(current_player.hand)}')
                            print(f"{bcolors.WARNING}" + "_" * 100 + f"{bcolors.ENDC}")

                            # we hve rearrange our hand so we need to check for blitz
                            blitz = is_blitz(current_player.hand)

                            break  # break from COMMAND 1 LOOP (indent lvl: 4)

                        # If user enter anything that is not in his hand this will be executed
                        else:
                            print("Invalid Card in your hand, Please enter a valid card!!!")
                            print("*" * 50)

                    # This is the second option that user can take
                    # After taking this option user can't try other options like before
                    # This the command to take the top card of the deck
                    elif user_command == "2":

                        deck_card = see_deck_card(pack)  # this is the card we took from the deck
                        print("-"*50)

                        result_check = pack_end(pack)  # To check whether the deck is finished
                        if result_check:  # break if it card deck is over
                            break  # break from COMMAND 1 LOOP (indent lvl: 4)

                        print("""\
                    1. Exchange with card in hand
                    2. Pass""")

                        # This loop is created to get the correct inputs from user to above commands (command 2)
                        # COMMAND 2 LOOP
                        while True:

                            # display the player hand and the deck card
                            print(f'Your hand is: {" ".join(current_player.hand)}')
                            print(f"The card is :{deck_card}")

                            user_command_2 = input("Enter the Command: ")

                            # This is what we accept from the user as command 2
                            if user_command_2 in ["1", "2"]:

                                # This loop come because after we take this decision we can change it later
                                # We use this loop to handle that kinds of situation - COMMAND 3 LOOP
                                while True:

                                    # This code will execute if user chose to replace a card in his hand
                                    if user_command_2 == "1":

                                        # Player can still change his option as command 2
                                        print("Enter 'X' if you want to chose another option")

                                        # ex_card: card we are going to discard
                                        ex_card = input("Enter the card you want to exchange: ").upper()

                                        # This is the code to remove the card from the hand if it is available in hand
                                        if ex_card in current_player.hand:

                                            current_player.get_card(deck_card, ex_card)  # exchange the card
                                            table_card = ex_card  # now the table card is what player discard

                                            print(f'Your hand is: {" ".join(current_player.hand)}')
                                            print(f"{bcolors.WARNING}" + "_" * 100 + f"{bcolors.ENDC}")

                                            blitz = is_blitz(current_player.hand)  # check blitz cause hand has updated
                                            next_player = True  # leaves the COMMAND 1 LOOP (indent lvl: 6)

                                            break  # break from COMMAND 3 LOOP (indent lvl: 8)

                                        # Player decide to chose command 2 again
                                        elif ex_card == "X":
                                            print("*"*50)
                                            break  # break from COMMAND 3 LOOP (indent lvl: 8)

                                        # If player enter an invalid input
                                        else:
                                            print("Please enter a valid input or a card in your hand!!!")
                                            print("*"*50)

                                    # This is the code if the player chose not to take the deck card
                                    elif user_command_2 == "2":

                                        table_card = deck_card  # Deck card is now being placed on the table

                                        print(f"{bcolors.WARNING}" + "_" * 100 + f"{bcolors.ENDC}")

                                        ex_card = "Passed"  # we use this variable to get away from the loop
                                        next_player = True  # leave COMMAND 2 LOOP (indent lvl: 6)

                                        break  # break COMMAND 3 LOOP (indent lvl: 8)

                            # If user enter wrong input as COMMAND 2
                            else:
                                print("invalid command, please enter a valid command number!!!")
                                print("*"*50)
                                continue  # redirect back to COMMAND 2 LOOP (indent lvl: 6)

                            # This is the condition we created to check whether this player no need to be in this loop
                            # And he had a taken an action correctly
                            if ex_card == table_card or ex_card == "Passed":
                                break  # break COMMAND 2 LOOP (indent lvl: 6)

                    # This is the code to if the player decided to knock when any other players have not knocked
                    elif user_command == "3" and not knock:
                        knock = True  # Get access to KNOCK LOOP
                        next_player = True  # leave COMMAND 1 LOOP (indent lvl: 4)
                        print(f"{bcolors.WARNING}" + "_" * 100 + f"{bcolors.ENDC}")

                    # This is the code to pass if player decided to pass
                    elif user_command == "4":
                        print(f'Your hand is: {" ".join(current_player.hand)}')
                        next_player = True  # break COMMAND 1 LOOP (indent lvl: 4)
                        print(f"{bcolors.WARNING}" + "_" * 100 + f"{bcolors.ENDC}")

                    # If this loop is going on a knocked situation
                    # This code is created to display other players that they can't knock again
                    elif knock:
                        print("A player has already knocked you can't knock now!!!")
                        user_command = common_cmd()  # taking the COMMAND 1 again

                # This execute if it is not knocked and card pack is over
                # result check is true because at this time results can be checked
                if not knock and result_check:
                    break  # break PLAYER LOOP

                # This execute if it is being knocked and card pack is over and it is not fair to check result
                # This situation count as a draw
                if knock and result_check:

                    # these are the variables that are needed to be reset before next round
                    result_check = False
                    knock = False
                    first_knock = False
                    card_pack_end = True  # This is a special variable created to avoid checking results
                    print("Card Pack is over and it is being knocked and It'declares a draw, Let's play a new round")

                    # This is a decoration
                    print("*" * 50)
                    # This display lives of players at the end of the round
                    for i in range(1, num_players + 1):
                        # This is the code to skip below steps if the player is no longer in the game
                        if i in not_in_game:
                            continue
                        print(f"{eval(f'player_{i}').name} you have {eval(f'player_{i}').lives} lives left")
                    print("_" * 100 + "\n")
                    print("_" * 100 + "\n")
                    print("\n")
                    break  # break from PLAYER LOOP

                # This selection was created to find out that the knock loop have gone correctly
                # it can't be knocked after card deck is finished ; )
                if knock:

                    # At the beginning first_knock was false
                    # and it is being True once this selection get executed
                    # Once it has been executed and get True for first_knock this selection will be always be false
                    if not first_knock:
                        # Here we are storing the number of the player who knocked
                        last_player_knocked = player_list.index(player)
                        knocked_player = player
                        first_knock = True

                    # This selection get passed if after knock, the exact player before the knocked player,
                    # has got his chance and it will break from the PLAYER LOOP
                    # After this become true we can who looses
                    if player_list[player_list.index(player)] == player_list[last_player_knocked - 1]:
                        result_check = True  # this variables will be need to check the result
                        knock = False  # because after this knock should be changed
                        first_knock = False
                        break  # break from PLAYER LOOP

            # This will pass if now it is time to check the results if card pack is not over when knocked
            # and also if the card pack is end before knock
            if result_check and not card_pack_end:

                # Because This RESULT SELECTION will give the final result of this round
                result_check = False
                new_round = True  # in next round we want a new shuffled deck

                # First we have to inform whether players that there was a blitz
                if blitz:
                    print("One Player got a blitz")

                print("_" * 100 + "\n")

                lowest_result = 31  # This is the lowest value can be get for each suit
                loosing_player_list = []  # place holder for loosing players

                # This is the loop for check who got the lowest max suit value from all the players
                # This creates the loosing_player_list
                for i in player_list:

                    max_suit = max_total(eval(f"player_{i}").hand)  # max value of the current hand
                    print(f'{eval(f"player_{i}").name}\'s maximum suit: {max_suit}')

                    # If the current i th player has the lower value
                    if lowest_result > max_suit:
                        lowest_result = max_suit  # New lowest value
                        loosing_player_list = [i]

                    # If we have multiple players who have same lowest value we are storing all of them in a list
                    elif lowest_result == max_suit:
                        loosing_player_list.append(i)

                print("*"*50)

                # if the all player is a losing player then it is a draw
                # Because it is a draw this round it is need to be play again
                if len(loosing_player_list) == len(player_list):
                    print("It is a Draw, Let's Go another round : )")
                    continue  # redirecting back to MAIN LOOP

                # This is the loop for reduce life of each of losers and let them know
                for loser in loosing_player_list:

                    looser_index = player_list.index(loser)  # index of a looser in player_list

                    print(f"{eval(f'player_{loser}').name} You lost this round")

                    # knocked player is the looser
                    if loser == knocked_player and len(loosing_player_list) == 1:
                        eval(f'player_{loser}').lives -= 2  # reducing two lives
                    else:
                        eval(f'player_{loser}').lives -= 1  # reducing a life

                    # This is the code to kick a player who lost all his lives from the game
                    if eval(f'player_{loser}').lives < 1:
                        print(f"{eval(f'player_{loser}').name} You have loosen the game")

                        end_index_player_list = len(player_list) - 1  # index of the last player in player list

                        not_in_game.append(loser)
                        player_list.remove(loser)

                        # This is the condition which last player of the player list lost the game
                        # rearrange player list
                        if looser_index == end_index_player_list:
                            player_list = rearrange(player_list, player_list[0])

                        # rearrange player list
                        else:
                            player_list = rearrange(player_list, player_list[looser_index])

                    else:
                        player_list = rearrange(player_list, loser)  # because in next round looser has to start

                # Winner Check
                if len(player_list) == 1:

                    winner = player_list[0]
                    print(f"{bcolors.BOLD}{bcolors.OKBLUE}Congratulations {eval(f'player_{winner}').name} "
                          f"You Won The Game!!!{bcolors.ENDC}")
                    print("_" * 100 + "\n")

                    # This is to check whether players need to play again
                    play_again = input("Do You Want To Play Again[Y/N]: ").upper()

                    if play_again == "Y":
                        main()
                    else:
                        print(f"{bcolors.OKGREEN}Thank You For Playing 31, Good Bye!!! : ){bcolors.ENDC}")
                        break  # break from MAIN LOOP

                # This is to find out if there is any user still playing the game
                for char_player in player_list:
                    if char_player not in npc_list:
                        break
                else:
                    print(f"{bcolors.FAIL}Only NPCs left, AI don't want to challenge AI ;-){bcolors.ENDC}")
                    print(f"{bcolors.FAIL}{bcolors.BOLD}Better Luck Next Time Users!!!{bcolors.ENDC}")

                    # This is to check whether players need to play again
                    play_again = input("Do You Want To Play Again[Y/N]: ").upper()

                    if play_again == "Y":
                        main()
                    else:
                        print(f"{bcolors.OKGREEN}Thank You For Playing 31, Good Bye!!! : ){bcolors.ENDC}")
                        break  # break from MAIN LOOP

                # decoration before next round
                print("*"*50)
                for i in player_list:
                    # This is the code to skip below steps if the player is no longer in the game
                    if i in not_in_game:
                        continue
                    print(f"{eval(f'player_{i}').name} you have {eval(f'player_{i}').lives} lives left")
                print("_" * 100 + "\n")
                print("_" * 100 + "\n")
                print("\n")
                time.sleep(10)


main()
