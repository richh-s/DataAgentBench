code = """import json, pandas as pd
from pathlib import Path

# Load trades
path = Path(var_call_cbC5NjeCVqOoYaixX3booJXX)
records = json.loads(path.read_text())

# North American indices in this dataset: NYA (NYSE Composite), IXIC (Nasdaq Composite), GSPTSE (Toronto)
na_indices = {"NYA", "IXIC", "GSPTSE"}

rows = [r for r in records if r["Index"] in na_indices]

df = pd.DataFrame(rows)

# Ensure numeric
for col in ["Open", "Close"]:
    df[col] = pd.to_numeric(df[col])

# Up/down flag
df["up"] = df["Close"] > df["Open"]
df["down"] = df["Close"] < df["Open"]

summary = df.groupby("Index")[['up','down']].sum().reset_index()
summary["more_up_than_down"] = summary["up"] > summary["down"]

result = summary.to_dict(orient="records")

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_myZarzTQZQ2SGqJxsQ4oz8Pe': ['index_info'], 'var_call_fkVxsSY1QHIFJKq0MCkaKxSB': ['index_trade'], 'var_call_MuxEnzw7mR2fiThaIUEZNdj4': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_E3CQihTV5AH2w62DZftumVCw': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_cbC5NjeCVqOoYaixX3booJXX': 'file_storage/call_cbC5NjeCVqOoYaixX3booJXX.json'}

exec(code, env_args)
