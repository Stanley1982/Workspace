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
    hb: m
    hm: m
    scenario: 1-dense urban 2-urban 3-suburban 4-rural
    """

    if scenario == 1:
        a_hm = 3.2 * math.log(11.75 * hm, 10) ** 2 - 4.97
        c_correct = 0
    elif scenario == 2:
        a_hm = (1.1 * math.log(f, 10)-0.7)*hm - (1.56*math.log(f, 10)-0.8)
        c_correct = 0
    elif scenario == 3:
        a_hm = 0
        c_correct = 2 * math.log(f/28.0, 10) ** 2 + 5.4
    elif scenario == 4:
        a_hm = 0
        c_correct = 4.78 * math.log(f, 10) ** 2 - 18.33 * math.log(f, 10) + 40.98
    else:
        print ("scenario setting is wrong should between 1 to 4")
        exit()

    path_temp = 69.55 + 21.16 * math.log(f, 10) - 13.82 * math.log(hb, 10) + (44.9-6.55 * math.log(hb, 10))*math.log(d, 10)

    add = - a_hm - c_correct

    path = path_temp + add

    return path
