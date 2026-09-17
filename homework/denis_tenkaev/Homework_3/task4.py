length1 = float(input("Введите длину первого катета: "))
length2 = float(input("Введите длину второго катета: "))

square = (length1 * length2)/2
length_g = (length1 ** 2 + length2 ** 2) ** 0.5
print(f"Площадь треугольника равна {square:g}, гипотенуза равна {length_g:g}")
