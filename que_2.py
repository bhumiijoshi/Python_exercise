from collections import Counter

names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White']
length_of_names = []

for name in names:
    length_of_names.append(len(name))

print(f"Names : {names}")
print(f"Name lengths : {length_of_names}")

count_1 = Counter(length_of_names)

print("The three most frequent name lengths are:")
for length, occurred in count_1.most_common(3):
    fre_list = [name for name in names if len(name) == length]
    print(f"{occurred} names of length {length} : {fre_list}" )

print("The three least frequent name lengths are:")
for length, occurred in count_1.most_common()[:-4:-1]:
    fre_list = [name for name in names if len(name) == length]
    print(f"{occurred} names of length {length} : {fre_list}" )