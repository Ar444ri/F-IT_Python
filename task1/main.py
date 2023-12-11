# TODO Написать 3 класса с документацией и аннотацией типов

import doctest


class Kitten:
    def __init__(self, lengthOfTheClaws: float, amountOfFoodEaten: float):
        """
        Создание и подготовка к работе объекта "Котёночек"
        :param lengthOfTheClaws: Длина коготочков нашего котика в сантиметрах
        :param amountOfFoodEaten: Количество пакетиков жидкого корма который съел малыш за день
        Примеры:
        >>> kitty = Kitten(0.9,4) # инициализация экземпляра класса
        """
        if not isinstance(lengthOfTheClaws, (int, float)):
            raise TypeError("Длина коготков котёнка должна быть типа int или float")
        if lengthOfTheClaws <= 0.5:
            raise ValueError("Нельзя так коротко стричь лапки . Ему больно !!!")
        if lengthOfTheClaws >= 1.5:
            raise ValueError("Бегом стричь !!!")
        self.lengthOfTheClaws = lengthOfTheClaws

        if not isinstance(amountOfFoodEaten, (int, float)):
            raise TypeError("Количество пачек корма должно быть int или float")
        if amountOfFoodEaten < 0:
            raise ValueError("Ну вы чего дите голодом морите(.Сами поели, а для него жалко?")
        if amountOfFoodEaten > 7:
            raise ValueError("Он сейчас лопнет")

        self.amountOfFoodEaten = amountOfFoodEaten

    def IsKittyHungry(self) -> bool:
        """
        Функция которая проверяет голодный ли котёночек
        :return: Является ли котенок голодным

        Примеры:
        >>> kitty = Kitten(0.9, 3)
        >>> kitty.IsKittyHungry()
        """
        ...

    @staticmethod
    def FeedingAKitten(food: float) -> None:
        """
        Кормление котёночка кормом. :param food: Количество пакетиков с кормом :raise ValueError: Если сумма
        добавленных пакетиков корма и уже имеющихся больше 6, то вызываем ошибку,чтобы котику не стало плохо Примеры:
        >>> kitty = Kitten(0.9, 1)
        >>> kitty.FeedingAKitten(2)
        """
        if not isinstance(food, (int, float)):
            raise TypeError("Добавляемый корм должен быть типа int или float")
        if food < 0:
            raise ValueError("Добавлять целых 0 пачек корма это конечно щедрость невиданная")
        ...

    def CuttingClaws(self, CutOffLength: float) -> None:
        """
        Стрижка коготков котеночка.
        :param CutOffLength: длина отрезанной части
        :raise ValueError:Если длина отрезанной части составляет больше
        50% от коготка, вызываем ошибку, чтобы не травмировать кису
        :return: Длина действительно отрезанной части коготка

        Примеры:
        >>> kitty = Kitten(0.9, 1)
        >>> kitty.CuttingClaws(0.3)
        """
        ...


class Flower:
    def __init__(self, height: float, numberOfLeaves: int):
        """
        Создание и подготовка к работе объекта "Стакан"

        :param height: высота цветочка в сантиметрах
        :param numberOfLeaves: количество листиков на стебельке

        Примеры:
        >>> rose = Flower(50, 20)  # инициализация экземпляра класса
        """
        if not isinstance(height, (int, float)):
            raise TypeError("Высота цветка должна быть типа int или float")
        if height <= 0:
            raise ValueError("Отрицательный рост может быть только в экономике. А я не экономика - я цветочек !")
        self.height = height

        if not isinstance(numberOfLeaves, int):
            raise TypeError("Количество листиков должно быть int ")
        if numberOfLeaves < 0:
            raise ValueError("Количество листиков  не может быть отрицательным числом")
        self.numberOfLeaves = numberOfLeaves

    def FlowerHasLeaves(self) -> bool:
        """
        Функция которая проверяет есть ли у цветочка листики
        :return: Является ли стебелек голым
        Примеры:
        >>> orchid = Flower(20, 5)
        >>> orchid.FlowerHasLeaves()
        """
        ...

    @staticmethod
    def CutTheStem(stemLenght: float) -> None:
        """
        Обрезка стебелька.
        :param stemLenght: длина отрезаемой части

        :raise ValueError: Если количество добавляемой жидкости превышает 90% от длины стебля, то вызываем ошибку

        Примеры:
        >>> pion = Flower(40, 17)
        >>> pion.CutTheStem(10)
        """
        if not isinstance(stemLenght, (int, float)):
            raise TypeError("Отрезаемая длина должна быть типа int или float")
        if stemLenght < 0:
            raise ValueError("Отрезаемая длина  должна быть  положительным числом")
        ...

    def TearingOffTheLeaves(self, numberOfSevered: int) -> None:
        """
        Отрывание листочков.

        :param numberOfSevered: Количество отрываемых листиков
        :raise ValueError: Если количество отрываемых листиков превышает количество листочков на цветочке,
        то возвращается ошибка.

        :return: количество действительно оторванных листочков

        Примеры:
        >>> alstroemeria = Flower(47, 25)
        >>> alstroemeria.TearingOffTheLeaves(7)
        """
        ...



class Elvinka:
    def __init__(self, scoreForHomework: float, levelOfJoy: int):
        """
        Создание и подготовка к работе объекта "Эльвинка"

        :param scoreForHomework: баллы по 10 бальной шкале, которые получит Эльвина за выполнение лабораторной работы
        :param levelOfJoy: количество радости испытываемое Эльвинкой в процентах

        Примеры:
        >>> Elvinochka = Elvinka(10, 80)  # инициализация экземпляра класса
        """
        if not isinstance(scoreForHomework, (int, float)):
            raise TypeError("Оценка должна быть типа int или float")
        if scoreForHomework <= 8:
            raise ValueError("Вы ошиблись оценочкой")
        self.capacity_volume = scoreForHomework

        if not isinstance(levelOfJoy, int):
            raise TypeError("Уровень радости должен быть типа int ")
        if levelOfJoy < 0:
            raise ValueError("Радость может отсутствовать , но отрицательной быть "
                             "не может - это уже называется грустью")
        if levelOfJoy > 100:
            raise ValueError("У нас есть всего 100%")
        self.levelOfJoy = levelOfJoy

    def ElvinkaHasScore(self) -> bool:
        """
        Функция которая проверяет есть ли у Эльвинки хоть какая-то оценка
        :return: Существует ли оценка
        Примеры:
        >>> Elvinochka = Elvinka(10, 70)
        >>> Elvinochka.ElvinkaHasScore()
        """
        ...

    @staticmethod
    def GiveJoy(joy: int) -> None:
        """
        Дарим радость Эльвинке.
        :param joy: количество подарреного счастья

        :raise ValueError: Если количество подаренной радости <=0 или сумма подаренной и имеющейся больше 100, то вызываем ошибку
        return: возвращает сумму полученной и имеющейся
        Примеры:
        >>> Elvinochka = Elvinka(10, 92)
        >>> Elvinochka.GiveJoy(8)
        """
        if not isinstance(joy, int):
            raise TypeError("Количество подаренной радости должно  быть типа int")
        if joy < 0:
            raise ValueError("Мы тут радость дарим, а не грусть, поэтому ,пожалуйста, введите положительное число")
        ...

    @staticmethod
    def ChekingHomework(score: int) -> None:
        """
        Оценка за домашнюю работу.

        :param score: баллы за лабораторную работу
        :raise ValueError: Если баллы больше 10 и меньше 9,
        то возвращается ошибка.

        :return: возвращается оценка

        Примеры:
        >>> Elvinochka = Elvinka(10, 92)
        >>> Elvinochka.ChekingHomework(10)
        """
        if not isinstance(score, int):
            raise TypeError("Баллы должны  быть типа int")
        if score <= 8:
            raise ValueError("Есть ощущение, что оценка выставлена неправильно")
        if score > 10:
            raise ValueError("Я конечно умничка, но у нас к сожалению всего 10 баллов. "
                             "Если хотите поставить мне 11, то предлагаю поставить 10 и купить шоколадку...")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
