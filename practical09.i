import pandas as pd
import matplotlib.pyplot as plt

print("Name: Pathan Mohid")
print("Roll No: S102")
print()

df = pd.read_csv(r"D:\mohid\python for data secinece\students (5).csv")

plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Marks"])
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(df["Name"], df["Marks"], marker="o")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.title("Student Marks - Line Chart")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df["Marks"], bins=5)
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Marks")
plt.show()

course_count = df["Course"].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(
    course_count,
    labels=course_count.index,
    autopct="%1.1f%%"
)
plt.title("Students by Course")
plt.show()
