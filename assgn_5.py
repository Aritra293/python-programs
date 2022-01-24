def search_longest_wrd(wordslist):
    word_len = []
    for n in wordslist:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
res = search_longest_wrd(["Python", "Java", "Javascript"])
print("\nLongest word: ",res[1])
print("Length of the longest word: ",result[0])