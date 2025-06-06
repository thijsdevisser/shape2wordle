import numpy as np
from utils import shape2wordle, plot, shape_dict

answer = 'cease'
shape = 'heart'
shape_dict = shape_dict()
colour = 2

shape = shape2wordle(answer, shape, colour, shape_dict)
plot(shape)