# -1. Names: Store the names of a few of your friends in a list called names. Print 
# each person’s name by accessing each element in the list, one at a time.
names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
for n in names:
    print(n)
#Greetings: Start with the list you used in Exercise 3-1, but instead of just 
# printing each person’s name, print a message to them. The text of each mes
# sage should be the same, but each message should be personalized with the 
# person’s name.
for n in names:
    print(f'Hello, {n}! Hope you are having a great day!')
# Your Own List: Think of your favorite mode of transportation, such as a 
# motorcycle or a car, and make a list that stores several examples. Use your list 
# to print a series of statements about these items, such as “I would like to own a 
# Honda motorcycle.”
transportation = ["car", "motorcycle", "bicycle", "scooter", "bus"]
for t in transportation:
    print(f'I would like to own a {t}.')
