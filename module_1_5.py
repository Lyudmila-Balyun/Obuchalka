# поменяла задания местами, чтобы в одном коде все примеры и комментарии написать
mutable_list = ['борщ:', 'капуста', 'болгарский перец', 'помидоры']
print(mutable_list)
mutable_list[2] = 'свекла'
mutable_list[3] = 'томатная паста' # не поняла, как в одной строке заменить 2 значения, чтобы не писать двумя строками
print(mutable_list)
immutable_var = 'марганцовка', 47, 36.6, True
print(immutable_var)
immutable_var[0] = 'хлоргексидин' #TypeError: 'tuple' object does not support item assignment = объект 'tuple' не поддерживает назначение элементов
