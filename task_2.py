from collections import Counter
from tkinter import *



class AppCalc(Frame):
    """Основной класс приложения, включает в себя следующие методы:
    create_widgets - Отвечает за создание виджетов приложения
    ycheck - Контроллер по проверке одинакового количества значений по оси y. Если одинаковых
    значений встречается нечетное количество, перенаправляет на контроллер проверки xcheck. Если четное
    запускает метод расчета наличия прямой.(calculation_x)
    xcheck - Контроллер по проверке одинакового количества значений по оси x. Если одинаковых
    значений встречается нечетное количество, прямой разделяющей множества нет. Если количество четное
    запускает метод расчета наличия прямой.(calculation_y)
    main - Контроллер приложения запускающий вышеуказанную логику"""


    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        """Создание виджетов для взаимодействия"""
        Label(self,
              text = 'Введите через пробел координаты точек.'
              ).grid(row = 0, column = 0, sticky = W)
        self.numbers = Entry(self,width=40)
        self.numbers.grid(row=1, column=0, sticky=W)
        self.info = Text(self, width = 30, height = 5, wrap = WORD)
        self.info.grid(row = 7, column = 0, sticky = W)
        Button(self,
               text = 'Результат',
               command = self.main
                   ).grid(row = 6, column = 0, sticky = W)


    def ycheck(self, numbers):
        """Проверка четного количества точек по оси y с одинаковыми значениями"""
        numbers2 = numbers[:]
        points_x = numbers[::2]
        points_y = numbers[::-2]
        points_y.reverse()
        check_y = Counter(points_y)
        sum_y = 0
        for i in check_y:
            if check_y.get(i) % 2 != 0:
                return self.xcheck(numbers, points_x)
            else:
                sum_y += 1
        if sum_y == len(check_y):
            if self.calculation_y(numbers, check_y) == 0:
                return self.xcheck(numbers2, points_x)
            else:
                return 'YES'


    def xcheck(self, numbers2, points_x):
        """Проверка четного количества точек по оси x с одинаковыми значениями"""
        check_x = Counter(points_x)
        sum_x = 0
        for k in check_x:
            if check_x.get(k) % 2 != 0:
                return 'NO'
            else:
                sum_x += 1
        if sum_x == len(check_x):
            return self.calculation_x(numbers2, check_x)


    def calculation_y(self, numbers, check_y):
        """Поиск одинаковой точки по оси x"""
        pairs = []
        sum_x = 0
        check_final = []
        while numbers:
            pairs.append([numbers[0], numbers[1]])
            numbers.remove(numbers[1])
            numbers.remove(numbers[0])
        for i in check_y:
            for a in pairs:
                if a[1] == i:
                    sum_x += a[0]
            check_final.append(sum_x/check_y.get(i))
            sum_x = 0
        if sum(check_final) / len(check_final) == check_final[0]:
            return "YES"
        else:
            return 0


    def calculation_x(self, numbers, check_x):
        """Поиск одинаковой точки по оси y"""
        pairs = []
        sum_y = 0
        check_final = []
        while numbers:
            pairs.append([numbers[0], numbers[1]])
            numbers.remove(numbers[1])
            numbers.remove(numbers[0])
        for i in check_x:
            for a in pairs:
                if a[0] == i:
                    sum_y += a[1]
            check_final.append(sum_y/check_x.get(i))
            sum_y = 0
        if sum(check_final) / len(check_final) == check_final[0]:
            return "YES"
        else:
            return "NO"


    def main(self):
        """Запуск кнопки"""
        numbers = self.numbers.get()
        if not numbers:
            info = 'Введите координаты точек.'
            self.info.delete(0.0, END)
            self.info.insert(0.0, info)
        numbers = [float(i) for i in numbers.split(' ')]
        amount_numbers = len(numbers)
        if amount_numbers % 2 != 0 or amount_numbers in range(2,1000,4):
            info = 'Укажите четное количество точек.'
            self.info.delete(0.0, END)
            self.info.insert(0.0, info)
        else:
            info = self.ycheck(numbers)
            self.info.delete(0.0, END)
            self.info.insert(0.0, info)



def main_app():
    """Запуск приложения"""
    root = Tk()
    root.title('Поиск прямой')
    app = AppCalc(root)
    app.mainloop()



if __name__ == "__main__":
    main_app()