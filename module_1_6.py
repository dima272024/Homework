my_dict = {'Dima': 1997, 'Kris': 2001, 'Natali': 1995}
print(my_dict)
print(my_dict['Dima'])
my_dict['Baki'] = 2024
print(my_dict.get('Baki'))
my_dict.update({'Liza': 1998,
                'Alex': 2007})
a= my_dict.pop('Natali')
print(a)
print(my_dict)
my_set = {10, 15, 10, 'Dima', 'abc', 'abc', (3,3)}
print(my_set)
my_set.update({25,35})
my_set.discard(15)
print(my_set)





