code = """import pandas as pd
import json

file_path = locals()['var_function-call-6265478658087228362']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Preprocess dates to handle " at "
def clean_date(d):
    if isinstance(d, str) and ' at ' in d:
        return d.replace(' at ', ' ')
    return d

df['Date_Clean'] = df['Date'].apply(clean_date)

# Convert to datetime
df['dt'] = pd.to_datetime(df['Date_Clean'], errors='coerce')

# Filter for >= 2020-01-01
df_2020 = df[df['dt'] >= '2020-01-01'].copy()

# Ensure numeric columns are float
cols = ['Open', 'High', 'Low']
for c in cols:
    df_2020[c] = pd.to_numeric(df_2020[c], errors='coerce')

# Drop rows with invalid Open, High, Low or Open == 0
df_2020 = df_2020.dropna(subset=cols)
df_2020 = df_2020[df_2020['Open'] > 0]

# Calculate volatility
df_2020['volatility'] = (df_2020['High'] - df_2020['Low']) / df_2020['Open']

# Group by Index and calculate mean
result = df_2020.groupby('Index')['volatility'].mean().sort_values(ascending=False)

print('__RESULT__:')
print(result.to_json())"""

env_args = {'var_function-call-14389522957611380655': ['index_info'], 'var_function-call-8240741329983985971': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-10910080142151504211': ['index_trade'], 'var_function-call-1717870473916640461': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'IXIC'}], 'var_function-call-8867451719225357961': [{'Date': '31 Dec 1986, 00:00'}], 'var_function-call-14265025779110911859': [{'parsed_date': '1986-12-31 00:00:00'}], 'var_function-call-11473412576929112904': [{'Date': '1965-01-05 00:00:00'}, {'Date': 'January 06, 1965 at 12:00 AM'}, {'Date': '07 Jan 1965, 00:00'}, {'Date': '1965-01-08 00:00:00'}, {'Date': '1965-01-12 00:00:00'}], 'var_function-call-14406713922952149': [{'cnt': '43132'}], 'var_function-call-6265478658087228362': 'file_storage/function-call-6265478658087228362.json'}

exec(code, env_args)
