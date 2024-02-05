class Animal:
    """
    Базовый класс, представляющий животное.
    """
    def __init__(self, name: str, weight: float, age: int, habitat: str, squad: str):
        """
        Конструктор класса Animal.

        Параметры:
        - name: str - кличка животного
        - weight: float - вес животного в кг
        - age: int - возраст животного полных лет
        - habitat: str - среда обитания животного
        - squad: str - отряд животного
        """
        self.name = name
        self._weight = weight
        # непубличный, сделаю сделаю метод проверки
        self._age = age
        # непубличный, сделаю сделаю метод проверки
        self.habitat = habitat
        self.squad = squad

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, new_weight):
        if not isinstance(new_weight, float):
            raise TypeError
        elif new_weight <= 0.0:
            raise ValueError
        else:
            self._weight = new_weight

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if not isinstance(new_age, int):
            raise TypeError
        elif new_age <= 0:
            raise ValueError
        else:
            self._age = new_age

    def next_weight_and_age(self, new_weight: float, new_age: int):
        """
        Метод для записи веса и возраста животного.

        Параметры:
        - new_weight: float - новый вес животного в кг
        - new_age: int - новый возраст животного полных лет
        """
        if isinstance(new_age, int) and isinstance(new_weight, float):
            if new_weight > 0 and new_age > 0:
                self._weight = new_weight
                self._age = new_age
            else:
                raise ValueError
        else:
            raise TypeError

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Animal.

        Возвращаемое значение:
        str - строка с информацией о животном
        """
        return (f"\nКличка животного - {self.name}; "
                f"Вес - {self.weight} килограмм(a); "
                f"Возраст - {self.age} года(лет); "
                f"Среда обитания - {self.habitat}; "
                f"Отряд - {self.squad}; ")

    def __repr__(self) -> str:
        """
        Возвращает представление объекта Animal.

        Возвращаемое значение:
        str - строка с кодом, создающим объект Animal
        """
        return f"{self.__class__.__name__}(" \
               f"name={self.name!r}, " \
               f"weight={self.weight!r}, " \
               f"age={self.age!r}, " \
               f"habitat={self.habitat!r}, " \
               f"squad={self.squad!r})"


class Elephant(Animal):
    """
    Животное - Слон.
    """
    def __init__(self, name: str, weight: float, age: int, habitat: str, squad: str, color: str, subspecies: str,
                 trunk_length: float, tusk_length: int):
        """
        Конструктор класса Elephant.

        Параметры:
        - name: str - имя животного
        - weight: float - вес животного в кг
        - age: int - возраст животного полных лет
        - habitat: str - среда обитания животного
        - squad: str - отряд животного
        - color: str - окрас животного
        - subspecies: str - подвид животного
        - trunk_length: float - длина хобота в метрах
        - tusk_length: int - длина бивня в сантиметрах
        """
        super().__init__(name, weight, age, habitat, squad)
        self.color = color
        self.subspecies = subspecies
        self._trunk_length = trunk_length
        # непубличный, сделаю сделаю метод проверки
        self._tusk_length = tusk_length
        # непубличный, сделаю сделаю метод проверки

    @property
    def tusk_length(self):
        return self._tusk_length

    @tusk_length.setter
    def tusk_length(self, new_tusk_length):
        if not isinstance(new_tusk_length, int):
            raise TypeError
        elif new_tusk_length < 0:
            raise ValueError
        else:
            self._tusk_length = new_tusk_length

    @property
    def trunk_length(self):
        return self._trunk_length

    @trunk_length.setter
    def trunk_length(self, new_trunk_length):
        if not isinstance(new_trunk_length, float):
            raise TypeError
        elif new_trunk_length < 0.0:
            raise ValueError
        else:
            self._trunk_length = new_trunk_length

    def next_weight_and_age_and_trunk_length_and_tusk_length(self, new_weight: float, new_age: int,
                                                             new_trunk_length: float, new_tusk_length: int):
        """
        Перегружаем метод для записи веса и возраста животного next_weight_and_age,
        и расширяем его функционал для записи длины хобота и бивня.

        Параметры:
        - new_weight: float - новый вес животного в кг
        - new_age: int - новый возраст животного полных лет
        - trunk_length: float - новый длина хобота в метрах
        - tusk_length: int - новый длина бивня в сантиметрах
        """
        super().next_weight_and_age(new_weight, new_age)
        # что бы не повторятся, перегружаю метод с базового класса
        if isinstance(new_age, int) and isinstance(new_trunk_length, float):
            if new_trunk_length > 0 and new_tusk_length > 0:
                self.trunk_length = new_trunk_length
                self._tusk_length = new_tusk_length
            else:
                raise ValueError
        else:
            raise TypeError

    def __str__(self):
        """
        Возвращает строковое представление объекта Elephant

        Возвращаемое значение:
        str - строка с информацией о животном
        """
        return f"{super().__str__()}\n"\
               f"Окрас - {self.color}; Подвид - {self.subspecies}; "\
               f"Длина хобота - {self.trunk_length} метра.; " \
               f"Длина бивня - {self.tusk_length} сантиметров; "

    def __repr__(self):
        """
        Возвращает представление объекта Elephant.

        Возвращаемое значение:
        str - строка с кодом, создающим объект Elephant
        """
        return f"{self.__class__.__name__}(" \
               f"name={self.name!r}, " \
               f"weight={self.weight!r}, " \
               f"age={self.age!r}, " \
               f"habitat={self.habitat!r}, " \
               f"squad={self.squad!r}, " \
               f"color={self.color!r}, " \
               f"subspecies={self.subspecies!r}, " \
               f"trunk_length={self.trunk_length!r}, " \
               f"tusk_length={self.tusk_length!r})"


if __name__ == "__main__":
    animal = Animal(name='Тоби', weight=3.5, age=5, habitat='Пустыня', squad='Насекомоядные')
    print(str(animal))
    print(repr(animal))
    animal.next_weight_and_age(3.6, 6)
    print(str(animal))
    print(repr(animal))

    elephant = Elephant(name='Гора', weight=1545.5, age=5, habitat='Савана', squad='Хоботовые',
                        color='Серый', subspecies='Африканский слон', trunk_length=1.7, tusk_length=120)
    print(str(elephant))
    print(repr(elephant))
    elephant.next_weight_and_age_and_trunk_length_and_tusk_length(1580.8, 7, 1.8, 130)
    print(str(elephant))
    print(repr(elephant))
