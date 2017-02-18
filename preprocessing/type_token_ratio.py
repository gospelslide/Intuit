import os
import sys
import cPickle as pickle

from constants import DATA_DIR, MAIL_DIR, META_LINE_LIMIT, BASE_DIR
from preprocessing import preprocess

authors = os.listdir(DATA_DIR)
authors = authors[1:]

for author in authors:
	print author
	email_info = preprocess(author)
	if not email_info:
		continue
	total = 0.0
	email_contents = email_info[1]
	no_content = 0
	for email_no in email_contents:
		unique_words = set(email_contents[email_no])
		total_words = len(email_contents[email_no])
		no_unique_words = len(unique_words)
		if total_words:
			type_token_ratio = no_unique_words/float(total_words)
			total += type_token_ratio
		else:
			no_content += 1
	deno = len(email_contents) - no_content
	avg_ratio = total/deno

	fow_storage = BASE_DIR + "features\\" + author + "\\features.p"
	read = open(fow_storage)
	occ = pickle.load(read)
	occ['type_token_ratio'] = avg_ratio
	store = open(fow_storage, "wb")
	pickle.dump(occ, store)
