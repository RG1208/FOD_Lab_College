# Step 1: Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Step 2: Create a sample dataset (Position level vs Salary)
# Position Level (1, 2, 3, ... 10) vs Salary
# This is a mock dataset simulating years of experience vs salary
levels = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
salaries = np.array([45000, 50000, 60000, 65000, 70000, 80000, 90000, 105000, 120000, 150000])

# Step 3: Apply Polynomial Regression
# We will use PolynomialFeatures to create higher-degree features
degree = 4  # You can try different degrees for better fit
poly_reg = PolynomialFeatures(degree=degree)

# Step 3a: Transform the feature matrix into polynomial features
X_poly = poly_reg.fit_transform(levels)

# Step 3b: Fit Linear Regression model on transformed features
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, salaries)

# Step 4: Make predictions
# Let's predict salary for levels 6.5, 8.5, and 9.5 (these might not be in the original dataset)
predicted_salary = lin_reg_2.predict(poly_reg.transform([[6.5], [8.5], [9.5]]))
print(f"Predicted salaries for levels 6.5, 8.5, and 9.5: {predicted_salary}")

# Step 5: Visualization
# Plotting the original data points
plt.scatter(levels, salaries, color='red')

# Plotting the polynomial regression curve
plt.plot(levels, lin_reg_2.predict(poly_reg.transform(levels)), color='blue')

plt.title('Polynomial Regression: Position Level vs Salary')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
