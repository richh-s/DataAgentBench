code = """import pandas as pd
import json
import dateutil.parser

# Load data
with open(locals()['var_function-call-18267896960875721156'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse dates
# The dates are mixed format. pd.to_datetime might handle it.
# Let's try pd.to_datetime with errors='coerce' first.
# If that fails for many, we might need a custom parser.
# Given the formats seen: "31 Dec 1986, 00:00", "January 02, 1987 at 12:00 AM", "1987-01-05 00:00:00"
# dateutil.parser.parse is robust.

def parse_date(d_str):
    try:
        return pd.to_datetime(d_str)
    except:
        return pd.NaT

df['Date'] = df['Date'].apply(parse_date)

# Drop invalid dates
df = df.dropna(subset=['Date'])

# Filter >= 2000-01-01
df = df[df['Date'] >= '2000-01-01']

# Ensure CloseUSD is numeric
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df = df.dropna(subset=['CloseUSD'])

# Sort
df = df.sort_values(by=['Index', 'Date'])

results = []

for idx_name, group in df.groupby('Index'):
    # Group by Year-Month to find investment days
    # Create a YearMonth column
    group['YearMonth'] = group['Date'].dt.to_period('M')
    
    # Select the first entry of each month
    monthly_investments = group.groupby('YearMonth').first().reset_index()
    
    # Calculate investment
    # Invest $1 each month
    monthly_investments['Units'] = 1.0 / monthly_investments['CloseUSD']
    
    total_units = monthly_investments['Units'].sum()
    total_invested = len(monthly_investments)
    
    # Final value
    # Get the very last available price in the dataset for this index
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

# Sort by Return descending
results_df = pd.DataFrame(results).sort_values(by='Return', ascending=False)

print("__RESULT__:")
print(results_df.to_json(orient='records'))"""

env_args = {'var_function-call-7582418552492946031': ['index_info'], 'var_function-call-7582418552492947708': ['index_trade'], 'var_function-call-7897424772466399632': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-16664814470342706309': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-10139612300660335222': [{'Index': 'J203.JO', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'cnt': '2346'}, {'Index': 'IXIC', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'cnt': '12690'}, {'Index': 'HSI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'cnt': '8492'}, {'Index': '000001.SS', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'cnt': '5791'}, {'Index': 'SSMI', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'cnt': '7671'}, {'Index': 'TWII', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'cnt': '5869'}, {'Index': 'NYA', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'cnt': '13947'}, {'Index': 'N100', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM', 'cnt': '5474'}, {'Index': '399001.SZ', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM', 'cnt': '5760'}, {'Index': 'N225', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'cnt': '13874'}, {'Index': 'GSPTSE', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'cnt': '10526'}, {'Index': 'NSEI', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM', 'cnt': '3346'}, {'Index': 'GDAXI', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM', 'cnt': '8438'}], 'var_function-call-5207441896460676504': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-7661938929931462669': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Close': '2568.300049', 'CloseUSD': '333.87900637'}], 'var_function-call-18267896960875721156': 'file_storage/function-call-18267896960875721156.json'}

exec(code, env_args)
