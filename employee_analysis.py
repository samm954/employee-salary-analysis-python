import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("employee_data.csv")
print(df)

#calculate department wise salary 
dept_salary=df.groupby("Department")["Salary"].mean()
print(dept_salary)

#find hieghest
highest_salary=df.loc[df["Salary"].idxmax()]
print("Highest Salary Employee:")
print(highest_salary) 

#graph
plt.figure(figsize=(5,3))
dept_salary.plot(kind="bar")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.savefig("salary_graph.png")
plt.show()