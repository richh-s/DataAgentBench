code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-4007717610855891085'], 'r') as f:
    opp_data = json.load(f)
with open(locals()['var_function-call-4007717610855894568'], 'r') as f:
    con_data = json.load(f)

df_opp = pd.DataFrame(opp_data)
df_con = pd.DataFrame(con_data)

# Helper to clean IDs
def clean_id(x):
    if not isinstance(x, str):
        return x
    return x.strip().lstrip('#')

# Clean relevant columns
df_opp['ContractID__c'] = df_opp['ContractID__c'].apply(clean_id)
df_opp['OwnerId'] = df_opp['OwnerId'].apply(clean_id)
df_con['Id'] = df_con['Id'].apply(clean_id)

# Filter contracts for April 2023
# CompanySignedDate format YYYY-MM-DD
df_con['CompanySignedDate'] = pd.to_datetime(df_con['CompanySignedDate'])
start_date = pd.Timestamp('2023-04-01')
end_date = pd.Timestamp('2023-04-30')

df_con_apr = df_con[(df_con['CompanySignedDate'] >= start_date) & (df_con['CompanySignedDate'] <= end_date)].copy()

# Join
# Inner join because we need the contract date for the calculation
merged = pd.merge(df_opp, df_con_apr, left_on='ContractID__c', right_on='Id', how='inner')

# Calculate cycle time
# CreatedDate format e.g. "2023-09-05T11:32:46.000+0000"
# We need to handle the timezone.
merged['CreatedDate'] = pd.to_datetime(merged['CreatedDate'], format='mixed')

# Policy: days between creation and signed date
# We'll use (SignedDate - CreatedDate).days
# But CreatedDate has time. Should we normalize CreatedDate to date or keep time?
# Usually "days between" might mean DateDiff. If Created 2023-04-01 23:00 and Signed 2023-04-02, is that 1 day?
# If we convert CreatedDate to just date part, it's safer.
merged['CreatedDate_dt'] = merged['CreatedDate'].dt.normalize().dt.tz_localize(None) # remove time and tz
# CompanySignedDate is already just date (set to midnight).

merged['cycle_days'] = (merged['CompanySignedDate'] - merged['CreatedDate_dt']).dt.days

# Group by Agent (OwnerId)
agent_stats = merged.groupby('OwnerId')['cycle_days'].mean().reset_index()
agent_stats = agent_stats.sort_values(by='cycle_days', ascending=True)

print("__RESULT__:")
print(agent_stats.head(5).to_json(orient='records'))"""

env_args = {'var_function-call-4007717610855891085': 'file_storage/function-call-4007717610855891085.json', 'var_function-call-4007717610855894568': 'file_storage/function-call-4007717610855894568.json'}

exec(code, env_args)
