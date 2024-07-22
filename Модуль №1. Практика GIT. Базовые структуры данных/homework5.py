immutable_var = 1, 5, True, 'exit'
print(immutable_var)
#  пункт 3 дз будет комментарием, т.к. иначе выйдет ошибка и коды к следующим заданиям не выведутся на экран
#  из-за ошибки
#  immutable_var[0]=6
#  print(immutable_var)
#  мы не можем изменить кортеж, т.к. это неизменяемая коллекция, но если бы он содержал в себе список, то мы могли бы
#  изменить элемент списка находящегося внутри кортежа
#  например:
example_1 = [1, 2, 3, True], 10, 25, 'exit'
print(example_1)
example_1[0][3] = False
print(example_1)
mutable_list = [14, 36, 'c', True, 'Process']
print(mutable_list)
mutable_list[4] = 'code'
print(mutable_list)
