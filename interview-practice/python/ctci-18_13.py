#!/usr/bin/env python
__author__ = 'julenka'
''' Finds the largest 'word square' that can be made from words in text file
common path is /usr/share/dict/words
'''
from collections import defaultdict
from itertools import product

def nthAlphabetic(n):
    return chr(ord('a') + n)

def findLargestWordSquare(word_list_path):

    words = [x.strip() for x in open(word_list_path).readlines()]

    # build map from word length to words that are this length
    len_to_words = defaultdict(list)
    for word in words:
        len_to_words[len(word)].append(word)

    word_lengths = [k for k,v in len_to_words.iteritems() if len(v) > k]
    word_lengths = list(reversed(sorted(word_lengths)))

    # word lengths N that have less than N words cannot be put into a box
    # go from larges to smallest word length...
    for word_length in word_lengths:
        # build map from letter to list of indices that this letter appears
        letter_idx_map = defaultdict(set)
        # map from letter, idx to all words where letter is at index idx
        # letter_idx_word_map = defaultdict(set)
        # list of words that have right length
        words = len_to_words[word_length]
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
        # row,letter -> words words in row r starting with letter x
        # row_letter_to_words = defaultdict(list)
        if(len(row_to_words) == word_length):
            for row, words in row_to_words.iteritems():
                print row, len(words)
            print letter_idx_map
            # print word_length
            # for row, words in row_to_words.iteritems():
            #     for word in words:
            #         row_letter_to_words


            # map from row, word to possible column words

            # row_word_to_column_words = defaultdict(list)
            # for row, words in row_to_words.iteritems():
            #
            #     for word in words:
            #         column_candidates = [letter_idx_word_map[c + "," + row] for c in word]
            #         row_word_to_column_words[row].append(product(column_candidates))
            #
            # all combinations of rows

            # for square in product(*row_to_words.values()):
            #     for col in xrange(word_length):
            #         # word from column in this square
            #         col_word = "".join((square[row][col] for row in xrange(word_length)))
            #         if col_word not in row_to_words[col]:
            #             break
            #     else:
            #         print square
            # for row, words in row_to_words.iteritems():
            #     for row2, words2 in row_to_words.iteritems():

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



