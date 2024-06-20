Eaten_food = list()
while True:
    food = input('What do you want to eat?').lower()
    match food:
        case 'stop':
            break
        case 'cordonyellow':
            print('Do not eat the creator of this program!')
        case 'github':
            print('You don\'t like Github? :(')
        case _:
            Eaten_food.append(food)
    print('You have so far eaten', Eaten_food)
