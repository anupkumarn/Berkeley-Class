while True:
    try:
        a = int(input('Please enter a number: '))
        print(' You entered the number ',a)
        print('I will now exit. Bye!')
        break
    except ValueError:
        print('You entered an invalid number. Please try again.')