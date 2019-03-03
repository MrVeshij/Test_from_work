from math import sqrt
from tkinter import *


class AppCalc(Frame):
    """
    В этой версии добавлены тесты для самопроверки приложения.

    Основной класс приложения, включает в себя следующие методы:
    create_widgets - Отвечает за создание виджетов приложения
    calculation - Логика расчетов
    command_calc - Логика работы кнопки
    test_main - Логика проверки корректности работы метода calculation
    testing - Тестовые случаи для проверки модуля calculation"""


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


    def calculation(self,m=None):
        """Блок основных вычислений по пересечениям прямых,
        принимает на вход кортеж с координатами прямых"""
        if not m:
            print('Введите координаты точек первой прямой.')
            x1_1, y1_1 = float(input('Координаты первой точки x = ')), float(input('y = '))
            x1_2, y1_2 = float(input('Координаты второй точки x = ')), float(input('y = '))
            print('Введите координаты точек второй прямой.')
            x2_1, y2_1 = float(input('Координаты первой точки x = ')), float(input('y = '))
            x2_2, y2_2 = float(input('Координаты второй точки x = ')), float(input('y = '))
            print('Введите координаты точек третьей прямой.')
            x3_1, y3_1 = float(input('Координаты первой точки x = ')), float(input('y = '))
            x3_2, y3_2 = float(input('Координаты второй точки x = ')), float(input('y = '))
        else:
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
            if not m:
                print("Прямые одинаковы")
            else: return ["Прямые одинаковы", "!", 0]

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
                    matches.append([x, y])
                    if not m:
                        a = sqrt((matches[1][0] - matches[0][0])**2 + (matches[1][1] - matches[0][1])**2)
                        b = sqrt((matches[2][0] - matches[1][0])**2 + (matches[2][1] - matches[1][1])**2)
                        c = sqrt((matches[0][0] - matches[2][0])**2 + (matches[0][1] - matches[2][1])**2)
                        p = (a + b + c) / 2
                        S = sqrt(p * (p - a) * (p - b) * (p - c))
                        print("Точки пересечения прямых", matches)
                        print("A^B^C")
                        print("Площадь треугольника ", S)
                    else:
                        a = sqrt((matches[1][0] - matches[0][0]) ** 2 + (matches[1][1] - matches[0][1]) ** 2)
                        b = sqrt((matches[2][0] - matches[1][0]) ** 2 + (matches[2][1] - matches[1][1]) ** 2)
                        c = sqrt((matches[0][0] - matches[2][0]) ** 2 + (matches[0][1] - matches[2][1]) ** 2)
                        p = (a + b + c) / 2
                        S = sqrt(p * (p - a) * (p - b) * (p - c))
                        print("Точки пересечения прямых", matches)
                        print("A^B^C")
                        print("Площадь треугольника ", S)
                        return ["A^B^C", True, S]
                else:
                    if not m:
                        print("A||C")
                        print("0")
                    else: return ['A||C', 'A||C', 0]
            else:
                if not m:
                    print("B||C")
                    print("0")
                else: return ['B||C', 'B||C', 0]
        else:
            if B2*A3 - B3*A2:
                y = (C3*A2 - C2*A3) / (B2*A3 - B3*A2)
                if A3 == 0:
                    x = (-C2 - B2 * y) / A2
                else:
                    x = (-C3 - B3 * y) / A3
                if not m:
                    print('Точка пересечения отрезков есть, координаты: ({0:f}, {1:f}).'.format(x, y))
                    print("A||B")
                    print("0")
                else: return ['A||B', 'A||B', 0]
            else:
                if not m:
                    print('Точки пересечения отрезков нет, A||B||C')
                    print("0")
                else: return ['Точки пересечения отрезков нет, A||B||C', False]


    def command_calc(self):
        """Запуск расчета логики через кнопку"""
        fs = self.first_straight.get()
        ss = self.second_straight.get()
        ts = self.third_straight.get()
        result = [float(i) for i in fs.split(' ')] + \
                 [float(i) for i in ss.split(' ')] + \
                 [float(i) for i in ts.split(' ')]
        information = str(self.calculation(result)[0]) + '\n' + str(self.calculation(result)[2])
        self.info.delete(0.0, END)
        self.info.insert(0.0, information)


    def test_main(self,m,msg=None,status=None):
        """Метод теста для проверки работы модуля"""
        if self.calculation(m)[1] == status:
            print(msg,'Test ok')
        elif self.calculation(m)[1] == '!':
            print(msg, 'Test ok(!)')
        elif self.calculation(m)[0] == 'A||C':
            print(msg,'Test ok(AC)')
        elif self.calculation(m)[0] == 'A||B':
            print(msg,'Test ok(AB)')
        elif self.calculation(m)[0] == 'B||C':
            print(msg,'Test ok(BC)')
        else: print(msg,'Test fail')


    def testing(self):
        """Случаи для проверки корректности работы модуля"""
        m1 = (1,-1,2,-1,-2,2,-1,2,1,1,2,1) #Проверка на паралельные прямые
        self.test_main(m1,"Тест ||\t",False)

        m2 = (1,1,1,2,2,1,2,2,3,1,3,2) #Проверка на параллельные прямые
        self.test_main(m2,"Тест ||\t", False)

        m3 = (2,3,5,6,2,5,5,3,4,3,4,6) #Проверка на пересечение 3 прямых
        self.test_main(m3,"Тест ^\t", True)

        m4 =(6,2,9,5,7,2,7,4,9,3,6,6) #Проверка на пересечение 3 прямых
        self.test_main(m4,"Тест ^\t", True)

        m5 = (3,8,4,8,8,-3,9,-3,10,1,10,3) #Проверка А||B
        self.test_main(m5,"Тест A||B\t")

        m6 = (-2,-1,-2,-2,2,-2,3,-2,3,2,3,3) #Проверка А||C
        self.test_main(m6,"Тест A||C\t")

        m7 = (1,-5,6,-3,3,-3,3,-6,10,1,10,3) #Проверка B||C
        self.test_main(m7,"Тест B||C\t")

        m8 = (-3,1,-2,1,1,1,2,1,5,1,6,1) #Проверка наложения прямых
        self.test_main(m8,"Тест !\t")


def main_app():
    """Запуск приложения"""
    root = Tk()
    root.title('Пересечения')
    app = AppCalc(root)
    app.mainloop()



if __name__ == "__main__":
    main_app()




