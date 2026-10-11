class Book:

    page_material = "бумага"
    text_included = True

    def __init__(self, title, author, pages, isbn, reserved):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved


first_book = Book(
    "Война и мир", "Л. Толстой", 1500, 978 - 5 - 8114 - 4403 - 8, False
    )
second_book = Book(
    "Анна Каренина", "Л. Толстой", 600, 978 - 5 - 8167 - 4403 - 8, False
    )
third_book = Book(
    "Преступление и наказание", "Ф. Достоевский",
    400, 978 - 5 - 8114 - 4412 - 8, True
)
fourth_book = Book(
    "Герой нашего времени", "М. Лермонтов",
    300, 978 - 5 - 7114 - 4421 - 8, False
)
fifth_book = Book(
    "Мастер и Маргарита", "М. Булгаков", 500, 978 - 5 - 8122 - 4430 - 8, False
)


def printing(book):
    print(
        f"Название: {book.title}, Автор: {book.author}, "
        f"страниц: {book.pages}, материал: {Book.page_material}"
        f"{', зарезервирована' if book.reserved is True else ''}"
    )


printing(first_book)
printing(second_book)
printing(third_book)
printing(fourth_book)
printing(fifth_book)
