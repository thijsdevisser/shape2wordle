import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import string

def shape2wordle(answer, desired_shape, colour, shape_dict):
    guesses = [0, 0, 0, 0, 0, 0]
    shape = [0, 0, 0, 0, 0, 0]

    with open('valid-wordle-words.txt', 'r') as file:
        for line in file:
            word = line.strip()
            if word == answer:
                continue
            letter_score = []
            counter = {letter: 0 for letter in string.ascii_lowercase}

            for i, letter in enumerate(word): 
                amount = 0
                for position in answer:
                    if letter == position:
                        amount += 1
                        
                if letter == answer[i]:
                    letter_score.append(2)
                    counter[letter] += 1 

                elif letter in answer and counter[letter] < amount:
                    letter_score.append(1)
                    counter[letter] += 1
                else:
                    letter_score.append(0)

            word_shape = np.array(letter_score, dtype = int)
            for i, row in enumerate(shape_dict[desired_shape]):
                if colour == 0:
                    row_mask = row != 0
                    word_shape_mask = word_shape != 0
                    if np.all(row_mask == word_shape_mask):
                        guesses[i] = word
                        shape[i] = word_shape
                elif colour == 1:
                    if np.all(row == word_shape) and 2 not in word_shape:
                        guesses[i] = word
                        shape[i] = word_shape
                elif colour == 2:
                    row[row == 1] = 2
                    if np.all(row == word_shape) and 1 not in word_shape:
                        guesses[i] = word
                        shape[i] = word_shape

                if all(guess != 0 for guess in guesses):
                    print(guesses)
                    print("Solution found!")
                    return shape
    print("No solution found.")
    return 

def plot(shape):
    cmap = ListedColormap(['gray', 'goldenrod', 'green'])
    plt.figure(figsize=(4, 2))  
    plt.imshow(shape, cmap=cmap, vmin=0, vmax=2)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.show()
    return

def shape_dict():
    shape_dict = {
        'heart': np.array([
            [0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [0, 1, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0]
        ]),
        'checkers': np.array([
            [0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1]
        ]),
        'doggy': np.array([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 0, 0, 1, 1],
            [0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0]
        ]),
        'smiley': np.array([
            [0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0]
        ]),
        'arrow_up': np.array([
            [0, 0, 1, 0, 0],
            [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 1],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0]
        ]),
        'letter_a': np.array([
            [0, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0]
        ]),
        'alien': np.array([
            [0, 1, 0, 1, 0],
            [1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1],
            [0, 1, 0, 1, 0],
            [1, 0, 0, 0, 1]
        ]),
        'rocket': np.array([
            [0, 0, 1, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0],
            [1, 0, 0, 0, 1]
        ]),
        'among_us': np.array([
            [0, 1, 1, 1, 0],
            [0, 1, 0, 0, 0],
            [1, 1, 1, 1, 0],
            [1, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0]
        ]),
        'uhh': np.array([
            [1, 0, 1, 1, 1],
            [1, 0, 1, 0, 0],
            [1, 1, 1, 1, 1],
            [0, 0, 1, 0, 1],
            [1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0]
        ]),
    }
    return shape_dict