code = """import pandas as pd
import json

# Load the casehistory__c query result from storage
records_path = var_call_qslKRqsMLF8TaFbzGLLoyNpZ

# records_path may be a filepath string
with open(records_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Normalize ID-like fields: strip leading '#' and whitespace
def normalize_id(x):
    if pd.isna(x):
        return None
    if isinstance(x, str):
        s = x.strip()
        if s.startswith('#'):
            s = s[1:]
        if s == '' or s.lower() == 'none':
            return None
        return s
    return str(x)

# Normalize relevant columns
for col in ['oldvalue__c', 'newvalue__c', 'caseid__c']:
    if col in df.columns:
        df[col] = df[col].apply(normalize_id)

# Parse dates
df['createddate'] = pd.to_datetime(df['createddate'], errors='coerce')

# Define date range: last 4 quarters up to today's date 2023-04-10
end_date = pd.to_datetime('2023-04-10')
start_date = end_date - pd.DateOffset(months=12)  # last 4 quarters ~ 12 months

# Filter Owner Assignment rows in date range
mask = (df['field__c'] == 'Owner Assignment') & (df['createddate'] >= start_date) & (df['createddate'] <= end_date)
df_oa = df[mask].copy()

# Compute handled cases per agent: count of distinct caseid__c where newvalue__c == agent
handled = df_oa.dropna(subset=['newvalue__c']).groupby('newvalue__c')['caseid__c'].nunique().reset_index()
handled.columns = ['agent_id', 'handled_cases_count']

# Compute transfer counts per agent: count of Owner Assignment rows where oldvalue__c is agent and represents a transfer
# A transfer row: oldvalue__c is not null, and oldvalue__c != newvalue__c
transfers = df_oa[(df_oa['oldvalue__c'].notna()) & (df_oa['oldvalue__c'] != df_oa['newvalue__c'])]
transfer_counts = transfers.groupby('oldvalue__c').size().reset_index(name='transfer_count')
transfer_counts.columns = ['agent_id', 'transfer_count']

# Merge handled and transfer_counts
merged = pd.merge(handled, transfer_counts, on='agent_id', how='left')
merged['transfer_count'] = merged['transfer_count'].fillna(0).astype(int)

# Filter agents who handled more than 0 cases
merged = merged[merged['handled_cases_count'] > 0]

# If no agents, return None
if merged.empty:
    result = None
else:
    # Find minimal transfer_count
    min_tc = merged['transfer_count'].min()
    candidates = merged[merged['transfer_count'] == min_tc].copy()
    # If multiple, pick lexicographically smallest agent id
    candidates['agent_id'] = candidates['agent_id'].astype(str)
    chosen = sorted(candidates['agent_id'].tolist())[0]
    result = chosen

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_jayA7wtKjIoOzqUL4RYaXKAM': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_qslKRqsMLF8TaFbzGLLoyNpZ': 'file_storage/call_qslKRqsMLF8TaFbzGLLoyNpZ.json'}

exec(code, env_args)
