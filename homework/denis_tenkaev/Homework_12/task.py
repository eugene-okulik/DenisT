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

    def __str__(self):
        return (f"{self.name}: color is {self.color},"
        f"выращен в {self.country},"
        f"price is {self.price}rub, lifetime {self.lifetime} days,"
        f"height {self.height} cm")

    def __repr__(self):
        return self.__str__()


class Tulips(Flower):

    seasonal = True

    def grow(self):
        print("Растет быстро")

    def __str__(self):
        return (f"{self.name}: color is {self.color},"
        f"выращен в {self.country},"
        f"price is {self.price}rub, lifetime {self.lifetime} days,"
        f"height {self.height} cm")

    def __repr__(self):
        return self.__str__()


class WildFlowers(Flower):

    medicinal = True

    def __str__(self):
        return (f"Wild Flower - {self.name}: color is {self.color},"
        f"price is {self.price}rub, lifetime {self.lifetime} days,"
        f" height {self.height} cm")

    def __repr__(self):
        return self.__str__()


spray_rose = Roses("Кустовая роза", "Россия", "orange", 20, 10, 300)
red_tulip = Tulips("Садовый тюльпан", "Беларусь", "red", 18, 11, 250)
white_rose = Roses("Белая роза обыкновенная", "Голландия", "white", 20, 12, 350)
camomile = WildFlowers("Ромашка полевая", "Польша", "white-yellow", 10, 15, 100)
yellow_tulip = Tulips("Желтый тюльпан", "Голландия", "yellow", 15, 10, 200)
yelow_rose = Roses("Желтая роза", "Россия", "yellow", 20, 10, 300)


class Bouquet:

    def __init__(self, flowers):

        self.flowers = flowers
        self.bouquet_cost = sum(flower.price for flower in flowers)

    def ltime(self):
        total_lifetime = sum(flower.lifetime for flower in self.flowers)
        lifetime = total_lifetime / len(self.flowers)
        return lifetime

    def sort(self, param):
        return sorted(self.flowers, key=lambda flower: getattr(flower, param))

    def finder(self, param, value):
        # if param == "color":
        #     result = [flower for flower in self.flowers if flower.color == value]
        #     return result
        # elif param == "lifetime":
        #     result = [flower for flower in self.flowers if flower.lifetime == value]
        #     return result
        # elif param == "height":
        #     result = [flower for flower in self.flowers if flower.height == value]
        #     return result
        # elif param == "price":
        #     result = [flower for flower in self.flowers if flower.price == value]
        #     return result
        # else:
        #     result = []

        result = []
        for flower in self.flowers:
            if getattr(flower, param) == value:
                result.append(flower)
        return result


wedding = Bouquet([spray_rose, red_tulip, white_rose, camomile])

print(wedding.finder("color", "red"))
