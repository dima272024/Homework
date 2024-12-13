immutable_var = 1, 2, 'abc', True
print(immutable_var)
#immutable_var[1] = ('kek') # объект "кортеж" не поддерживает назначение элементов
#print(immutable_var)
mutable_list = [5, 10, 'v']
mutable_list[1] = 'Banana'
print(mutable_list)
mutable_list.extend('Kek')
print(mutable_list)


