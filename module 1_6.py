my_dict = {'Katya' : 2000 , 'Dima' : 1999 , 'Sasha' : 1998}
print(my_dict)

print(my_dict.get('Katya'))
print(my_dict.get('Vasya'))

my_dict.update({'Kirill' : 1997 ,
                'Denis' : 2001})
print(my_dict)

del my_dict ['Dima']
print(my_dict)