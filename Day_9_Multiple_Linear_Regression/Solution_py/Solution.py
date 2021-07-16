import numpy as np


def center(X, meanX, a=None):
    return X - np.mean(meanX, axis=a)


def calBeta(X_R, Y_R):
    return np.dot(np.linalg.inv(np.dot(X_R.T, X_R)), np.dot(X_R.T, Y_R))


def predict(X_new, X, Y):
    X_R = center(X, X, a=0)
    Y_R = center(Y, Y)
    beta = calBeta(X_R, Y_R)
    X_new_R = center(X_new, X, a=0)
    Y_new_R = np.dot(X_new_R, beta)
    return [round(elem, 2) for elem in list(map(float, Y_new_R + np.mean(Y)))]


if __name__ == "__main__":
    m, n = list(map(int, input().strip().split()))
    X = []
    Y = []
    for i in range(n):
        data = list(map(float, input().strip().split()))
        X.append(data[:m])
        Y.append(data[m:])
    q = int(input().strip())
    X_new = []
    for x in range(q):
        X_new.append(list(map(float, input().strip().split())))

    # print
    for i in predict(X_new, X, Y):
        print(i)
