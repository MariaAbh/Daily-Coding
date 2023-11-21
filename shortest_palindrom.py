def palindrome(word, index_start, index_end):
	pref = ''
	suf = ''
	word_len = len(word)

	if word == word[::-1]:
		return word
	if word[index_start] != word[index_end]:
		pref = word[:index_start] + word[index_end] + word[index_start:]
		word_index_end = word_len + index_end +1
		if word_index_end == word_len:
			suf = word + word[index_start]
		else:
			suf = word[:index_end+1] + word[index_start] + word[word_len+index_end+1:]
	else:
		pref = word
		suf = word

	prefix = palindrome(pref,index_start+1,index_end-1)
	suffix = palindrome(suf,index_start+1,index_end-1)
	
	return min(prefix,suffix,key=len)


def pal(word):
	

# word = 'google'
# word = 'tbat'
word = 'titouan'
pal = palindrome(word,0,-1)
print('Given word:',word)
print('Sortest palindrome:',pal)

