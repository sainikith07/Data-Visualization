import matplotlib.pyplot as plt

# Plotting two columns (e.g., Height vs Index)
plt.plot(df['Index'], df['Height(Inches)'])

plt.title('Height Trend')
plt.xlabel('Index')
plt.ylabel('Height (Inches)')
plt.grid(True)
plt.show()
