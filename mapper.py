#!/usr/bin/env python
import sys

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace #remove lower case
    line = line.strip().lower()

    # split the line into words; splits on any whitespace
    words = line.split()

    # remove stopwords and punctuation
    stopwords = set(['the', 'and', '.', ',', 'i', ';', 'to', 'of', 'you', 'a', 'my', 'that', ':', '!', 'in', 'on', '?', 'is', 'not', 'me', 'you', 'he', 'she', 'it'])

    # output tuples (word, 1) in tab-delimited format
    for word in words:
	if word not in stopwords:
		print '%s\t%s' % (word, "1")
