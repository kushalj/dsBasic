#%%
import csv
from pathlib import Path
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

# plt.switch_backend('GTK')

dates = []
prices = []


def get_data(filename):
    timepoint = 0
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            date_parts = row[0].split('-')
            # just need the day:
            int_date = int("".join([date_parts[2]]))
            # dates.append(int_date)

            dates.append(timepoint)
            timepoint += 1
            prices.append(float(row[4]))
    return

def predict_price(dates, prices, x):
    dates = np.reshape(dates,(len(dates), 1))

    svr_lin = SVR(kernel='linear', C=1e3)
    svr_poly = SVR(kernel='poly', C=1e3, degree = 2)
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
    svr_lin.fit(dates, prices)
    svr_poly.fit(dates, prices)
    svr_rbf.fit(dates, prices)

    plt.scatter(dates, prices, color='black', label='Data')
    plt.plot(dates, svr_lin.predict(dates), color='green', label='Linear model')
    plt.plot(dates, svr_poly.predict(dates), color='blue', label='Polynomial model')
    plt.plot(dates, svr_rbf.predict(dates), color='red', label='RBF model')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Support Vector Regression')
    plt.legend()
    plt.show()

    return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]

home = str(Path.home())
get_data('%s/Downloads/BTC-USD.csv' % home)

predicted_price = predict_price(dates, prices, len(dates))

print(predicted_price)

