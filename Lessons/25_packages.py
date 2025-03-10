# import custom_packages.Our_Custom_module
import custom_packages.Our_Custom_module as ocm
from custom_packages.Our_Custom_module import add_two_numbers as add_two ,User
#custom_packages.Our_Custom_module.add_two_numbers(15,20)

#ocm.add_two_numbers(15,20)
add_two(25,60)
print(User.username)
user = User(False)
print(user.is_admin)