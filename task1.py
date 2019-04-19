import hashlib
import random
import string


def string_gen(n):
    """
    Random string generator
    :param n: number of letters in a string
    :return: string
    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(n))


def substring(s):
    """Function will split string into all possible substrings, keep only unique hashes and return len of the list"""
    subslist = []
    for k in range(1, 1 + len(s)):
        for a in range(1 + len(s) - k):
            h_subs = hashlib.sha1(s[a:a + k].encode('utf-8')).hexdigest()
            if h_subs not in subslist:
                subslist.append(h_subs)
    return len(subslist)


inp_str = string_gen(int(input("Enter number of letters for string: ")))

print("Random string: {}, Unique substrings: {}".format(inp_str, substring(inp_str)))
