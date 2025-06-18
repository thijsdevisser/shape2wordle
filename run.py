import numpy as np
from utils import shape2wordle, plot, shape_dict

answer = 'plaid'
shape = 'uhh'
shape_dict = shape_dict()
colour = 0


shape = shape2wordle(answer, shape, colour, shape_dict)
plot(shape)