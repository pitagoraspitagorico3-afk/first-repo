def get_item(x):
    if x == 1:
        return 'Cheeseburger'
    elif x == 2:
        return 'Fries'
    elif x == 3:
        return 'Soda'
    elif x == 4:
        return 'Ice cream'
    elif x == 5:
        return 'Cookie'
    else:
        return 'Invalid option'


def welcome():
    print('Welcome to Sonnyboy\'s Diner!')
    print('Here\'s the menu:')
    print('1. 🍔 Cheeseburger')
    print('2. 🍟 Fries')
    print('3. 🥤 Soda')
    print('4. 🍦 Ice Cream')
    print('5. 🍪 Cookie')


welcome()

option = int(input('what would you like to order?'))
print(get_item(option))