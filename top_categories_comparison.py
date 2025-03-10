import pandas as pd
import matplotlib.pyplot as plt

# Assuming df is the DataFrame with Google Play Store data
# and it has 'Category', 'Installs', and 'Last Updated' columns

# Convert 'Last Updated' to datetime format if not already
df['Last Updated'] = pd.to_datetime(df['Last Updated'], errors='coerce')

# Filter data based on a date range
start_date = '2018-01-01'
end_date = '2019-01-01'
filtered_df = df[(df['Last Updated'] >= start_date) & (df['Last Updated'] < end_date)]

# Group by 'Category' and sum the 'Installs'
top_categories = filtered_df.groupby('Category')['Installs'].sum().sort_values(ascending=False).head(10)

# Plot the grouped bar chart
plt.figure(figsize=(10, 6))
plt.bar(top_categories.index, top_categories.values)
plt.xticks(rotation=45)
plt.xlabel('Category')
plt.ylabel('Total Installs')
plt.title('Top 10 App Categories by Installs ({} to {})'.format(start_date, end_date))
plt.tight_layout()
plt.show()