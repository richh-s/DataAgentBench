code = """import json, pandas as pd
from datetime import datetime

path = var_call_TiQGbQAVJMUCAfkkQMfmtTtI
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# parse dates
df['CreatedDate'] = pd.to_datetime(df['CreatedDate'].str[:19])

# define window: past 10 months from 2021-04-10 inclusive
anchor = datetime(2021,4,10)
start = (anchor.replace(day=1) - pd.DateOffset(months=9)).to_pydatetime()
end = anchor

mask = (df['CreatedDate'] >= start) & (df['CreatedDate'] <= end)
window_df = df[mask].copy()

if window_df.empty:
    result = None
else:
    # count per month (year-month) within window
    window_df['year_month'] = window_df['CreatedDate'].dt.to_period('M')
    counts = window_df.groupby('year_month').size().sort_values(ascending=False)

    if counts.empty:
        result = None
    else:
        top = counts.iloc[0]
        second = counts.iloc[1] if len(counts) > 1 else 0
        # "significantly exceeds" -> require at least 50% more than next month
        if top >= 1.5 * second and top >= 2:
            top_period = counts.index[0]
            month_name = top_period.to_timestamp().strftime('%B')
            result = month_name
        else:
            result = None

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_TiQGbQAVJMUCAfkkQMfmtTtI': 'file_storage/call_TiQGbQAVJMUCAfkkQMfmtTtI.json'}

exec(code, env_args)
