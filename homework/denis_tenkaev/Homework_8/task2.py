def fibo():
    num = 0
    b = 1
    while True:
        yield num
        num, b = b, num + b


def fibo_num(a):
    gen = fibo()
    count = 1
    for x in gen:
        if count == a:
            print(x)
            break
        count += 1


fibo_num(100001)
fibo_num(1001)
fibo_num(201)
fibo_num(6)
