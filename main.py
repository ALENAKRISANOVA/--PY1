class Stuff:
    """Базовый класс для инструментов"""

    def __init__(self, name: str, durability: int):
        """Конструктор объектов класса Stuff"""
        if not isinstance(name, str):
            raise TypeError(f"Имя инструмента должно быть строкой, а не {type(name)}")
        if not isinstance(durability, int):
            raise TypeError(f"Прочность инструмента должна быть целым числом, а не {type(name)}")
        if durability <= 0:
            raise ValueError("Изначальная прочность инструмента должна быть больше 0")
        self._name = name  # атрибут открыт только для чтения так как имя инструмента не надо менять после его иницализации
        self._durability = durability  # атрибут открыт только для чтения так как за изменение прочность ответсвенны
        # соотвествующие методы внутри класса

    # Геттеры (read only атрибуты)
    @property
    def name(self) -> str:
        """Возвращает имя инструмента"""
        return self._name

    @property
    def durability(self) -> int:
        """Возвращает текущую прочность инструмента"""
        return self._durability

    # Методы экземпляров класса
    def __str__(self):
        return f"Инструмент {self.name}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, durability={self.durability})"

    def weapon_break(self) -> None:
        """Метод срабатывающий при поломке инструмента"""
        ...

    def reduce_durability(self) -> None:
        """Метод уменьшающий прочность инструмента после его использования"""
        ...


class HeavyStuff(Stuff):
    """Класс для профессионального инструмента"""

    def __init__(self, name: str, durability: int):
        """Конструктор объектов класса HeavyStuff"""
        super().__init__(name, durability)

    # Методы экземпляров класса
    def __str__(self):
        return f"Профессиональный инструмент {self.name}."

    def reduce_durability(self) -> None:
        """Метод уменьшающий прочность профессионального инструмента после его использования
        (перегружен так как по задумке формулы для расчёта прочности обычного
        и профессионального инструмента различны)"""
        ...


class RangeStuff(Stuff):
    """Класс для буровых инструментов"""

    def __init__(self, name: str, durability: int, distance: int = 0):
        """Конструктор объектов класса RangeStuff"""
        super().__init__(name, durability)
        self.distance = distance  # доступ к атрибуту distance реализуется через сеттер и геттер для уменьшения
        # количества возможных ошибок при взаимодействии с ним

    # Сеттеры и геттеры
    @property
    def distance(self) -> int:
        """Возвращает заданную глубину бурения"""
        return self._distance

    @distance.setter
    def distance(self, new_distance: int) -> None:
        """Устанавливает дистанцю бурения"""
        if not isinstance(new_distance, int):
            raise TypeError("расстояние до цели должно быть целым чисолом")
        if new_distance < 0:
            raise ValueError("расстояние до цели должно быть положительным числом")
        self._distance = new_distance

    # Методы экземпляров класса

    def __str__(self):
        return f"Буровые инструменты {self.name}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, durability={self.durability}, distance={self.distance})"

    def reduce_durability(self) -> None:
        """Метод уменьшающий прочность бурового инструмента после его использования"""
        ...


def main() -> None:
    hammer = Stuff("Hammer", 100)
    jigsaw = HeavyStuff("Jigsaw", 200)
    drill = RangeStuff("Drill", 15)
    print(hammer, jigsaw, drill)
    print(repr(hammer), repr(jigsaw), repr(drill))
    drill.distance = 100
    print(repr(drill))


if __name__ == "__main__":
    # Write your solution here
    main()
    pass
