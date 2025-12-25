code = """# Re-run logic with sanity checks
import pandas as pd
import json

with open(locals()['var_function-call-2221653753642693092']) as f:
    opps = json.load(f)
with open(locals()['var_function-call-2221653753642695317']) as f:
    contracts = json.load(f)

df_opp = pd.DataFrame(opps)
df_con = pd.DataFrame(contracts)

def clean_id(x):
    if pd.isna(x): return None
    x = str(x).strip()
    if x.startswith('#'):
        x = x[1:]
    return x

df_opp['ContractID__c'] = df_opp['ContractID__c'].apply(clean_id)
df_opp['OwnerId'] = df_opp['OwnerId'].apply(clean_id)
df_con['Id'] = df_con['Id'].apply(clean_id)

merged = pd.merge(df_opp, df_con, left_on='ContractID__c', right_on='Id', how='inner')

merged['CreatedDate'] = pd.to_datetime(merged['CreatedDate']).dt.tz_convert(None)
merged['CompanySignedDate'] = pd.to_datetime(merged['CompanySignedDate'])

start_date = pd.Timestamp('2023-04-01')
end_date = pd.Timestamp('2023-04-30')

filtered = merged[(merged['CompanySignedDate'] >= start_date) & (merged['CompanySignedDate'] <= end_date)].copy()

filtered['Turnaround'] = (filtered['CompanySignedDate'] - filtered['CreatedDate'].dt.normalize()).dt.days

# Sanity check: Filter out negative turnaround
valid_filtered = filtered[filtered['Turnaround'] >= 0].copy()

print(f"DEBUG: Records before non-negative filter: {len(filtered)}")
print(f"DEBUG: Records after non-negative filter: {len(valid_filtered)}")

if not valid_filtered.empty:
    agent_stats = valid_filtered.groupby('OwnerId')['Turnaround'].agg(['mean', 'count']).reset_index()
    # Sort by mean ascending
    best_agent = agent_stats.sort_values('mean', ascending=True).iloc[0]
    result = best_agent['OwnerId']
    print(f"DEBUG: Best Agent Stats: Mean={best_agent['mean']}, Count={best_agent['count']}")
else:
    result = "No valid records"

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-2221653753642693092': 'file_storage/function-call-2221653753642693092.json', 'var_function-call-2221653753642695317': 'file_storage/function-call-2221653753642695317.json', 'var_function-call-378924546127320741': '005Wt000003NDEBIA4'}

exec(code, env_args)
