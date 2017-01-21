import os
import sys

from constants import DATA_DIR, MAIL_DIR, META_LINE_LIMIT, BASE_DIR
sys.path.insert(0, BASE_DIR + "dictionary")
from check_valid_word import has_key
from preprocessing import preprocess

authors = os.listdir(DATA_DIR)
authors = authors[1:]

for author in authors:
	email_info = preprocess(authors[0])
	content = email_info[1]
	print content
	break