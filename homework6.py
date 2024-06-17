my_dict = {'Dmitry' : 8800123456789, 'Mary' : 8800987654321}
print(my_dict)
print (my_dict['Mary'])
print (my_dict.get('Alex', 'Такого ключа нет'))
my_dict.update({'Peter' : 8800789456123,
                 'Jek' : 8800321654987})
print(my_dict)
b = my_dict.pop('Mary')
print(b)
print(my_dict)
my_set = {1, 1, 2, 2, 'String', True , (7,8,9)}
print(my_set)
print(my_set.add(5))
print(my_set.add(6))
print(my_set)
print(my_set.discard(6))
print(my_set)
