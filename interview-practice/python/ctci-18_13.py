#!/usr/bin/env python
__author__ = 'julenka'
''' Finds the largest 'word rectangle' that can be made from words in text file
common path is /usr/share/dict/words
'''
from collections import defaultdict
from marisa_trie import Trie, RecordTrie

class WordRect:
    def __init__(self, trie, rows, cols):
        self.rows = []
        self.trie = trie
        self.num_rows = rows
        self.num_cols = cols

    def isComplete(self):
        # print len(self.rows), self.num_rows
        # print self
        return len(self.rows) == self.num_rows

    def isValid(self):
        for c in xrange(self.num_cols):
            prefix = self.getColumn(c)
            if len(self.trie.keys(unicode(prefix))) == 0:
                return False
        return True

    def addRow(self, word):
        self.rows.append(word)

    def removeLast(self):
        del self.rows[-1]

    def getColumn(self, col):
        return "".join((r[col] for r in self.rows))

    def __str__(self):
        return "\n".join([ "".join(row) for row in self.rows])
#

def factors(n):
    return (reduce(list.__add__,
                ([[i, n//i]] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def makeRect(word_bank, word_rect):
    if(word_rect.isComplete()):
        return word_rect
    for word in word_bank:
        word_rect.addRow(word)
        if(word_rect.isValid()):
            result = makeRect(word_bank, word_rect)
            if result:
                return result
        word_rect.removeLast()
    return None

def findLargestWordSquare(word_list_path, max_len):
    # we are working in unicode because that's what the trie library wants
    words = [unicode(x.strip().lower()) for x in open(word_list_path).readlines()]
    trie =  Trie(words)

    # build map from word length to words that are this length
    len_to_words = defaultdict(list)
    for word in words:
        if(len(word) > max_len):
            continue
        len_to_words[len(word)].append(word)

    max_len = max(len_to_words.keys())
    max_area = pow(max_len, 2)

    for area in xrange(max_area, 1, -1):
        print area, "..."
        # iterate over all possible numbers of rows, cols that can lead to given area.
        # note that max word length is max_len so cols must be at most max_len
        for (n_rows, n_cols) in ((f1, f2) for (f1, f2) in factors(area) if f2 <= max_len):
            word_rect = makeRect(len_to_words[n_cols], WordRect(trie, n_rows, n_cols))
            if word_rect:
                return word_rect

    return None

    # go from larges to smallest word length...
    # for word_length in word_lengths:
    #     if word_length > max_len:
    #         continue
    #     print word_length
    #     words = len_to_words[word_length]
    #     row_to_words = getRowToWords(words)
    #     row_to_words_trie = {}
    #     for i, words in row_to_words.iteritems():
    #         row_to_words_trie[i] = Trie(words)
    #
    #     if(len(row_to_words) != word_length):
    #         # if we can't fill in every row, then continue
    #         continue
    #
    #     # use the trie to quickly find words that share prefix
    #     trie =  Trie(words)
    #     wordSquare = WordSquare(word_length)
    #     result = findLargestHelper(wordSquare, trie, row_to_words, 0, 0)
    #     if(result):
    #         print result
    #         return
    # print "no word square found"


def main(args):
    if len(args) < 1:
        print "usage: {0} [word list]"
    debug_path = '/usr/share/dict/words'
    print findLargestWordSquare(sys.argv[1], int(sys.argv[2]))
    # findLargestWordSquare(debug_path, max_len)

if __name__ == "__main__":
    import sys
    main(sys.argv)



# def findLargestHelper(wordSquare, trie, row_to_words, row, col):
#     if(row >= wordSquare.size):
#         return wordSquare
#     # print row, col
#     # guess a value from set of words that are valid
#     row_prefix = unicode(wordSquare.getRow(row))
#     possible_row_characters = getKeysFromTrie(trie,row_prefix, col)
#     col_prefix = unicode(wordSquare.getColumn(col))
#     possible_col_characters = getKeysFromTrie(trie, col_prefix, row)
#     possible_characters = possible_col_characters & possible_row_characters
#     for c in possible_characters:
#         wordSquare.setChar(row, col, c)
#         newCol = col + 1
#         newRow = row
#         if(newCol >= wordSquare.size):
#             newCol = 0
#             newRow = row + 1
#         result = findLargestHelper(wordSquare, trie, row_to_words, newRow, newCol)
#         if(result):
#             return result
#     wordSquare.setChar(row, col, "")
#     return None

