code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-8540390000505140219'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'], format='mixed', utc=True)
df = df[df['Date'] >= pd.to_datetime('2000-01-01', utc=True)]
df = df.sort_values(['Index', 'Date'])

country_map = {
    'J203.JO': 'South Africa',
    'N225': 'Japan',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'IXIC': 'United States',
    'HSI': 'Hong Kong',
    'NYA': 'United States',
    '000001.SS': 'China',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'N100': 'Europe',
    '399001.SZ': 'China'
}

results = []

for idx, group in df.groupby('Index'):
    # Resample to monthly (first trading day)
    group['YM'] = group['Date'].dt.to_period('M')
    monthly_data = group.groupby('YM').first().reset_index()
    
    invest_amount = 1.0
    prices = monthly_data['Adj Close'].astype(float).values
    
    if len(prices) == 0:
        continue
        
    units = invest_amount / prices
    total_units = units.sum()
    total_invested = len(units) * invest_amount
    
    last_price = float(group.iloc[-1]['Adj Close'])
    final_value = total_units * last_price
    
    ret = (final_value - total_invested) / total_invested
    
    results.append({
        'Index': idx,
        'Country': country_map.get(idx, 'Unknown'),
        'Return': ret,
        'Total_Invested': total_invested,
        'Start_Date': monthly_data['Date'].min().strftime('%Y-%m-%d'),
        'End_Date': group['Date'].max().strftime('%Y-%m-%d')
    })

results_df = pd.DataFrame(results).sort_values('Return', ascending=False)

print("__RESULT__:")
print(json.dumps(results_df.to_dict(orient='records')))"""

env_args = {'var_function-call-200894980028602229': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-200894980028601412': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-8540390000505140219': 'file_storage/function-call-8540390000505140219.json', 'var_function-call-10329044522485616302': [{'Index': 'IXIC', 'Country': 'United States', 'Return': 3.8267206896926007, 'Total_Invested': 257.0, 'Final_Value': 1240.4672172509984, 'Start_Date': '2000-01-03', 'End_Date': '2021-05-28'}, {'Index': 'NSEI', 'Country': 'India', 'Return': 1.3584343632740843, 'Total_Invested': 165.0, 'Final_Value': 389.1416699402239, 'Start_Date': '2007-09-18', 'End_Date': '2021-05-31'}, {'Index': 'GDAXI', 'Country': 'Germany', 'Return': 1.3482393078921664, 'Total_Invested': 257.0, 'Final_Value': 603.4975021282868, 'Start_Date': '2000-01-04', 'End_Date': '2021-05-31'}, {'Index': '399001.SZ', 'Country': 'China', 'Return': 1.34795269599869, 'Total_Invested': 258.0, 'Final_Value': 605.771795567662, 'Start_Date': '2000-01-05', 'End_Date': '2021-06-02'}, {'Index': 'TWII', 'Country': 'Taiwan', 'Return': 1.2966523209671978, 'Total_Invested': 257.0, 'Final_Value': 590.2396464885699, 'Start_Date': '2000-01-05', 'End_Date': '2021-05-31'}, {'Index': 'N225', 'Country': 'Japan', 'Return': 1.1702659031549252, 'Total_Invested': 258.0, 'Final_Value': 559.9286030139707, 'Start_Date': '2000-01-04', 'End_Date': '2021-06-03'}, {'Index': 'NYA', 'Country': 'United States', 'Return': 1.0150320720311592, 'Total_Invested': 257.0, 'Final_Value': 517.8632425120079, 'Start_Date': '2000-01-03', 'End_Date': '2021-05-28'}, {'Index': 'GSPTSE', 'Country': 'Canada', 'Return': 0.7295061267178053, 'Total_Invested': 257.0, 'Final_Value': 444.483074566476, 'Start_Date': '2000-01-04', 'End_Date': '2021-05-31'}, {'Index': '000001.SS', 'Country': 'China', 'Return': 0.6421953031927815, 'Total_Invested': 257.0, 'Final_Value': 422.04419292054484, 'Start_Date': '2000-01-04', 'End_Date': '2021-05-31'}, {'Index': 'N100', 'Country': 'Europe', 'Return': 0.6125512204196312, 'Total_Invested': 258.0, 'Final_Value': 416.03821486826484, 'Start_Date': '2000-01-03', 'End_Date': '2021-06-02'}]}

exec(code, env_args)
