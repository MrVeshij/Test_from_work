numbers = [1,2,3,4,5,6,7,8,9,10]
# points_x = numbers[::2]
# points_y = numbers[::-2]
# points_y.reverse()

#print(points_x ,'\n',points_y)

points_x = []
points_y = []
k = 0
temp_list = []
amount = len(numbers)/2


def transfer(numbers):
    pairs = []
    while numbers:
        pairs.append([numbers[0], numbers[1]])
        numbers.remove(numbers[1])
        numbers.remove(numbers[0])
    return pairs


x = transfer(numbers)

print(x)