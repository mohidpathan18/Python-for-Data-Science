import pandas as pd
print("Name: Pathan Mohid")
print("Roll No: S102")
print()
data = {
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Amit", "Sneha", "Rahul", "Priya",
             "Neha", "Rohan", "Pooja", "Karan"],
    "Age": [19, 20, 19, 21, 20, 19, 21, 20],
    "Gender": ["Male", "Female", "Male", "Female",
               "Female", "Male", "Female", "Male"],
    "Course": ["BSc CS", "BSc CS", "BSc IT", "BSc CS",
               "BSc IT", "BSc CS", "BSc IT", "BSc CS"],
    "Marks": [78, 85, 67, 92, 88, 74, 81, 69]
}
df = pd.DataFrame(data)
print("Complete Dataset:")
print(df)
print("\nFirst 5 Records:")
print(df.head(5))
print("\nLast 5 Records:")
print(df.tail(5))
print("\nNumber of Rows and Columns:")
print(df.shape)
print("\nColumn Names:")
print(df.columns)
print("\nBasic Information:")
df.info()
print("\nStatistical Information:")
print(df.describe())
