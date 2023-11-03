import csv

# Data
teams = ["Team"] + ["Patriots"] * 4 + ["Colts"] * 4 + ["Pressure Drop"] + ["0.85", "1.475", "1.175", "1.65", "1225", "0.725", "0.425", "1.175", "1.35", "1.8", "1.375", "0.475", "0.475", "0.275", "0.65", "Shuffled Drop", "1.175", "1.375", "0.85", "0.65", "1.65", "1.225", "0.725", "0.475", "1.475", "0.275", "1.175", "1.8", "0.475", "0.425", "1.35"]

# Create a list of lists to represent rows and columns
data = [teams[i:i + 2] for i in range(0, len(teams), 2)]

# Specify the file name
file_name = "data.csv"

# Write the data to a CSV file
with open(file_name, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data)

print(f"CSV file '{file_name}' has been created successfully.")
