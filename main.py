def read_input():
    global n
    global colors; global names; global foods; global cities

    n = int(input('Please enter number of participants:'))

    colors = ['' for x in range(n)]; names = ['' for x in range(n)]
    foods = ['' for x in range(n)]; cities = ['' for x in range(n)]

    print('-----------------------------------------------')
    print('Answers for all participants should be entered in the order of {name, color, food, city} in one line, space seperated')
    print('-----------------------------------------------')

    for i in range(n):
        [names[i], colors[i], foods[i], cities[i]] = input('Please enter participant {i} answers: ')
    
    solve()
        
def solve():
    for i in range(n):
        print([names[i], colors[i], foods[i], cities[i]])


def main():
    read_input()


main()