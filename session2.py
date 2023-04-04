game = input('what game do you like: ')
instrument = input('what instrument do you like: ')

print('you like {} and you like {}' .format(game,instrument))

friends = int(input('number of friends at your house?: '))
slices = int(input('number of slice in each pizza?: '))
pizza = friends/(slices*2)
print('i need {} pizza for {} friends'.format(pizza,friends))

import datetime
x = datetime.datetime.now()
print(x)

total = 0
print('total value before for loop is {}'.format(total))
for num in range(3):
    print('we are in loop',str(num),'of our for loop')
    total = total+1

print('total value after for loop is {}'.format(total))

def circle_area(radius): #add the radius argument inside the bracket
    area = 3.14*(radius**2)
    return area

circle1 = circle_area(10)
print('Area of the circle with radius 10 is',circle_area(10))


def days_in_hours(days):
    hours = days * 24
    return hours

print(days_in_hours(10))