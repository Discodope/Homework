my_dict = {'Dasha' : 1993 , 'Vanya' : 2002 , 'Dima' : 1999}
print(my_dict
      )
print(my_dict.get('Dima'))

print(my_dict.get('A'))

my_dict.update({'Lena' : 2000 , 'Vasya' : 1997})
print(my_dict)

del my_dict['Vanya']
print(my_dict)

my_set = {1 , 2 , 2 , 3, 5, 4 , 5}
set_ = my_set
print(my_set)

my_set.add({77 , 77 , 0.5})
print(my_set)

my_set.discard(77)
print(my_set)
