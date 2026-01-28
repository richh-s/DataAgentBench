code = """import json
import pandas as pd

# Data from previous query stored in var_call_EBM48G9wwKIeBAblMQyGxnwJ
records = var_call_EBM48G9wwKIeBAblMQyGxnwJ

df = pd.DataFrame(records)

# Normalize OwnerId: remove leading '#' and surrounding whitespace
df['OwnerId'] = df['OwnerId'].astype(str).str.lstrip('#').str.strip()

# Parse dates
# CreatedDate includes time and timezone like '2023-04-25T10:45:30.000+0000'
# CompanySignedDate is date only like '2023-06-13'
df['CreatedDate'] = pd.to_datetime(df['CreatedDate'], utc=True, errors='coerce')
df['CompanySignedDate'] = pd.to_datetime(df['CompanySignedDate'], utc=True, errors='coerce')

# Compute turnaround in days (company_signed - created)
# Use total seconds / 86400 to get fractional days, then keep as float
df['turnaround_days'] = (df['CompanySignedDate'] - df['CreatedDate']).dt.total_seconds() / 86400.0

# Group by OwnerId and compute average turnaround
grouped = df.groupby('OwnerId', dropna=True)['turnaround_days'].mean().reset_index()

# Find OwnerId with minimum average turnaround
if grouped.empty:
    result = None
else:
    min_row = grouped.loc[grouped['turnaround_days'].idxmin()]
    result = min_row['OwnerId']

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_EBM48G9wwKIeBAblMQyGxnwJ': [{'OwnerId': '005Wt000003NJgAIAW', 'CreatedDate': '2023-04-25T10:45:30.000+0000', 'CompanySignedDate': '2023-06-13'}, {'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'CompanySignedDate': '2023-10-13'}, {'OwnerId': '#005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'CompanySignedDate': '2023-09-30'}]}

exec(code, env_args)
