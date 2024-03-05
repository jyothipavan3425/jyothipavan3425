import pandas as pd
# Assuming data_sample.csv is in the same directory
data = pd.read_csv("C:/Users/saibu/OneDrive/Desktop/dv assignment/data.csv")

# Calculate Actual Cost and Sold Price
data["ActualCost"] = data["RawMaterial"] + data["Workmanship"] + data["StorageCost"]
data["SoldPrice"] = data["EstimatedCost"] * 1.1

# Calculate Margin of Profit
data["Margin of Profit"] = data["SoldPrice"] - data["ActualCost"]

# Select desired columns
data = data[["date", "EstimatedCost", "RawMaterial",
              "Workmanship", "StorageCost", "ActualCost",
              "SoldPrice", "Margin of Profit"]]

# Specify the file path for the output CSV file
output_file_path = 'C:/Users/saibu/OneDrive/Desktop/dv assignment/output.csv'

# Save the DataFrame to a CSV file
data.to_csv(output_file_path, index=False)

print(f'Data has been saved to {output_file_path}')