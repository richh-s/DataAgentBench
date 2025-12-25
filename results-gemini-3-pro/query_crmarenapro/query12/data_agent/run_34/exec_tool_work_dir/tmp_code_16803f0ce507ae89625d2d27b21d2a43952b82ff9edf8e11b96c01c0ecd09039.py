code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-277624887650380128'], 'r') as f:
    opp_data = json.load(f)
with open(locals()['var_function-call-277624887650381671'], 'r') as f:
    con_data = json.load(f)

df_opp = pd.DataFrame(opp_data)
df_con = pd.DataFrame(con_data)

# Clean IDs function
def clean_id(x):
    if x is None: return None
    return str(x).strip().lstrip('#')

# Apply cleaning
if not df_opp.empty:
    df_opp['ContractID__c'] = df_opp['ContractID__c'].apply(clean_id)
    df_opp['OwnerId'] = df_opp['OwnerId'].apply(clean_id)

if not df_con.empty:
    df_con['Id'] = df_con['Id'].apply(clean_id)

# Convert dates
# Handle potential errors with coerce
df_opp['CreatedDate'] = pd.to_datetime(df_opp['CreatedDate'], errors='coerce')
df_con['CompanySignedDate'] = pd.to_datetime(df_con['CompanySignedDate'], errors='coerce')

# Drop rows with NaT if any (essential for calculation)
df_opp = df_opp.dropna(subset=['CreatedDate'])
df_con = df_con.dropna(subset=['CompanySignedDate'])

# Filter Contracts for April 2023
# Year=2023, Month=4
df_con_apr = df_con[
    (df_con['CompanySignedDate'].dt.year == 2023) & 
    (df_con['CompanySignedDate'].dt.month == 4)
]

# Merge
# Inner join to get opportunities that have a corresponding contract signed in April 2023
merged = pd.merge(df_opp, df_con_apr, left_on='ContractID__c', right_on='Id', how='inner')

# Calculate Sales Cycle (in days)
# Definition: Days between Opportunity Creation and Company Signed Date
# Using date part only to measure whole days
merged['CreatedDate_date'] = merged['CreatedDate'].dt.date
merged['CompanySignedDate_date'] = merged['CompanySignedDate'].dt.date
merged['sales_cycle'] = (merged['CompanySignedDate_date'] - merged['CreatedDate_date']).apply(lambda x: x.days)

# Group by Agent (OwnerId) and calculate average
agent_stats = merged.groupby('OwnerId')['sales_cycle'].mean().reset_index()

# Find the quickest (minimum average duration)
if not agent_stats.empty:
    quickest_agent = agent_stats.sort_values(by='sales_cycle', ascending=True).iloc[0]
    result_id = quickest_agent['OwnerId']
else:
    result_id = "No agents found"

print("__RESULT__:")
print(json.dumps(result_id))"""

env_args = {'var_function-call-277624887650380128': 'file_storage/function-call-277624887650380128.json', 'var_function-call-277624887650381671': 'file_storage/function-call-277624887650381671.json'}

exec(code, env_args)
