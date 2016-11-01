import os


directory = "/Users/Vishal/Intuit/dataset/"
folder = "/_sent_mail"
authors = os.listdir(directory)
authors = authors[1:]

# converting to lower case
for author in authors:
    current_dir = directory + author + folder
    emails = os.listdir(current_dir)
    for email in emails:
        txt = open(current_dir + "/" + email)
        print txt.read()
        break
    break