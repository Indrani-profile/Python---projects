import random

def create_word_list(words):
    """Creates a list of words to be used in the crossword puzzle"""
    return random.sample(words, 5)

def generate_crossword(word_list):
    """Generates a crossword puzzle based on the provided word list"""
    grid = [['' for _ in range(5)] for _ in range(5)]

    for word in word_list:
        # Code to place the word in the grid goes here
        # ...

    return grid

def display_crossword(grid):
    """Displays the crossword puzzle grid"""
    for row in grid:
        print(' '.join(row))

if __name__ == "__main__":
    words = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'lemon', 'mango', 'nectarine', 'orange', 'papaya', 'peach', 'pineapple', 'plum', 'raspberry', 'strawberry', 'tangerine', 'ugli fruit', 'vanilla', 'watermelon']
    word_list = create_word_list(words)
    crossword = generate_crossword(word_list)
    display_crossword(crossword)
