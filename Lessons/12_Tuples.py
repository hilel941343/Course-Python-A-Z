# List - mutable ניתן לעשות שינויים
my_list = [1, 2, 3, 4, 5]
print(my_list)
print(id(my_list))
my_list[2] = 10
print(my_list)
print(id(my_list))
#--------------------------------------------------------
# Tuple - Immutable לא ניתן לעשות שינויים

my_tuple = (1, 2, 3, 4, 3)
# print(id(my_tuple))
# # print(my_tuple)
# # print(type(my_tuple))
# # print(my_tuple)
# # print(my_tuple[2])
# # print(my_tuple.count(3))

# print(my_tuple)

# list_from_tuple = list(my_tuple)
# print(list_from_tuple)
# list_from_tuple[-1] = 5
# print(list_from_tuple)

# my_tuple = tuple(list_from_tuple)
# print(my_tuple)
# print(id(my_tuple))