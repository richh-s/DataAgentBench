code = """import pandas as pd
import json

# Load the full result from the file
with open(locals()['var_function-call-1798190552623397067'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Convert 'Open' and 'Close' to numeric, handling potential errors
df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

# Drop rows with NaN in 'Open' or 'Close' after conversion
df.dropna(subset=['Open', 'Close'], inplace=True)

# Attempt to parse dates with multiple formats
date_formats = [
    '%Y-%m-%d %H:%M:%S',
    '%d %b %Y, %H:%M',
    '%B %d, %Y at %I:%M %p'
]

def parse_date(date_str):
    for fmt in date_formats:
        try:
            return pd.to_datetime(date_str, format=fmt)
        except ValueError:
            continue
    return pd.NaT

df['ParsedDate'] = df['Date'].apply(parse_date)

# Filter for the year 2018 and valid dates
df_2018 = df[df['ParsedDate'].dt.year == 2018].copy()

# Calculate up and down days
df_2018['UpDay'] = df_2018['Close'] > df_2018['Open']
df_2018['DownDay'] = df_2018['Close'] < df_2018['Open']

up_days = df_2018.groupby('Index')['UpDay'].sum()
down_days = df_2018.groupby('Index')['DownDay'].sum()

# Combine into a single DataFrame
summary_df = pd.DataFrame({'UpDays': up_days, 'DownDays': down_days})

# Filter for indices with more up days than down days
result = summary_df[summary_df['UpDays'] > summary_df['DownDays']].index.tolist()

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-9490773837024715485': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_function-call-1960221335447693946': [], 'var_function-call-9464330560762967202': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'IXIC'}], 'var_function-call-1798190552623397067': 'file_storage/function-call-1798190552623397067.json'}

exec(code, env_args)
