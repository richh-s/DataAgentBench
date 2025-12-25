code = """import json, pandas as pd, os

path = var_call_YtptZfRYPgid9CL5kDp7Tuu6
with open(path, 'r') as f:
    data = json.load(f)

# Build DataFrame
df = pd.DataFrame(data)

# Ensure numeric
for col in ["Open", "High", "Low"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Normalize date to ISO and filter since 2020-01-01
# Dates appear in multiple string formats; let pandas parse flexibly
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Filter
df = df[df["Date"] >= pd.Timestamp("2020-01-01")]

# Drop rows with missing needed fields or nonpositive Open
df = df.dropna(subset=["Open", "High", "Low"])
df = df[df["Open"] > 0]

# Compute intraday volatility
df["vol"] = (df["High"] - df["Low"]) / df["Open"]

# Group by index
avg_vol = df.groupby("Index")["vol"].mean().sort_values(ascending=False)

result = avg_vol.reset_index().to_dict(orient="records")

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Tdwk66GxvSbat8eywFjhnMcE': ['index_info'], 'var_call_aWnx3k9jO7MixbVlYKzk3fjX': ['index_trade'], 'var_call_ZEMiEIVeqLncfydH3oJaDwGj': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_qFCMsJUDPXa9EQ3if6u7nwh9': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'IXIC'}], 'var_call_5y8jGTBG3MqrG3v3FfbIplhV': {'asia_indices': ['HSI', '000001.SS', 'N225', '399001.SZ', 'NSEI', 'J203.JO', 'TWII']}, 'var_call_YtptZfRYPgid9CL5kDp7Tuu6': 'file_storage/call_YtptZfRYPgid9CL5kDp7Tuu6.json'}

exec(code, env_args)
