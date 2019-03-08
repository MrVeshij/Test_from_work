from math import sqrt




def main(m):
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
        else: return "!"


    if B1*A2 - B2*A1 and A1:
        y = (C2*A1 - C1*A2) / (B1*A2 - B2*A1)
        x = (-C1 - B1*y) / A1
        matches.append([x, y])
        if B2*A3 - B3*A2 and A2:
            y = (C3*A2 - C2*A3) / (B2*A3 - B3*A2)
            x = (-C2 - B2*y) / A2
            matches.append([x, y])
            if B1*A3 - B3*A1 and A1:
                y = (C3*A1 - C1*A3) / (B1*A3 - B3*A1)
                x = (-C1 - B1*y) / A1
                matches.append([x, y])
                if not m:
                    print("Точки пересечения прямых", matches)
                    print("A^B^C")
                else: return True

                #Высчитывает длину сторон
                a = sqrt((matches[1][0] - matches[0][0])**2 + (matches[1][1] - matches[0][1])**2)
                b = sqrt((matches[2][0] - matches[1][0])**2 + (matches[2][1] - matches[1][1])**2)
                c = sqrt((matches[0][0] - matches[2][0])**2 + (matches[0][1] - matches[2][1])**2)
                #Думаю это периметр
                p = (a + b + c) / 2
                S = sqrt(p * (p - a) * (p - b) * (p - c))
                print("Площадь треугольника ", S)
            else:
                if not m:
                    print("A||C")
                    print("0")
                else: return 'AC'
        else:
            if not m:
                print("B||C")
                print("0")
            else: return 'BC'
    else:
        if B2*A3 - B3*A2 and A2:
            y = (C3*A2 - C2*A3) / (B2*A3 - B3*A2)
            x = (-C2 - B2*y) / A2
            if not m:
                print('Точка пересечения отрезков есть, координаты: ({0:f}, {1:f}).'.format(x, y))
                print("A||B")
                print("0")
            else: return 'AB'
        else:
            if not m:
                print('Точки пересечения отрезков нет, A||B||C')
                print("0")
            else: return False

def test_main(m,msg=None,status=None):
    if main(m) == status:
        print(msg,'Test ok')
    elif main(m) == 'AC':
        print(msg,'Test ok(AC)')
    elif main(m) == 'AB':
        print(msg,'Test ok(AB)')
    elif main(m) == 'BC':
        print(msg,'Test ok(BC)')
    elif main(m) == '!':
        print(msg,'Test ok(!)')
    else: print(msg,'Test fail')



def testing():
    m1 = (1,-1,2,-1,-2,2,-1,2,1,1,2,1) #Проверка на паралельные прямые
    test_main(m1,"Тест ||\t",False)

    m2 = (1,1,1,2,2,1,2,2,3,1,3,2) #Проверка на параллельные прямые
    test_main(m2,"Тест ||\t", False)

    m3 = (2,3,5,6,2,5,5,3,4,3,4,6) #Проверка на пересечение 3 прямых
    test_main(m3,"Тест ^\t", True)

    m4 =(6,2,9,5,7,2,7,4,9,3,6,6) #Проверка на пересечение 3 прямых
    test_main(m4,"Тест ^\t", True)

    m5 = (3,8,4,8,8,-3,9,-3,10,1,10,3) #Проверка А||B
    test_main(m5,"Тест A||B\t")

    m6 = (-2,-1,-2,-2,2,-2,3,-2,3,2,3,3) #Проверка А||C
    test_main(m6,"Тест A||C\t")

    m7 = (1,-5,6,-3,3,-3,3,-6,10,1,10,3) #Проверка B||C
    test_main(m7,"Тест B||C\t")

    m8 = (-3,1,-2,1,1,1,2,1,5,1,6,1) #Проверка наложения прямых
    test_main(m8,"Тест !\t")

testing()






