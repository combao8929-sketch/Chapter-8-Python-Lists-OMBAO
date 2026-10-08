fname = open('romeo.txt')

words = []

for line in fname:
    line_words = line.split()

    for word in line_words:
        if word not in words:
        words.append(word)

words.sort()
print(words)