#использован метод №2 Bottom - up
#идея следующая: унас есть 8 независимых объектов - королев
#каждая королева хочет как-то встать на доску. Как нужно встать знаем только мы
#поэтому мы поочередно встречаемся с каждой королевой и "удовлетворяем" ее желание встать на поле.
#мы (поле) уже сами решаем, куда она может встать

current_x = 0
current_y = 0
queen_count = 1
queen_positions = [[0, 0] for i in range(9)]
queen_positions[0] = [0, 0]

for i in range(1, 9):
    current_y+=2
    current_x+=1
    if current_y>8:
        current_y = -1
        flag = True
        while flag:
            current_y+=1
            flag = False
            for j in range(i):
                if current_y == queen_positions[i][1]:
                    flag = True
    if current_x >8:
        current_x = -1
        flag = False
        while flag:
            current_x+=1
            for j in range(0, i):
                if current_x == queen_positions[i][0]:
                    flag = True
    queen_positions[i] = [current_x, current_y]    
for i in range(9):
    print(queen_positions[i][0], " ", queen_positions[i][1])
