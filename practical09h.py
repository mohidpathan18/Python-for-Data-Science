import pandas as pd

print("Name: Pathan Mohid")
print("Roll No: S102")
print()

df = pd.read_csv(r"D:\mohid\python for data secinece\students (5).csv")

print("Number of Students in Each Course:")
print(df.groupby("Course")["Name"].count())

print("\nAverage Marks by Course:")
print(df.groupby("Course")["Marks"].mean())

print("\nMaximum Marks by Course:")
print(df.groupby("Course")["Marks"].max())

print("\nAverage Attendance by Course:")
print(df.groupby("Course")["Attendance"].mean())
