#coding: utf-8
import re, collections
book_path = 'ANIMAL FARM.txt'
book_res = open(book_path)
all_words = []
for line in book_res:
	words = re.findall(r'[a-zA-Z]+', line)
	if words :
		all_words.extend(words)

words_count = collections.Counter(all_words)
print(words_count);exit();