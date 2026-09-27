first_sentence = "результат операции: 42"

second_sentence = "результат операции: 54"

third_sentence = "результат работы программы: 209"

fourth_sentence = "результат: 2"

def slicer(sentence):
     print(int(sentence.split()[-1]) + 10)

slicer(first_sentence)
slicer(second_sentence)
slicer(third_sentence)
slicer(fourth_sentence)
