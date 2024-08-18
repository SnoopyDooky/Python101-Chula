n = int(input())
words = {}  # ex. {'good': 'Adjective', 'goose': 'Noun', ...}
first_two_words = {}  # ex. {'go': ['good', 'goose'], 'wr': ['wrap,' 'write', ...], ...}
# add data to words and first_two_words
for i in range(n):
    parts_of_speech, word = input().split()
    words[word] = parts_of_speech
    if word[:2] in first_two_words:
        first_two_words[word[:2]].append(word)
    else:
        first_two_words[word[:2]] = [word]
# sort
l = [(-len(v), k) for k, v in first_two_words.items()]
l.sort()
# show results
print(l[0][1])   # ex. 'wr'
print(-l[0][0])  # ex. 5
for e in first_two_words[l[0][1]]:
    print(e, words[e])
