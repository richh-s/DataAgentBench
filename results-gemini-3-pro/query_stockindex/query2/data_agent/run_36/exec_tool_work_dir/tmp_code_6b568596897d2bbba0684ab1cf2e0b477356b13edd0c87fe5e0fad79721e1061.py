code = """import pandas as pd
import json

# Load the data
file_path = locals()['var_function-call-13061758539908281550']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Convert columns to numeric
df['Open'] = pd.to_numeric(df['Open'])
df['Close'] = pd.to_numeric(df['Close'])

# Parse dates
# Since formats vary, we let pandas guess. The preview shows consistent year '2018' in text.
# We just need to make sure we are looking at 2018. The SQL filter `LIKE '%2018%'` was applied.
# Let's just verify the year to be safe.
# Using `coerce` to handle errors if any, but `LIKE '%2018%'` suggests valid dates mostly.
df['DateParsed'] = pd.to_datetime(df['Date'], errors='coerce')

# Filter for year 2018 strictly
df = df[df['DateParsed'].dt.year == 2018]

# Calculate Up/Down
df['Up'] = df['Close'] > df['Open']
df['Down'] = df['Close'] < df['Open']

# Group by Index and count
results = df.groupby('Index')[['Up', 'Down']].sum()

# Filter indices where Up > Down
more_up_than_down = results[results['Up'] > results['Down']].index.tolist()

print("__RESULT__:")
print(json.dumps(more_up_than_down))"""

env_args = {'var_function-call-7813116232473084298': ['index_info'], 'var_function-call-7813116232473084081': ['index_trade'], 'var_function-call-17618777129370107511': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-7590832105320527244': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-15213542186855282615': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}], 'var_function-call-14053612812454351889': [{'Date': '31 Dec 1986, 00:00'}], 'var_function-call-15787814323667666595': [{'Date': '31 Dec 1986, 00:00', 'parsed_date': '1986-12-31 00:00:00'}], 'var_function-call-9966686775635477593': [{'Date': 'January 02, 2018 at 12:00 AM'}, {'Date': 'January 03, 2018 at 12:00 AM'}, {'Date': '04 Jan 2018, 00:00'}, {'Date': '05 Jan 2018, 00:00'}, {'Date': 'January 08, 2018 at 12:00 AM'}, {'Date': '2018-01-09 00:00:00'}, {'Date': '10 Jan 2018, 00:00'}, {'Date': '11 Jan 2018, 00:00'}, {'Date': 'January 12, 2018 at 12:00 AM'}, {'Date': '2018-01-16 00:00:00'}], 'var_function-call-13061758539908281550': 'file_storage/function-call-13061758539908281550.json'}

exec(code, env_args)
