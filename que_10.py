n = 5
m = (n+1)//2  # Integer division
for i in range(1, n+1):
    if i <= m:
        b = 2 * i - 1
        s = m - i
    else:
        b = 2 * (n - i) + 1
        s = i - m
    for _ in range(s):
        print('*', end='')
    for _ in range(b):
        print(' ', end='')
    for _ in range(s):
        print('*', end='')
    print()
    
print("------------------------------")

n = 5
m = (n+1)//2  # Integer division
for i in range(1, n+1):
    if i <= m:
        b = 2 * i - 1
        s = m - i
    else:
        b = 2 * (n - i) + 1
        s = i - m
    for _ in range(s):
        print(' ', end='')
    for _ in range(b):
        print('*', end='')
    for _ in range(s):
        print(' ', end='')
    print()

print("------------------------------")

n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        if j==1 or j==i or i==n:
            print('*',end='')
        else:
            print(' ',end='')
    print()

print("------------------------------")

n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or j==n or i==1 or i==n:
            print('*',end='')
        else:
            print(' ',end='')
    print()
    
print("------------------------------")

n = 5
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        
        print(num,end='')
        num += 1
    print()

print("------------------------------")