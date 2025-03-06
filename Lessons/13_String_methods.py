text = "HeLLo world and HILLEL!"
# print(text)
# print(text[2])
# print(text[0:7])
# print(text[0:12:2])
# print(text[::-1])
# text[2] = "E" #TypeError: 'str' object does not support item assignment
print(text)
print(text.capitalize())
print(text.title())
print(text.upper())
print(text.lower())
print(text)

text_from_web = "Name\t\nId\t\nDate"
print(text_from_web)
formated_text = text_from_web.replace("\t\n" , ',')
print(formated_text)
print(type(formated_text))

list_from_string = formated_text.split(",")
print(list_from_string)
print(list_from_string[2])

new_string = " | ".join(list_from_string)
print(new_string)
print(type(new_string))

#אתר ללמידה:https://www.w3schools.com/python/python_ref_string.asp