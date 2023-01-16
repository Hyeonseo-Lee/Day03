#while


#while True:
#    dan = int(input('Dan (0 to quit) : '))

#    if dan == 0:
#        break

#    if 1 < dan < 10:
    #if dan >= 2 and dan <= 9:
#        for i in range(1, 10, 1):
#
#            print('{0} * {1} = {2}'.format(dan, i, dan*i))
#            i = i + 1
#        break
#    else:
#        print('2에서 9사이의 값을 입력 하세요')


numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
    position += 1
else:
    print('No even number found')
print(len(numbers))