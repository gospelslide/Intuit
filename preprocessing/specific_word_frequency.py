import os
import sys
import cPickle as pickle

from constants import DATA_DIR, MAIL_DIR, META_LINE_LIMIT, BASE_DIR
sys.path.insert(0, BASE_DIR + "dictionary")
from check_valid_word import has_key
from preprocessing import preprocess

words = ['and', 'but', 'however', 'if', 'that', 'more', 'must', 'might', 'this', 'very']

authors = os.listdir(DATA_DIR)
authors = authors[1:]

for author in authors:
	total_words = 0
	email_info = preprocess(author)
	if not email_info:
		continue 
	content = email_info[1]
	occurences = dict()

	print author

	for key in content:
		for word in content[key]:
			if word in occurences:
				occurences[word] += 1
			else:
				if has_key(word) and word in words:
					occurences[word] = 1
			total_words += 1

	for word in occurences:
		occurences[word] /= float(total_words)

	for w in words:
		if w not in occurences:
			occurences[w] = 0.0
	# print author
	# print occurences

	fow_storage = BASE_DIR + "features/" + author + "/features.p"
	if not os.path.exists(fow_storage):
		store = open(fow_storage, "a")
		pickle.dump(occurences, store)
	# read = open(BASE_DIR + "features/" + author + "/fow.p", "r")
	# occ = pickle.load(read)