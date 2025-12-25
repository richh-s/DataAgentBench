code = """import json, pandas as pd
from pathlib import Path

path = Path(var_call_7xhSYW0fOwUcPbEx2cp8Xage)
records = json.loads(path.read_text())

# Determine North American indices using geographic knowledge
north_america_indices = {
    'NYA': 'New York Stock Exchange',   # USA
    'IXIC': 'NASDAQ',                  # USA
    'GSPTSE': 'Toronto Stock Exchange' # Canada
}

_df = pd.DataFrame(records)
_df['Open'] = _df['Open'].astype(float)
_df['Close'] = _df['Close'].astype(float)

na_df = _df[_df['Index'].isin(north_america_indices.keys())]

summary = (
    na_df.assign(
        up = lambda d: d['Close'] > d['Open'],
        down = lambda d: d['Close'] < d['Open']
    )
    .groupby('Index')
    .agg(up_days=('up','sum'), down_days=('down','sum'))
    .reset_index()
)

summary['more_up_than_down'] = summary['up_days'] > summary['down_days']

result = summary.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_PzlvnbO1nmdyZIpXP6Hk9JNF': ['index_info'], 'var_call_o3DhNSzDy8Q2AiWC8ErUX59m': ['index_trade'], 'var_call_3me9Shu6UNYWecK78twcXho7': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_wy9aWJsFfT2vjVvaw0pHZEwB': [{'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'J203.JO'}], 'var_call_7xhSYW0fOwUcPbEx2cp8Xage': 'file_storage/call_7xhSYW0fOwUcPbEx2cp8Xage.json'}

exec(code, env_args)
