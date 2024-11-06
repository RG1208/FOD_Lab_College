import pandas as pd
from faker import Faker
import random

fake = Faker()

# Define the number of fake records to generate
num_records = 10

# Lists to hold generated data
data = {
    "ID": [],
    "Name": [],
    "Age": [],
    "Grade": [],
    "Major": []
}

# Define possible grades and majors
grades = ["A", "B", "C", "D", "F"]
majors = ["Computer Science", "Mathematics", "Physics", "Chemistry", "Biology", "Engineering", "Economics"]

# Generate fake data
for i in range(1, num_records + 1):
    data["ID"].append(i)
    data["Name"].append(fake.name())
    data["Age"].append(random.randint(18, 25))  # Random age between 18 and 25
    data["Grade"].append(random.choice(grades))  # Random grade
    data["Major"].append(random.choice(majors))  # Random major

# Convert to DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv("students.csv", index=False)
print("Fake data saved to students.csv")

# Read and print the data
print("\nStudent Information Dataset:")
print(df)
