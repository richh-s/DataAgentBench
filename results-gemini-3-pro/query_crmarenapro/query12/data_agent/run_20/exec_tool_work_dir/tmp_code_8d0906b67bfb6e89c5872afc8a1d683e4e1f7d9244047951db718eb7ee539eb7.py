code = """import json
import pandas as pd

# Load Opportunity data
with open(locals()['var_function-call-16291847767838896705'], 'r') as f:
    opp_data = json.load(f)

# Load Contract data
with open(locals()['var_function-call-16291847767838900130'], 'r') as f:
    contract_data = json.load(f)

df_opp = pd.DataFrame(opp_data)
df_cont = pd.DataFrame(contract_data)

# Clean IDs
def clean_id(x):
    if isinstance(x, str):
        return x.lstrip('#').strip()
    return x

df_opp['Id'] = df_opp['Id'].apply(clean_id)
df_opp['ContractID__c'] = df_opp['ContractID__c'].apply(clean_id)
df_opp['OwnerId'] = df_opp['OwnerId'].apply(clean_id)
df_cont['Id'] = df_cont['Id'].apply(clean_id)

# Filter valid contracts
df_opp = df_opp[df_opp['ContractID__c'] != 'None']

# Merge
df_merged = pd.merge(df_opp, df_cont, left_on='ContractID__c', right_on='Id', how='inner')

# Convert dates
# CreatedDate format: 2023-09-05T11:32:46.000+0000
# CompanySignedDate format: 2021-07-16
df_merged['CreatedDate_dt'] = pd.to_datetime(df_merged['CreatedDate'])
df_merged['CompanySignedDate_dt'] = pd.to_datetime(df_merged['CompanySignedDate'])

# Filter for April 2023 signed date
# April 2023: 2023-04-01 to 2023-04-30
start_date = pd.Timestamp('2023-04-01').tz_localize(None)
end_date = pd.Timestamp('2023-04-30').tz_localize(None)

# Handle timezone in CreatedDate_dt
# If CreatedDate has timezone, we should convert to naive or handle it.
# CompanySignedDate usually has no time, so it's naive (00:00:00).
# Let's convert CreatedDate to naive (UTC) or just date.
# Policy says "number of days between ...". Usually this is date diff.
df_merged['CreatedDate_date'] = df_merged['CreatedDate_dt'].dt.date
df_merged['CompanySignedDate_date'] = df_merged['CompanySignedDate_dt'].dt.date

# Convert date objects to datetime for comparison or use string comparison
df_merged['CompanySignedDate_dt_naive'] = pd.to_datetime(df_merged['CompanySignedDate_date'])

april_contracts = df_merged[
    (df_merged['CompanySignedDate_dt_naive'] >= start_date) & 
    (df_merged['CompanySignedDate_dt_naive'] <= end_date)
].copy()

# Calculate duration
# Difference in days
april_contracts['Duration'] = (pd.to_datetime(april_contracts['CompanySignedDate_date']) - pd.to_datetime(april_contracts['CreatedDate_date'])).dt.days

# Group by OwnerId and calc mean
avg_duration = april_contracts.groupby('OwnerId')['Duration'].mean().reset_index()
avg_duration = avg_duration.sort_values(by='Duration', ascending=True)

print("__RESULT__:")
print(avg_duration.to_json(orient='records'))"""

env_args = {'var_function-call-16291847767838896705': 'file_storage/function-call-16291847767838896705.json', 'var_function-call-16291847767838900130': 'file_storage/function-call-16291847767838900130.json'}

exec(code, env_args)
