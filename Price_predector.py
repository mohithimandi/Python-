from sklearn.linear_model import LinearRegression
import numpy as np

# sample data (car age vs price)
age = np.array([[1], [2], [3], [4], [5]])
price = np.array([800000, 700000, 600000, 500000, 400000])

model = LinearRegression()
model.fit(age, price)

new_age = int(input("Enter car age: "))
predicted_price = model.predict([[new_age]])

print("Predicted Car Price:", predicted_price[0])
