def read_input():
    global n
    global colors; global names; global foods; global cities
    global base_char

    n = int(input('Please enter number of participants: ').strip())
    base_char = input('Please enter The Char of your game: ').strip()


    colors = [['', x] for x in range(n)]; names = [['', x] for x in range(n)]
    foods = [['', x] for x in range(n)]; cities = [['', x] for x in range(n)]

    print('-----------------------------------------------')
    print('Answers for all participants should be entered in the order of {name, color, food, city} in one line, space seperated')
    print('-----------------------------------------------')

    user_input_text = 'Please enter participant {} answers: '
    for i in range(n):
        [names[i][0], colors[i][0], foods[i][0], cities[i][0]] = input(user_input_text.format(i +1)).split(' ')
    
    solve()
        
def check(entery):
    if entery.startswith(base_char):
        return True
    return False

def check_identity(arr, index):
    indexes = []
    if index > 0:
        indexes.append(index -1)
    if index < n -1:
        indexes.append(index +1)
    
    for i in indexes:
        if arr[index][0] == arr[i][0]:
            return False
    
    return True

def solve():
    global points
    points = [0 for x in range(n)]

    names.sort(); colors.sort(); foods.sort(); cities.sort()
    for i in range(n):
        if check(names[i][0]):
            if check_identity(names, i):
                points[names[i][1]] += 10
            else:
                points[names[i][1]] += 5

        if check(foods[i][0]):
            if check_identity(foods, i):
                points[foods[i][1]] += 10
            else:
                points[foods[i][1]] += 5

        if check(colors[i][0]):
            if check_identity(colors, i):
                points[colors[i][1]] += 10
            else:
                points[colors[i][1]] += 5

        if check(cities[i][0]):
            if check_identity(cities, i):
                points[cities[i][1]] += 10
            else:
                points[names[i][1]] += 5
    

    user_output_text = 'Point of participant {} is: '
    for i in range(n):
        print(user_output_text.format(i +1), points[i] )



def main():
    read_input()


main()