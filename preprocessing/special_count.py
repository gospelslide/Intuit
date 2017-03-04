import os
import sys
import cPickle as pickle

from constants import DATA_DIR, MAIL_DIR, META_LINE_LIMIT, BASE_DIR
from preprocessing import preprocess,preprocess_special

special_chars = [',',';','\'','?','!','-']

authors = os.listdir(DATA_DIR)
authors = authors[1:]



for author in authors:
	occurences = dict()
	email_info = preprocess_special(author)
	if not email_info:
		continue

	total_count = email_info[1]
	if total_count == 0:
		continue

	for special_char in special_chars:
		count = email_info[0].count(special_char)
		occurences[special_char] = float(count*1.0/total_count)


	fow_storage = BASE_DIR + "features/" + author + "/special_chars.p"
	if not os.path.exists(fow_storage):
		store = open(fow_storage, "a")
		pickle.dump(occurences, store)
print "Done Successfully"
	

