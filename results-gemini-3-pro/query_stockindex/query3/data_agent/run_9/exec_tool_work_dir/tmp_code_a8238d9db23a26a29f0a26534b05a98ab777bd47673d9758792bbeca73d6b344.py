code = """import pandas as pd
import json

# Load data from both files
with open(locals()['var_function-call-18267896960875721156'], 'r') as f:
    data1 = json.load(f)
with open(locals()['var_function-call-12440529723021961085'], 'r') as f:
    data2 = json.load(f)

df = pd.DataFrame(data1 + data2)

# Parse dates
def parse_date(d_str):
    try:
        return pd.to_datetime(d_str)
    except:
        return pd.NaT

df['Date'] = df['Date'].apply(parse_date)
df = df.dropna(subset=['Date'])
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['CloseUSD'])

# Filter indices that start <= 2000-01-31
valid_indices = []
for idx_name, group in df.groupby('Index'):
    min_date = group['Date'].min()
    if min_date <= pd.Timestamp('2000-02-01'):
        valid_indices.append(idx_name)

df = df[df['Index'].isin(valid_indices)]

# Filter data >= 2000-01-01
df = df[df['Date'] >= '2000-01-01']

# Sort
df = df.sort_values(by=['Index', 'Date'])

results = []

for idx_name, group in df.groupby('Index'):
    group['YearMonth'] = group['Date'].dt.to_period('M')
    monthly_investments = group.groupby('YearMonth').first().reset_index()
    
    monthly_investments['Units'] = 1.0 / monthly_investments['CloseUSD']
    total_units = monthly_investments['Units'].sum()
    total_invested = len(monthly_investments)
    
    last_price = group.iloc[-1]['CloseUSD']
    final_value = total_units * last_price
    
    overall_return = (final_value - total_invested) / total_invested
    
    results.append({
        "Index": idx_name,
        "Return": overall_return,
        "TotalInvested": total_invested,
        "FinalValue": final_value,
        "LastDate": group.iloc[-1]['Date'].strftime('%Y-%m-%d')
    })

results_df = pd.DataFrame(results).sort_values(by='Return', ascending=False)

print("__RESULT__:")
print(results_df.to_json(orient='records'))"""

env_args = {'var_function-call-7582418552492946031': ['index_info'], 'var_function-call-7582418552492947708': ['index_trade'], 'var_function-call-7897424772466399632': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-16664814470342706309': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-10139612300660335222': [{'Index': 'J203.JO', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'cnt': '2346'}, {'Index': 'IXIC', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'cnt': '12690'}, {'Index': 'HSI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'cnt': '8492'}, {'Index': '000001.SS', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'cnt': '5791'}, {'Index': 'SSMI', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'cnt': '7671'}, {'Index': 'TWII', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'cnt': '5869'}, {'Index': 'NYA', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'cnt': '13947'}, {'Index': 'N100', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'cnt': '5474'}, {'Index': '399001.SZ', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'cnt': '5760'}, {'Index': 'N225', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'cnt': '13874'}, {'Index': 'GSPTSE', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'cnt': '10526'}, {'Index': 'NSEI', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM', 'cnt': '3346'}, {'Index': 'GDAXI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'cnt': '8438'}], 'var_function-call-5207441896460676504': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-7661938929931462669': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Close': '2568.300049', 'CloseUSD': '333.87900637'}], 'var_function-call-18267896960875721156': 'file_storage/function-call-18267896960875721156.json', 'var_function-call-7419551228304709129': [{'Index': 'IXIC', 'Return': 3.8269431542, 'TotalInvested': 257, 'FinalValue': 1240.5243906305, 'LastDate': '2021-05-28'}, {'Index': 'GDAXI', 'Return': 1.3470287159, 'TotalInvested': 257, 'FinalValue': 603.1863799884, 'LastDate': '2021-05-31'}, {'Index': 'N225', 'Return': 1.169064758, 'TotalInvested': 258, 'FinalValue': 559.618707556, 'LastDate': '2021-06-03'}, {'Index': 'NYA', 'Return': 1.0150701719, 'TotalInvested': 257, 'FinalValue': 517.8730341865, 'LastDate': '2021-05-28'}, {'Index': 'GSPTSE', 'Return': 0.7302115617, 'TotalInvested': 257, 'FinalValue': 444.6643713625, 'LastDate': '2021-05-31'}, {'Index': 'HSI', 'Return': 0.6049598222, 'TotalInvested': 257, 'FinalValue': 412.4746742945, 'LastDate': '2021-05-31'}, {'Index': 'SSMI', 'Return': 0.587967437, 'TotalInvested': 257, 'FinalValue': 408.1076313007, 'LastDate': '2021-05-28'}], 'var_function-call-12440529723021961085': 'file_storage/function-call-12440529723021961085.json'}

exec(code, env_args)
