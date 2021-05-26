def get_deck(num_cards):
    # imports
    import random
    # variables
    first_card = True
    cards_player = []
    chosen_types = []
    chosen_emblems = []
    new_card = ()
    # check if number of cards_player defined
    # generate the deck
    for i in range(0, num_cards):
        if first_card:
            cards_player.append(random.randint(0, 52))
        elif not first_card:
            new_card = random.randint(0, 52)
            while new_card in cards_player:
                new_card = random.randint(0, 52)
            cards_player.append(new_card)
    if len(cards_player) == len(set(cards_player)):
        print('Good no repeats')
    print(cards_player)
    for i in range(0, number_cards):
        # get emblems and append to chosen emblems list
        if cards_player[i] in range(0, 12):
            chosen_emblems.append(1)
        elif cards_player[i] in range(14, 26):
            chosen_emblems.append(2)
        elif cards_player[i] in range(27, 39):
            chosen_emblems.append(3)
        elif cards_player[i] in range(40, 52):
            chosen_emblems.append(4)
        # get types and append them to the chosen types list
        if cards_player[i] in [1, 14, 27, 40]:
            chosen_types.append(1)
        elif cards_player[i] in [2, 15, 28, 41]:
            chosen_types.append(2)
        elif cards_player[i] in [3, 16, 29, 42]:
            chosen_types.append(3)
        elif cards_player[i] in [4, 17, 30, 43]:
            chosen_types.append(4)
        elif cards_player[i] in [5, 18, 31, 44]:
            chosen_types.append(5)
        elif cards_player[i] in [6, 19, 32, 45]:
            chosen_types.append(6)
        elif cards_player[i] in [7, 20, 33, 46]:
            chosen_types.append(7)
        elif cards_player[i] in [8, 21, 34, 47]:
            chosen_types.append(8)
        elif cards_player[i] in [9, 22, 35, 48]:
            chosen_types.append(9)
        elif cards_player[i] in [10, 23, 36, 49]:
            chosen_types.append(10)
        elif cards_player[i] in [11, 24, 37, 50]:
            chosen_types.append(11)
        elif cards_player[i] in [12, 25, 38, 51]:
            chosen_types.append(12)
        elif cards_player[i] in [13, 26, 39, 52]:
            chosen_types.append(13)
    # we then return,
    # the variables being globals there is not need to return them
    return


get_deck(50)
