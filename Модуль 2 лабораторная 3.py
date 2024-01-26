class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    # по заданию не требуется но можно добавить проверки и в материнский класс,
    # набросок кода ниже

        # if not isinstance(name, str):
        #     raise TypeError("Название книги надо вводить в виде строки")
        # elif name == "":
        #     raise ValueError("Вы не написали название книги")
        # else:
        #     self._name = name
        # if not isinstance(author, str):
        #     raise TypeError("Имя автора надо вводить в виде строки")
        # elif author == "":
        #     raise ValueError("Вы не написали имя автора")
        # else:
        #     self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга - '{self.name}'. Автор - '{self.author}'."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, new_pages):
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно вводиться в цифровом формате int-целочисленное")
        elif new_pages <= 0:
            raise ValueError("Количество страниц не может быть отрицательным или равным нулю")
        else:
            self._pages = new_pages

    def __str__(self):
        return f"{super().__str__()} Количество страниц - {self.pages}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, new_duration):
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность должна вводиться в цифровом формате float-с плавающей точкой")
        elif new_duration <= 0:
            raise ValueError("Продолжительность не может быть отрицательной или равной нулю")
        else:
            self._duration = new_duration

    def __str__(self):
        return f"{super().__str__()} Продолжительность - {self.duration}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"

# код ниже для себя для проверки


if __name__ == "__main__":
    Audio_Book = AudioBook("Хроники Амбера", "Роджер Железны", 9.1)
    print(Audio_Book)
    print(f"{Audio_Book}")
    print(str(Audio_Book))
    print(f"{Audio_Book!r}")
    print(repr(Audio_Book))

    Paper_Book = PaperBook("Хроники Амбера", "Роджер Железны", 185)
    print(Paper_Book)
    print(f"{Paper_Book}")
    print(str(Paper_Book))
    print(f"{Paper_Book!r}")
    print(repr(Paper_Book))

    print(AudioBook.mro())
    print(PaperBook.mro())
