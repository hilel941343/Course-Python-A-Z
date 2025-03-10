# import Custom_module 
# import Custom_module as cm

from Custom_module import add_two_numbers,User as U

# Custom_module.add_two_numbers(5,10)
# print(Custom_module.basic_url)
# print(Custom_module.User.username)
# user = Custom_module.User(True)
# print(user.is_admin)

# cm.add_two_numbers(5,10)
# print(cm.basic_url)
# print(cm.User.username)
# user = cm.User(True)
# print(user.is_admin)

add_two_numbers(5,10)
user = U(True)
print(U.username)
print(user.is_admin)