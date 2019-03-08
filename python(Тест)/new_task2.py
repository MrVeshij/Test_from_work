def calculation(numbers):
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


def main(numbers=None):
    if not numbers:
        numbers = input('Введите координаты точек')
    numbers = [float(i) for i in numbers.split(' ')]
    amount_numbers = len(numbers)
    if amount_numbers % 2 != 0 or amount_numbers in range(2,1000,4):
        print('Укажите четное количество точек.')
        return 'Укажите четное количество точек.'
    else:
        return calculation(numbers)

