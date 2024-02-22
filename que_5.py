import itertools

Numbers = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]
n = 12
first = 0
main_list = []

for c in itertools.combinations(sorted(Numbers), 2):

        if (c[0] + c[1]) == n:
        
            sub_list = []
            sub_list.append(c[0])
            sub_list.append(c[1])
            sub_list.sort()
        
            if sub_list not in main_list:
                main_list.append(sub_list)
        
print(main_list)