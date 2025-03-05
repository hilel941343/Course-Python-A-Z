# # name = input("Please enter your name: ")

# # print(f" Hello, {name}")

number_1 = int(input("Please enter number 1: "))
number_2 = float(input("Please enter number 2: "))
Result = number_1 + number_2
print (f"Result : {Result}")

print(type(Result))

result_string = str(Result)
print(type(result_string))

#print(int("ABC")) # ValueError: invalid literal for int() with base 10: 'ABC'