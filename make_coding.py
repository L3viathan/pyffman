import sys
import pickle
from collections import Counter

def codes(what, prefix=""):
    if len(what) == 2:
        yield (prefix, what[1])
    elif len(what) > 2:
        yield from codes(what[1], prefix+"0")
        yield from codes(what[2], prefix+"1")
    else:
        print(len(what))

with open(sys.argv[1]) as f:
    corpus = f.read()

remaining = [(y,x) for x, y in Counter(corpus).most_common()]

extra_tokens = [
        'def ',
        'return',
        'lambda ',
        'from ',
        'import ',
        "''.join(",
        'print(',
        'map(',
        'min(',
        'max(',
        'input()',
        'range(',
        'len',
        'sorted(',
        'set(',
        'zip(',
        'list(',
        'for ',
        ' in ',
        'if ',
        'else',
        'elif ',
        '.count',
        'not ',
        'any(',
        'all(',
        'sum(',
        ' and ',
        ' or ',
        '.split(',
        '.replace(',
        '.find(',
        '  ',
        '   ',
        ]

remaining.extend([(1, 'END'), *[(corpus.count(token), token) for token in extra_tokens]])

while len(remaining) > 1:
    remaining.sort(reverse=True, key=lambda x: x[0])
    x = remaining.pop()
    y = remaining.pop()
    remaining.append((x[0]+y[0], x, y))

result = remaining[0]

coding = {y:x for x,y in codes(result)}
with open("coding.dat", "wb") as f:
    pickle.dump(coding, f)

for letter in coding:
    print(repr(letter), coding[letter], sep="\t")
