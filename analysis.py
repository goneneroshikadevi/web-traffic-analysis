import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('traffic_data.csv')

print("\n=== WEBSITE TRAFFIC ANALYSIS ===\n")

# Most viewed pages
page_views = df['Page'].value_counts()
print("Most Viewed Pages:\n")
print(page_views)

# Average time spent
avg_time = df.groupby('Page')['Time_Spent_Minutes'].mean()
print("\nAverage Time Spent Per Page:\n")
print(avg_time)

# Exit page analysis
exit_rate = df['Exit_Page'].value_counts()
print("\nExit Page Analysis:\n")
print(exit_rate)

# Chart 1
plt.figure(figsize=(8,5))
page_views.plot(kind='bar')
plt.title('Most Viewed Pages')
plt.savefig('page_views_chart.png')

# Chart 2
plt.figure(figsize=(8,5))
avg_time.plot(kind='bar')
plt.title('Average Time Spent')
plt.savefig('time_spent_chart.png')

print("\nCharts created successfully!")