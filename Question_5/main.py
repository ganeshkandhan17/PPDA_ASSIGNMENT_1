import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sales = pd.read_csv('sales.csv')
products = pd.read_csv('products.csv')
stores = pd.read_csv('stores.csv')
customers = pd.read_csv('customers.csv')
inventory = pd.read_csv('inventory.csv')
def clean_data(df):
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    return df

sales = clean_data(sales)
products = clean_data(products)
stores = clean_data(stores)
customers = clean_data(customers)
inventory = clean_data(inventory)
df = sales.merge(products, on='product_id', how='inner') \
          .merge(stores, on='store_id', how='left') \
          .merge(customers, on='customer_id', how='left') \
          .merge(inventory, on='product_id', how='left')
def inventory_analysis(df):
    inventory_summary = df.groupby('product_id').agg({
        'inventory_level': 'mean',
        'sales_amount': 'sum',
        'quantity_sold': 'sum'
    }).rename(columns={'inventory_level': 'avg_inventory', 'sales_amount': 'total_sales'})
    
    inventory_summary['sales_per_inventory'] = inventory_summary['total_sales'] / inventory_summary['avg_inventory']
    
    return inventory_summary

inventory_summary = inventory_analysis(df)
print("Inventory Summary:\n", inventory_summary.head())

def customer_satisfaction(df):
    customer_summary = df.groupby('customer_id').agg({
        'sales_amount': 'sum',
        'quantity_sold': 'sum'
    }).rename(columns={'sales_amount': 'total_spent', 'quantity_sold': 'total_items'})
    customer_summary['satisfaction_score'] = customer_summary['total_spent'] / customer_summary['total_items']
    
    return customer_summary

customer_summary = customer_satisfaction(df)
print("Customer Summary:\n", customer_summary.head())
def sales_trends(df):
    df['sale_date'] = pd.to_datetime(df['sale_date'])
    sales_trends = df.groupby(df['sale_date'].dt.to_period('M')).agg({
        'sales_amount': 'sum'
    }).rename(columns={'sales_amount': 'monthly_sales'})
    
    return sales_trends

monthly_sales = sales_trends(df)
print("Monthly Sales Trends:\n", monthly_sales.head())
def visualize_data(df, title, xlabel, ylabel):
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()
plt.figure(figsize=(12, 6))
sns.barplot(x=inventory_summary.index, y=inventory_summary['sales_per_inventory'])
plt.title('Sales Per Inventory Level by Product')
plt.xlabel('Product ID')
plt.ylabel('Sales Per Inventory')
plt.xticks(rotation=90)
plt.show()
plt.figure(figsize=(12, 6))
sns.histplot(customer_summary['satisfaction_score'], bins=30)
plt.title('Distribution of Customer Satisfaction Scores')
plt.xlabel('Satisfaction Score')
plt.ylabel('Frequency')
plt.show()
visualize_data(monthly_sales, 'Monthly Sales Trends', 'Date', 'Monthly Sales')
def recommendations(df):
    top_products = df.groupby('product_id').agg({
        'total_sales': 'sum'
    }).sort_values('total_sales', ascending=False).head(10)
    
    top_customers = df.groupby('customer_id').agg({
        'total_spent': 'sum'
    }).sort_values('total_spent', ascending=False).head(10)
    
    return top_products, top_customers

top_products, top_customers = recommendations(df)
print("Top Products:\n", top_products)
print("Top Customers:\n", top_customers)
