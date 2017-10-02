from __future__ import division
import pickle
import time
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials
from pprint import pprint
import hyperopt.pyll.stochastic
from hyperopt import fmin, tpe
import hyperopt
import sys
import time
from search_color import Search_Color
from sample_color import sample_color
from config import *
from color_space import *
import os

min = 1
state = ''
# define an objective function
def objective(args):
    global min
    global state
    global color
    global log


    threshold, roiScale, filtratio = args[0:3]
    color_param = args[3:]
    color_param = [int(param) for param in color_param]

    thr = 0.1 + threshold * 0.05

    total,this_color_count,fp,fn = sample_color(thr, roiScale, filtratio, color_param,color)
    tp = total - fp - fn
    beta = 10

    f1_score = float(((1 + beta**2) * tp)) / ((1 + beta**2)*tp + beta**2 * fn + fp)

    if(1 - f1_score < min):
        min = 1 - f1_score
        state = {
            'color'      :   color,
            'Total_frame':   total,
            'Color_frame':   this_color_count,
            'f1_score':      round(1-f1_score,3),
            'fp':            round(fp/(total-this_color_count),3),
            'fn':            round(fn/this_color_count,3),
            'thr':           thr,
            'roiScale':      roiScale,
            'filtratio':     filtratio,
            'color_param':   color_param,

        }
        with open(os.path.join('log',color + log_subfix), "a") as res_log:
            pprint(state, res_log)
        pprint(state)
        print('\n')

    return {
        'loss': 1-f1_score,
        'status': STATUS_OK,
        'eval_time':time.time()
    }

for color in color2opt:
    if color in colorset:
        print color

        space = base_space + color_space_dict['color_space_' + color]

        #pprint(trials.trials)
        print('\n')

        trials = Trials()
        best = fmin(objective, space, algo=tpe.suggest, max_evals=6000,trials= trials)

        pprint(best)
        print('\n')

        pprint(trials.losses())
        #pprint(hyperopt.space_eval(space, best))
        print('\n')
