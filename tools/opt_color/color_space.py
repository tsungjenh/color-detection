#config.py
from hyperopt import hp
base_space = [
    hp.uniform('threshold',0,10), #threshold of detection
    hp.uniform('roiScale',4,10), #roi scale
    hp.uniform('filtratio',0.5,0.75),  #mask filter threshold

]
color_space_dict = {
    'color_space_black' : [
        hp.uniform('black_h_lower',15,45),
        hp.uniform('black_h_upper',50,80),
        hp.uniform('black_s_lower', 60,120)
    ],

    'color_space_red' : [
        hp.uniform('red_h_lower',140,160),
        hp.uniform('red_h_upper',200,220),
        hp.uniform('red_s_lower',  30,80),
        hp.uniform('red_v_lower',20,100),
    ],
    'color_space_yellow' : [
        hp.uniform('green_h_lower',18,25),
        hp.uniform('green_h_upper',35,75),
        hp.uniform('yellow_s_lower', 30,80),
        hp.uniform('yellow_v_lower',20,100),
    ],
    'color_space_blue' : [
        hp.uniform('blue_h_lower',70,90),
        hp.uniform('blue_h_upper',120,140),
        hp.uniform('blue_s_lower', 30,80),
        hp.uniform('blue_v_lower',20,100),
    ],
    'color_space_green' : [
        hp.uniform('green_h_lower',36,50),
        hp.uniform('green_h_upper',70,115),
        hp.uniform('green_s_lower', 30,80),
        hp.uniform('green_v_lower',20,100),
    ],
    'color_space_white' : [
        hp.uniform('white_h_lower',170,210),
        hp.uniform('white_h_upper',0,20),
        hp.uniform('white_s_lower', 160,210),
        hp.uniform('white_v_lower',15,60),
    ]
}

colorset    = ['red','yellow','blue','green','white','black',]
color2opt   = ['red','yellow','blue','green','white','black',]
log_prefix         = 'res_log.txt'
