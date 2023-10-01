import pandas as pd
import matplotlib.pyplot as plt

c = pd.read_csv('terms.csv')

pname = c['program_code'].head(8)
c_hr = c['cumulative_credit_hours'].head(8)

plt.barh(pname, c_hr, color='#0077b5')

plt.title('Top 8 Programs by Cumulative Credit Hours', fontweight='bold')
plt.xlabel('Cumulative Credit Hours', labelpad=10)
plt.ylabel('Program Code', labelpad=10)

# Show the plot
plt.show()
