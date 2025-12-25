code = """import json, pandas as pd
from datetime import datetime

# Load full data from file
with open(var_call_pgw5EL3zspQ0LMs2S3KUWJwl, 'r') as f:
    data = json.load(f)

# Put into DataFrame
df = pd.DataFrame(data)

# Parse Date into datetime; handle various formats
fmt_list = [
    '%Y-%m-%d',
    '%d %b %Y, %H:%M',
    '%B %d, %Y at %I:%M %p'
]

def parse_date(x):
    for fmt in fmt_list:
        try:
            return datetime.strptime(x, fmt)
        except Exception:
            continue
    return pd.NaT

df['Date_parsed'] = df['Date'].apply(parse_date)

# Filter from 2020-01-01
cutoff = datetime(2020,1,1)
df = df[df['Date_parsed'] >= cutoff]

# Convert price columns to float
for col in ['Open','High','Low']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop rows with missing needed values
df = df.dropna(subset=['Open','High','Low'])

# Compute intraday volatility (High-Low)/Open
df['vol'] = (df['High'] - df['Low']) / df['Open']

# Map indices to regions (Asia vs others) based on knowledge
asia_indices = {'HSI','N225','399001.SZ','000001.SS','TWII','NSEI'}

asia_df = df[df['Index'].isin(asia_indices)]

# Compute average volatility per index
result = asia_df.groupby('Index')['vol'].mean().sort_values(ascending=False)

result_dict = result.to_dict()

out = {"asia_index_with_max_avg_intraday_vol_since_2020": max(result_dict, key=result_dict.get),
       "average_vol_by_index": result_dict}

out_json = json.dumps(out)
print("__RESULT__:")
print(out_json)"""

env_args = {'var_call_Dk0Upzd9vnKdWIuvliJYimmo': ['index_info'], 'var_call_rnn429SWJyuVywJwDAMenzZ2': ['index_trade'], 'var_call_gIvXV8nbPJaqDd3WTLAG3hht': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_pgw5EL3zspQ0LMs2S3KUWJwl': 'file_storage/call_pgw5EL3zspQ0LMs2S3KUWJwl.json'}

exec(code, env_args)
