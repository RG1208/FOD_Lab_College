import pandas as pd
from faker import Faker
import random

fake = Faker()

num_records = 10

data = {
    "ID": [],
    "Name": [],
    "Age": [],
    "Grade": [],
    "Major": []
}

grades = ["A", "B", "C", "D", "F"]
majors = ["Computer Science", "Mathematics", "Physics", "Chemistry", "Biology", "Engineering", "Economics"]

for i in range(1, num_records + 1):
    data["ID"].append(i)
    data["Name"].append(fake.name())
    data["Age"].append(random.randint(18, 25))  
    data["Grade"].append(random.choice(grades))  
    data["Major"].append(random.choice(majors))  

df = pd.DataFrame(data)
df.to_csv("students.csv", index=False)
print("Fake data saved to students.csv")

print("\nStudent Information Dataset:")
print(df)
