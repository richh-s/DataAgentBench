code = """import json
import pandas as pd
from datetime import datetime

# Load data
with open(locals()['var_function-call-15161469565546595437'], 'r') as f:
    cases = json.load(f)
with open(locals()['var_function-call-14198618089919666215'], 'r') as f:
    history = json.load(f)

# Helper to clean IDs
def clean_id(x):
    if x is None: return None
    x = str(x).strip()
    if x.startswith('#'):
        x = x[1:]
    return x

# Convert to DataFrame
df_case = pd.DataFrame(cases)
df_hist = pd.DataFrame(history)

# Clean IDs
df_case['id'] = df_case['id'].apply(clean_id)
df_case['ownerid'] = df_case['ownerid'].apply(clean_id)
df_hist['caseid__c'] = df_hist['caseid__c'].apply(clean_id)
df_hist['newvalue__c'] = df_hist['newvalue__c'].apply(clean_id)
df_hist['oldvalue__c'] = df_hist['oldvalue__c'].apply(clean_id)

# Parse dates
def parse_date(x):
    if x is None or x == 'None': return pd.NaT
    # Format: 2023-07-02T11:00:00.000+0000
    try:
        return pd.to_datetime(x, format="%Y-%m-%dT%H:%M:%S.%f%z")
    except:
        return pd.to_datetime(x, errors='coerce')

df_case['createddate'] = df_case['createddate'].apply(parse_date)
df_case['closeddate'] = df_case['closeddate'].apply(parse_date)
df_hist['createddate'] = df_hist['createddate'].apply(parse_date)

# Define window
end_date = pd.Timestamp('2023-09-02', tz='UTC')
start_date = pd.Timestamp('2023-05-02', tz='UTC')

# Filter 1: Identify "Single Owner" cases
# Policy: "For cases that have NOT been transferred... only ONE 'Owner Assignment'"
# We count 'Owner Assignment' rows in history per case.
# Note: field__c could be 'Owner' or 'OwnerId' or 'Owner Assignment'
# Check unique values of field__c in history
owner_fields = ['Owner Assignment', 'Owner', 'OwnerId']
df_hist_owner = df_hist[df_hist['field__c'].isin(owner_fields)]

# Count assignments per case
assignment_counts = df_hist_owner.groupby('caseid__c').size().reset_index(name='count')

# Merge count to cases
df_case = df_case.merge(assignment_counts, left_on='id', right_on='caseid__c', how='left')
df_case['count'] = df_case['count'].fillna(0) 
# If count is 0, it might mean no history recorded? 
# Or maybe the initial assignment isn't in history?
# Policy says "there will be only ONE". This implies if it's not transferred, count is 1.
# If count is 0, maybe we assume 1? Or maybe data is missing.
# Let's inspect if count 1 is common.

# Handle Time Calculation
# Filter cases closed in window
mask_closed_in_window = (df_case['closeddate'] >= start_date) & (df_case['closeddate'] <= end_date)
# Filter single owner: count == 1 (Based on policy)
# "When computing handle time, we do not compute handle time for cases that have been transferred to other agents."
# This means we EXCLUDE cases with count > 1.
# What about count 0? If policy says "there will be ONE", count 0 is suspicious. 
# But let's assume count <= 1 is Single Owner (Not Transferred).
# Actually, if count > 1 it is transferred. 
mask_single_owner = (df_case['count'] <= 1)

df_ht = df_case[mask_closed_in_window & mask_single_owner].copy()
df_ht['handle_time'] = (df_ht['closeddate'] - df_ht['createddate']).dt.total_seconds()

# Average Handle Time per Agent
# Agent is 'ownerid'
avg_ht = df_ht.groupby('ownerid')['handle_time'].mean().reset_index()

# Filter 2: "Processing more than one case"
# Identify agents who processed > 1 case in the past 4 months.
# What counts as processing in the window?
# - Being 'ownerid' of a case active in the window (Created before end, Closed after start or Open)
# - Being in history (newvalue/oldvalue) in the window?
# A simpler, inclusive definition:
# Any agent appearing as ownerid in cases active in window?
# Or appearing in history assignments in window?
# Active cases:
mask_active = (df_case['createddate'] <= end_date) & ((df_case['closeddate'] >= start_date) | (df_case['closeddate'].isna()))
active_cases = df_case[mask_active]

# Agents involved in active cases
# 1. Current owners of active cases
agent_cases = []
for _, row in active_cases.iterrows():
    agent_cases.append({'agent': row['ownerid'], 'case': row['id']})

# 2. History assignments in window?
# If a case was transferred TO an agent in the window, they processed it.
# If a case was transferred FROM an agent in the window, they processed it.
mask_hist_window = (df_hist_owner['createddate'] >= start_date) & (df_hist_owner['createddate'] <= end_date)
hist_window = df_hist_owner[mask_hist_window]
for _, row in hist_window.iterrows():
    if row['newvalue__c']: agent_cases.append({'agent': row['newvalue__c'], 'case': row['caseid__c']})
    if row['oldvalue__c']: agent_cases.append({'agent': row['oldvalue__c'], 'case': row['caseid__c']})

# Create dataframe of agent-case pairs
df_agent_cases = pd.DataFrame(agent_cases).drop_duplicates()
# Count cases per agent
agent_counts = df_agent_cases.groupby('agent').size().reset_index(name='case_count')

# Filter agents with > 1 case
agents_gt_1 = agent_counts[agent_counts['case_count'] > 1]['agent'].tolist()

# Final Selection
# Filter avg_ht for these agents
final_stats = avg_ht[avg_ht['ownerid'].isin(agents_gt_1)].sort_values('handle_time')

print("__RESULT__:")
print(final_stats.head(5).to_json(orient='records'))"""

env_args = {'var_function-call-8046065142198950751': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-15161469565546595437': 'file_storage/function-call-15161469565546595437.json', 'var_function-call-14198618089919666215': 'file_storage/function-call-14198618089919666215.json'}

exec(code, env_args)
