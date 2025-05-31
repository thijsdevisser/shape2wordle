import numpy as np
from utils import get_guesses_test, plot, shape_dict

answer = 'maria'
shape = 'alien'
shape_dict = shape_dict()
colour = 2

shape = get_guesses_test(answer, shape, colour, shape_dict)
plot(shape)