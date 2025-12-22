import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sample data: Hours studied vs Test scores

data = pd.read_csv('StudentPerformance.csv')

''' print("Study Time (hrs):", study_time_hrs)
print("Test Scores:", test_scores)

print(data)'''

# Mean Squared Error Loss funcion

'''def loss_function(m, b, points):
    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i].Hours_Studied
        y = points.iloc[i].Test_Scores
        total_error += (y - (m * x + b)) ** 2
    
    total_error /= float(len(points))
    return total_error'''

def gradient_descent(m_now, b_now, points, L):
    x = points.hours_studied.values
    y = points.performance_index.values
    n = len(points)

    y_pred = m_now * x + b_now
    error = y - y_pred

    m_gradient = (-2 / n) * np.dot(x, error)
    b_gradient = (-2 / n) * error.sum()

    m = m_now - L * m_gradient
    b = b_now - L * b_gradient

    return m, b


def mse(m, b, points):
    preds = m * points.hours_studied + b
    return ((points.performance_index - preds) ** 2).mean()

m = 0.0
b = 0.0
L = 0.005  # safer learning rate to avoid overflow
epochs = 3000

for i in range(epochs):
    if i % 50 == 0:
        print("Epoch:", i)
        print("  mse:", mse(m, b, data))
    m, b = gradient_descent(m, b, data, L)

    if not (np.isfinite(m) and np.isfinite(b)):
        print("Stopping early due to non-finite parameters.")
        break

print(f"\nFinal parameters: m = {m:.4f}, b = {b:.4f}")
print(f"Final mse: {mse(m, b, data):.4f}")

plt.scatter(data.hours_studied, data.performance_index, color='blue')
x_line = np.linspace(data.hours_studied.min(), data.hours_studied.max(), 100)
plt.plot(x_line, m * x_line + b, color='red')
plt.show()
