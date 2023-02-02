import numpy as np


def calculate(list):
    myArr = np.array([list[0:3], list[3:6], list[6:9]])
    flat = myArr.flatten()

    if len(flat) < 9:
        return "List must contain nine numbers."

    mean = [
        myArr.sum(axis=0) / 3,
        myArr.sum(axis=1) / 3,
        flat.sum() / len(flat),
    ]

    variance = [myArr.var(axis=0), myArr.var(axis=1), flat.var()]
    standard_deviation = [myArr.std(axis=0), myArr.std(axis=1), flat.std()]
    maxm = [myArr.max(axis=0), myArr.max(axis=1), flat.max()]
    minm = [myArr.min(axis=0), myArr.min(axis=1), flat.min()]
    summ = [myArr.sum(axis=0), myArr.sum(axis=1), flat.sum()]
    myDic = {
        "mean": mean,
        "variance": variance,
        "standard deviation": standard_deviation,
        "max": maxm,
        "min": minm,
        "sum": summ,
    }
    print(myDic)
    return myDic


calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
