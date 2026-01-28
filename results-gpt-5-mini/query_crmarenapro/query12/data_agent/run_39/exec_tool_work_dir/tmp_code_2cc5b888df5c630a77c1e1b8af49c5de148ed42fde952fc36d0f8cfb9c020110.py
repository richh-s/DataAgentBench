code = """import pandas as pd
import json
# var_call_hIEt70gliFe8uhQFJLI3Ftwe is available from storage
records = var_call_hIEt70gliFe8uhQFJLI3Ftwe

df = pd.DataFrame(records)
# parse dates
df['CreatedDate'] = pd.to_datetime(df['CreatedDate'])
df['CompanySignedDate'] = pd.to_datetime(df['CompanySignedDate'])
# compute turnaround days (sales cycle)
df['TurnaroundDays'] = (df['CompanySignedDate'] - df['CreatedDate'].dt.normalize()).dt.days
# compute average turnaround per OwnerId
res = df.groupby('OwnerId', dropna=False)['TurnaroundDays'].mean().reset_index()
# find owner with minimum average
min_row = res.loc[res['TurnaroundDays'].idxmin()]

result = {'AgentId': min_row['OwnerId'], 'AverageTurnaroundDays': float(min_row['TurnaroundDays'])}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_hIEt70gliFe8uhQFJLI3Ftwe': [{'OpportunityId': '#006Wt000007BChmIAG', 'OwnerId': '005Wt000003NJgAIAW', 'CreatedDate': '2023-04-25T10:45:30.000+0000', 'ContractID__c': '800Wt00000DE9FFIA1', 'ContractId': '800Wt00000DE9FFIA1', 'CompanySignedDate': '2023-06-13'}, {'OpportunityId': '006Wt000007BDApIAO', 'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'ContractID__c': '800Wt00000DE8sgIAD', 'ContractId': '800Wt00000DE8sgIAD', 'CompanySignedDate': '2023-10-13'}, {'OpportunityId': '006Wt000007BHPhIAO', 'OwnerId': '005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'ContractID__c': '800Wt00000DE9ryIAD', 'ContractId': '800Wt00000DE9ryIAD', 'CompanySignedDate': '2023-09-30'}]}

exec(code, env_args)
