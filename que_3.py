sentences = ["My name is Ram", "He is a good person", "You should be careful while coding", "He can do better", "The person is mysterious", "Jay Shree Ram", "It is my pen."]
sentence_tree = []

for sentence in sentences:
    sentence_tree.append(sentence.split())
    
print("word_trees:")
print(sentence_tree)

# Flatten the list
flat_list = sum(sentence_tree, [])

words_occurrence = {key:flat_list.count(key) for key in flat_list}

print("Number of time each word appears:")
print(words_occurrence)

       