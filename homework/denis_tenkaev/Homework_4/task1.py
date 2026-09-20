my_dict = {"tuple": ("yes", "no", 3, 42, 10) , "list": [4.2, 5, 8, 11, 35, "dog", "cat"
],  "dict": {"fruit":"apple", "animals": "dog", "car": "Toyota", 5: 76, 4.42: "names"
}, "set": {2, 10, "Anna", 5.33, None, "public_key"}}

print(my_dict["tuple"][-1])  # Выводим последний элемент для ключа "tuple"
my_dict["list"].append("mouse")  # Добавляем еще один элемент в конец ключа "list"
my_dict["list"].pop(1)  # Удаляем второй элемент списка
my_dict["dict"]["i am a tuple"] = "mouse"  # Добавляем новый элемент для ключа "dict"
my_dict["dict"].pop("car")  # Удаляем элемент из ключа "dict"
my_dict["set"].add(8)  # Добавляем еще один элемент в ключ "set"
my_dict["set"].pop()  # Удаляем элемент из ключа "set"

print(my_dict)
