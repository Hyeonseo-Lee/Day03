#6.3

guess_me = 5

for number in range (10):
    if number < guess_me:
        print('too low')
    if number == guess_me:
        print('found it!')
    if number > guess_me:
        print('oops')
        break