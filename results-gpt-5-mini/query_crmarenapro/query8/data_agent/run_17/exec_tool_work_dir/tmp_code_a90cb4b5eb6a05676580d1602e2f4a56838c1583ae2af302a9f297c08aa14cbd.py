code = """import json
import pandas as pd
from pathlib import Path

# Load the large result file from previous query
fp = Path(var_call_hjXNcvYymgcH2lFk3bEJeF3w)
with fp.open('r', encoding='utf-8') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Normalize owner values: strip whitespace, remove leading '#'
def norm_owner(x):
    if x is None:
        return None
    s = str(x).strip()
    if s == '':
        return None
    if s.lower() == 'none':
        return None
    if s.startswith('#'):
        s = s.lstrip('#')
    return s

for col in ['oldvalue__c', 'newvalue__c']:
    if col in df.columns:
        df[col] = df[col].apply(norm_owner)
    else:
        df[col] = None

# Parse createddate with UTC
df['createddate'] = pd.to_datetime(df['createddate'], errors='coerce', utc=True)

# Define last 4 quarters window: last 12 months from 2023-04-10 (inclusive)
end = pd.Timestamp('2023-04-10', tz='UTC')
start = end - pd.DateOffset(months=12)

# Filter Owner Assignment records within window and where field is Owner Assignment already done in query
mask = (df['createddate'] >= start) & (df['createddate'] <= end)
df = df.loc[mask].copy()

# Compute handled cases per agent: distinct caseid__c where agent appears in old or new
# Normalize case ids as strings and strip
df['caseid__c'] = df['caseid__c'].astype(str).str.strip()

agents = {}

for idx, row in df.iterrows():
    caseid = row['caseid__c']
    old = row['oldvalue__c']
    new = row['newvalue__c']
    # handled: if old or new present
    for a in (old, new):
        if a is None:
            continue
        if a not in agents:
            agents[a] = {'handled_cases': set(), 'transfer_count': 0}
        agents[a]['handled_cases'].add(caseid)
    # transfer count: if old present and not None, increment for old agent
    if old is not None:
        agents[old]['transfer_count'] += 1

# Filter agents with handled_cases > 0
filtered = {a: {'handled': len(v['handled_cases']), 'transfers': v['transfer_count']} for a, v in agents.items() if len(v['handled_cases']) > 0}

if not filtered:
    result = None
else:
    # Find minimum transfer count
    min_transfers = min(v['transfers'] for v in filtered.values())
    # Agents with that min
    mins = [a for a, v in filtered.items() if v['transfers'] == min_transfers]
    # Choose lexicographically smallest Id to be deterministic
    chosen = sorted(mins)[0]
    result = chosen

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_rWulKkeYQyXKayIa38ivkINr': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_WDoCyrqsSiBgIfeD2gpsm57u': [{'field__c': 'Owner Assignment'}, {'field__c': 'Case Closed'}, {'field__c': 'Case Creation'}], 'var_call_hjXNcvYymgcH2lFk3bEJeF3w': 'file_storage/call_hjXNcvYymgcH2lFk3bEJeF3w.json'}

exec(code, env_args)
