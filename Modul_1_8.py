my_dict={'Маша':2001, "Вика":2005, "Артур Леонидович":1976, "Кирилл":2000}
print('dict:', my_dict)
print('Год рождениея:',my_dict['Вика'])
print(my_dict.get('Андрей'))
my_dict.update({"Андрей":2005,"Алексей":2003})
del my_dict['Артур Леонидович']
print('dict:', my_dict)
print(my_dict.keys())
print(my_dict.values())
my_set={1,2,102,"test",102,'good day',4,2}
print(my_set)
print(my_set.add(12))
print(my_set.add('как добавить больше одного элемента?'))
print(my_set.add((1,2,3)))
print(my_set.discard(102))
print(my_set)

