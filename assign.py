import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('terms.csv')

print(df)
pname = df['program_code'].head(8)
c_hr = df['cumulative_credit_hours'].head(8)
fig = plt.figure(figsize =(10, 7))
plt.bar(pname[0:10], c_hr[0:10])
# Show Plot
plt.show()