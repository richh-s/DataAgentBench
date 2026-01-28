code = """import pandas as pd
import json
# var_call_BihVrs4EnrbSm1UKMwjsS0WB is available
records = var_call_BihVrs4EnrbSm1UKMwjsS0WB

df = pd.DataFrame(records)
# Clean Ids: remove leading # and trim whitespace
for col in ['OpportunityId','OwnerId','ContractId']:
    if col in df.columns:
        df[col] = df[col].astype(str).str.replace('#','', regex=False).str.strip()

# Parse dates
df['CreatedDate'] = pd.to_datetime(df['CreatedDate'])
# CompanySignedDate may be date-only
df['CompanySignedDate'] = pd.to_datetime(df['CompanySignedDate'])

# Calculate sales cycle in days
df['SalesCycleDays'] = (df['CompanySignedDate'] - df['CreatedDate']).dt.days

# For each agent (OwnerId), compute avg sales cycle
agg = df.groupby('OwnerId', as_index=False)['SalesCycleDays'].mean()
agg['SalesCycleDays'] = agg['SalesCycleDays'].round(6)

# Get agent with minimum average days
min_row = agg.loc[agg['SalesCycleDays'].idxmin()]
result = {"AgentId": min_row['OwnerId']}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_BihVrs4EnrbSm1UKMwjsS0WB': [{'OpportunityId': '#006Wt000007BChmIAG', 'OwnerId': '005Wt000003NJgAIAW', 'CreatedDate': '2023-04-25T10:45:30.000+0000', 'ContractId': '#800Wt00000DE9FFIA1', 'CompanySignedDate': '2023-06-13'}, {'OpportunityId': '006Wt000007BDApIAO', 'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'ContractId': '800Wt00000DE8sgIAD', 'CompanySignedDate': '2023-10-13'}, {'OpportunityId': '006Wt000007BHPhIAO', 'OwnerId': '#005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'ContractId': '800Wt00000DE9ryIAD', 'CompanySignedDate': '2023-09-30'}]}

exec(code, env_args)
