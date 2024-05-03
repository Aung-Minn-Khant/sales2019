import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="My Sale Dashboard",page_icon=':bar_chart:',layout='wide')
df = pd.read_csv('all_df.csv')
st.sidebar.header('Please Filter Here')

product=st.sidebar.multiselect(
    "Select Product",
    options = df['Product'].unique(),
    default = df['Product'].unique()[:5]
)
city=st.sidebar.multiselect(
    "Select City",
    options = df['City'].unique(),
    default = df['City'].unique()[:5]
)
month=st.sidebar.multiselect(
    "Select Month",
    options = df['Month'].unique(),
    default = df['Month'].unique()[:5]
)
st.title(":bar_chart: Sale Dashboard 2019")
st.markdown("##")
total_sales = df['Total'].sum()
product_num = df['Product'].nunique()
left_col,right_col = st.columns(2)
with left_col:
    st.subheader('Total Sales')
    st.subheader(f'US $ {total_sales}')
with right_col:
    st.subheader('Number of Product')
    st.subheader(f'{product_num}')

df_select=df.query("City==@city and Product==@product and Month==@month")
sales_by_product=df_select.groupby('Product')['Total'].sum().sort_values()
sales_fig=px.bar(
    sales_by_product,
    x=sales_by_product.values,
    y=sales_by_product.index,
    orientation='h',
    title='Sales by Product'
    
)
a_col,b_col,c_col=st.columns(3)
a_col.plotly_chart(sales_fig,user_container_wide=True)

city_fig=px.pie(
    df_select,
    values='Total',
    names='City',
    title='Sales of City'
    
)
b_col.plotly_chart(city_fig,user_container_wide=True)

sales_by_month=df_select.groupby('Month')['Total'].sum().sort_values()
month_fig=px.bar(
    sales_by_month,
    x=sales_by_month.values,
    y=sales_by_month.index,
    orientation='h',
    title='Sales by Month'
    
)
c_col.plotly_chart(month_fig,user_container_wide=True)

d_col,e_col = st.columns(2)
dfmonth_fig = px.line(
    df,
    x = sales_by_month.index,
    y= sales_by_month.values,
    title = 'Sales by Month in All data'
)
d_col.plotly_chart(dfmonth_fig,user_container_wide = True)
scatter_fig = px.scatter(
    df,
    x = 'Total',
    y= 'QuantityOrdered',
    title = 'Total of All Item Amount'
)
e_col.plotly_chart(scatter_fig,user_container_wide = True)