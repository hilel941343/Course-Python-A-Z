# names = ["Alex","Ilay","David","Omri"]
# for name in names:
#     print(f"Good evening,{name}!")

# for item in range(1,20):
#     if item == 15:
#         print(f"I'm number {item} inside 'break' block")
#         break
#     if item % 2 != 0:
#         continue
#     print(item)
# print("After for loop")
# for letter in "Hello World":
#     print(letter, end = " | ")

# names = ["Alex","Ilay","David","Omri"]

names_tuple =("Alex","Ilay","David","Yan","Omri")
for name in names_tuple:
    if name == "Yana":
        print("Test was passed as well")
        break
    print(name)
else:
    print("The exepted name was not found!")

