import functools

@functools.lru_cache(None)
def fibonacci(num):
    if num == 1 or num ==2:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

fibo_ans = fibonacci(int(input("Enter number: ")))
print(f"Answer of fibonacci series: {fibo_ans}")

def sumOfList(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + sumOfList(num_list[1:])
    
list_1 = [23, 44, 5, 67, 1, 1, 2, 4, 5]
print(f"Sum of the list {list_1} : {sumOfList(list_1)}")