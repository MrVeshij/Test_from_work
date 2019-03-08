from tkinter import *


class AppCalc(Frame):
    """Основной класс приложения, включает в себя следующие методы:
    create_widgets - Отвечает за создание виджетов приложения
    calculation - Логика расчетов
    command_calc - Логика работы кнопки
    main - Метод проверки корректности ввода и преобразования ввода"""


    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        """Создание виджетов для взаимодействия"""
        Label(self,
              text = 'Введите через пробел координаты точек.'
              ).grid(row = 0, column = 0, sticky = W)
        self.numbers = Entry(self)
        self.numbers.grid(row=1, column=0, sticky=W)
        self.info = Text(self, width = 15, height = 3, wrap = WORD)
        self.info.grid(row = 7, column = 0, sticky = W)
        Button(self,
               text = 'Результат',
               command = self.command_calc
                   ).grid(row = 6, column = 0, sticky = W)


    def calculation(self, numbers):
        points_x = numbers[::2]
        points_y = list(set(numbers).difference(set(points_x)))
        list_x = []
        list_y = []
        while points_x:
            x = (min(points_x) + max(points_x))/2
            points_x.remove(min(points_x))
            points_x.remove(max(points_x))
            list_x.append(x)

        while points_y:
            y = (min(points_y) + max(points_y)) / 2
            points_y.remove(min(points_y))
            points_y.remove(max(points_y))
            list_y.append(y)

        if sum(list_x)/len(list_x) == list_x[0]:
            print('Yes')
            return 'Yes'
        elif sum(list_y)/len(list_y) == list_y[0]:
            print('Yes')
            return 'Yes'
        else:
            print('No')
            return 'No'


    def command_calc(self):
        numbers = self.numbers.get()
        info = self.main(numbers)
        self.info.delete(0.0, END)
        self.info.insert(0.0, info)


    def main(self, numbers=None):
        if not numbers:
            numbers = input('Введите координаты точек')
        numbers = [float(i) for i in numbers.split(' ')]
        amount_numbers = len(numbers)
        if amount_numbers % 2 != 0 or amount_numbers in range(2,1000,4):
            print('Укажите четное количество точек.')
            return 'Укажите четное количество точек.'
        else:
            return self.calculation(numbers)


def main_app():
    """Запуск приложения"""
    root = Tk()
    root.title('Поиск прямой')
    app = AppCalc(root)
    app.mainloop()



if __name__ == "__main__":
    main_app()