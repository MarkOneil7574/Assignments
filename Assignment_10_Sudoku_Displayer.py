sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]
linetime =  0
count = 0
print ( "-------------------------")
for i in sudoku:
    for j in i:
        if count in [3,6]:
            print(" | ", j, end = " ") 
        else:            
            print(j, end = (lambda x : "\n" if x == 8 else " ")(count))
        count += 1
    count = 0
    linetime += 1
    if linetime % 3 == 0:
        print ( "-------------------------")
