import pandas as pd

# Read dataset
data = pd.read_csv("../dataset/motor_data.csv")

print(data.head())

print("\nDataset Shape:")
print(data.shape)