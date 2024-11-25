class Vehicle: # транспорт
    __COLOR_VARIANTS = ['pink', 'blue', 'green', 'black', 'white', 'yellow']  # Допустимые цвета

    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        self.owner = owner  # Владелец транспорта
        self.__model = model  # Модель транспорта
        self.__engine_power = engine_power  # Мощность двигателя
        self.__color = color  # Цвет транспорта

    def get_model(self) -> str: # модель
        return f"Модель: {self.__model}"

    def get_horsepower(self) -> str: # мощность
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self) -> str: # цвет
        return f"Цвет: {self.__color}"

    def print_info(self): # результат методов и владелец
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color: str): # Проверка цвета без учета регистра
        if new_color.lower() in (color.lower() for color in self.__COLOR_VARIANTS):
            self.__color = new_color.lower()  # Меняем цвет на новый
        else:
            print(f"Нельзя сменить цвет на {new_color}") # нет в списке


class Sedan(Vehicle): # наследник класса Vehicle
    __PASSENGERS_LIMIT = 5  # количество пассажиров

    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        super().__init__(owner, model, color, engine_power)


print('Информация о машине и владельце')
vehicle1 = Sedan('Fedor', 'Toyota Mark II', 'pink', 400)
vehicle1.print_info()  # Изначальные свойства

print('попытки скрыть следы аварии')
vehicle1.set_color('red')  # Попытка установить недопустимый цвет
vehicle1.set_color('BLUE')  # Установка допустимого цвета
print('Фёдор продал Ваську машину')
vehicle1.owner = 'Vasyok'  # Изменение владельца
vehicle1.print_info()