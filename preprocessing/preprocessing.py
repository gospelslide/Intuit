# strip all whitespace, special characeters and replace numbers by 0
# convert meta data into a dictionary object
# all words are in a list object
import os
import re


directory = "/Users/Vishal/Intuit/dataset/"
folder = "/_sent_mail"
authors = os.listdir(directory)
authors = authors[1:]
meta_info = 15

# for each author
for author in authors:

    current_dir = directory + author + folder
    emails = os.listdir(current_dir)

    # for all sent mails
    for email in emails:

        # extract meta data & convert to lower case
        txt = open(current_dir + "/" + "15.")
        meta_data = dict()
        message = list()
        line_no = 0

        for line in txt:

            line_no += 1
            # process meta data
            if line_no <= meta_info:
                content = line.rstrip().split(":")
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
    break