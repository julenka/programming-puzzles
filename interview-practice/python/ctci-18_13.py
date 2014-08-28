#!/usr/bin/env python
__author__ = 'julenka'
''' Finds the largest 'word square' that can be made from words in text file
common path is /usr/share/dict/words
'''
from collections import defaultdict
from itertools import product
from marisa_trie import Trie, RecordTrie

class WordSquare:
    def __init__(self, size):
        self.rows = [["" for y in xrange(size)] for x in xrange(size)]
        self.size = size

    def isFull(self):
        return len(self.rows) == self.size

    def setChar(self, row, col, character):
        self.rows[row][col] = character

    def setRow(self, row, word):
        self.rows[row] = list(word)

    def unsetRow(self, row):
        self.rows[row] = ["" for c in xrange(self.size)]

    def getRow(self, row):
        return "".join(self.rows[row])

    def getColumn(self, col):
        return "".join((r[col] for r in self.rows))

    def __str__(self):
        return "\n".join([ "".join(row) for row in self.rows])


def getRowToWords(words):
    ''' Return a map from row->all words that could be in this row
    for row i, each letter in a word must be the ith letter in some other word
    '''
    letter_idx_map = defaultdict(set)
    for word in words:
        for i, c in enumerate(word):
            letter_idx_map[c.lower()].add(i)
            # letter_idx_word_map[c + "," +i].add(word)
    # word -> rows it can be in
    # row -> possible words
    row_to_words = defaultdict(list)
    for word in words:
        # set(indices first char appears in) , set(indices second char appears in), ...
        letter_indices = [letter_idx_map[c] for c in word]
        rows_word_can_be_in = set.intersection(*letter_indices)
        if(len(rows_word_can_be_in) > 0):
            for row in rows_word_can_be_in:
                row_to_words[row].append(word)
    return row_to_words


def findLargestHelper(wordSquare, trie, row_to_words, row_to_words_trie, row, col):
    if(row >= wordSquare.size):
        return wordSquare
    # guess a value from set of words that are valid
    row_prefix = unicode(wordSquare.getRow(row))
    possible_row_characters = set((word[col] for word in row_to_words_trie[row].keys(row_prefix)))
    col_prefix = unicode(wordSquare.getColumn(col))
    possible_col_characters = set((word[row] for word in trie.keys(col_prefix)))
    possible_characters = possible_col_characters & possible_row_characters
    for c in possible_characters:
        wordSquare.setChar(row, col, c)
        newCol = col + 1
        newRow = row
        if(newCol >= wordSquare.size):
            newCol = 0
            newRow = row + 1
        result = findLargestHelper(wordSquare, trie, row_to_words, row_to_words_trie, newRow, newCol)
        if(result):
            return result
    wordSquare.setChar(row, col, "")
    return None



def findLargestWordSquare(word_list_path):
    # we are working in unicode because that's what the trie library wants
    words = [unicode(x.strip()) for x in open(word_list_path).readlines()]

    # build map from word length to words that are this length
    len_to_words = defaultdict(list)
    for word in words:
        len_to_words[len(word)].append(word)

    # assume that if a word length set has less than word length words, this can be skipped
    word_lengths = [k for k,v in len_to_words.iteritems() if len(v) > k]
    word_lengths = list(reversed(sorted(word_lengths)))

    # go from larges to smallest word length...
    for word_length in word_lengths:
        # if word_length > 5:
        #     continue
        print word_length
        words = len_to_words[word_length]
        row_to_words = getRowToWords(words)
        row_to_words_trie = {}
        for i, words in row_to_words.iteritems():
            row_to_words_trie[i] = Trie(words)

        if(len(row_to_words) != word_length):
            # if we can't fill in every row, then continue
            continue

        # use the trie to quickly find words that share prefix
        trie =  Trie(words)
        wordSquare = WordSquare(word_length)
        result = findLargestHelper(wordSquare, trie, row_to_words, row_to_words_trie, 0, 0)
        if(result):
            print result
            return
    print "no word square found"


def main(args):
    if len(args) < 1:
        print "usage: {0} [word list]"
    debug_path = '/usr/share/dict/words'
    # findLargestWordSquare(sys.argv[0])
    findLargestWordSquare(debug_path)

if __name__ == "__main__":
    import sys
    main(sys.argv)



