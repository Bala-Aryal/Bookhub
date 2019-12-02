class KeywordTrie:
    '''
    This trie is used for efficient lookup of words in a book description
    in order to look for keywords on a character by character basis.
    The trie keeps track of where it is between calls of searchWord()
    so keywords that are more than just one word long can be used

    '''

    def __init__(self):
        self.trie = {}     # The entire trie is created using dictionaries
        self.end_key = '!' # An arbitrary special character used to mark the end of a keyword
        self.curr_node = self.trie #This variable is used to store the current character it is on

    def insertIntoTrie(self, word, genre, score):
        # Inserts word into trie
        # Returns nothing
        i,W,node = 0, len(word),self.trie
        while i < W:
            node = node.setdefault(word[i],{})
            i+=1
        # A tuple is inserted with the end_key as its key
        node.setdefault(self.end_key,[]).append((genre,score))

    def searchSingleWord(self, word):
        #In the case that there is a continuing phrase, this function
        #will do the same search without continuation
        i, W, curr_node, out = 0, len(word), self.trie, []
        while i < W:
            if word[i] not in curr_node:
                break
            curr_node = curr_node[word[i]]

            if self.end_key in curr_node:
                out.extend(curr_node[self.end_key])
            i += 1
        return out #An array of tuples with genre as well as the score

    def searchWord(self, word):
        #The main search function, will search the trie and keep track
        #of its location in the trie as it is called upon repeatedly
        i, W, curr_node, out = 0, len(word), self.curr_node, []
        continuing = curr_node != self.trie
        while i < W:
            if word[i] not in curr_node: #Reset to beginning of the trie
                if word[i] in self.trie:
                    curr_node = self.trie[word[i]]
                else:
                    curr_node = self.trie

                if not i: #Continuation breaks if the first character not found in current node
                    continuing = False
            else:
                curr_node = curr_node[word[i]]

            if self.end_key in curr_node:
                out.extend(curr_node[self.end_key])
            i += 1

        #The continuation clause between words
        if ' ' in curr_node:
            self.curr_node = curr_node[' ']
        else:
            self.curr_node = curr_node

        if continuing:
            # If the phrase is still continuing, then search
            # the individual word as well
            out += self.searchSingleWord(word)

        return out
