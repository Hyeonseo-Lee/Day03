#6.2

guess_me = 7
number = 1

while number <=8:
    if number < guess_me:
        print('too low')
    if number == guess_me:
        print('found it!')
    if number > guess_me:
        print('oops')
        break
    number = number + 1