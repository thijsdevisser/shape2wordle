import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def get_green_guesses(answer, desired_shape, shape_dict):
    guesses = [0, 0, 0, 0, 0, 0]
    shape = [0, 0, 0, 0, 0, 0]
    with open('valid-wordle-words.txt', 'r') as file:
        for line in file:
            word = line.strip()
            letter_score = []

            for j, letter in enumerate(word): 

                if letter == answer[j]:
                    letter_score.append(2) 

                else:
                    letter_score.append(0)

            word_shape = np.array(letter_score)

            for i, row in enumerate(shape_dict[desired_shape]):

                row_mask = row != 0
                word_shape_mask = word_shape != 0

                if np.all(row_mask == word_shape_mask):
                        guesses[i] = word
                        shape[i] = word_shape

                        if all(guess != 0 for guess in guesses):
                            return True, guesses, shape
    return False, [], []

def get_guesses_test(answer, desired_shape, colour, shape_dict):
    guesses = [0, 0, 0, 0, 0, 0]
    shape = [0, 0, 0, 0, 0, 0]

    with open('valid-wordle-words.txt', 'r') as file:
        for line in file:
            word = line.strip()
            letter_score = []
            counter = 0

            for i, letter in enumerate(reversed(word)): 
                index = 4 - i
                amount = 0
                for position in answer:
                    if letter == position:
                        amount += 1
                        
                if letter == answer[index]:
                    letter_score.append(2)
                    counter += 1 

                elif letter in answer and counter < amount:
                    letter_score.append(1)
                    counter += 1
                else:
                    letter_score.append(0)

            word_shape = np.array(letter_score, dtype = int)[::-1]
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
                    return True, guesses, shape
    return False, [], []

def last_resort(answer, desired_shape, shape_dict):
    guesses = [0, 0, 0, 0, 0, 0]
    shape = [0, 0, 0, 0, 0, 0]

    with open('valid-wordle-words.txt', 'r') as file:
        for line in file:
            word = line.strip()
            letter_score = []
            counter = 0
            for j, letter in enumerate(reversed(word)): 
                index = 4 - j
                amount = 0
                for position in answer:
                    if letter == position:
                        amount += 1
                        
                if letter == answer[index]:
                    letter_score.append(2)
                    counter += 1 

                elif letter in answer and counter < amount:
                    letter_score.append(1)
                    counter += 1
                else:
                    letter_score.append(0)

            word_shape = np.array(letter_score)[::-1]

            for i, row in enumerate(shape_dict[desired_shape]):
            
                row_mask = row != 0
                word_shape_mask = word_shape != 0

                if np.all(row_mask == word_shape_mask):
                    guesses[i] = word
                    shape[i] = word_shape

                    if all(guess != 0 for guess in guesses):
                        return True, guesses, shape
    return False, [], []

def get_guesses(answer, desired_shape, shape_dict):

    # green_found, green_guesses, green_shape = get_green_guesses(answer, desired_shape, shape_dict)
    # if green_found:

    #     print("Green guess found")
    #     print(green_guesses)

    #     cmap = ListedColormap(['gray', 'yellow', 'green'])
    #     plt.figure(figsize=(4, 2))  
    #     plt.imshow(green_shape, cmap=cmap)
    #     plt.xticks([])
    #     plt.yticks([])
    #     plt.grid(False)
    #     plt.show()
    #     return green_guesses, green_shape
    
    orange_found, orange_guesses, orange_shape = get_guesses_test(answer, desired_shape, shape_dict)
    if orange_found:
        print("Orange guess found")
        print(orange_guesses)

        cmap = ListedColormap(['gray', 'yellow', 'green'])
        plt.figure(figsize=(4, 2))  
        plt.imshow(orange_shape, cmap=cmap)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.show()
        return orange_guesses, orange_shape
    
    last_resort_found, last_resort_guesses, last_resort_shape = last_resort(answer, desired_shape, shape_dict)
    if last_resort_found:
        print("Last resort found")
        print(last_resort_guesses)

        cmap = ListedColormap(['gray', 'yellow', 'green'])
        plt.figure(figsize=(4, 2))  
        plt.imshow(last_resort_shape, cmap=cmap)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.show()
        return last_resort_guesses, last_resort_shape

    print("No guesses found")
    return [], []  

