class Book:

    page_material = "бумага"
    text_included = True

    def __init__(self, title, author, pages, isbn, reserved):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved


class SchoolBook(Book):
    def __init__(
            self, title, author, pages, isbn,
            reserved, subject, group, exercises):
        super().__init__(title, author, pages, isbn, reserved)
        self.subject = subject
        self.group = group
        self.exercises = exercises


english_book = SchoolBook(
    "Happy English", "Т. Гроттер",
    300, 9785661444038, False, "Английский язык", 5, True
)
math_book = SchoolBook(
    "Теоремы и доказательства", "Евклид",
    400, 9785665431038, True, "Геометрия", 8, False
)
history_book = SchoolBook(
    "История средних веков", "Нестор",
    600, 9785632431038, True, "История", 6, True
)


def printing(book):
    print(
        f"Название: {book.title}, Автор: {book.author}, "
        f"страниц: {book.pages}, предмет: {book.subject}, класс: {book.group}"
        f"{', зарезервирована' if book.reserved is True else ''}"
    )


printing(english_book)
printing(math_book)
printing(history_book)
