import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

salesDataFrame = pd.read_csv('sales_data.csv', parse_dates=['Date'])
sdf_info = salesDataFrame.info()
print(sdf_info)

graph_size = (14, 6)

# What's the mean of Customer_Age?
mean_customers_age = salesDataFrame['Customer_Age'].mean()
# kde of Customer_Age
# customers_age_dens = salesDataFrame['Customer_Age'].plot(kind='kde', figsize=graph_size)
# box plot
# customers_age_boxplot = salesDataFrame['Customer_Age'].plot(kind='box', figsize=graph_size)

# How many sales per year do we have?
sales_per_year = salesDataFrame['Year'].value_counts()
# pie plot
# sales_per_year_pie = salesDataFrame['Year'].value_counts().plot(kind='pie', figsize=graph_size)

# How many sales per month do we have?
sales_per_month = salesDataFrame['Month'].value_counts()
# bar plot
# sales_per_month_bar = salesDataFrame['Month'].value_counts().plot(kind='bar', figsize=graph_size)

# Which country has the most sales quantity of sales?
most_sales_country = salesDataFrame['Country'].value_counts().head(1)
most_sales_country_name = most_sales_country.index[0]







plt.show()

