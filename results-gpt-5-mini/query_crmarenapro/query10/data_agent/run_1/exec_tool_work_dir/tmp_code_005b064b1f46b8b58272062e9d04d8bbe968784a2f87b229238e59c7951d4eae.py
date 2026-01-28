code = """import json
import pandas as pd
from datetime import datetime

# Load data from previous query stored in var_call_Z3UwYp3NzqQoeZ7kuhzrEnfo
file_path = var_call_Z3UwYp3NzqQoeZ7kuhzrEnfo
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Normalization function
def norm_id(x):
    if x is None:
        return None
    s = str(x).strip()
    if s == '' or s.lower() == 'none':
        return None
    if s.startswith('#'):
        s = s[1:]
    return s

# Normalize relevant columns
for col in ['caseid__c','oldvalue__c','newvalue__c','field__c','id']:
    if col in df.columns:
        df[col] = df[col].apply(norm_id)

# Parse createddate
df['createddate_parsed'] = pd.to_datetime(df['createddate'], errors='coerce')

# Ensure timezone naive (remove tz) for comparisons
if df['createddate_parsed'].dt.tz is not None:
    df['createddate_parsed'] = df['createddate_parsed'].dt.tz_convert(None)

# Filter relevant fields just in case
df = df[df['field__c'].isin(['Owner Assignment','Case Creation','Case Closed'])]

# Build agent -> set(caseids) for processed count (count any Owner Assignment occurrence)
owner_rows = df[df['field__c']=='Owner Assignment']
agent_case_map = {}
for _, row in owner_rows.iterrows():
    agent = row['newvalue__c']
    caseid = row['caseid__c']
    if agent is None or caseid is None:
        continue
    agent_case_map.setdefault(agent, set()).add(caseid)

processed_count = {agent: len(cases) for agent, cases in agent_case_map.items()}

# Define time window: past four months from 2023-09-02 -> from 2023-05-02 to 2023-09-02 inclusive
end_date = pd.to_datetime('2023-09-02T23:59:59')
start_date = pd.to_datetime('2023-05-02T00:00:00')

# Group by case
cases = []
for caseid, g in df.groupby('caseid__c'):
    creation_rows = g[g['field__c']=='Case Creation']
    closed_rows = g[g['field__c']=='Case Closed']
    owner_rows_case = g[g['field__c']=='Owner Assignment']
    # Unique owner ids ignoring None
    owners = sorted(set([norm_id(x) for x in owner_rows_case['newvalue__c'].tolist() if norm_id(x) is not None]))
    creation_date = None
    closed_date = None
    if not creation_rows.empty:
        # take earliest creation
        creation_date = creation_rows['createddate_parsed'].min()
    if not closed_rows.empty:
        # take latest closed
        closed_date = closed_rows['createddate_parsed'].max()
    cases.append({
        'caseid': caseid,
        'creation_date': creation_date,
        'closed_date': closed_date,
        'owner_unique_ids': owners,
    })

cases_df = pd.DataFrame(cases)

# Drop rows without dates
cases_df = cases_df.dropna(subset=['creation_date','closed_date'])

# Ensure naive datetimes for comparison
cases_df['creation_date'] = pd.to_datetime(cases_df['creation_date']).dt.tz_localize(None)
cases_df['closed_date'] = pd.to_datetime(cases_df['closed_date']).dt.tz_localize(None)

# Filter closed in window
cases_df = cases_df[(cases_df['closed_date'] >= start_date) & (cases_df['closed_date'] <= end_date)]

# For handle time, exclude transferred cases: only include cases where owner_unique_ids has length 1
cases_df['is_transferred'] = cases_df['owner_unique_ids'].apply(lambda x: False if (isinstance(x, list) and len(x)==1) else True)
cases_df = cases_df[ cases_df['is_transferred'] == False ]

# Compute handle time seconds and owner id
cases_df['owner'] = cases_df['owner_unique_ids'].apply(lambda x: x[0] if isinstance(x, list) and len(x)==1 else None)
cases_df['handle_seconds'] = (cases_df['closed_date'] - cases_df['creation_date']).dt.total_seconds()

# Build per-agent handle times
agent_times = {}
for _, row in cases_df.iterrows():
    owner = row['owner']
    if owner is None:
        continue
    secs = row['handle_seconds']
    if secs is None or secs < 0:
        continue
    agent_times.setdefault(owner, []).append(secs)

# Compute average handle time for agents who processed more than one case (processed_count > 1)
avg_handle = {}
for agent, times in agent_times.items():
    if processed_count.get(agent,0) > 1 and len(times) > 0:
        avg = sum(times)/len(times)
        avg_handle[agent] = avg

# Find agent with lowest average handle time
if not avg_handle:
    result = None
else:
    # min by average, tie-breaker by agent id
    min_agent = min(sorted(avg_handle.keys()), key=lambda a: avg_handle[a])
    result = min_agent

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_dxxMKKK7PO4Etx13KVbtKySO': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_k12Ddy3OBi381N89aCOiMOqd': [{'field__c': 'Owner Assignment'}, {'field__c': 'Case Closed'}, {'field__c': 'Case Creation'}], 'var_call_Z3UwYp3NzqQoeZ7kuhzrEnfo': 'file_storage/call_Z3UwYp3NzqQoeZ7kuhzrEnfo.json'}

exec(code, env_args)
