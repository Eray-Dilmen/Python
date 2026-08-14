from models import Card, Deck, Player # veya import * diyerek dosyanın içindeki tamamını alabilirdik.

if __name__ == "__main__":

    player_one = Player("One")
    player_two = Player("Two")

    deck = Deck()
    deck.shuffle()

    # Distribute 26 cards to each player
    for _ in range(26):
        player_one.add_card(deck.distribute_card())
        player_two.add_card(deck.distribute_card())

    in_game = True
    round_num = 0

    while in_game:
        round_num += 1
        print(f"Round {round_num}")

        # Win condition check
        if len(player_one.all_cards) == 0:
            print("Player One out of cards. Player Two wins!")
            in_game = False
            break
        elif len(player_two.all_cards) == 0:
            print("Player Two out of cards. Player One wins!")
            in_game = False
            break

        # Initialize table for the current round
        player_one_cards = [player_one.player_put_to_table()]
        player_two_cards = [player_two.player_put_to_table()]

        at_war = True

        while at_war:
            # Player One has the higher card
            if player_one_cards[-1].value > player_two_cards[-1].value:
                player_one.add_card(player_one_cards)
                player_one.add_card(player_two_cards)
                at_war = False

            # Player Two has the higher card
            elif player_one_cards[-1].value < player_two_cards[-1].value:
                player_two.add_card(player_one_cards)
                player_two.add_card(player_two_cards)
                at_war = False

            # Tie condition triggers WAR
            else:
                print('WAR!')

                # Check for minimum card requirement to execute war (5 cards)
                if len(player_one.all_cards) < 5:
                    print("Player One doesn't have enough cards to declare war. Player Two wins!")
                    in_game = False
                    break
                elif len(player_two.all_cards) < 5:
                    print("Player Two doesn't have enough cards to declare war. Player One wins!")
                    in_game = False
                    break
                else:
                    # Both players add 5 cards to the table
                    for _ in range(5):
                        player_one_cards.append(player_one.player_put_to_table())
                        player_two_cards.append(player_two.player_put_to_table())