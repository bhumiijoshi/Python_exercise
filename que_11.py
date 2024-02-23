from collections import Counter

def a_p_correction(a_p):
    
    difference = []
    for num in range(0,len(a_p)-1):
        diff = a_p[num+1] - a_p[num]
        difference.append(diff)
        
    counter = Counter(difference)
    common_difference = counter.most_common(1)[0][0]

    for num in range(0,len(a_p)-1):
        if a_p[num+1] - a_p[num] != common_difference:
            a_p[num+1] = a_p[num] + common_difference
            
    print(a_p)

def g_p_correction(g_p):
    ratio = []
    
    for num in range(0,len(g_p)-1):
        diff_1 = g_p[num+1]/g_p[num]
        ratio.append(diff_1)

    counter = Counter(ratio)
    common_ratio = counter.most_common(1)[0][0]
    
    for num in range(0,len(g_p)-1):
        if g_p[num+1]/g_p[num] != common_ratio:
            g_p[num+1] = g_p[num] * common_ratio
    
    print(g_p)

a_p_correction([2, 5, 8, 11, 13, 17])
g_p_correction([2,4,8,16,30,64])
