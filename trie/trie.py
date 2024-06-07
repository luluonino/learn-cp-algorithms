class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word: str):
        return self.root.insert(word, 0)

    def search(self, word: str):
        return self.root.search(word, 0)

    def shortestPrefix(self, word: str):
        return self.root.shortestPrefix(word, 0)

    def print(self):
        self.root.print(0)

    def getNode(self, letter: str):
        if letter in self.root.dictionary: 
            return self.root.dictionary[letter]
        else:
            return None

class TrieNode: 
    def __init__(self, char: str):
        self.char = char
        self.dictionary = {}
        self.isWord = False

    def insert(self, word: str, d: int): # d -> depth 
        char = word[d]
        if char not in self.dictionary:
            self.dictionary[char] = TrieNode(char)
        if d == len(word) - 1:            
            self.dictionary[char].isWord = True
            return 
        self.dictionary[char].insert(word, d + 1)

    def search(self, word: str, d: int):
        if d == len(word):
            return self.isWord
        if word[d] not in self.dictionary:
            return False
        else: 
            return self.dictionary[word[d]].search(word, d + 1)
    
    def shortestPrefix(self, word: str, d: int):
        if self.isWord:
            return word[:d]
        elif d == len(word):
            return None
        if word[d] not in self.dictionary:
            return None
        else:
            return self.dictionary[word[d]].shortestPrefix(word, d + 1)

    def print(self, d: int):
        print(f"{d}: {self.char}")
        if self.isWord:
            print(True)
        for letter in self.dictionary:
            self.dictionary[letter].print(d + 1)

    def getNode(self, letter: str):
        if letter in self.dictionary:
            return self.dictionary[letter]
        else:
            return None
