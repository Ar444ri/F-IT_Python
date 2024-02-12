if __name__ == "__main__":
    class Berry:
        """
            Базовый класс для ягодок
            Атрибуты:
                name (str): Название ягоды.
                color (str): Цвет ягоды.
            """

        def __init__(self, name: str, color: str):
            """
            Конструктор для инициализации атрибутов.Входной аргумент-строковый тип данных
                        """
            self.name = name
            self.color = color

        def taste(self) -> str:
            """
            Метод, возвращающий описание вкуса ягоды.Входной аргумент-строковый тип данных.Возвращает так же строку
            """
            return "Вкусненько!"

        def __str__(self) -> str:
            """
             Метод, возвращающий строковое представление объекта.
             Входной аргумент-строковый тип данных.Возвращает так же строку
                        """
            return f"A {self.color} {self.name}"

        def __repr__(self) -> str:
            """
                        Метод, возвращающий каноническое представление объекта.
                        Входной аргумент-строковый тип данных.Возвращает так же строку
                                   """
            return f"{self.__class__.__name__}(name='{self.name}', color='{self.color}')"


    class Raspberry(Berry):
        """
      Дочерний класс от Berry
      Дополнительный атрибут - размер ягодки
                                         """

        def __init__(self, name: str, color: str, size: str):
            super().__init__(name, color)
            self.size = size

        def taste(self) -> str:  # перегрузка
            return "Вкусненько, но только если там нет жуков-пахучек"


    class Strawberry(Berry):
        """
            Дочерний класс от Berry
            Дополнительный атрибут - размер ягодки
                                               """

        def __init__(self, name: str, color: str, size: str):
            super().__init__(name, color)
            self.size = size

        def taste(self) -> str:  # перегрузка
            return "Очень вкусно"


    """
    Классы Raspberry и Strawberry наследуются от базового класса Berry.
    - Почему использовано: Наследование использовалось для того, 
    чтобы дочерние классы могли наследовать основные атрибуты и методы, 
    определенные в базовом классе Berry. Это позволяет избежать дублирования кода 
    и обеспечить повторное использование функциональности базового класса.
    Метод taste был перегружен в классах Raspberry и Strawberryдля предоставления точного описания
    вкуса каждого вида ягоды (малины и земляники), отличного от общего описания в базовом классе.
    Метод __init__ был унаследован в дочерних классах Raspberry (малина) и Strawberry (земляника) от 
    базового класса Berry.Он позволяет инициализировать общие атрибуты для всех классов и их
    уникальные атрибуты в дочерних классах.
              """
    pass