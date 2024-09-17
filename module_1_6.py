my_dict = {'Alex': 1963, 'Lena': 1967, 'Vera': 1989, 'Lyuda': 1998}
print(my_dict)
print(my_dict['Lyuda'])
my_dict['Stas'] = 2018
print(my_dict['Stas'])
my_dict.update({'Guzenica': 2016,
                'Lucifer': 2019})
a = my_dict.pop('Lena')
print(a)
print(my_dict)

my_set = {'Остеохондродиплазия', 'Остеохондродиплазия','Gaster', 'Gaster', 2012, 2, 0, 1, 2, True}
print(my_set)
my_set.add('k-pop')
my_set.add(66)
my_set.discard(1)
print(my_set)
