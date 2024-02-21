numbers = [2, 4, 5, 2, 12, 44, 5, 1, 2, 3]

operation = input("Select any option from A | B | C | D | E : ").lower()

if(operation == 'a'):
    print(f"Length of List : {len(numbers)}")

elif(operation == 'b'):
    print(f"First three numbers : {numbers[:3]}")

elif(operation == 'c'):
    sum = 0
    for num in numbers:
        if num%2 != 0:
            sum += num
    print(f"Sum of odd number : {sum}")

elif(operation == 'd'):
    duplicate = {num for num in numbers if numbers.count(num) > 1}
    print(f"Number of duplicate numbers:{len(duplicate)}, ({duplicate} are repeat numbers)")

elif(operation == 'e'):
    new_list = []
    [new_list.append(num) for num in numbers if num not in new_list]
    print(f"List without duplicate numbers : {new_list}")

else:
    print("Please enter valid option")