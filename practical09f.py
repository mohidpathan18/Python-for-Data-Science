import pandas as pd
print("Name: Pathan Mohid")
print("Roll No: S102")
print()
df = pd.read_csv(r"D:\mohid\python for data secinece\students (5).csv")
df["Result"] = df["Marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

df["Grade"] = df["Marks"].apply(calculate_grade)

print("Dataset with Result and Grade:")
print(df)
