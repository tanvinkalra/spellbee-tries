# spellbee-tries

## Overview
This project aims to solve the Spelling Bee game efficiently by utilizing a Trie data structure, a search algorithm, and Selenium for automated interaction with the game's webpage. The goal is to automate the process of forming valid words using a given set of characters and then enter those words into the game to maximize the score.

### How It Works

- **Trie Data Structure**: A Trie is used to store and search a [large corpus of words](https://github.com/dolph/dictionary). This allows for efficient retrieval of words that can be formed using a given set of characters.
- **Search Algorithm**: Custom search algorithms are implemented to find all possible valid words that can be formed using the characters of the day plus the central character.
- **Web Automation with Selenium**: Selenium is used to interact with the game's webpage. It retrieves the characters of the day and the central character, enters the words formed by the search algorithm, and simulates clicking the submit button to submit the words.
