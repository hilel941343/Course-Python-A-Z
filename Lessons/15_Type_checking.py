value = True
#טייפ  משייך את הקלאסיפיקציה של המשתנה - הדרך הכי נכונה ומדוייקת לבדוק ערך של משתנה
if type(value) is str :
    print("The value is string")
elif type(value) is int:
    print("The value is integer")
elif type(value) is bool:
    print("The value is boolean")
elif type(value) is list:
    print("The value is list")
else:
    print("The value is unkown type!")

#אינסטנס מחזיר את הסאב קלאס  לדוגמא עבור ערך בולייני יחזיר מספר שלם! מכיוון שנכון  זה 1 ולא נכון זה 0
if isinstance(value,str):
    print("The value is string")
elif isinstance(value,int):
    print("The value is integer")
elif isinstance(value,bool):
    print("The value is boolean")
elif isinstance(value,list):
    print("The value is list")
else:
    print("The value is unkown type!")