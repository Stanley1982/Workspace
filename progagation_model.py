import math


def free_space_path_loss(d, f):
    """
    free_space_path_loss
    d: km
    f: MHz
    """
    path = 20 * math.log(d, 10) + 20 * math.log(f, 10) + 32.45
    return path


def okumura_model_path_loss(d, f, hb, hm, scenario):
    """
    okumura_model_path_loss
    d: km
    f: MHz
    scenario:1
    """
    if scenario == 1


    path = 69.55 + 21.16 * math.log(d, 10) - 13.82 * math.log(hb, 10) - a_hm + (44.9-6.55*math.log(hb,10))*math.log(10, d)

    return path
