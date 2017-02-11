# strip all whitespace, special characters and replace numbers by 0
# convert meta data into a dictionary object
# all words are in a list object
import os
import re
from constants import DATA_DIR, MAIL_DIR, META_LINE_LIMIT, BASE_DIR

def preprocess(author):
    authors = os.listdir(DATA_DIR)
    authors = authors[1:]

    # temporary script to create all author folders 
    # for author in authors:
    #     os.makedirs(BASE_DIR + "features/" + author)

    current_dir = DATA_DIR + author + MAIL_DIR
    if not os.path.exists(current_dir):
        return False
    emails = os.listdir(current_dir)

    meta = dict()
    words_used = dict()

    # for all sent mails
    # divide into test & train set
    for email in emails:

        # extract meta data & convert to lower case
        txt = open(current_dir + "/" + email)
        # print txt.read()
        meta_data = dict()
        message = list()
        line_no = 0

        for line in txt:
            line_no += 1
            # process meta data
            if line_no <= META_LINE_LIMIT:
                content = line.rstrip().split(":")
                if len(content) >= 2:
                    meta_data[content[0]] = content[1]
            # process message data
            else:
                words = line.rstrip().lower().split(" ")
                for i in range(len(words)):
                    if words[i].isdigit():
                        words[i] = "0"
                    if not words[i].isalnum():
                        words[i] = re.sub('[^a-zA-Z0-9-_*.]', '', words[i])
                        if words[i].isdigit():
                            words[i] = "0"
                        elif not words[i].isalnum():
                            words[i] = ""
                message += words

        message = filter(None, message)

        meta[email] = meta_data
        words_used[email] = message
        # print meta_data
        # print message
    return meta, words_used
    # a tuple of two dictionaries both contain email no as the key and 
    # meta contains metadata as value and words_used contains all words in 
    # the email in a list as the value
