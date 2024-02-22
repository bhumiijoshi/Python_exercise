numbers = [2, 5, 6, 1, 3, 8, 9, 10]

for i in range(0,len(numbers)-1):
    for j in range(i+1,len(numbers)-1):
        if numbers[i] > numbers[j]:
            numbers[i],numbers[j] = numbers[j],numbers[i]

print(numbers)