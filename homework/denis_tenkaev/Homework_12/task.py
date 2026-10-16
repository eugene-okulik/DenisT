from abc import abstractmethod


class Flower:

    leaves = True
    petals = True

    def __init__(self, name, country, color, height, lifetime, price):
        self.name = name
        self.country = country
        self.__color = color
        self.__height = height
        self.__lifetime = lifetime
        self.__price = price

    @abstractmethod
    def grow(self):
        pass

    @property
    def color(self):
        return self.__color

    @property
    def height(self):
        return self.__height

    @property
    def lifetime(self):
        return self.__lifetime

    @property
    def price(self):
        return self.__price


class Roses(Flower):

    thorns = True

    def grow(self):
        print("растет медленно")


class Tulips(Flower):

    seasonal = True

    def grow(self):
        print("Растет быстро")


class WildFlowers(Flower):

    medicinal = True


spray_rose = Roses("Кустовая роза", "Россия", "orange", 20, 10, 300)
red_tulip = Tulips("Садовый тюльпан", "Беларусь", "red", 18, 11, 250)
white_rose = Roses("Белая роза обыкновенная", "Голландия", "white", 20, 12, 350)
camomile = WildFlowers("Ромашка полевая", "Польша", "white-yellow", 10, 15, 100)


class Bouquet:

    def __init__(self, flowers):

        self.flowers = flowers
        self.bouquet_cost = sum(flower.price for flower in flowers)

    def ltime(self):
        total_lifetime = sum(flower.lifetime for flower in self.flowers)
        lifetime = total_lifetime / len(self.flowers)
        return print(f" Время увядания составит {lifetime: .0f} дней")


wedding = Bouquet([spray_rose, red_tulip, white_rose])
print(wedding.bouquet_cost)
wedding.ltime()
