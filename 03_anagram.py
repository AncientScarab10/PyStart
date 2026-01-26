# Przygotuj program, który będzie sprawdzał czy dwa podane słowa są wzajemnymi
# anagramami.

word1 = "abcdef"
word2 = "fedcba"

list1 = sorted(list(word1))
list2 = sorted(list(word2))

print(list1 == list2)


