code = """import json, pandas as pd, datetime as dt
from datetime import datetime

# Load full datasets
with open(var_call_kUAi8OMKJE2TuSTlYYTRBXJw, 'r') as f:
    cases = json.load(f)
with open(var_call_bHsF9dEUW3txgCut2OuUXNGb, 'r') as f:
    hist = json.load(f)

cases_df = pd.DataFrame(cases)
hist_df = pd.DataFrame(hist)

# Normalize IDs by stripping leading '#'
for col in ['id','ownerid']:
    cases_df[col] = cases_df[col].astype(str).str.lstrip('#')
for col in ['caseid__c','oldvalue__c','newvalue__c']:
    hist_df[col] = hist_df[col].astype(str).str.lstrip('#')

# Filter last 4 quarters relative to 2023-04-10 -> last 12 months: 2022-04-10 to 2023-04-10
start = pd.Timestamp('2022-04-10T00:00:00Z')
end = pd.Timestamp('2023-04-10T23:59:59Z')

hist_df['createddate'] = pd.to_datetime(hist_df['createddate'])

# Owner assignments only within window
owner_hist = hist_df[hist_df['field__c'] == 'Owner Assignment'].copy()
owner_hist = owner_hist[(owner_hist['createddate'] >= start) & (owner_hist['createddate'] <= end)]

# Build transfer records: each Owner Assignment after the first for a case is a transfer FROM oldvalue__c
# Need chronological per case
owner_hist = owner_hist.sort_values(['caseid__c','createddate'])

transfers = []
for case_id, grp in owner_hist.groupby('caseid__c'):
    # First assignment can be creation assignment; transfers are where oldvalue__c is not None/NaN and not 'None'
    for _, row in grp.iterrows():
        old = row['oldvalue__c']
        if pd.isna(old) or str(old) in ['None','']:
            continue
        from_agent = str(old)
        transfers.append({'from_agent': from_agent})

transfers_df = pd.DataFrame(transfers)

if transfers_df.empty:
    result = None
else:
    # Count transfers per from_agent
    counts = transfers_df.groupby('from_agent').size().reset_index(name='transfer_count')

    # Now determine agents who handled more than 0 cases in same period
    cases_df['createddate'] = pd.to_datetime(cases_df['createddate'])
    period_cases = cases_df[(cases_df['createddate'] >= start) & (cases_df['createddate'] <= end)].copy()

    # Build owner history including case initial owner from Case table and subsequent owner assignments
    # Initial owner is the Case.ownerid at creation
    initial_assign = period_cases[['id','ownerid']].rename(columns={'id':'caseid__c','ownerid':'agent'})

    # Owner assignments in period: newvalue__c is the agent
    oa_period = owner_hist.copy()
    oa_period = oa_period[(oa_period['createddate'] >= start) & (oa_period['createddate'] <= end)]
    oa_period = oa_period[~oa_period['newvalue__c'].isin(['None','', 'nan'])]
    oa_agents = oa_period[['caseid__c','newvalue__c']].rename(columns={'newvalue__c':'agent'})

    all_assignments = pd.concat([initial_assign, oa_agents], ignore_index=True)
    # Agents with >0 cases handled (distinct caseids)
    handled = all_assignments.groupby('agent')['caseid__c'].nunique().reset_index(name='case_count')
    handled = handled[handled['case_count'] > 0]

    # Join transfer counts with handled agents
    merged = handled.merge(counts, left_on='agent', right_on='from_agent', how='left')
    merged['transfer_count'] = merged['transfer_count'].fillna(0).astype(int)

    # Among handled agents, find min transfer_count (> =0) and pick agent with fewest transfers
    min_tc = merged['transfer_count'].min()
    fewest = merged[merged['transfer_count'] == min_tc].sort_values('agent').iloc[0]['agent']
    result = fewest

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_kUAi8OMKJE2TuSTlYYTRBXJw': 'file_storage/call_kUAi8OMKJE2TuSTlYYTRBXJw.json', 'var_call_bHsF9dEUW3txgCut2OuUXNGb': 'file_storage/call_bHsF9dEUW3txgCut2OuUXNGb.json'}

exec(code, env_args)
