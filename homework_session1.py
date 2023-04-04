#q1 - the nails are wrong, how to correct it ?
chairs = '15'
nails = 4
total_nails = chairs * nails
#message = 'I need to buy {} nails'.format(total_nails)
print('You need to buy {} nails'.format(total_nails))
#Answer - variable chairs is a string, not a integer - it should be an integer
#correct code is as follow
chairs = 15
nails: int = 4
total_nails = chairs * nails
print(total_nails)
message = 'I need to buy {} nails'.format(total_nails)
print('You need to buy {} nails'.format(total_nails))

#q2 - error in running the program, what is the error

my_name = Penelope
my_age = 29
message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)

#answer - Penelope is not defined - since python is not able to configure it in a datatype
#we will put penelope in brakets
#testing the correct code as follow -
my_name = 'Penelope'
my_age = 29
message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)

#q3 - I have a lot of boxes of eggs in my fridge and I want to calculate
# how many omelettes I can make. Write a program to calculate this.
#Assume that a box of eggs contains six eggs and I need four eggs for each omelette,
# but I should be able to easily change these values if I want.
# The output should say something like "You can make 9 omelettes with 6 boxes of eggs".

e_in_b = int(input('enter number of eggs in each box = '))
n_e_om = int(input('enter number of eggs required for each omlette = '))
n_of_boxes = int(input('enter number of boxes in the fridge = '))

n_of_om = (n_of_boxes*e_in_b)/n_e_om
print('you can make {} omelettes with {} boxes of eggs'.format(n_of_om,n_of_boxes))


