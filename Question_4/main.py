import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
customers = pd.read_csv('customers.csv')
orders = pd.read_csv('orders.csv')
products = pd.read_csv('products.csv')
reviews = pd.read_csv('reviews.csv')
def clean_data(df):
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    return df

customers = clean_data(customers)
orders = clean_data(orders)
products = clean_data(products)
reviews = clean_data(reviews)
df = orders.merge(customers, on='customer_id', how='inner') \
           .merge(products, on='product_id', how='inner') \
           .merge(reviews, on='product_id', how='left')
def customer_behavior(df):
    customer_summary = df.groupby('customer_id').agg({
        'order_id': 'count',
        'total_price': 'sum'
    }).rename(columns={'order_id': 'total_orders', 'total_price': 'total_spent'})
    
    return customer_summary

customer_summary = customer_behavior(df)
print("Customer Summary:\n", customer_summary.head())
def product_performance(df):
    product_summary = df.groupby('product_id').agg({
        'order_id': 'count',
        'total_price': 'sum',
        'review_rating': 'mean'
    }).rename(columns={'order_id': 'total_orders', 'total_price': 'total_revenue'})
    
    return product_summary

product_summary = product_performance(df)
print("Product Summary:\n", product_summary.head())
def sales_trends(df):
    df['order_date'] = pd.to_datetime(df['order_date'])
    sales_trends = df.groupby(df['order_date'].dt.to_period('M')).agg({
        'total_price': 'sum'
    }).rename(columns={'total_price': 'monthly_sales'})
    
    return sales_trends

monthly_sales = sales_trends(df)
print("Monthly Sales Trends:\n", monthly_sales.head())
def visualize_data(df, title, xlabel, ylabel):
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
visualize_data(customer_summary['total_spent'].sort_values(), 'Customer Spending', 'Customer ID', 'Total Spent')
visualize_data(product_summary['total_revenue'].sort_values(), 'Product Revenue', 'Product ID', 'Total Revenue')
visualize_data(monthly_sales, 'Monthly Sales Trends', 'Date', 'Monthly Sales')
def recommendations(df):
    top_products = df.groupby('product_id').agg({'total_revenue': 'sum'}).sort_values('total_revenue', ascending=False).head(10)
    top_customers = df.groupby('customer_id').agg({'total_spent': 'sum'}).sort_values('total_spent', ascending=False).head(10)
    
    return top_products, top_customers

top_products, top_customers = recommendations(df)
print("Top Products:\n", top_products)
print("Top Customers:\n", top_customers)
