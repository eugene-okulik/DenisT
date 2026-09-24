text = "результат операции: 42"
index = (text.find(':')) + 1
result = int(text[index:]) + 10
print(result)

text = "результат операции: 514"
index = (text.find(':')) + 1
result = int(text[index:]) + 10
print(result)

text = "результат работы программы: 9"
index = (text.find(':')) + 1
result = int(text[index:]) + 10
print(result)
