tuple_ = ('Urban' , 1 , 2 , 3.5)
immutable_var = tuple_
print(immutable_var , type(immutable_var))

tuple_ = ('Urban' , 1 , 2 , 3.5) * 2 #Нельзя изменить неизменяемые объекты кортежа (tuple_). Исключение: сложение\умножение
print(tuple_)

mutable_list = ['Apple' , 22 , 0.5]
print(mutable_list)

mutable_list.extend(['Urban'])
print(mutable_list)

mutable_list .remove(22)
print(mutable_list)

print('Apple' in mutable_list)

