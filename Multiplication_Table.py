col = 1
while col <= 9:
    row = 1
    while row <= col:
        print(f'{col} X {row} = {col * row}', end='\t')
        row += 1
    print("")
    col += 1