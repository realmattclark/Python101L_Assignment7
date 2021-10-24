cars_list = {'year': '2000', 'make': 'Nissan', 'Model': 'Altra EV', 'mpg': '85.000'}

def mpg():
    
    user_input = int(input('Enter the MPG for the vehicle: '))
    if user_input > 100:
        print('Must be less than 100')
        
    elif user_input <= 0:
        print('MPG must be equal to or greater than 0')
        
    else:
        text_file = input('Enter the name of the input vehicle text: ')
        if text_file != 'vehicles2.txt':
            print('Error')
        else:
            print(cars_list)

mpg()
