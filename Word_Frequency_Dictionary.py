# Get a sentence from the user
sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.split()

# Create an empty dictionary
word_count = {}

# Count frequency of each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Display word frequency
print("Word Frequency:")
for word, count in word_count.items():
    print(word, ":", count)