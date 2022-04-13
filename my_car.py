command = ''
status = 'stopped'
while True:
    command = input('>').lower()
    if command == 'start':
        if status == 'stopped':
            print('car started')
            status = 'started'
        else:
            print('The car is already started')
    elif command == 'stop':
        if status == 'started':
            print('car stopped')
            status = 'stopped'
        else:
            print('The car is already stopped')

    elif command == 'quit':
        break
    else:
        print("I don't understand your command")

        