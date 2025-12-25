code = """import json
import pandas as pd

# Retrieve file paths
opp_file_path = locals()['var_function-call-13256013357000701406']
contract_file_path = locals()['var_function-call-13256013357000701169']

# Load data
with open(opp_file_path, 'r') as f:
    opp_data = json.load(f)
with open(contract_file_path, 'r') as f:
    contract_data = json.load(f)

df_opp = pd.DataFrame(opp_data)
df_contract = pd.DataFrame(contract_data)

def clean_id(x):
    if x is None: return None
    return str(x).strip().lstrip('#')

df_opp['ContractID_clean'] = df_opp['ContractID__c'].apply(clean_id)
df_opp['OwnerId_clean'] = df_opp['OwnerId'].apply(clean_id)
df_contract['Id_clean'] = df_contract['Id'].apply(clean_id)

# Convert dates
# CreatedDate is likely tz-aware
df_opp['CreatedDate_dt'] = pd.to_datetime(df_opp['CreatedDate'], format='mixed')
# SignedDate is likely tz-naive
df_contract['SignedDate_dt'] = pd.to_datetime(df_contract['CompanySignedDate'], format='mixed')

# Make CreatedDate tz-naive (convert to UTC then drop tz info to match SignedDate which is naive 00:00:00)
# Or easier: Make SignedDate tz-aware (UTC).
# But standard practice for "days between" involving just a date (Signed) and a timestamp (Created)
# is to take the date part of Created.
# df['CreatedDate_dt'].dt.date returns python date objects, which subtract fine from pd.Timestamp.date().

# Let's normalize CreatedDate to remove time and timezone
# If we use .dt.tz_localize(None), we get naive datetime.
if df_opp['CreatedDate_dt'].dt.tz is not None:
    df_opp['CreatedDate_dt'] = df_opp['CreatedDate_dt'].dt.tz_convert(None)

# Now both are naive
merged = pd.merge(df_opp, df_contract, left_on='ContractID_clean', right_on='Id_clean', how='inner')

start_date = pd.Timestamp('2023-04-01')
end_date = pd.Timestamp('2023-04-30')

filtered = merged[(merged['SignedDate_dt'] >= start_date) & (merged['SignedDate_dt'] <= end_date)].copy()

if filtered.empty:
    print("__RESULT__:")
    print(json.dumps("No data found for April 2023"))
else:
    # Turnaround: SignedDate - CreatedDate (normalized to midnight)
    filtered['TurnaroundDays'] = (filtered['SignedDate_dt'] - filtered['CreatedDate_dt'].dt.normalize()).dt.days
    
    agent_stats = filtered.groupby('OwnerId_clean')['TurnaroundDays'].mean().reset_index()
    
    if agent_stats.empty:
         print("__RESULT__:")
         print(json.dumps("No agents found"))
    else:
        best_agent = agent_stats.sort_values(by='TurnaroundDays', ascending=True).iloc[0]
        result = {
            "AgentId": best_agent['OwnerId_clean'],
            "AverageDays": best_agent['TurnaroundDays']
        }
        print("__RESULT__:")
        print(json.dumps(result))"""

env_args = {'var_function-call-7921673078029791617': [{'Id': '006Wt000007AvVeIAK', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIqXIAW', 'CreatedDate': '2023-09-05T11:32:46.000+0000'}, {'Id': '006Wt000007Aw3WIAS', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIc1IAG', 'CreatedDate': '2024-04-05T12:15:30.000+0000'}, {'Id': '006Wt000007Aw3XIAS', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NJZhIAO', 'CreatedDate': '2021-02-10T14:23:45.000+0000'}, {'Id': '006Wt000007Aya9IAC', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NDJ0IAO', 'CreatedDate': '2023-08-11T09:30:00.000+0000'}, {'Id': '006Wt000007AyaAIAS', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NJxtIAG', 'CreatedDate': '2022-07-20T14:13:45.000+0000'}], 'var_function-call-7921673078029794800': [{'Id': '#800Wt00000DD0SZIA1', 'CompanySignedDate': '2021-07-16'}, {'Id': '800Wt00000DD0SaIAL', 'CompanySignedDate': '2021-09-28'}, {'Id': '#800Wt00000DD0SbIAL', 'CompanySignedDate': '2023-07-12'}, {'Id': '800Wt00000DDDuRIAX', 'CompanySignedDate': '2024-04-16'}, {'Id': '800Wt00000DDNFUIA5', 'CompanySignedDate': '2023-07-02'}], 'var_function-call-14703004230402979661': [{'count_star()': '163'}], 'var_function-call-14703004230402980654': [{'count_star()': '163'}], 'var_function-call-13256013357000701406': 'file_storage/function-call-13256013357000701406.json', 'var_function-call-13256013357000701169': 'file_storage/function-call-13256013357000701169.json'}

exec(code, env_args)
