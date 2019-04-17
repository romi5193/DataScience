import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston

# Boston housing dataset
boston = load_boston()

df = pd.DataFrame(boston.data, columns = boston.feature_names)

# x-values are the nitrogen oxide concentration:
X = df[['NOX']]
# Y-values are the prices:
y = boston.target


line_fitter=LinearRegression()
line_fitter.fit(X, y)

y_predict=line_fitter.predict(X)
plt.plot(X, y_predict)



plt.scatter(X, y, alpha=0.4)
plt.title("Boston Housing Dataset")
plt.xlabel("Nitric Oxides Concentration")
plt.ylabel("House Price ($)")
plt.show()
