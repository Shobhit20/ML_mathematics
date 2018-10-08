import numpy as np
from sklearn import datasets, linear_model


def preprocess_X(X):
    theta0 = np.ones((442,1))
    X = np.append(theta0, X, axis=1)
    return X


def cost_function(X, y_hyp, y):
    samples = y.shape[0]
    return (1/(2*samples))*np.sum((X.dot(y_hyp) - y)**2)


def linreg_data_gd(X, y, iters=100000, lr=0.01):
    y_hyp = np.zeros(X.shape[1])
    samples = y.shape[0]

    cost_arr = np.zeros(iters)
    for iter in range(iters):
        y_pred = X.dot(y_hyp)
        grad = X.T.dot(y_pred - y)/samples
        y_hyp = y_hyp - lr*grad
        cost_arr[iter] = cost_function(X, y_hyp, y)
    return y_hyp, cost_arr


def main():
    diabetes = datasets.load_diabetes()
    X = diabetes.data
    X = preprocess_X(X)
    y = diabetes.target
    y_hyp, cost_arr = linreg_data_gd(X, y)
    print("Final Cost - ", cost_function(X, y_hyp, y))
    print("Coefficients for the reg fit are - ", y_hyp)


if __name__=="__main__":
    main()
