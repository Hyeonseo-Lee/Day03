

subjects = ' $ python, data structure, database      $$$'
print(subjects.find('data'), subjects.index('data'))
print(subjects.find('help')) # -1로 표현
print(subjects.index('help')) # Error가 뜸
print(subjects.rfind('data'), subjects.rindex('data'))
print(subjects.count('a'))



subjects = ' $  python, data structure, databse    '
print(subjects.strip('$'))

inha = 'a duck goes into a sea'
print(inha.replace('a ', 'a nice'))
pokemons_list = ['피카츄', '꼬부기', '이상해', '파이리']
pokemons_string = '/'.join(pokemons_list)
print(pokemons_string)
univ = 'Inha University'
print(univ.split('i'))
print(len(univ))
print(univ[::2])
print(univ[5:])
print(univ[5:15])
print(univ[-10:])