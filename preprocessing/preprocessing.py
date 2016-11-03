# strip all whitespace, special characeters and replace numbers by 0
# convert meta data into a dictionary object
# all words are in a list object
import os
import re
from constants import DATA_DIR, MAIL_DIR, META_LINE_LIMIT

authors = os.listdir(DATA_DIR)
authors = authors[1:]
print authors

# for each author
for author in authors:

    current_dir = DATA_DIR + author + MAIL_DIR
    emails = os.listdir(current_dir)

    # for all sent mails
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
        print meta_data
        print message
    break