code = """import pandas as pd
import json

# Load the data from the file
with open(locals()["var_function-call-1238247793098822744"], "r") as f:
    df_raw = pd.DataFrame(json.load(f))

# Convert 'Date' to datetime, handling mixed formats
date_formats = [
    "%d %b %Y, %H:%M",  # e.g., "31 Dec 1986, 00:00"
    "%B %d, %Y at %I:%M %p", # e.g., "January 02, 1987 at 12:00 AM"
    "%Y-%m-%d" # standard format if present
]

def parse_date(date_str):
    for fmt in date_formats:
        try:
            return pd.to_datetime(date_str, format=fmt)
        except ValueError:
            continue
    return pd.NaT # Return Not a Time for unparseable dates

df_raw['Date'] = df_raw['Date'].apply(parse_date)

# Drop rows where date parsing failed
df_raw = df_raw.dropna(subset=['Date'])

# Convert 'CloseUSD' to numeric
df_raw['CloseUSD'] = pd.to_numeric(df_raw['CloseUSD'], errors='coerce')

# Drop rows with NaN in 'CloseUSD'
df_raw = df_raw.dropna(subset=['CloseUSD'])

# Filter data from 2000 onwards
df_filtered = df_raw[df_raw['Date'] >= '2000-01-01']

# Sort by Index and Date
df_filtered = df_filtered.sort_values(by=['Index', 'Date'])

# Get the first and last CloseUSD for each index
first_prices = df_filtered.groupby('Index')['CloseUSD'].first()
last_prices = df_filtered.groupby('Index')['CloseUSD'].last()

# Calculate overall return
returns = ((last_prices - first_prices) / first_prices) * 100

# Get the top 5 indices by return
top_5_indices = returns.nlargest(5).index.tolist()
top_5_returns = returns.nlargest(5).tolist()

result = {
    "top_5_indices": top_5_indices,
    "top_5_returns": top_5_returns
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-15490260447422397754': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'IXIC'}], 'var_function-call-1238247793098822744': 'file_storage/function-call-1238247793098822744.json'}

exec(code, env_args)
