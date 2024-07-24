from Trie import Trie

def readWordsFromFile(file_path):
    """
    Reads words from a given file, one per line, and returns a list of words
    that are at least 4 characters long.
    """
    words = []
    with open(file_path, 'r') as file:
        for line in file:
            word = line.strip() 
            if len(word) >= 4:
                words.append(word)
    return words

if __name__ == "__main__":

    trie = Trie()
    words = readWordsFromFile('enable1.txt')
    for word in words:
        trie.insert(word)
    
    letters = "arwihos"
    centerLetter = "s"

    valid_words = trie.formWords(letters, centerLetter)
    print(valid_words)