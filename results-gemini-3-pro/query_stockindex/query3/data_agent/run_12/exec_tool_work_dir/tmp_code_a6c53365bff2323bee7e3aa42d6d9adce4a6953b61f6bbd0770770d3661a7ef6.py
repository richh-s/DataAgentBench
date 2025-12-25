code = """import json
import pandas as pd

# Load data again (simulating persistent state or re-running logic)
file_path = locals()['var_function-call-6499139532502453844']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'], format='mixed', utc=True)
df = df[df['Date'] >= '2000-01-01']
df = df.sort_values(['Index', 'Date'])

index_country_map = {
    'NYA': 'United States',
    'IXIC': 'United States',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    'N225': 'Japan',
    'N100': 'Europe', 
    '399001.SZ': 'China',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'GDAXI': 'Germany',
    'TWII': 'Taiwan',
    'SSMI': 'Switzerland',
    'J203.JO': 'South Africa'
}

results = []
for idx, group in df.groupby('Index'):
    group['YearMonth'] = group['Date'].dt.to_period('M')
    monthly_data = group.drop_duplicates(subset='YearMonth', keep='first').copy()
    
    first_date = monthly_data['Date'].iloc[0]
    if first_date > pd.Timestamp('2000-02-01', tz='UTC'):
        continue
    
    monthly_data['Units'] = 1 / monthly_data['CloseUSD'].astype(float)
    total_units = monthly_data['Units'].sum()
    total_invested = len(monthly_data)
    final_price = group['CloseUSD'].astype(float).iloc[-1]
    final_value = total_units * final_price
    overall_return = (final_value - total_invested) / total_invested
    
    results.append({
        'Index': idx,
        'Country': index_country_map.get(idx, 'Unknown'),
        'Return': overall_return
    })

res_df = pd.DataFrame(results)
res_df = res_df.sort_values('Return', ascending=False)

print("__RESULT__:")
print(res_df.to_json(orient='records'))"""

env_args = {'var_function-call-7298216697624936112': ['index_info'], 'var_function-call-7298216697624936091': ['index_trade'], 'var_function-call-4885089669788374823': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-4885089669788375530': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_function-call-8519188745840322015': [{'cid': '0', 'name': 'Exchange', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'Currency', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-4714276876713809212': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-4714276876713808055': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-6499139532502453844': 'file_storage/function-call-6499139532502453844.json', 'var_function-call-16163031396378802661': [{'Index': 'IXIC', 'Country': 'United States', 'Return': 3.8269431542, 'FinalValue': 1240.5243906305, 'Invested': 257}, {'Index': '399001.SZ', 'Country': 'China', 'Return': 1.3474636719, 'FinalValue': 605.6456273462, 'Invested': 258}, {'Index': 'GDAXI', 'Country': 'Germany', 'Return': 1.3470287159, 'FinalValue': 603.1863799884, 'Invested': 257}, {'Index': 'TWII', 'Country': 'Taiwan', 'Return': 1.2982003158, 'FinalValue': 590.6374811721, 'Invested': 257}, {'Index': 'N225', 'Country': 'Japan', 'Return': 1.169064758, 'FinalValue': 559.618707556, 'Invested': 258}], 'var_function-call-10942610521338892629': ['01 Apr 2014, 00:00', '01 Apr 2021, 00:00', '01 Aug 2008, 00:00', '01 Aug 2012, 00:00', '01 Aug 2014, 00:00'], 'var_function-call-2873427569183613234': '2007-09-17 00:00:00+00:00', 'var_function-call-9615421946822574332': '2012-02-08 00:00:00+00:00'}

exec(code, env_args)
