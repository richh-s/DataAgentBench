code = """import pandas as pd
import json

df = pd.DataFrame(var_call_icl7iJEu3JSPSxaQodXrtjwR)
# Normalize OwnerId: remove leading # and trim
if 'OwnerId' in df.columns:
    df['OwnerId'] = df['OwnerId'].astype(str).str.replace('#', '', regex=False).str.strip()
# Parse dates
df['CreatedDate'] = pd.to_datetime(df['CreatedDate'], utc=True)
# CompanySignedDate may be date-only
df['CompanySignedDate'] = pd.to_datetime(df['CompanySignedDate'], utc=True)
# Compute sales cycle in days
df['turnaround_days'] = (df['CompanySignedDate'] - df['CreatedDate']).dt.total_seconds() / 86400.0
# Group by OwnerId and compute average
grouped = df.groupby('OwnerId', as_index=False)['turnaround_days'].mean()
# Find owner with minimum average turnaround
min_row = grouped.loc[grouped['turnaround_days'].idxmin()]
result_id = min_row['OwnerId']

print("__RESULT__:")
print(json.dumps(result_id))"""

env_args = {'var_call_icl7iJEu3JSPSxaQodXrtjwR': [{'OwnerId': '005Wt000003NJgAIAW', 'CreatedDate': '2023-04-25T10:45:30.000+0000', 'CompanySignedDate': '2023-06-13'}, {'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'CompanySignedDate': '2023-10-13'}, {'OwnerId': '#005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'CompanySignedDate': '2023-09-30'}]}

exec(code, env_args)
