code = """import json
import pandas as pd
from datetime import datetime

# Load data
with open(locals()['var_function-call-11359853726072965882'], 'r') as f:
    opps = json.load(f)
with open(locals()['var_function-call-11359853726072963635'], 'r') as f:
    contracts = json.load(f)

# Create DataFrames
df_opp = pd.DataFrame(opps)
df_cont = pd.DataFrame(contracts)

# Clean IDs function
def clean_id(x):
    if x and isinstance(x, str):
        return x.lstrip('#').strip()
    return x

# Apply cleaning
df_opp['ContractID__c'] = df_opp['ContractID__c'].apply(clean_id)
df_opp['OwnerId'] = df_opp['OwnerId'].apply(clean_id)
df_cont['Id'] = df_cont['Id'].apply(clean_id)

# Filter Contracts for April 2023
# CompanySignedDate format "YYYY-MM-DD"
df_cont['CompanySignedDate'] = pd.to_datetime(df_cont['CompanySignedDate'])
start_date = pd.Timestamp('2023-04-01')
end_date = pd.Timestamp('2023-04-30')
df_cont_apr = df_cont[(df_cont['CompanySignedDate'] >= start_date) & (df_cont['CompanySignedDate'] <= end_date)]

# Join
# Opportunity.ContractID__c = Contract.Id
merged = pd.merge(df_opp, df_cont_apr, left_on='ContractID__c', right_on='Id', how='inner')

if merged.empty:
    print("__RESULT__:")
    print(json.dumps("No records found"))
else:
    # Calculate duration
    # CreatedDate format "2023-09-05T11:32:46.000+0000"
    # CompanySignedDate is datetime64[ns]
    
    # Parse CreatedDate. It has offset. CompanySignedDate does not (naive, date only).
    # We should normalize to date or convert both to timezone-naive.
    # The policy says "days between". Usually this means date difference.
    
    merged['CreatedDate'] = pd.to_datetime(merged['CreatedDate']).dt.tz_localize(None)
    
    # Calculate days difference
    merged['duration_days'] = (merged['CompanySignedDate'] - merged['CreatedDate']).dt.total_seconds() / (24 * 3600)
    
    # In case created date is after signed date (should not happen but data can be dirty), take absolute or filter?
    # Policy says "creation date and ... signed date". Implies Signed - Created.
    # If negative, it's weird, but we follow formula.
    
    # Group by OwnerId
    agent_stats = merged.groupby('OwnerId')['duration_days'].mean().reset_index()
    
    # Find min
    min_agent = agent_stats.loc[agent_stats['duration_days'].idxmin()]
    
    result = min_agent['OwnerId']
    
    print("__RESULT__:")
    print(json.dumps(result))"""

env_args = {'var_function-call-11359853726072965882': 'file_storage/function-call-11359853726072965882.json', 'var_function-call-11359853726072963635': 'file_storage/function-call-11359853726072963635.json'}

exec(code, env_args)
