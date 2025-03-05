class Book:
    def __init__(self, book_name, author, num_pages, isbn):
        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.is_reserved = False  # Флаг резервации
        self.reserved_by = None   # Кто зарезервировал книгу
        self.is_borrowed = False  # Флаг выдачи книги
        self.borrowed_by = None   # Кто взял книгу

    def reserve(self, reader):
        """Резервирование книги."""
        if self.is_borrowed:
            print(
                f"Книга '{self.book_name}' уже выдана. "
                "Невозможно зарезервировать."
            )

        elif self.is_reserved:
            print(
                f"Книга '{self.book_name}' уже зарезервирована. "
                "Невозможно зарезервировать."
            )

        else:
            self.is_reserved = True
            self.reserved_by = reader
            print(
                f"Книга '{self.book_name}' зарезервирована для {reader.name}."
            )

    def cancel_reserve(self, reader):
        """Отмена резервации книги."""
        if self.is_reserved and self.reserved_by == reader:
            self.is_reserved = False
            self.reserved_by = None
            print(
                f"Резервация книги '{self.book_name}' отменена для {reader.name}."
            )
        else:
            print(
                f"Резервация книги '{self.book_name}' не может быть отменена "
                f"для {reader.name}."
            )

    def get_book(self, reader):
        """Выдача книги."""
        if self.is_borrowed:
            print(
                f"Книга '{self.book_name}' уже выдана. Невозможно выдать."
            )
        elif self.is_reserved and self.reserved_by != reader:
            print(
                f"Книга '{self.book_name}' зарезервирована другим пользователем. "
                "Невозможно выдать."
            )
        else:
            self.is_borrowed = True
            self.borrowed_by = reader
            self.is_reserved = False  # Снимаем резервацию при выдаче
            self.reserved_by = None
            print(
                f"Книга '{self.book_name}' выдана {reader.name}."
            )

    def return_book(self, reader):
        """Возврат книги."""
        if self.is_borrowed and self.borrowed_by == reader:
            self.is_borrowed = False
            self.borrowed_by = None
            print(
                f"Книга '{self.book_name}' возвращена {reader.name}."
            )
        else:
            print(
                f"Книга '{self.book_name}' не может быть возвращена {reader.name}."
            )


class Reader:
    def __init__(self, name):
        self.name = name

    def reserve_book(self, book):
        """Резервирование книги читателем."""
        book.reserve(self)

    def cancel_reserve(self, book):
        """Отмена резервации книги читателем."""
        book.cancel_reserve(self)

    def get_book(self, book):
        """Получение книги читателем."""
        book.get_book(self)

    def return_book(self, book):
        """Возврат книги читателем."""
        book.return_book(self)


# Пример
book = Book(
    book_name="The Hobbit",
    author="J.R.R. Tolkien",
    num_pages=400,
    isbn="0006754023"
)

vasya = Reader("Vasya")
petya = Reader("Petya")

vasya.reserve_book(book)
petya.reserve_book(book)

vasya.cancel_reserve(book)

petya.reserve_book(book)
vasya.get_book(book)

petya.get_book(book)
vasya.return_book(book)

petya.return_book(book)

vasya.get_book(book)
