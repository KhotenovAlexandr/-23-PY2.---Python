import doctest


class BasketballPlayer:
    """
    Документация на класс.
    Класс описывает модель игрока в баскетбол.
    """
    def __init__(self, name: str,  height: (int, float), age: (int, float)):
        """
        Создание и подготовка к работе объекта "Баскетболист"

        :param height: Рост баскетболиста в сантиметрах
        :param age: Возраст баскетболиста

        Примеры:
        >>> basketball_player = BasketballPlayer("Alex", 196, 30)  # инициализация экземпляра класса

        """
        if not isinstance(name, str):
            raise TypeError("Имя баскетболиста должено быть типа str")
        if not name.isalpha():
            raise ValueError("Имя баскетболиста должено быть написано буквами")
        self.name = name

        if not isinstance(height, (int, float)):
            raise TypeError("Рост баскетболиста должен быть типа int или float")
        if height < 170:
            raise ValueError("Рост баскетболиста  должен быть больше 170 см")
        self.height = height

        if not isinstance(age, (int, float)):
            raise TypeError("Возраст баскетболиста должен быть int или float")
        if 40 < age < 18:
            raise ValueError("Возраст баскетболиста должен быть в диапазоне от 18 до 40 лет")
        self.age = age

    def agetest(self, age: (int, float)) -> bool:
        """
        Функция которая проверяет опытный ли игрок старше 30 лет или нет

        :param age: Возраст баскетболиста

        :raise TypeError: если возраст задан не int или float

        :return: True или False

        Примеры:
        >>> basketball_player = BasketballPlayer("Pit", 196, 33)
        >>> basketball_player.agetest(33)

        """
        ...

    def heighttest(self, height: (int, float)) -> str:
        """
        Проверяет игрок выше 200
        если игрок ниже вызывает ошибку

        :param height: рост баскетболиста

        :raise TypeError: если рост задан не int или float
        :raise ValueError: Игрок не подходит на позицию защитника
        если игрок 200 и выше

        :return: "игрок подходит на позицию защитника"


        Примеры:
        >>> basketball_player = BasketballPlayer("Bred", 170, 25)
        >>> basketball_player.heighttest(200)

        """
        ...

    def nametest(self, listname: list) -> list:
        """
        Проверяет есть ли имя игрока в списках прошлых сезонов
        если есть то ничего не делает
        если нет выводит тескт предупреждения что игрок новенький
        и заносит имя в список новичков

        :param listname: список игроков прошлых сезонов

        :return: список новичков

        Примеры:
        >>> basketball_player = BasketballPlayer("Tom", 220, 37)
        >>> basketball_player.nametest(["Bred", "Zod", "Alex" ])

        """
        ...


class GasTank:
    """
    Документация на класс.
    Класс описывает модель бензобака автомобиля.
    """
    def __init__(self, gas_tank_capacity: float, amount_of_gasoline: float):
        """
        Создание и подготовка к работе объекта "Бензобак"

        :param gas_tank_capacity: Объем бензобака
        :param amount_of_gasoline: количество бензина в баке

        Примеры:
        >>> gas_tank = GasTank(50, 25)  # инициализация экземпляра класса

        """
        if not isinstance(gas_tank_capacity, (int, float)):
            raise TypeError("Объем ,бензобака должен быть типа int или float")
        if gas_tank_capacity <= 0:
            raise ValueError("Объем бензобака должен быть положительным числом")
        self.gas_tank_capacity = gas_tank_capacity

        if not isinstance(amount_of_gasoline, (int, float)):
            raise TypeError("Количество бензина должно быть int или float")
        if amount_of_gasoline < 0:
            raise ValueError("Количество бензина не может быть отрицательным числом")
        self.amount_of_gasoline = amount_of_gasoline

    def empty_gas_tank(self) -> bool:
        """
        Функция которая проверяет является ли стакан пустым

        :return: Является ли стакан пустым True или False

        Примеры:
        >>> gas_tank = GasTank(50, 25)
        >>> gas_tank.empty_gas_tank()

        """
        ...

    def tank(self, petrol: float) -> None:
        """
        Добавление воды в стакан.

        :param petrol: Объем добавляемой бензина

        :raise ValueError: Если количество добавляемой бензина превышает свободное место в баке, то вызываем ошибку

        :return: None

        Примеры:
        >>> gas_tank = GasTank(50, 25)
        >>> gas_tank.tank(15)

        """
        if not isinstance(petrol, (int, float)):
            raise TypeError("Добавляемый бензин должна быть типа int или float")
        if petrol < 0:
            raise ValueError("количество бензина должно положительным числом")
        ...

    def fuel_consumption(self, consumable_gasoline: float) -> float:
        """
        Рассход топлива.

        :param consumable_gasoline: Объем израсходованного бензина

        :raise ValueError: Если количество израсходованного бензина
        превышает количество бензина в баке,
        то возвращается ошибка

        :return: Объем реально израсходованного топлива

        Примеры:
        >>> gas_tank = GasTank(50, 35)
        >>> gas_tank.fuel_consumption(40)
        """
        ...


class MusicAlbum:
    """
    Документация на класс.
    Класс описывает модель музыкального альбома.
    """

    def __init__(self, executor: str, album: list, number_of_songs: int, track_number: int):
        """
        Создание и подготовка к работе объекта музыкальный альбом

        :param executor: имя исполнителя
        :param album: список альбомов исполнителя
        :param number_of_songs: кроличество песен
        :param track_number: номер песни

        Примеры:
        >>> music_album = MusicAlbum("Джексон", ["Луна","Цветы","Свобода"], 20, 5)  # инициализация экземпляра класса

        """
        if not isinstance(executor, str):
            raise TypeError("Имя исполнителя должено быть типа str")
        if not executor.isalpha():
            raise ValueError("Имя имя исполнителя должено быть написано буквами")
        self.executor = executor

        if not isinstance(album, list):
            raise TypeError("Название альбома должено быть типа list")
        self.album = album

        if not isinstance(number_of_songs, int):
            raise TypeError("Количество песен должен быть типа int")
        if number_of_songs < 0:
            raise ValueError("Количество песен не может быть отрицательным")
        self.number_of_songs = number_of_songs

        if not isinstance(track_number, int):
            raise TypeError("Номер песни должен быть типа int")
        if track_number < 0:
            raise ValueError("Номер песни не может быть отрицательным")
        self.track_number = track_number

    def listen_to_music(self, track_number: int) -> None:
        """
        Метод увеличивает последнюю прослушанную песню.

        :param track_number: Количество прослeшенных треков

        Примеры:
        >>> music_album = MusicAlbum("Джексон", ["Луна","Цветы","Свобода"], 20, 5)  # инициализация экземпляра класса
        >>> music_album.listen_to_music(6)

        """
        if not isinstance(track_number, int):  # проверяем, что прослушаные пести типа int
            raise TypeError("Прослушанные песни должны быть типа int")  # вызываем ошибку

        if track_number < 0:
            raise ValueError("Прослушанные песни должны быть положительным числом")

        # и только после всех проверок
        self.track_number += track_number

    def random(self) -> str:
        """
        Случайным образом выбирает альбом исполнителя
        параметры не принимает

        Примеры:
        >>> music_album = MusicAlbum("Джексон", ["Луна","Цветы","Свобода"], 20, 5)  # инициализация экземпляра класса
        >>> music_album.random()

        :return: название альбома в виде строки
        """


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации