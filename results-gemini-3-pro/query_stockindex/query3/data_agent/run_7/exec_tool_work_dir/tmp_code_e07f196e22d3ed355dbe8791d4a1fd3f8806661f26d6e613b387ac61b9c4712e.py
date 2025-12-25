code = """# Re-run printing top 10 to check plausibility
import json
import pandas as pd

with open(locals()['var_function-call-5773205835372737063'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'], format='mixed', errors='coerce')
df = df[df['Date'] >= '2000-01-01']
df['Adj Close'] = pd.to_numeric(df['Adj Close'])

index_country_map = {
    'J203.JO': 'South Africa',
    'IXIC': 'United States',
    'HSI': 'Hong Kong',
    'N225': 'Japan',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    '000001.SS': 'China',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'N100': 'Europe',
    '399001.SZ': 'China',
    'NYA': 'United States'
}

results = []

for index_name, group in df.groupby('Index'):
    group = group.sort_values('Date')
    group['Month'] = group['Date'].dt.to_period('M')
    monthly_investment_dates = group.groupby('Month')['Date'].min()
    
    total_shares = 0
    total_invested = 0
    monthly_amount = 100.0
    
    for month, date in monthly_investment_dates.items():
        price = group.loc[group['Date'] == date, 'Adj Close'].iloc[0]
        if price > 0:
            shares = monthly_amount / price
            total_shares += shares
            total_invested += monthly_amount
            
    if total_invested > 0:
        last_price = group.iloc[-1]['Adj Close']
        final_value = total_shares * last_price
        pct_return = (final_value - total_invested) / total_invested * 100
        
        results.append({
            'Index': index_name,
            'Country': index_country_map.get(index_name, 'Unknown'),
            'Total_Invested': total_invested,
            'Final_Value': final_value,
            'Return_Pct': pct_return
        })

results_df = pd.DataFrame(results).sort_values('Return_Pct', ascending=False)
print("__RESULT__:")
print(results_df.head(10).to_json(orient='records'))"""

env_args = {'var_function-call-10021783300953503103': ['index_info'], 'var_function-call-11595194589530822852': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-6069480066467942252': ['index_trade'], 'var_function-call-3250475692665861912': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'NYA'}], 'var_function-call-14715549604581522807': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-5773205835372737063': 'file_storage/function-call-5773205835372737063.json', 'var_function-call-7036163351833230080': [{'Index': 'IXIC', 'Country': 'United States', 'Total_Invested': 60400.0, 'Final_Value': 2429423.8253394477, 'Return_Pct': 3922.2248763898}, {'Index': 'NYA', 'Country': 'United States', 'Total_Invested': 66600.0, 'Final_Value': 817050.9202259702, 'Return_Pct': 1126.8031835225}, {'Index': 'N225', 'Country': 'Japan', 'Total_Invested': 67800.0, 'Final_Value': 313518.5993999899, 'Return_Pct': 362.4168132743}, {'Index': 'GDAXI', 'Country': 'Germany', 'Total_Invested': 40200.0, 'Final_Value': 172457.4271819551, 'Return_Pct': 328.9985750795}, {'Index': 'GSPTSE', 'Country': 'Canada', 'Total_Invested': 50400.0, 'Final_Value': 200155.4685047093, 'Return_Pct': 297.1338660808}], 'var_function-call-13868661964618368795': [{'Index': '000001.SS', 'Min_Date': '2000-01-04 00:00:00', 'Max_Date': '2021-05-31 00:00:00', 'Months': 257, 'Rows': 4076}, {'Index': '399001.SZ', 'Min_Date': '2000-01-05 00:00:00', 'Max_Date': '2021-06-02 00:00:00', 'Months': 258, 'Rows': 4113}, {'Index': 'GDAXI', 'Min_Date': '2000-01-04 00:00:00', 'Max_Date': '2021-05-31 00:00:00', 'Months': 257, 'Rows': 4212}, {'Index': 'GSPTSE', 'Min_Date': '2000-01-04 00:00:00', 'Max_Date': '2021-05-31 00:00:00', 'Months': 257, 'Rows': 4214}, {'Index': 'HSI', 'Min_Date': '2000-01-04 00:00:00', 'Max_Date': '2021-05-31 00:00:00', 'Months': 257, 'Rows': 4133}, {'Index': 'IXIC', 'Min_Date': '2000-01-03 00:00:00', 'Max_Date': '2021-05-28 00:00:00', 'Months': 257, 'Rows': 4206}, {'Index': 'J203.JO', 'Min_Date': '2012-02-08 00:00:00', 'Max_Date': '2021-05-31 00:00:00', 'Months': 112, 'Rows': 1854}, {'Index': 'N100', 'Min_Date': '2000-01-03 00:00:00', 'Max_Date': '2021-06-02 00:00:00', 'Months': 258, 'Rows': 4245}, {'Index': 'N225', 'Min_Date': '2000-01-04 00:00:00', 'Max_Date': '2021-06-03 00:00:00', 'Months': 258, 'Rows': 4143}, {'Index': 'NSEI', 'Min_Date': '2007-09-18 00:00:00', 'Max_Date': '2021-05-31 00:00:00', 'Months': 165, 'Rows': 2577}, {'Index': 'NYA', 'Min_Date': '2000-01-03 00:00:00', 'Max_Date': '2021-05-28 00:00:00', 'Months': 257, 'Rows': 4190}, {'Index': 'SSMI', 'Min_Date': '2000-01-04 00:00:00', 'Max_Date': '2021-05-28 00:00:00', 'Months': 257, 'Rows': 4188}, {'Index': 'TWII', 'Min_Date': '2000-01-05 00:00:00', 'Max_Date': '2021-05-31 00:00:00', 'Months': 257, 'Rows': 4120}], 'var_function-call-8045616465862886683': [{'Index': 'IXIC', 'Country': 'United States', 'Total_Invested': 25700.0, 'Final_Value': 124046.7217250998, 'Return_Pct': 382.6720689693}, {'Index': 'NSEI', 'Country': 'India', 'Total_Invested': 16500.0, 'Final_Value': 38914.1669940224, 'Return_Pct': 135.8434363274}, {'Index': 'GDAXI', 'Country': 'Germany', 'Total_Invested': 25700.0, 'Final_Value': 60349.7502128287, 'Return_Pct': 134.8239307892}, {'Index': '399001.SZ', 'Country': 'China', 'Total_Invested': 25800.0, 'Final_Value': 60577.1795567662, 'Return_Pct': 134.7952695999}, {'Index': 'TWII', 'Country': 'Taiwan', 'Total_Invested': 25700.0, 'Final_Value': 59023.964648857, 'Return_Pct': 129.6652320967}]}

exec(code, env_args)
