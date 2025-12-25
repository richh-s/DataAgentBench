code = """import json
import pandas as pd

# Load data
file_path = locals()['var_function-call-11696950529192728079']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

try:
    df['Date'] = pd.to_datetime(df['Date'], format='mixed')
except:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

df = df[df['Date'] >= '2000-01-01']
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])
df = df.sort_values(['Index', 'Date'])

results = []
indices = df['Index'].unique()

for idx in indices:
    idx_data = df[df['Index'] == idx].copy()
    if idx_data.empty: continue
    
    idx_data['YearMonth'] = idx_data['Date'].dt.to_period('M')
    monthly_investments = idx_data.groupby('YearMonth').first().reset_index()
    
    monthly_invest_amount = 100
    total_invested = 0
    total_units = 0
    
    for _, row in monthly_investments.iterrows():
        price = row['CloseUSD']
        if pd.notnull(price) and price > 0:
            units = monthly_invest_amount / price
            total_units += units
            total_invested += monthly_invest_amount
            
    if monthly_investments.empty: continue

    last_price = idx_data.iloc[-1]['CloseUSD']
    final_value = total_units * last_price
    
    if total_invested > 0:
        total_return_pct = (final_value - total_invested) / total_invested * 100
    else:
        total_return_pct = 0
        
    results.append({
        'Index': idx,
        'Total_Return_Pct': total_return_pct
    })

results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Total_Return_Pct', ascending=False)

print("__RESULT__:")
print(results_df.to_json(orient='records'))"""

env_args = {'var_function-call-12239121071183399536': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-12239121071183400583': [{'Index': 'J203.JO', 'start_date': '2012-02-08 00:00:00', 'end_date': 'September 30, 2019 at 12:00 AM', 'count': '1854'}, {'Index': 'IXIC', 'start_date': '2000-01-06 00:00:00', 'end_date': 'September 30, 2015 at 12:00 AM', 'count': '7351'}, {'Index': 'N225', 'start_date': '2000-01-04 00:00:00', 'end_date': 'September 30, 2020 at 12:00 AM', 'count': '7979'}, {'Index': 'GSPTSE', 'start_date': '2000-01-05 00:00:00', 'end_date': 'September 30, 2016 at 12:00 AM', 'count': '6506'}, {'Index': 'NSEI', 'start_date': '2007-09-25 00:00:00', 'end_date': 'September 30, 2014 at 12:00 AM', 'count': '2577'}, {'Index': 'GDAXI', 'start_date': '2000-01-05 00:00:00', 'end_date': 'September 30, 2016 at 12:00 AM', 'count': '5590'}, {'Index': 'HSI', 'start_date': '2000-01-14 00:00:00', 'end_date': 'September 30, 2019 at 12:00 AM', 'count': '5604'}, {'Index': 'NYA', 'start_date': '2000-01-03 00:00:00', 'end_date': 'September 30, 2020 at 12:00 AM', 'count': '7960'}, {'Index': '000001.SS', 'start_date': '2000-01-04 00:00:00', 'end_date': 'September 30, 2015 at 12:00 AM', 'count': '4354'}, {'Index': 'SSMI', 'start_date': '2000-01-05 00:00:00', 'end_date': 'September 30, 2020 at 12:00 AM', 'count': '5188'}, {'Index': 'TWII', 'start_date': '2000-01-17 00:00:00', 'end_date': 'September 30, 2020 at 12:00 AM', 'count': '4385'}, {'Index': 'N100', 'start_date': '2000-01-10 00:00:00', 'end_date': 'September 30, 2019 at 12:00 AM', 'count': '4245'}, {'Index': '399001.SZ', 'start_date': '2000-01-05 00:00:00', 'end_date': 'September 30, 2015 at 12:00 AM', 'count': '4355'}], 'var_function-call-11696950529192728079': 'file_storage/function-call-11696950529192728079.json', 'var_function-call-16147675759970171906': [{'Index': 'IXIC', 'Total_Return_Pct': 3922.2248763898, 'Total_Invested': 60400, 'Final_Value': 2429423.8253394477}, {'Index': 'NYA', 'Total_Return_Pct': 1126.8031835225, 'Total_Invested': 66600, 'Final_Value': 817050.9202259702}, {'Index': 'N225', 'Total_Return_Pct': 362.4168132743, 'Total_Invested': 67800, 'Final_Value': 313518.5993999903}, {'Index': 'GDAXI', 'Total_Return_Pct': 328.9985750795, 'Total_Invested': 40200, 'Final_Value': 172457.4271819553}, {'Index': 'GSPTSE', 'Total_Return_Pct': 296.5661921532, 'Total_Invested': 50400, 'Final_Value': 199869.3608452358}], 'var_function-call-565721591931142804': [{'Index': 'IXIC', 'Total_Return_Pct': 382.6720689693, 'Total_Invested': 25700, 'Final_Value': 124046.7217250998, 'Start': '2000-01-03', 'End': '2021-05-28'}, {'Index': 'GDAXI', 'Total_Return_Pct': 134.8239307892, 'Total_Invested': 25700, 'Final_Value': 60349.7502128287, 'Start': '2000-01-04', 'End': '2021-05-31'}, {'Index': '399001.SZ', 'Total_Return_Pct': 134.7928823154, 'Total_Invested': 25800, 'Final_Value': 60576.5636373844, 'Start': '2000-01-05', 'End': '2021-06-02'}, {'Index': 'TWII', 'Total_Return_Pct': 129.6645021996, 'Total_Invested': 25700, 'Final_Value': 59023.7770652956, 'Start': '2000-01-05', 'End': '2021-05-31'}, {'Index': 'N225', 'Total_Return_Pct': 117.0265903155, 'Total_Invested': 25800, 'Final_Value': 55992.8603013971, 'Start': '2000-01-04', 'End': '2021-06-03'}]}

exec(code, env_args)
