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
		fow_storage = BASE_DIR + "features\\" + author + "\\features.p"
		read = open(fow_storage)
		occ = pickle.load(read)
		mean_sentence_length = occ['mean_sentence_length']
		standard_deviation = 0.0
		num = 0.0
		count_sentence = 0.0
		#if folder _sent_items exists for the author then only process further
		emails = os.listdir(current_dir)
		for email in emails:
			txt = open(current_dir + "\\" + email)
			content = txt.read()
			sent_tokenize_list = sent_tokenize(content)
		
			for sentence in sent_tokenize_list:
				total_words = len(word_tokenize(sentence))
				count_sentence += 1
				num += np.power(total_words - mean_sentence_length, 2)
		standard_deviation = (float)(np.power((num/count_sentence), 0.5))
		print author
		print standard_deviation
		#Store feature
		occ['sentence_standard_deviation'] = standard_deviation
		store = open(fow_storage, "wb")
		pickle.dump(occ, store)
	