import os
import re
from constants import DATA_DIR, MAIL_DIR, META_LINE_LIMIT, BASE_DIR
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import numpy as np
import cPickle as pickle

authors = os.listdir(DATA_DIR)
authors = authors[0:]
for author in authors:
	
	#for every author
	current_dir = DATA_DIR + author + MAIL_DIR
	if os.path.exists(current_dir):
		total_words = 0
		standard_deviation = 0
		numerator = 0
		total_sentence = 0
		#if folder _sent_items exists for the author then only process further
		emails = os.listdir(current_dir)
		for email in emails:

			txt = open(current_dir + "\\" + email)
			content = txt.read()
			sent_tokenize_list = sent_tokenize(content)
			total_sentence += len(sent_tokenize_list)
		
			for sentence in sent_tokenize_list:
				total_words += len(word_tokenize(sentence))
			
		mean_sentence_length = 1.0 * total_words/total_sentence
		
		#Store feature
		fow_storage = BASE_DIR + "features\\" + author + "\\features.p"
		read = open(fow_storage)
		occ = pickle.load(read)
		occ['mean_sentence_length'] = mean_sentence_length
		store = open(fow_storage, "wb")
		pickle.dump(occ, store)
	break	
	