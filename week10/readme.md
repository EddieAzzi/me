TODO: Reflect on what you learned this week and what is still unclear.

list comprehensions

lambdas 
e.g. 
def get_2x_len(my_string):
    return len(my_string) * 2
print (list(map(get_2x_len, pets)))

^^^ writing as lambda (anonymous function: used and thrown away) ^^^
print (list(map(lambda x: len(x) * 2, pets)))
# print(map(lambda x: x[1], pets))

print(list(map(len, pets)))

Built ins
from random import randint
my_odd_list = [randint(0,100) for _ in range(1000)]

max(my_odd_list)

min(my_old_list)

list(zip(range(len(pets)), pets))

numerate
for p in enumerate(pets):
    print(p)

generators
