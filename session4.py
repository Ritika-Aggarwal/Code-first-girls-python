import math
import random
#program1
clothes = [
    "shorts",
    "shoes",
    "t-shirt",
]

if clothes[0] == 'shorts':
    clothes[0] = 'warm coat'

#program2
'''
Make a list of game scores. Using list functions write code to output information of the scores in the following format:
Extension: Output all of the scores in descending order
'''


list_game_scores = [30,20,40,3,50,24,25,29,89,200]
print('Number of scores:',len(list_game_scores))
print('Highest score:',max(list_game_scores))
print('Lowest score:',min(list_game_scores))
print('highest to lowest scores:',list(reversed(sorted(list_game_scores))))

#program3
'''
Whenever I'm shopping and I buy some bread I always forget to buy butter. Create a list
and if 'bread' is in the list, add 'butter' to the shopping list.
Try running the program with and without bread in the list to check that your program works.
Remember the in operator checks if an item is in a list and the .append() method adds an item to a
list.
'''

shopping_list = ['bread','cookies','milk']

if 'bread' in shopping_list:
    shopping_list.append('butter')
else:
    print('bread is not in your shopping list')

print(shopping_list)

#problem4
'''
I want to work out how much money I've spent on lunch this week. I've created a list of
what I spent each day.
Write a program that uses a for loop to calculate the total cost
'''

costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
total_cost = 0

for lunch_money in costs:
    total_cost += lunch_money

print('total spent on lunch this week is {}'.format(total_cost))

#problem5
'''
Print the values of name , post_code and street_number from the dictionary
Print the values of longitude and latitude from the inner dictionary
'''
place = {
    'name': 'The Anchor',
    'post_code': 'E14 6HY',
    'street_number': '54',
    'location': {
        'longitude': 127,
        'latitude': 63,
    }
}

print(place['name'],place['post_code'],place['street_number'])
print(place['location']['longitude'],place['location']['latitude'])

#problem6
'''
Using a for loop, output the values name , colour and 
price of each dictionary in the list
'''
fruits = [
{'name': 'apple', 'colour': 'red', 'price': 0.12},
{'name': 'banana', 'colour': 'yellow', 'price': 0.2},
{'name': 'pear', 'colour': 'green', 'price': 0.19},
]

for fruit in fruits:
    print(fruit['name'])
    print(fruit['colour'])
    print(fruit['price'])

#random module and choice function
import _practice
colours = ['red', 'green', 'blue']
chosen_colour = random.choice(colours)
print(chosen_colour)

#problem7
'''
Write a program to create a random name. You should have a list of random firstnames
and a list of lastnames. Choose a random item from each and display the result.
Extension: Using list of verbs and a list of nouns, create randomised sentences
'''

firstname = ['Ritika','Rashika','Sanchit']
lastname = ['Hogman','Weinrich','Gupta','Sharma']

chosen_First_name = random.choice(firstname)
chosen_Last_name = random.choice(lastname)
random_name = chosen_First_name +' '+ chosen_Last_name
print('The random name is {}'.format(random_name))

noun = ['kids','friends','workers']
connection = ['are','were','will be','should be']
verb = ['playing','eating','working','studying']

sentence = random.choice(noun)+' '+random.choice(connection)+' '+random.choice(verb)+'.'
print(sentence)

