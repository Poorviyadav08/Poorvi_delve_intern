#A.
rows_input=int(input("Enter row count: "))
num = 1
for i in range(1, rows_input + 1):
    for j in range(i):
        print(num,end=' ')
        num += 1
        if j !=i-1:
            print('*',end=' ')
    print()

#B.
rows_input = int(input("Enter row count: "))
for i in range(1,rows_input+1):
    print(' '*(rows_input-i),end='')
    print('* '*i)
for i in range(rows_input-1,0,-1):
    print(' '*(rows_input-i),end='')
    print('* '*i)

#C.
user_input = int(input("Enter row count: "))
num = 1
values =[]
for i in range(1, user_input + 1):
    row_vals=[]
    for j in range(i):
        row_vals.append(str(num))
        num+=1
    values.append(row_vals)
for row in values:
    print(' * '.join(row))
for row in reversed(values[:-1]):
    print(' * '.join(row))

#D.
user_input=int(input("Enter number of rows: "))
for i in range(user_input):
    if i==0:
        print("  ***")
    elif i==user_input - 1:
        print("  ***")
    elif i== user_input // 2:
        print(" * ***")
    elif i > user_input // 2:
        print(" *   *")
    else:
        print(" *")
#E.
user_input = int(input("Enter odd row count: "))
center = user_input // 2
for i in range(user_input):
    for j in range(user_input):
        if i==0 or i==user_input-1 or j==center:
            print('1',end=' ')
        else:
            print('0',end=' ')
    print()
