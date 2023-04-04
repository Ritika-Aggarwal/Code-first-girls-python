#program 1
for i in range(0,9):
    print('~'*i)

#program 2 - boolean
today = input('what day is it? ')
is_monday = today == 'Monday' or today == 'monday'

print('today is monday?: {}'.format(is_monday))

#program 3
price = input('Enter your budget price? ')

budget = float(price) <= 10.00

print('Burger is within budget: {}'.format(budget))

#program 4
price = input('Is burger within budget? y/n ')
budget = price == 'y'

veg = input('does the place have veg option? y/n ')
veg_option = veg == 'y'

meet_criteria = budget and veg_option

print('Restaurant meets the criteria: {}'.format(meet_criteria))

#program 5
price = input('enter the buget price? ')
budget = float(price) <= 10.0

veg = input('does the place have veg option? y/n ')
veg_option = veg == 'y'

if budget and veg_option:
    print('Restaurant is a great choice')

if not budget or not veg_option:
    print('probably not a good idea')

#program 6
price = input('enter the buget price? ')
budget = float(price) <= 10.0

veg = input('does the place have veg option? y/n ')
veg_option = veg == 'y'

if budget and veg_option:
    print('Restaurant is a great choice')
else:
    print('probably not a good idea')

#program 7 - calculate the price and apply a discount
meal_price = float(input('how much did the meal cost? '))

if meal_price >= 20:
    print('discount applied')
    dis = (10/100)*meal_price
    price_to_pay = meal_price-dis
    print('price to pay = {}'.format(price_to_pay))
else:
    print('no discount')


temp = int(input('enter the temp? '))

if temp >= 200:
    print('the oven is too hot')
elif temp <150:
    print('the oven is too cold')
elif temp == 180:
    print('the oven is at the perfect temperature')
else:
    print('the temperature is close enough')

