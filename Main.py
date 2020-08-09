import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

salesDataFrame = pd.read_csv('sales_data.csv', parse_dates=['Date'])
sdf_info = salesDataFrame.info()
print(sdf_info)

graph_size = (20, 8)

# # What's the mean of Customer_Age?
# mean_customers_age = salesDataFrame['Customer_Age'].mean()
# # kde of Customer_Age
# # customers_age_dens = salesDataFrame['Customer_Age'].plot(kind='kde', figsize=graph_size)
# # box plot
# # customers_age_boxplot = salesDataFrame['Customer_Age'].plot(kind='box', figsize=graph_size)
#
# # How many sales per year do we have?
# sales_per_year = salesDataFrame['Year'].value_counts()
# # pie plot
# # sales_per_year_pie = salesDataFrame['Year'].value_counts().plot(kind='pie', figsize=graph_size)
#
# # How many sales per month do we have?
# sales_per_month = salesDataFrame['Month'].value_counts()
# # bar plot
# # sales_per_month_bar = salesDataFrame['Month'].value_counts().plot(kind='bar', figsize=graph_size)
#
# # Which country has the most sales quantity of sales?
# most_sales_country = salesDataFrame['Country'].value_counts().head(1)
# most_sales_country_name = most_sales_country.index[0]
# # bar plot
# # most_sales_country_bar = salesDataFrame['Country'].value_counts().plot(kind='bar', figsize=graph_size)
#
# # Create a list of every product sold
# product_list = salesDataFrame['Product'].unique()
# # bar plot showing the 10 most sold products (best sellers):
# ten_most_sold_products = salesDataFrame['Product'].value_counts().head(10)
# # ten_most_sold_products_bar = ten_most_sold_products.plot(kind='bar', figsize=graph_size)
#
# # relationship between Unit_Cost and Unit_Price
#
# # unit_cost_coor_unit_price = salesDataFrame.plot(kind='scatter', x='Unit_Cost', y='Unit_Price', figsize=graph_size)
# corr_unitcost_unitprice = salesDataFrame['Unit_Cost'].corr(salesDataFrame['Unit_Price'])
#
# # relationship between Order_Quantity and Profit
# corr_orderquantity_profit = salesDataFrame['Order_Quantity'].corr(salesDataFrame['Profit'])
# # order_quantity_coor_profit = salesDataFrame.plot(kind='scatter', x='Order_Quantity', y='Profit', figsize=graph_size)
# # salesDataFrame[['Order_Quantity', 'Profit']].plot(kind='scatter', x='Order_Quantity', y='Profit', figsize=graph_size)
#
# # relationship between Profit per Country       <--- quantitative and categorical
# profit_country = ['Profit', 'Country']
# # profit_country_box = salesDataFrame[profit_country].boxplot(by='Country', figsize=graph_size)
#
# # relationship between Customer_Age per Country
# customerAge_Country = ['Customer_Age', 'Country']
# # customerAge_Country_box = salesDataFrame[customerAge_Country].boxplot(by='Country', figsize=graph_size)
#
# # New date form (YYYY-MM-DD) for Calculated_Date
# year_month_day = ['Year', 'Month', 'Day']
# salesDataFrame['Calculated_Date'] = salesDataFrame[year_month_day].apply( lambda x: '{}-{}-{}'.format(x[0], x[1], x[2]), axis=1)
# # Calculated_Date -> datetime object
# salesDataFrame['Calculated_Date'] = pd.to_datetime(salesDataFrame['Calculated_Date'])
#
# # How did sales evolve through the years?
# # calculatedDate_sales = salesDataFrame['Calculated_Date'].value_counts().plot(kind='line', figsize=graph_size)
#
# # increase $50 revenue to every sale
# salesDataFrame['Revenue'] += 50

# # How many orders were made in Canada | France
# orders_CanadaOrFrance = salesDataFrame.loc[(salesDataFrame['Country'] == 'Canada') | (salesDataFrame['Country'] == 'France')]
# num_orders_CanadaOrFrance = orders_CanadaOrFrance.shape[0]

# # How many orders were made in each region (state) of France
# orders_France_region = salesDataFrame.loc[(salesDataFrame['Country'] == 'France'), 'State'].value_counts()
# # bar plot
# orders_France_region_bar = orders_France_region.plot(kind='bar', figsize=graph_size)

# # how man orders were made per accessory sub-categories
# accessory_subcategories = salesDataFrame.loc[(salesDataFrame['Product_Category'] == 'Accessories'), 'Sub_Category'].value_counts()
# # bar plot
# accessory_subcategories_bar = accessory_subcategories.plot(kind='bar', figsize=graph_size)

# # which gender has the most amount of sales?
# sales_gender = salesDataFrame['Customer_Gender'].value_counts().head().index[0]

# # How many sales with more than 500 in Revenue were made by men?
# morethan_500Revenue_men = salesDataFrame.loc[(salesDataFrame['Customer_Gender'] == 'M') & (salesDataFrame['Revenue'] > 500), 'Customer_Gender'].value_counts()[0]

# # get the top-5 sales with the highest revenue
# top_5_revenue = salesDataFrame.sort_values(['Revenue'], ascending=False).head(5)

# # get the sale with the highest revenue
# highest_revenue = salesDataFrame.loc[salesDataFrame['Revenue'] == salesDataFrame['Revenue'].max()]

# # What is the mean Order_Quantity of orders with more than 10K in revenue
# order_quantity_morethan10K = salesDataFrame.loc[(salesDataFrame['Revenue'] > 10_000), 'Order_Quantity']
# mean_order_quantity_morethan10K = order_quantity_morethan10K.mean()

# # How many orders were made between May and July of 2016
# May_to_July_2016 = salesDataFrame.loc[(salesDataFrame['Year'] == 2016) & (salesDataFrame['Month'].isin(['May', 'June', 'July'])), ['Month', 'Profit']]
# May_to_July_2016_totalOrders = May_to_July_2016.shape[0]
# May_to_July_2016_box = May_to_July_2016.boxplot(by='Month', figsize=graph_size)

# # Add 7.2% TAX on every sale Unit_Price within US
# unitprice_us = salesDataFrame.loc[(salesDataFrame['Country'] == 'United States'), 'Unit_Price']
# changed_unitprice_us = unitprice_us * (1 + 0.072)

# plt.show()

