sentence = "Hey I am walking here I am walking here o captain my captain waterwater everywhere nor a drop to drink"
sentence_L = sentence.split()
# split sentence into list of words
sentence_list = sentence.split() # You will have to fill out the function
sentence_set = set(sentence_L)
print(sentence_L, '\n')
# convert list to set to get unique words
sentence_set = set(sentence_L)
print(sentence_set, '\n')
# print the number of unique words
num_unique = len(sentence_set)
print(num_unique, '\n')