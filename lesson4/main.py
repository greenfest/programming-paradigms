import math


def mean(data):
    return sum(data) / len(data)


def covariance(x, y):
    n = len(x)
    mean_x = mean(x)
    mean_y = mean(y)
    return sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))


def correlation(x, y):
    covar = covariance(x, y)
    std_dev_x = math.sqrt(sum((xi - mean(x)) ** 2 for xi in x))
    std_dev_y = math.sqrt(sum((yi - mean(y)) ** 2 for yi in y))

    if std_dev_x * std_dev_y == 0:
        return 0

    return covar / (std_dev_x * std_dev_y)


x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6]

correlation_value = correlation(x, y)
print(f"Корреляция Пирсона: {correlation_value}")
