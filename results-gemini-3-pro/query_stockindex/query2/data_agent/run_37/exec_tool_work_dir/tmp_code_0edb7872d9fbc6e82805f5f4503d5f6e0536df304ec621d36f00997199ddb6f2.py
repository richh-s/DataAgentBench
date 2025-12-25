code = """import pandas as pd
import json
import datetime

# Load the data
with open('var_function-call-1773212316373150054.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Function to parse dates
def parse_date(date_str):
    try:
        # Try standard pandas parsing
        return pd.to_datetime(date_str)
    except:
        return pd.NaT

# Since formats are mixed and potentially weird, let's try a few explicit formats if pd.to_datetime is not smart enough or strict.
# However, pd.to_datetime is usually good. But let's check one thing.
# The 'Date' column in preview: "December 31, 1965 at 12:00 AM", "03 Jan 1966, 00:00"
# pd.to_datetime(['December 31, 1965 at 12:00 AM']) works?
# Let's try to convert the whole column.
# Note: pd.to_datetime might be slow on list if not vectorized or if formats differ a lot.
# But for <100k rows it should be fine.

df['dt'] = pd.to_datetime(df['Date'], errors='coerce')

# Check if we have many NaTs
# If so, we might need custom parsing.
# The preview showed:
# 1. "Month DD, YYYY at HH:MM AM/PM"
# 2. "DD Mon YYYY, HH:MM"
# 3. "YYYY-MM-DD HH:MM:SS"

# Filter for 2018
df_2018 = df[df['dt'].dt.year == 2018].copy()

# Ensure numeric columns are floats
cols = ['Open', 'Close']
for col in cols:
    df_2018[col] = pd.to_numeric(df_2018[col], errors='coerce')

# Calculate Up/Down
# Up: Close > Open
# Down: Close < Open
# Tie: Close == Open (ignore or count as neither? "more up days than down days" implies strict inequality comparison)

results = {}
for idx in df_2018['Index'].unique():
    sub = df_2018[df_2018['Index'] == idx]
    up = (sub['Close'] > sub['Open']).sum()
    down = (sub['Close'] < sub['Open']).sum()
    results[idx] = {'up': int(up), 'down': int(down)}

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-16831980965409320818': ['index_info'], 'var_function-call-16831980965409317307': ['index_trade'], 'var_function-call-4220619263127830695': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_function-call-15424594137061085806': [{'Index': 'J203.JO'}, {'Index': 'HSI'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'IXIC'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-4766578470714734566': [{'Date': '31 Dec 1986, 00:00'}], 'var_function-call-1773212316373150054': 'file_storage/function-call-1773212316373150054.json'}

exec(code, env_args)
