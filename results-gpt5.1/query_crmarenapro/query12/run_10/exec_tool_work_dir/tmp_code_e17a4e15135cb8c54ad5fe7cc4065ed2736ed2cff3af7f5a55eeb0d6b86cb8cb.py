code = """import pandas as pd, json

data = var_call_WpmK6w9r9rxdjBqz7v7SE4ZV

df = pd.DataFrame(data)

for col in ['AgentId', 'OppId']:
    df[col] = df[col].astype(str).str.replace('#', '', regex=False).str.strip()

# Parse dates; force both to be timezone-naive

df['OppCreatedDate'] = pd.to_datetime(df['OppCreatedDate'], utc=True).dt.tz_convert(None)
df['CompanySignedDate'] = pd.to_datetime(df['CompanySignedDate'])

# Compute sales cycle in days
df['cycle_days'] = (df['CompanySignedDate'] - df['OppCreatedDate']).dt.total_seconds() / 86400.0

agg = df.groupby('AgentId', as_index=False)['cycle_days'].mean()
min_row = agg.loc[agg['cycle_days'].idxmin()]
result = min_row['AgentId']

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_h7Yg8ltunGwz1FKbUvWJV5bt': [{'AgentId': '005Wt000003NJgAIAW', 'OppId': '#006Wt000007BChmIAG', 'OppCreatedDate': '2023-04-25T10:45:30.000+0000', 'CompanySignedDate': '2023-06-13'}, {'AgentId': '005Wt000003NISMIA4', 'OppId': '006Wt000007BDApIAO', 'OppCreatedDate': '2023-04-10T10:15:30.000+0000', 'CompanySignedDate': '2023-10-13'}, {'AgentId': '#005Wt000003NEa3IAG', 'OppId': '006Wt000007BHPhIAO', 'OppCreatedDate': '2023-04-15T09:12:34.000+0000', 'CompanySignedDate': '2023-09-30'}], 'var_call_WpmK6w9r9rxdjBqz7v7SE4ZV': [{'AgentId': '005Wt000003NJgAIAW', 'OppId': '#006Wt000007BChmIAG', 'OppCreatedDate': '2023-04-25T10:45:30.000+0000', 'CompanySignedDate': '2023-06-13'}, {'AgentId': '005Wt000003NISMIA4', 'OppId': '006Wt000007BDApIAO', 'OppCreatedDate': '2023-04-10T10:15:30.000+0000', 'CompanySignedDate': '2023-10-13'}, {'AgentId': '#005Wt000003NEa3IAG', 'OppId': '006Wt000007BHPhIAO', 'OppCreatedDate': '2023-04-15T09:12:34.000+0000', 'CompanySignedDate': '2023-09-30'}]}

exec(code, env_args)
