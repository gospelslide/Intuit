import cPickle as pickle
import os
import preprocessing 

curr_dir = os.path.dirname(__file__)
read = open(curr_dir + "/saved.p", "rb")
trie = pickle.load(read)

# check if word exists
def has_key(key):
    br = retrieve_branch(key)
    if br == None:
        return False
    else:
        return is_trie_bucket(get_child_branches(br)[0])


def is_trie_bucket(x):
    return isinstance(x, tuple) and len(x) == 2 and isinstance(x[0], str) and isinstance(x[1], list) and len(x[1]) == 1


def is_trie_branch(x):
    return isinstance(x, list)


# Used to return the string stored in the tuple
def get_bucket_key(b):
    return b[0]


# Used to return the weight or value stored in tuple
def get_bucket_val(b):
    return b[1][0]


def get_child_branches(trie):
    if trie == []:
        return []
    else:
        return trie[1:]


# find a branch in trie that is indexed under k.
def retrieve_branch(key):
    if key == '':
        return None
    else:
        tr = trie
        for c in key:
            br = find_child_branch(tr, c)
            if br == None:
                return None
            else:
                tr = br
        return tr


def find_child_branch(trie, c):
    for branch in get_child_branches(trie):
        if branch[0] == c:
            return branch
    return None




