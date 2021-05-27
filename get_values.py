import deck

# creating and setting up deck
num_cards = 52
deck.d(num_cards)
deck.p(num_cards)

# setting up variables
ace_positions = []
ace_positions_d = []
values_p = []
values_d = []
for i in range(0, 50):
    if deck.chosen_types_d[i] == 1:
        ace_positions_d.append(i)
        values_d.append(11)
    if deck.chosen_types_d[i] in range(2, 11):
        values_d.append(deck.chosen_types[i])
    elif deck.chosen_types_d[i] in range(10, 14):
        values_d.append(deck.chosen_types[10])
for i in range(0, 50):
    # saving the positions of the aces
    if deck.chosen_types[i] == 1:
        ace_positions.append(i)
        values_p.append(11)
    if deck.chosen_types[i] in range(2, 11):
        values_p.append(deck.chosen_types[i])
    elif deck.chosen_types[i] in range(10, 14):
        values_p.append(deck.chosen_types[10])

print('Dealer')
print(deck.chosen_types_d)
print(values_d)
print('player')
print(deck.chosen_types)
print(values_p)