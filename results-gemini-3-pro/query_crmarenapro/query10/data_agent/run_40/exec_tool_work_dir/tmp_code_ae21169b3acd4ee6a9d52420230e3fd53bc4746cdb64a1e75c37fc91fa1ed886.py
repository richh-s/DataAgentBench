code = """import json
import pandas as pd
from datetime import datetime

# Load data
with open(locals()['var_function-call-437118952432706320'], 'r') as f:
    cases_data = json.load(f)
with open(locals()['var_function-call-7020999343042824830'], 'r') as f:
    history_data = json.load(f)

cases_df = pd.DataFrame(cases_data)
history_df = pd.DataFrame(history_data)

# Clean IDs (remove leading # and whitespace)
def clean_id(x):
    if pd.isna(x): return x
    return str(x).replace('#', '').strip()

cases_df['id'] = cases_df['id'].apply(clean_id)
cases_df['ownerid'] = cases_df['ownerid'].apply(clean_id)
cases_df['createddate'] = pd.to_datetime(cases_df['createddate'])
cases_df['closeddate'] = pd.to_datetime(cases_df['closeddate'], errors='coerce') # None becomes NaT

history_df['caseid__c'] = history_df['caseid__c'].apply(clean_id)
history_df['newvalue__c'] = history_df['newvalue__c'].apply(clean_id)
history_df['oldvalue__c'] = history_df['oldvalue__c'].apply(clean_id)
history_df['createddate'] = pd.to_datetime(history_df['createddate'])

# Define window
end_date = pd.Timestamp('2023-09-02').tz_localize('UTC')
start_date = end_date - pd.DateOffset(months=4)
# 2023-05-02 to 2023-09-02

# Filter History for Owner Assignment
# We need to know if a case was transferred.
# "For cases that have NOT been transferred... only ONE 'Owner Assignment', and for those that have been transferred, there will be MORE THAN ONE 'Owner Assignment'."
# So we count 'Owner Assignment' records per caseid.

owner_changes = history_df[history_df['field__c'] == 'Owner Assignment']
transfer_counts = owner_changes.groupby('caseid__c').size()

# Helper to check if single owner
def is_single_owner(case_id):
    # If count is <= 1, it's single owner.
    # Note: Some cases might not have history if they are old or created without history trigger?
    # But policy implies history tracks it.
    # If 0 history, assume Single Owner (the current one).
    count = transfer_counts.get(case_id, 0)
    return count <= 1

# 1. Identify "Managed Cases" per Agent in the window
# Managed means Agent was an owner (Initial or Transferred-to) and the case was "active" in the window?
# Or simply: Identify all (Agent, Case) pairs.
# Then filter those relevant to the window.
# But "managed in the past 4 months" implies the management happened or existed then.
# Simplification:
#   - Find all cases that were OPEN at any point in the window (Created <= End AND (Closed >= Start or Open)).
#   - For these cases, identify all agents who owned them.
#   - Since we don't have exact start/end dates for each ownership segment easily (without sorting history),
#     and the policy says "filter applies to both...", we can approximate:
#     If a case is active in the window, ALL agents who ever owned it "managed" it in the context of the case's lifecycle?
#     Maybe too broad.
#     Better: An agent managed a case in the window if they were the owner DURING the window.
#     Let's try to be precise.
#     Segments:
#       - Segment 1: Start = CreatedDate. Owner = First Owner (from history or current if no history). End = Date of first transfer (or Close/Now).
#       - Segment 2: Start = Date of transfer. Owner = New Owner. End = Next transfer/Close/Now.
#     We can build these segments.
#     Then check overlap with [Start, End].

# Build case ownership timeline
case_timelines = []

for case_id, case_row in cases_df.iterrows():
    cid = case_row['id']
    created = case_row['createddate']
    closed = case_row['closeddate'] if pd.notnull(case_row['closeddate']) else pd.Timestamp.now(tz='UTC') # Treat open as now for timeline
    
    # Get history for this case, sorted by date
    hist = owner_changes[owner_changes['caseid__c'] == cid].sort_values('createddate')
    
    segments = []
    
    if hist.empty:
        # Single owner: current owner
        owner = case_row['ownerid']
        segments.append({'owner': owner, 'start': created, 'end': closed})
    else:
        # Multiple owners
        # First segment: from creation to first history event
        # Who was first owner?
        # The first history entry has newvalue = 2nd owner? Or 1st?
        # Sample: field='Owner Assignment', newvalue='005...', oldvalue='None'.
        # This implies the history *records* the assignment.
        # If oldvalue is None, it's the first assignment (at creation or close to it).
        # Let's assume the history captures all assignments.
        # So each history row is a segment start.
        
        # Is there an implicit owner before the first history?
        # If the first history is at CreatedDate, then no.
        # If first history is later, who owned it before?
        # Usually Salesforce creates an Owner Assignment on create.
        # Let's assume the history covers it.
        
        current_time = created
        for _, h_row in hist.iterrows():
            new_owner = h_row['newvalue__c']
            change_date = h_row['createddate']
            
            # If there was a gap (e.g. created at T0, assigned at T1), who owned it T0-T1?
            # Maybe the creator? Or a default?
            # But usually 'Owner Assignment' at T0 exists if meaningful.
            # If the first record is at T1 (>> T0), we might have a gap.
            # But let's assume the segments are defined by these transitions.
            # Actually, looking at sample:
            # Created: 2023-09-07T16:30
            # History: 2023-09-07T16:30, NewValue: OwnerID.
            # So the history logs the initial assignment.
            
            # So, for each history row:
            # It starts a period of ownership for NewValue.
            # It ends the previous period.
            
            # What about the period *before* the first history?
            # If history starts at creation, there is no before.
            # If history starts later, the previous owner is unknown or it's the 'OldValue'.
            # If OldValue is None, maybe no previous owner?
            
            # Let's just collect all owners in history + current owner (to be safe).
            # And assume they managed it "during the case life".
            # If the case life overlaps the window, they managed it in the window.
            # This is a simplification but likely sufficient given "processing more than one case" usually refers to the case volume.
            
            pass

    # Alternative approach for "Managed Count":
    # Identify all cases active in the window (Created <= WindowEnd AND (Closed >= WindowStart OR Open)).
    # For each such case, identifying the agents involved.
    # Agents involved = Set of all owners in history + Current Owner.
    # Add (Agent, CaseID) to a list.
    
    is_active = (created <= end_date) and (closed >= start_date)
    if is_active:
        owners = set()
        owners.add(case_row['ownerid'])
        # Add from history
        h_owners = hist['newvalue__c'].unique()
        for o in h_owners:
            owners.add(o)
        
        for o in owners:
            if o and str(o).startswith('005'): # Only Users
                case_timelines.append({'agent': o, 'case_id': cid})

managed_df = pd.DataFrame(case_timelines).drop_duplicates()
managed_counts = managed_df.groupby('agent').size()
agents_more_than_one = managed_counts[managed_counts > 1].index.tolist()

# 2. Calculate Handle Time for Single Owner cases closed in window
# Filter cases
#  - Closed in window
#  - Single Owner (count of Owner Assignment <= 1)
#  - Agent is the Owner

ht_data = []

for _, row in cases_df.iterrows():
    # Check closed in window
    if pd.isna(row['closeddate']):
        continue
        
    c_date = row['closeddate']
    if c_date < start_date or c_date > end_date:
        continue
        
    cid = row['id']
    
    # Check single owner
    # Single owner means NO TRANSFER.
    # Transfers are 'Owner Assignment' > 1?
    # Or 'Owner Assignment' entries where new owner != old owner?
    # Sample showed "Owner Assignment" with old=None, new=Owner. That's 1 assignment (Initial).
    # If transferred, there would be a 2nd assignment (old=Owner, new=Owner2).
    # So Count <= 1 means Single Owner.
    # Count > 1 means Transferred.
    
    if transfer_counts.get(cid, 0) > 1:
        continue
    
    # Calculate Handle Time
    # Duration in hours? "lowest average handle time". Unit doesn't matter for comparison, but seconds/minutes is standard.
    # Definition: Closed - Created.
    duration = (row['closeddate'] - row['createddate']).total_seconds()
    
    # Owner
    owner = row['ownerid']
    if not str(owner).startswith('005'): continue
    
    ht_data.append({'agent': owner, 'handle_time': duration, 'case_id': cid})

ht_df = pd.DataFrame(ht_data)

# Filter for agents with > 1 managed cases
eligible_ht = ht_df[ht_df['agent'].isin(agents_more_than_one)]

# Compute average
avg_ht = eligible_ht.groupby('agent')['handle_time'].mean()

# Find lowest
if not avg_ht.empty:
    lowest_agent = avg_ht.idxmin()
    lowest_val = avg_ht.min()
    res = {'agent': lowest_agent, 'avg_ht': lowest_val}
else:
    res = {'agent': None, 'avg_ht': None}

print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-5978767766511989517': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-1984943891141236948': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_function-call-10018399236316566610': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-6693518546746403679': [{'count': '153'}], 'var_function-call-437118952432706320': 'file_storage/function-call-437118952432706320.json', 'var_function-call-16968160693626402289': [{'count': '393'}], 'var_function-call-7020999343042824830': 'file_storage/function-call-7020999343042824830.json'}

exec(code, env_args)
