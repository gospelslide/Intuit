import os
import sys
import cPickle as pickle

from constants import DATA_DIR, MAIL_DIR, META_LINE_LIMIT, BASE_DIR
sys.path.insert(0, BASE_DIR + "dictionary")
from check_valid_word import has_key
from preprocessing import preprocess

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
	total_word_length = 0

	for key in content:
		for word in content[key]:
			total_word_length += len(word)
			total_words += 1
		break
	avg_word_length = total_word_length/float(total_words)

	for word in occurences:
		occurences[word] /= float(total_words)

	fow_storage = BASE_DIR + "features/" + author + "/features.p"
	read = open(fow_storage)
	occ = pickle.load(read)
	occ['mean_word_length'] = avg_word_length
	store = open(fow_storage, "wb")
	pickle.dump(occ, store)