import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

california_housing = fetch_california_housing()

data = pd.DataFrame(california_housing.data, columns=california_housing.feature_names)
target = california_housing.target

print("Print first 10 rows of California Housing data:")
print(data.head(10))

X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)


print(f"Mean Squared Error: {mse}")
print(f"R² Score: {r2}")

plt.scatter(y_test, y_pred, alpha=0.5)
plt.title('Actual vs Predicted Housing Prices')
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.show()
