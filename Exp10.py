import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


data = {
        "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"],
        "Python": [85, 67, 91, 73, 88, 75, 94, 78, 84, 89],
        "Java": [78, 89, 62, 85, 90, 76, 88, 70, 95, 87],
        "C": [92, 76, 88, 77, 79, 81, 85, 82, 80, 83]
    }


df = pd.DataFrame(data)
csv_file = 'students.csv'

df.to_csv(csv_file, index=False)
print(f"{csv_file} created with sample data.")


df = pd.read_csv(csv_file)


print("Student Marks Data:")
print(df)

print("\nStatistics:")
mean = df[['Python', 'Java', 'C']].mean()
std_dev = df[['Python', 'Java', 'C']].std()
min_marks = df[['Python', 'Java', 'C']].min()
max_marks = df[['Python', 'Java', 'C']].max()
quantile_1 = df[['Python', 'Java', 'C']].quantile(0.25)
quantile_3 = df[['Python', 'Java', 'C']].quantile(0.75)

print("Mean:\n", mean)
print("\nStandard Deviation:\n", std_dev)
print("\nMinimum Marks:\n", min_marks)
print("\nMaximum Marks:\n", max_marks)
print("\n1st Quantile (25th Percentile):\n", quantile_1)
print("\n3rd Quantile (75th Percentile):\n", quantile_3)
print("\nMaximum Marks in Each Category:\n", max_marks)


subjects = ['Python', 'Java', 'C']
for subject in subjects:
    plt.figure(figsize=(8, 5))
    plt.hist(df[subject], bins=5, color='skyblue', edgecolor='black')
    plt.title(f"Histogram of Marks in {subject}")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig('/home/rachit/projects/FOD_LAB_College/plot.png')
    plt.show()
