import numpy as np

answer = 'habbit'
desired_shape = 'heart'

def get_guesses(answer, desired_shape):
    guesses = [0, 0, 0, 0, 0, 0]
    shape = [0, 0, 0, 0, 0, 0]
    all_shapes = dict()
    all_shapes["heart"] = np.array([[0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]])
    with open('valid-wordle-words.txt', 'r') as file:
        for line in file:
            word = line.strip()
            letter_score = []
            for j, letter in enumerate(word):
                if letter == answer[j]:
                    letter_score.append(1)
                elif letter in answer:
                    letter_score.append(1)
                else:
                    letter_score.append(0)
            word_shape = np.array(letter_score)
            for i, row in enumerate(all_shapes[desired_shape]):
                    print(row)
                    print(word_shape)
                    print(row == word_shape)
                    if np.all(row == word_shape):
                        guesses[i] = word
                        shape[i] = word_shape
                        if all(guess != 0 for guess in guesses):
                            print(guesses)
                            print(shape[0])
                            print(shape[1])
                            print(shape[2])
                            print(shape[3])
                            print(shape[4])
                            print(shape[5])
                            return

get_guesses(answer, desired_shape)


