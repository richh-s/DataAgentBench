code = """import json
import pandas as pd
from dateutil import parser

# Load data
with open(locals()['var_function-call-10345639744164598555'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Function to parse date
def parse_date(date_str):
    try:
        dt = parser.parse(date_str)
        return dt
    except:
        return None

df['parsed_date'] = df['Date'].apply(parse_date)
df = df.dropna(subset=['parsed_date'])
df['year'] = df['parsed_date'].dt.year

# Filter for 2018
df_2018 = df[df['year'] == 2018].copy()

# Calculate Up and Down days
df_2018['is_up'] = df_2018['Close'] > df_2018['Open']
df_2018['is_down'] = df_2018['Close'] < df_2018['Open']

# Group by Index
results = df_2018.groupby('Index')[['is_up', 'is_down']].sum()

# Filter indices where Up > Down
final_indices = results[results['is_up'] > results['is_down']].index.tolist()

print("__RESULT__:")
print(json.dumps(final_indices))"""

env_args = {'var_function-call-5834036211217615728': ['index_info'], 'var_function-call-5834036211217616147': ['index_trade'], 'var_function-call-3120195457054773382': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}], 'var_function-call-5419050431242429501': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-9305720569387398332': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-8162046437870080195': [{'Date': '31 Dec 1986, 00:00'}], 'var_function-call-41112584349359193': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}], 'var_function-call-7376973814999857113': [{'count_star()': '37163'}], 'var_function-call-10345639744164598555': 'file_storage/function-call-10345639744164598555.json'}

exec(code, env_args)
