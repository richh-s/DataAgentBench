code = """import pandas as pd
import json
records = var_call_hIEt70gliFe8uhQFJLI3Ftwe

df = pd.DataFrame(records)
# parse dates, make both timezone-aware or naive consistently
# CreatedDate has timezone info; CompanySignedDate is date only
# parse CreatedDate then normalize to date (remove tz)
df['CreatedDate'] = pd.to_datetime(df['CreatedDate']).dt.tz_convert(None)
# ensure CompanySignedDate parsed as date (no tz)
df['CompanySignedDate'] = pd.to_datetime(df['CompanySignedDate']).dt.tz_localize(None)

# compute turnaround days as difference in days between CompanySignedDate and CreatedDate date
# use date() to ignore times
df['CreatedDate_date'] = df['CreatedDate'].dt.normalize()
df['TurnaroundDays'] = (df['CompanySignedDate'] - df['CreatedDate_date']).dt.days

res = df.groupby('OwnerId', dropna=False)['TurnaroundDays'].mean().reset_index()
min_row = res.loc[res['TurnaroundDays'].idxmin()]
result = {'AgentId': min_row['OwnerId'], 'AverageTurnaroundDays': float(min_row['TurnaroundDays'])}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_hIEt70gliFe8uhQFJLI3Ftwe': [{'OpportunityId': '#006Wt000007BChmIAG', 'OwnerId': '005Wt000003NJgAIAW', 'CreatedDate': '2023-04-25T10:45:30.000+0000', 'ContractID__c': '800Wt00000DE9FFIA1', 'ContractId': '800Wt00000DE9FFIA1', 'CompanySignedDate': '2023-06-13'}, {'OpportunityId': '006Wt000007BDApIAO', 'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'ContractID__c': '800Wt00000DE8sgIAD', 'ContractId': '800Wt00000DE8sgIAD', 'CompanySignedDate': '2023-10-13'}, {'OpportunityId': '006Wt000007BHPhIAO', 'OwnerId': '005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'ContractID__c': '800Wt00000DE9ryIAD', 'ContractId': '800Wt00000DE9ryIAD', 'CompanySignedDate': '2023-09-30'}]}

exec(code, env_args)
