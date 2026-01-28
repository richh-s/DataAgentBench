code = """import pandas as pd
import json

# var_call_t4WbSmc9Rj57p85kCRSqKtLp is provided by the previous query_db call
records = var_call_t4WbSmc9Rj57p85kCRSqKtLp

df = pd.DataFrame(records)
# Clean OwnerId: strip whitespace and leading '#'
df['OwnerId'] = df['OwnerId'].astype(str).str.strip().str.lstrip('#')

# Parse dates
df['CreatedDate'] = pd.to_datetime(df['CreatedDate'], utc=True)
# CompanySignedDate may be just a date string
df['CompanySignedDate'] = pd.to_datetime(df['CompanySignedDate']).dt.tz_localize('UTC')

# Compute turnaround in days (as float)
df['turnaround_days'] = (df['CompanySignedDate'] - df['CreatedDate']).dt.total_seconds() / 86400.0

# Group by OwnerId and compute average turnaround
grouped = df.groupby('OwnerId', as_index=False)['turnaround_days'].mean()

# Find owner with minimum average turnaround
min_row = grouped.loc[grouped['turnaround_days'].idxmin()]
best_owner = min_row['OwnerId']

# Print result as a JSON string (just the agent Id)
print("__RESULT__:")
print(json.dumps(best_owner))"""

env_args = {'var_call_t4WbSmc9Rj57p85kCRSqKtLp': [{'OppId': '006Wt000007BDApIAO', 'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'ContractId': '800Wt00000DE8sgIAD', 'CompanySignedDate': '2023-10-13'}, {'OppId': '006Wt000007BHPhIAO', 'OwnerId': '#005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'ContractId': '800Wt00000DE9ryIAD', 'CompanySignedDate': '2023-09-30'}]}

exec(code, env_args)
