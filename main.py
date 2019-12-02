import sys
import csv
import json
from KeywordTrie import KeywordTrie
from Scores import ScoreBoard

trie = KeywordTrie()

#parse CRV file
with open(sys.argv[1], 'r') as csv_file:
    text = csv.reader(csv_file)
    for row in text:
        genre, key_phrase, score = row[0].strip(), row[1].strip(), int(row[2].strip())
        #Building a char by char trie
        trie.insertIntoTrie(key_phrase, genre, score)


score_boards = []

#parse books file
with open(sys.argv[2]) as json_file:
    books = json.load(json_file)
    # 1. ITERATE THROUGH BOOKS
    for index,book in enumerate(books):
        description = book['description'].split()
        scores = ScoreBoard(book['title'])
        for idx,word in enumerate(description):
            # print(word)
            search_result = trie.searchWord(word)
            if search_result:
                scores.addScores(search_result)

        score_boards.append(scores)

for board in score_boards:
    print('\n')
    print(board)
    print('\n')
