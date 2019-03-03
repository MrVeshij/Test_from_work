from math import sqrt
from tkinter import *


class AppCalc(Frame):
    """Основной класс приложения, включает в себя следующие методы:
    create_widgets - Отвечает за создание виджетов приложения
    calculation - Логика расчетов
    command_calc - Логика работы кнопки"""


    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        """Создание виджетов для взаимодействия"""
        Label(self,
              text = 'Введите через пробел \nкоординаты прямой A(x1,y1,x2,y2)'
              ).grid(row = 0, column = 0, sticky = W)
        self.first_straight = Entry(self)
        self.first_straight.grid(row=1, column=0, sticky=W)
        Label(self,
              text='Введите через пробел \nкоординаты прямой B(x1,y1,x2,y2)'
              ).grid(row=2, column=0, sticky=W)
        self.second_straight = Entry(self)
        self.second_straight.grid(row=3, column=0, sticky=W)
        Label(self,
              text='Введите через пробел \nкоординаты прямой C(x1,y1,x2,y2)'
              ).grid(row=4, column=0, sticky=W)
        self.third_straight = Entry(self)
        self.third_straight.grid(row = 5, column = 0, sticky = W)
        self.info = Text(self, width = 24, height = 5, wrap = WORD)
        self.info.grid(row = 7, column = 0, sticky = W)
        Button(self,
               text = 'Результат',
               command = self.command_calc
                   ).grid(row = 6, column = 0, sticky = W)


    def calculation(self,m):
        """Блок основных вычислений по пересечениям прямых,
        принимает на вход кортеж с координатами прямых возвращает
        в виде списка состояние и площадь треугольника"""
        x1_1, y1_1, x1_2, y1_2 = m[0], m[1], m[2], m[3]
        x2_1, y2_1, x2_2, y2_2 = m[4], m[5], m[6], m[7]
        x3_1, y3_1, x3_2, y3_2 = m[8], m[9], m[10], m[11]

        #Представление прямой 1
        A1 = y1_1 - y1_2
        B1 = x1_2 - x1_1
        C1 = x1_1*y1_2 - x1_2*y1_1
        #Представление прямой 2
        A2 = y2_1 - y2_2
        B2 = x2_2 - x2_1
        C2 = x2_1*y2_2 - x2_2*y2_1
        #Представление прямой 3
        A3 = y3_1 - y3_2
        B3 = x3_2 - x3_1
        C3 = x3_1*y3_2 - x3_2*y3_1

        matches = []
        if A1 == A2 == A3 and B1 == B2 == B3 and C1 == C2 == C3:
            return ["Прямые одинаковы", 0]

        if B1*A2 - B2*A1:
            y = (C2*A1 - C1*A2) / (B1*A2 - B2*A1)
            if A1 == 0:
                x = (-C2 - B2 * y) / A2
            else:
                x = (-C1 - B1*y) / A1
            matches.append([x, y])
            if B2*A3 - B3*A2:
                y = (C3*A2 - C2*A3) / (B2*A3 - B3*A2)
                if A2 == 0:
                    x = (-C3 - B3 * y) / A3
                else:
                    x = (-C2 - B2*y) / A2
                matches.append([x, y])
                if B1*A3 - B3*A1:
                    y = (C3*A1 - C1*A3) / (B1*A3 - B3*A1)
                    if A1 == 0:
                        x = (-C3 - B3 * y) / A3
                    else:
                        x = (-C1 - B1*y) / A1
                    #Блок расчета площади треугольника
                    matches.append([x, y])
                    a = sqrt((matches[1][0] - matches[0][0]) ** 2 + (matches[1][1] - matches[0][1]) ** 2)
                    b = sqrt((matches[2][0] - matches[1][0]) ** 2 + (matches[2][1] - matches[1][1]) ** 2)
                    c = sqrt((matches[0][0] - matches[2][0]) ** 2 + (matches[0][1] - matches[2][1]) ** 2)
                    p = (a + b + c) / 2
                    S = sqrt(p * (p - a) * (p - b) * (p - c))
                    return ["A^B^C",S]

                else:
                    return ['A||C', 0]
            else:
                return ['B||C',0]
        else:
            if B2*A3 - B3*A2:
                return ['A||B', 0]
            else:
                return ['A||B||C', 0]


    def command_calc(self):
        """Интерфейс - Запуск расчета логики и проверка на корректность ввода"""
        fs = self.first_straight.get()
        ss = self.second_straight.get()
        ts = self.third_straight.get()
        if fs and ss and ts:
            result = [float(i) for i in fs.split(' ')] + \
                     [float(i) for i in ss.split(' ')] + \
                     [float(i) for i in ts.split(' ')]
            if len(result) != 12:
                information = 'Проверьте ввод координат на корректность'
            else:
                information = str(self.calculation(result)[0]) + '\n' + str(self.calculation(result)[1])
            self.info.delete(0.0, END)
            self.info.insert(0.0, information)
        else:
            self.info.delete(0.0, END)
            self.info.insert(0.0, 'Заполните все поля')



def main_app():
    """Запуск приложения"""
    root = Tk()
    root.title('Пересечения')
    app = AppCalc(root)
    app.mainloop()



if __name__ == "__main__":
    main_app()