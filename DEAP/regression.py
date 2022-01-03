import numpy as np

targetPath = 'C:\\Users\\aleks\\OneDrive\\Pulpit\\data_preprocessed_python\\'

file_x = targetPath + 'asdf.csv'
# file_x = targetPath + 'fftValues.csv'
# labelFile0 = targetPath + '0.csv'
# labelFile1 = targetPath + '1.csv'
labelFile0 = targetPath + 'labels_252_0_01.dat'
labelFile1 = targetPath + 'labels_252_1_01.dat'



from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import mean_squared_error, r2_score
from scipy import stats


def shuffle_data(x, y):
    idx = np.random.permutation(len(x))
    x_data= x[idx]
    y_labels=y[idx]
    return x_data, y_labels

def regression(file_y):
    mae, rmse, p = 0.0, 0.0, 0.0
    X = np.genfromtxt(file_x, delimiter=' ')
    y = np.genfromtxt(file_y, delimiter=' ')
    for i in range(10):
        d, l = shuffle_data(X, y)

        X_train, X_test, y_train, y_test = train_test_split(d, l, test_size=0.3, random_state=42)

        regressor = LinearRegression()
        regressor.fit(X_train, y_train)

        y_pred = regressor.predict(X_test)

        rmse += np.sqrt(mean_squared_error(y_test, y_pred))
        # rscore += regressor.score(X_test, y_test)
        mae += metrics.mean_absolute_error(y_test, y_pred)
        fvalue, pvalue = stats.ttest_ind(y_test, y_pred, equal_var=False)
        p += pvalue
    print("RMSE:", rmse / 10.0)
    print("MAE:", mae / 10.0)
    print("pValue:", p / 10.0)

print('Valence:')
regression(labelFile0)
print('Arousal:')
regression(labelFile1)


