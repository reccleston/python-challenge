# 
# PyParagraph
# Ryan Eccleston-Murdock
# 28 November 2020 
# 
# Purpose: Convert old employee records into the new format.
#
# Sources: 

import os
import re

in_path = './raw_data'
in_file_name = 'paragraph_1.txt'
in_filepath = os.path.join(in_path, in_file_name)

def findPuncuation(word):

	one_sentence = 0
	for letter in word:
		if letter == '.' or letter == '!' or letter == '?':
			one_sentence = 1

	return one_sentence

def wordLength(word):

	word_len = 0
	for letter in word:
		word_len += 1

	word_lengths.append(word_len)

with open(in_filepath, 'r') as inFile:

	paragraph = inFile
	total_words = 0
	split_para = re.split("(?<=[.!?]) +", paragraph)
	num_sentence = len(split_para)
	# word_by_word = [word.split() for word in paragraph]
	word_lengths = []

	print(split_para)
	print(num_sentence)
	# for text_block in word_by_word:
	# 	for word in text_block:
	# 		total_words += 1
	# 		wordLength(word)
	# 		num_sentence += findPuncuation(word)

	# print(total_words)
	# approx_average_word_len = sum(word_lengths) / len(word_lengths)
	# print(approx_average_word_len)
	# print(num_sentence)
