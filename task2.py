codes = {}


def freqdict(text):
    """Creates a dictionary of unique letters with frequency number"""
    frequency = {}
    for letter in text:
        if letter not in frequency:
            frequency[letter] = 1
        else:
            frequency[letter] += 1
    return frequency


def sortfreqdict(freqs):
    """Swap keys and values, then sort list based on the key value"""
    letters = freqs.keys()
    sortlist = []
    for i in letters:
        sortlist.append((freqs[i], i))
    sortlist.sort()
    type(sortlist)
    return sortlist


def buildtree(freqlist):
    """Build a tree of tuples and sort items in the end"""
    while len(freqlist) > 1:
        leasttwo = tuple(freqlist[0:2])
        therest  = freqlist[2:]
        combfreq = leasttwo[0][0] + leasttwo[1][0]
        freqlist = therest + [(combfreq, leasttwo)]
        freqlist = sorted(freqlist, key=lambda tup: tup[0])
    return freqlist[0]


def trimtree(tree):
    """Trim the frequency counters off the tree, let's leave just letters"""
    p = tree[1]
    if isinstance(p, str):
        return p
    else:
        return (trimtree(p[0]), trimtree(p[1]))


def codeassign(node, pat=''):
    """Codes may be assigned recursively traversing the tree"""
    global codes
    if isinstance(node, str):
        codes[node] = pat
    else:
        codeassign(node[0], pat + "0")
        codeassign(node[1], pat + "1")


word = input("Enter a desired sentence for encoding: ")
dict_word = freqdict(word)
sorted_dict_word = sortfreqdict(dict_word)
tree = buildtree(sorted_dict_word)
trimmed_tree = trimtree(tree)
codeassigned_tree = codeassign(trimmed_tree)

print(word)
print(sorted_dict_word)
print(codes)



