import os
from constants import *
from shutil import move

authors = os.listdir(DATA_DIR)
authors = authors[1:]

os.makedirs(DATA_DIR + 'test')
CURR_DIR = DATA_DIR + 'training/'

for author in authors:
	folders = os.listdir(DATA_DIR + author)
	folders = folders[1:]
	for folder in folders:
		if os.path.isdir(DATA_DIR + author + '/' + folder):
			if not os.path.exists(CURR_DIR + author + '/' + folder):
				os.makedirs(CURR_DIR + author + '/' + folder)
			emails = os.listdir(DATA_DIR + author + '/' + folder)
			n = len(emails)*4/5
			i = 0
			for email in emails:
				src = DATA_DIR + author + '/' + folder + '/' + email
				dest = CURR_DIR + author + '/' + folder + '/' + email
				if os.path.isfile(src) and os.path.isdir(CURR_DIR + author + '/' + folder):
					move(src, dest)
				i += 1
				if i == n:
					break
