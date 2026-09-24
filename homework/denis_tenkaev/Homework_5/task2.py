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

# Еще один способ вчера в голову пришел, после того как запушил

text = "результат операции: 42"
result = int(text.split()[-1]) + 10
print(result)

text = "результат операции: 514"
result = int(text.split()[-1]) + 10
print(result)

text = "результат работы программы: 9"
result = int(text.split()[-1]) + 10
print(result)
