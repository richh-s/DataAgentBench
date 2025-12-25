code = """import pandas as pd
import json

# Get the file path from the variable
file_path = locals()['var_function-call-16915743951299197497']

# Load the data
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'], format='mixed', utc=True)
df = df[df['Date'] >= pd.Timestamp('2000-01-01', tz='UTC')]
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['CloseUSD', 'Date'])

indices = df['Index'].unique()
results = []

for idx in indices:
    sub_df = df[df['Index'] == idx].sort_values('Date')
    if sub_df.empty: continue
        
    sub_df['YearMonth'] = sub_df['Date'].dt.to_period('M')
    monthly_investments = sub_df.groupby('YearMonth').first().reset_index()
    
    monthly_investment_amount = 100.0
    monthly_investments['Units_Bought'] = monthly_investment_amount / monthly_investments['CloseUSD']
    
    total_units = monthly_investments['Units_Bought'].sum()
    total_invested = len(monthly_investments) * monthly_investment_amount
    last_price = sub_df.iloc[-1]['CloseUSD']
    final_value = total_units * last_price
    
    overall_return_pct = ((final_value - total_invested) / total_invested) * 100 if total_invested > 0 else 0
    
    results.append({
        'Index': idx,
        'Return_Pct': overall_return_pct,
        'Total_Invested': total_invested
    })

results_df = pd.DataFrame(results).sort_values('Return_Pct', ascending=False)
print("__RESULT__:")
print(results_df.head(10).to_json(orient='records'))"""

env_args = {'var_function-call-14617990700424002054': ['index_info'], 'var_function-call-4135645301445920250': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-16673487984124826334': ['index_trade'], 'var_function-call-3415968944644571791': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_function-call-6580303457518588185': [{'cid': '0', 'name': 'Exchange', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'Currency', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-7063044302034232475': [{'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-15938523053680967718': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-2457982519986606704': [{'count_star()': '104224'}], 'var_function-call-16915743951299197497': 'file_storage/function-call-16915743951299197497.json', 'var_function-call-9959983072761892303': [{'Index': 'IXIC', 'Return_Pct': 382.6943154204, 'Total_Invested': 25700.0, 'Final_Value': 124052.4390630478, 'Start_Date': '2000-01-03 00:00:00+00:00', 'End_Date': '2021-05-28 00:00:00+00:00'}, {'Index': 'NSEI', 'Return_Pct': 135.842734458, 'Total_Invested': 16500.0, 'Final_Value': 38914.0511855678, 'Start_Date': '2007-09-17 00:00:00+00:00', 'End_Date': '2021-05-31 00:00:00+00:00'}, {'Index': '399001.SZ', 'Return_Pct': 134.7463671885, 'Total_Invested': 25800.0, 'Final_Value': 60564.5627346235, 'Start_Date': '2000-01-04 00:00:00+00:00', 'End_Date': '2021-06-02 00:00:00+00:00'}, {'Index': 'GDAXI', 'Return_Pct': 134.7028715908, 'Total_Invested': 25700.0, 'Final_Value': 60318.6379988427, 'Start_Date': '2000-01-03 00:00:00+00:00', 'End_Date': '2021-05-31 00:00:00+00:00'}, {'Index': 'TWII', 'Return_Pct': 129.8200315845, 'Total_Invested': 25700.0, 'Final_Value': 59063.7481172075, 'Start_Date': '2000-01-04 00:00:00+00:00', 'End_Date': '2021-05-31 00:00:00+00:00'}]}

exec(code, env_args)
