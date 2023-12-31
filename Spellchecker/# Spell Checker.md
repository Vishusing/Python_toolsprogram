 # Spell Checker

This Python script uses the `spellchecker` module to check the spelling of words. It prompts the user to input a word, and then checks if the word is spelled correctly. If the word is spelled incorrectly, it suggests the best spelling and provides a list of possible candidate words.

## Installation

To use this script, you will need to install the `spellchecker` module. You can do this by running the following command in your terminal:

```
pip install spellchecker
```

## Usage

Once you have installed the `spellchecker` module, you can run the script by opening a terminal window and navigating to the directory where the script is saved. Then, type the following command:

```
python spell_checker.py
```

The script will prompt you to input a word to spell check. Type a word and press Enter. The script will then check the spelling of the word and provide feedback.

## Code Explanation

The script is written in Python and uses the `spellchecker` module to check the spelling of words. Here is a step-by-step explanation of the code:

1. The script imports the `SpellChecker` class from the `spellchecker` module.

```python
from spellchecker import SpellChecker
```

2. The script creates an instance of the `SpellChecker` class.

```python
spell = SpellChecker()
```

3. The script enters a while loop that prompts the user to input a word to spell check.

```python
while True:
    word = input('Input a word to spell check: ')
```

4. If the user presses Enter without inputting a word, the loop will break and the script will terminate.

```python
    if word == '':  # not sure, but need a way to kill the program...
        break
```

5. The script converts the input word to lowercase.

```python
    word = word.lower()
```

6. The script checks if the word is spelled correctly using the `in` operator.

```python
    if word in spell:
```

7. If the word is spelled correctly, the script prints a message indicating that the word is spelled correctly.

```python
        print("'{}' is spelled correctly!".format(word))
```

8. If the word is spelled incorrectly, the script uses the `correction` method of the `SpellChecker` class to find
