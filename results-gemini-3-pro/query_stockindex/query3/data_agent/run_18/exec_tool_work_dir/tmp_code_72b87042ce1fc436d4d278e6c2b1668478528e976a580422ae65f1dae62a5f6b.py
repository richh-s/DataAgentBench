code = """import pandas as pd
import json
import dateutil.parser

file_path = locals()['var_function-call-14002920760052114969']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

def parse_date(date_str):
    try:
        return dateutil.parser.parse(date_str)
    except:
        return None

df['Date'] = df['Date'].apply(parse_date)
df = df[df['Date'] >= pd.Timestamp('2000-01-01')]
df = df.sort_values(by=['Index', 'Date'])

# Convert to numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

# Check availability of CloseUSD
# If CloseUSD is NaN, fill with Close for US indices? 
# IXIC (Nasdaq) and NYA (NYSE) are in USD. 
# GSPTSE (Canada) is in CAD.
# Just to be safe, let's see which indices have missing CloseUSD.
missing_stats = df.groupby('Index')['CloseUSD'].apply(lambda x: x.isna().sum())
total_stats = df.groupby('Index')['CloseUSD'].count()
# print("Missing CloseUSD:", missing_stats)

# For US indices, if CloseUSD is missing, use Close.
us_indices = ['IXIC', 'NYA']
for idx in us_indices:
    mask = (df['Index'] == idx) & (df['CloseUSD'].isna())
    df.loc[mask, 'CloseUSD'] = df.loc[mask, 'Close']

df['YearMonth'] = df['Date'].dt.to_period('M')
monthly_df = df.groupby(['Index', 'YearMonth']).first().reset_index()

results = []
indices = monthly_df['Index'].unique()

for idx in indices:
    sub_df = monthly_df[monthly_df['Index'] == idx].sort_values('Date')
    
    # Filter valid prices
    sub_df = sub_df.dropna(subset=['CloseUSD'])
    
    if sub_df.empty:
        continue

    start_date = sub_df['Date'].iloc[0]
    
    invested = 0
    units = 0
    
    for _, row in sub_df.iterrows():
        price = row['CloseUSD']
        if price > 0:
            units += 100.0 / price
            invested += 100.0
            
    # Final price
    # Get the last available daily price, not just the monthly one
    daily_idx = df[df['Index'] == idx].dropna(subset=['CloseUSD'])
    if daily_idx.empty:
        final_price = 0
    else:
        final_price = daily_idx.iloc[-1]['CloseUSD']

    final_value = units * final_price
    if invested > 0:
        return_pct = ((final_value - invested) / invested) * 100
    else:
        return_pct = 0
    
    results.append({
        'Index': idx,
        'Return_Pct': return_pct,
        'Start_Date': start_date.isoformat()
    })

results_df = pd.DataFrame(results).sort_values(by='Return_Pct', ascending=False)

print("__RESULT__:")
print(results_df.to_json(orient='records'))"""

env_args = {'var_function-call-15045155276809644361': ['index_info'], 'var_function-call-15045155276809645240': ['index_trade'], 'var_function-call-8875709257747002473': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-8875709257747005048': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}], 'var_function-call-15054097013438635701': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-15054097013438633364': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-14791774478946530287': [{'count_star()': '104224'}], 'var_function-call-14002920760052114969': 'file_storage/function-call-14002920760052114969.json'}

exec(code, env_args)
