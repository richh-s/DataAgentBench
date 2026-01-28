code = """import json
import pandas as pd

# Load the data from query
price_data_path = var_functions.query_db:38
with open(price_data_path, 'r') as f:
    price_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(price_data)
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])

# Sort by index and date
df = df.sort_values(['Index', 'Date'])

# Map indices to countries
index_to_country = {
    'IXIC': 'United States',
    'NYA': 'United States', 
    'N225': 'Japan',
    'GDAXI': 'Germany',
    'HSI': 'Hong Kong'
}

# DCA parameters
monthly_investment = 100  # USD

# Calculate DCA returns for each index
results = []

for index in df['Index'].unique():
    idx_data = df[df['Index'] == index].copy()
    
    # Group by month and get first trading day of each month
    idx_data['YearMonth'] = idx_data['Date'].dt.to_period('M')
    monthly_first = idx_data.groupby('YearMonth').first().reset_index()
    
    # DCA simulation
    total_invested = 0
    total_shares = 0
    
    for _, row in monthly_first.iterrows():
        price = row['CloseUSD']
        if pd.notna(price) and price > 0:
            shares_bought = monthly_investment / price
            total_shares += shares_bought
            total_invested += monthly_investment
    
    # Calculate final value
    current_price = idx_data['CloseUSD'].iloc[-1]
    current_value = total_shares * current_price
    
    # Calculate returns
    total_return_pct = ((current_value - total_invested) / total_invested * 100) if total_invested > 0 else 0
    
    # Annualized return
    years = (idx_data['Date'].iloc[-1] - monthly_first['Date'].iloc[0]).days / 365.25
    if years > 0 and total_invested > 0:
        annualized_return = ((current_value / total_invested) ** (1/years) - 1) * 100
    else:
        annualized_return = 0
    
    results.append({
        'Index': index,
        'Country': index_to_country.get(index, 'Unknown'),
        'Total_Invested': round(total_invested, 2),
        'Current_Value': round(current_value, 2),
        'Total_Return_Pct': round(total_return_pct, 2),
        'Annualized_Return_Pct': round(annualized_return, 2),
        'Months': len(monthly_first)
    })

# Sort by total return percentage
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Total_Return_Pct', ascending=False)
top_5 = results_df.head(5)

# Create final answer
final_answer = "Top 5 Indices by DCA Returns (Monthly $100 since 2000):\n\n"
for i, (_, row) in enumerate(top_5.iterrows(), 1):
    final_answer += f"{i}. {row['Index']} ({row['Country']})\n"
    final_answer += f"   Total Return: {row['Total_Return_Pct']:.2f}%\n"
    final_answer += f"   Annualized Return: {row['Annualized_Return_Pct']:.2f}%\n"
    final_answer += f"   Total Invested: ${row['Total_Invested']:,.2f}\n"
    final_answer += f"   Current Value: ${row['Current_Value']:,.2f}\n\n"

print('__RESULT__:')
print(final_answer)"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:9': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:20': ['index_info'], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:28': [{'Index': 'J203.JO', 'days': '1854', 'first_date': '2012-02-08 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'min_price': '2302.1214454000005', 'max_price': '4805.917265800001'}, {'Index': 'IXIC', 'days': '7351', 'first_date': '2000-01-06 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'min_price': '55.48', 'max_price': '14138.78027'}, {'Index': 'HSI', 'days': '5604', 'first_date': '2000-01-14 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'min_price': '265.27799688', 'max_price': '4310.0357417000005'}, {'Index': 'NYA', 'days': '7960', 'first_date': '2000-01-03 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'min_price': '347.769989', 'max_price': '16590.42969'}, {'Index': '000001.SS', 'days': '4354', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'min_price': '161.9355176', 'max_price': '965.80492192'}, {'Index': 'SSMI', 'days': '5188', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'min_price': '1466.19902664', 'max_price': '12683.026932900002'}, {'Index': 'TWII', 'days': '4385', 'first_date': '2000-01-17 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'min_price': '137.8504004', 'max_price': '703.8360156'}, {'Index': 'N225', 'days': '7979', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'min_price': '10.2677002', 'max_price': '388.7694141'}, {'Index': 'GSPTSE', 'days': '6506', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'min_price': '1122.40904067', 'max_price': '16477.325352599997'}, {'Index': 'NSEI', 'days': '2577', 'first_date': '2007-09-25 00:00:00', 'last_date': 'September 30, 2014 at 12:00 AM', 'min_price': '25.24199951', 'max_price': '155.8279981'}, {'Index': 'GDAXI', 'days': '5590', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'min_price': '1158.0727878', 'max_price': '18934.3761734'}, {'Index': 'N100', 'days': '4245', 'first_date': '2000-01-10 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'min_price': '531.27340122', 'max_price': '1541.6163939'}, {'Index': '399001.SZ', 'days': '4355', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'min_price': '411.37601568', 'max_price': '3124.9840624'}], 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:32': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
