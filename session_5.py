my_dic = [
    {'species': 'zebra', 'name': 'Penelope'},
    {'species': 'penguin', 'name': 'Jenn'},
    {'species': 'elephant', 'name': 'Harris'},
    {'species': 'flamingo', 'name': 'Florence'},
]

for value in my_dic:
    print(value['species'])

with open('todo.txt', 'w+') as text_file:
    to_do_items = 'buy_groceries \npick_up_car \ngo_to_gym \n'

    text_file.write(to_do_items)

with open('todo.txt', 'r') as text_file:
    contents = text_file.read()

print(contents)
new_item = 'make_supper'
with open('todo.txt','a+') as text_file:
    text_file.write(new_item)

with open('todo.txt','r') as text_file:
    contents = text_file.read()

print(contents)

heights = []
import csv
with open('trees.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    for row in spreadsheet:
        tree_height = row['height']
        heights.append(tree_height)

shortest_height = min(heights)
print(shortest_height)
