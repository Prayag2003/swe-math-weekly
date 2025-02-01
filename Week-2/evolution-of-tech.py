import numpy as np
import pandas as pd

dataset = pd.read_csv("data.csv", header=None)
X_prev = dataset.iloc[:, :2].values  
Y_next = dataset.iloc[:, 2:].values

creators = pd.read_csv("creators.csv", header=None)
X_current = creators.values 

# A= (((XT).X) ^ (−1)) .(XT).Y
A = np.linalg.inv(X_prev.T @ X_prev) @ X_prev.T @ Y_next
print("Transformation matrix A:")
print(A)

def predict(A, x0, k):
    eigenvalues, eigenvectors = np.linalg.eig(A)
    return eigenvectors @ np.diag(eigenvalues ** k) @ np.linalg.inv(eigenvectors) @ x0

k = 4
final_states = np.array([predict(A, x0, k) for x0 in X_current])

highest_tech_index = np.argmax(final_states[:, 0])
print(f"Index of Creator with highest technical depth after 4 weeks: {highest_tech_index}")

highest_entertainment_index = np.argmax(final_states[:, 1])
print(f"Index of Creator with highest entertainment value after 4 weeks: {highest_entertainment_index}")

switched_tech_to_entertainment = []
switched_entertainment_to_tech = []

for i in range(len(X_current)):
    tech_initial, entertainment_initial = X_current[i]
    tech_final, entertainment_final = final_states[i]

    if tech_initial > entertainment_initial and tech_final < entertainment_final:
        switched_tech_to_entertainment.append(i)
    elif entertainment_initial > tech_initial and entertainment_final < tech_final:
        switched_entertainment_to_tech.append(i)

print(f"Creators who switched from tech-focused to entertainment-focused: {switched_tech_to_entertainment}")
print(f"Creators who switched from entertainment-focused to tech-focused: {switched_entertainment_to_tech}")
