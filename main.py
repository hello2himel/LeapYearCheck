print('Welcome! You can check if a year is a leap year using this program.')

year = int(input('Please type the year: '))

if year % 100 == 0:
    if year % 400 == 0:
        print(f'{year} is a leap year.')
    else:
        print(f'{year} is not a leap year.')
else:
    if year % 4 == 0:
        print(f'{year} is a leap year.')
    else:
        print(f'{year} is not a leap year.')