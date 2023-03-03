class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"
    @property
    def name(self):
        return self._name
    @property
    def author(self):
        return self._author

class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self._pages}"

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages):
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise TypeError("Количество страниц должно быть положительным числом")
        self._pages = pages





class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Длительность {self._duration}"

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        if not isinstance(duration, (int, float)):
            raise TypeError("Длительность должна быть типа float")
        if duration <= 0:
            raise TypeError("Длительность должна быть положительным числом")
        self._duration = duration