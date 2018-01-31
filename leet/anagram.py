# Swami Shreeji
# https://leetcode.com/problems/group-anagrams/description/

from collections import Counter

# wordsList = ["eat", "tea", "tan", "ate", "nat", "bat"]
wordsList = ["halo", "loha", "ahlo", "sully"]

target = 0
anagrams = [] 
for elem in wordsList:
	test = 1
	while test < len(wordsList):
		if target >= len(wordsList) - 1:
			break
		if Counter(wordsList[target]) == Counter(wordsList[test]):
		   anagram = wordsList[target] + " : " + wordsList[test]
		   anagrams.append(anagram)
		   # print 'Yes Anagram {} {}'.format(wordsList[target], wordsList[test])
		else:
		   print 'Not Anagram {} {}'.format(wordsList[target], wordsList[test])
		test += 1
	target += 1; test += 1
print anagrams
