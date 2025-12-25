code = """import json
import pandas as pd
from dateutil import parser

# Load the data from the file
file_path = locals()['var_function-call-2687488736843281053']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse dates
# Since dateutil.parser.parse can be slow on large lists, apply it carefully.
# But 30-40k rows is fine.
def parse_date(d_str):
    try:
        return parser.parse(d_str)
    except:
        return None

df['dt'] = df['Date'].apply(parse_date)

# Filter for 2018
df_2018 = df[df['dt'].dt.year == 2018].copy()

# Calculate stats
results = []
for idx in df_2018['Index'].unique():
    sub = df_2018[df_2018['Index'] == idx]
    up = (sub['Close'] > sub['Open']).sum()
    down = (sub['Close'] < sub['Open']).sum()
    results.append({
        'Index': idx,
        'Up': int(up),
        'Down': int(down)
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-13435841548751938839': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-13435841548751939088': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'IXIC'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-4586942093490243808': [{'Index': 'GSPTSE', 'up_days': '44.0', 'down_days': '41.0'}, {'Index': 'IXIC', 'up_days': '44.0', 'down_days': '31.0'}, {'Index': 'NYA', 'up_days': '37.0', 'down_days': '42.0'}], 'var_function-call-7537918577132548343': [{'Date': '29 Jun 1979, 00:00', 'Index': 'GSPTSE', 'Open': '1614.699951', 'Close': '1618.400024'}, {'Date': 'July 03, 1979 at 12:00 AM', 'Index': 'GSPTSE', 'Open': '1613.599976', 'Close': '1602.800049'}, {'Date': '04 Jul 1979, 00:00', 'Index': 'GSPTSE', 'Open': '1601.5', 'Close': '1591.400024'}, {'Date': '05 Jul 1979, 00:00', 'Index': 'GSPTSE', 'Open': '1590.0', 'Close': '1583.900024'}, {'Date': 'July 06, 1979 at 12:00 AM', 'Index': 'GSPTSE', 'Open': '1583.900024', 'Close': '1586.599976'}], 'var_function-call-2687488736843281053': 'file_storage/function-call-2687488736843281053.json'}

exec(code, env_args)
