from TrieNode import TrieNode

class Trie:    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()    

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        current = self.root 
        for letter in word:
            index = ord(letter) - ord('a')
            if not current.children[index]:
                current.children[index] = TrieNode()
            current = current.children[index]
        current.isLeaf = True

    def formWords(self, letters, centerLetter):
        """
        Generate a list of valid words that can be formed using the given letters
        and that contain the center letter at least once.
        """
        words = []

        def dfs(node, containsCenterLetter, curWord):
            if(node.isLeaf and containsCenterLetter):
                words.append(curWord)
            for letter in letters:
                index = ord(letter) - ord('a')
                if node.children[index]:
                    dfs(node.children[index], containsCenterLetter or (letter == centerLetter), curWord + letter)

        dfs(self.root, False, "")

        return words