Numbers = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]
n = 12
first = 0

list_1 = []
for first in range(0,len(Numbers)-1):
    for last in range(first +1 ,len(Numbers)-1):

   
        if (Numbers[first] + Numbers[last]) == n:
        
            list_2 = []
            list_2.append(Numbers[first])
            list_2.append(Numbers[last])
            list_2.sort()
        
            if list_2 not in list_1:
                list_1.append(list_2)
        
print(list_1)