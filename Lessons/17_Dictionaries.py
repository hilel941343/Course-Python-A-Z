#במילון אין אפשרות לעשות שינויים -Immmutable
hillel_info = {
    "name":"Hillel",
    "age": 24,
    "my_languages":{
        "first": "java"
    },
    "grades":80.5,
    # 80: "karmiel",
    # 105.6: "coord",
    # ("name" "last_name"):["Hillel", "Touitou"],
    # "name":"Hilleltouitou"
}

# print(hillel_info["name"])
# print(hillel_info.keys())
# print(hillel_info.values())
# print(list(hillel_info.items())[0])
# print(hillel_info)

# print(hillel_info.get("grades"))
# print(hillel_info["grades"])
print(hillel_info)
hillel_info.update({"has_car": True})
hillel_info["father"] =" victor"
hillel_info["car"] = hillel_info.pop("has_car")
print(hillel_info)