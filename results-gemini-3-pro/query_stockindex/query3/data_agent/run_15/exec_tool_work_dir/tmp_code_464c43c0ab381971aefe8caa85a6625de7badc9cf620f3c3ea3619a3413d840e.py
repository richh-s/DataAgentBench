code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-7669815343368743674'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['CloseUSD', 'Date'])

results = []
indices = df['Index'].unique()

for idx in indices:
    sub_df = df[df['Index'] == idx].sort_values('Date')
    
    sub_df['YearMonth'] = sub_df['Date'].dt.to_period('M')
    monthly_invest = sub_df.groupby('YearMonth').first().reset_index()
    monthly_invest['Shares'] = 1.0 / monthly_invest['CloseUSD']
    total_shares = monthly_invest['Shares'].sum()
    total_invested = len(monthly_invest)
    last_price = sub_df.iloc[-1]['CloseUSD']
    final_value = total_shares * last_price
    
    if total_invested > 0:
        roi = (final_value - total_invested) / total_invested
    else:
        roi = 0
    
    results.append({
        'Index': idx,
        'ROI': roi,
        'Start_Date': sub_df['Date'].iloc[0],
        'End_Date': sub_df['Date'].iloc[-1]
    })

results_df = pd.DataFrame(results)
results_df = results_df.sort_values('ROI', ascending=False)
print("__RESULT__:")
print(results_df.to_json(orient='records', date_format='iso'))"""

env_args = {'var_function-call-13441364534165871433': ['index_info'], 'var_function-call-13441364534165871896': ['index_trade'], 'var_function-call-8023527505821607131': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-8023527505821609228': [{'IndexSymbol': 'J203.JO'}, {'IndexSymbol': 'N225'}, {'IndexSymbol': 'GSPTSE'}, {'IndexSymbol': 'NSEI'}, {'IndexSymbol': 'GDAXI'}, {'IndexSymbol': 'IXIC'}, {'IndexSymbol': 'HSI'}, {'IndexSymbol': 'NYA'}, {'IndexSymbol': '000001.SS'}, {'IndexSymbol': 'SSMI'}, {'IndexSymbol': 'TWII'}, {'IndexSymbol': 'N100'}, {'IndexSymbol': '399001.SZ'}], 'var_function-call-7669815343368743674': 'file_storage/function-call-7669815343368743674.json', 'var_function-call-505363906880158823': [{'Index': 'IXIC', 'Country': 'United States', 'ROI': 3.8220467671, 'Start_Date': '2000-01-06T00:00:00.000', 'End_Date': '2021-05-27T00:00:00.000'}, {'Index': 'NSEI', 'Country': 'India', 'ROI': 1.3608849755, 'Start_Date': '2007-09-25T00:00:00.000', 'End_Date': '2021-05-31T00:00:00.000'}, {'Index': 'GDAXI', 'Country': 'Germany', 'ROI': 1.3474623836, 'Start_Date': '2000-01-05T00:00:00.000', 'End_Date': '2021-05-31T00:00:00.000'}, {'Index': '399001.SZ', 'Country': 'China', 'ROI': 1.3445453364, 'Start_Date': '2000-01-05T00:00:00.000', 'End_Date': '2021-06-02T00:00:00.000'}, {'Index': 'TWII', 'Country': 'Taiwan', 'ROI': 1.2374061754, 'Start_Date': '2000-01-17T00:00:00.000', 'End_Date': '2021-05-26T00:00:00.000'}, {'Index': 'N225', 'Country': 'Japan', 'ROI': 1.1545960543, 'Start_Date': '2000-01-04T00:00:00.000', 'End_Date': '2021-06-01T00:00:00.000'}, {'Index': 'NYA', 'Country': 'United States', 'ROI': 1.0065591545, 'Start_Date': '2000-01-03T00:00:00.000', 'End_Date': '2021-05-24T00:00:00.000'}, {'Index': 'GSPTSE', 'Country': 'Canada', 'ROI': 0.6754596567, 'Start_Date': '2000-01-05T00:00:00.000', 'End_Date': '2021-05-13T00:00:00.000'}, {'Index': '000001.SS', 'Country': 'China', 'ROI': 0.6416057718, 'Start_Date': '2000-01-04T00:00:00.000', 'End_Date': '2021-05-31T00:00:00.000'}, {'Index': 'N100', 'Country': 'Europe', 'ROI': 0.5986654389, 'Start_Date': '2000-01-10T00:00:00.000', 'End_Date': '2021-05-31T00:00:00.000'}]}

exec(code, env_args)
