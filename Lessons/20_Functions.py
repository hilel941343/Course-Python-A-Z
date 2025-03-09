import random

#______________________________________________________________________________________

######### Simple functions without param 
# def print_hello_world():
#     print("Hello, World!!")

# print_hello_world()
# print_hello_world()

#______________________________________________________________________________________
########### Function with param

# def print_greeting(name: str):
#     print(f"Hello ,{name.upper()}")

# print_greeting("Hillel")
# print_greeting(123)    #AttributeError: 'int' object has no attribute 'upper'


#______________________________________________________________________________________

####### Function with params and with return

# def sum_two_numbers(number_1:int , number_2 : int):
#     return number_1 + number_2
 
# def increase_and_print_result(result:int):
#     print(f"Increased Result is = {result + 1}")

# regular_result = sum_two_numbers(5,10)
# print(regular_result)

# increase_and_print_result(regular_result)


#______________________________________________________________________________________

#################### Fonctions only with return

# def generate_random_number():
#     return random.randint(0, 1000000)

# print(generate_random_number())


#______________________________________________________________________________________
################### Functions with default params and changing order


# def print_worker_bonus(name:str , bonus :int = 3000):
#     print(f"worker {name.upper()} is going to get bonus of {bonus}!")
# print_worker_bonus("Hillel",6000)
# print_worker_bonus("Omry", 4000)
# print_worker_bonus(bonus = 10000, name = "Yan")


#______________________________________________________________________________________
################### Functions with *args
# names = ["Alex", "Yan","Omry"]

# def print_list_of_names(list_of_names : list):
#     print(type(list_of_names))
#     list_of_names[-1] = "OMRY"
#     print(list_of_names)
# print_list_of_names(names)

# def print_tuple_of_names(*list_of_names : str):
#     print(type(list_of_names))
#     print(list_of_names)

# print_tuple_of_names("Alex", "Yan","Omry","david")



#______________________________________________________________________________________
################### Functions with **kwargs

def print_kwargs(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print(kwargs.items())
print_kwargs(name = "Hillel" , age = 35 ,is_working = True)