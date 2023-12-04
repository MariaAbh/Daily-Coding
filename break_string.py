#57 Given a string and an int, break up the string such that each line has a lenght<=k.

def break_string(s,k):
    words = s.split(' ')
    sublist = []
    i = 0
    counter = 10
    substr = ''
    while i < len(words):
        word = words[i]
        counter -= len(word)
        if counter >= 0:
            substr += word +' '
            i += 1
            counter -= 1
        else:
            sublist.append(substr[:-1])
            counter = 10
            substr = ''
    sublist.append(substr[:-1])
    return sublist

s = "the quick brown fox jumps over the lazy dog"
k = 10
print(break_string(s,k))
