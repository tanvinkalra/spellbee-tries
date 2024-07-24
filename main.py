from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time
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

    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    driver.get("https://spellbee.org/")

    hexLinks = driver.find_elements(By.CSS_SELECTOR, 'a.hexLink')
    letters = []
    centerLetter = None


    # Loop through each <a> tag and find <p> tags within it
    for aTag in hexLinks:
        aId = aTag.get_attribute('id')
            
        p_tags = aTag.find_elements(By.TAG_NAME, 'p')
        for p in p_tags:
            letter = p.text.lower() 
            if aId == "center-letter":
                centerLetter = letter
            letters.append(letter)
    

    trie = Trie()
    words = readWordsFromFile('enable1.txt')
    for word in words:
        trie.insert(word)

    validWords = trie.formWords(letters, centerLetter)

    driver.execute_script("document.getElementById('testword-value').type = arguments[0];", 'visible')
    submitButton = driver.find_element(By.ID, 'submit_button')

    # Iterate over the list of words and interact with the input field
    for word in validWords:
        driver.execute_script("document.getElementById('testword-value').value = arguments[0];", word)
        submitButton.click()
        time.sleep(1)
