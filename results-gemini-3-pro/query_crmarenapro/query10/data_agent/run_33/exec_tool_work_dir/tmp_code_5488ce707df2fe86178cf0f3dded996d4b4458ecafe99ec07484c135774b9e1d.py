code = """import json
import pandas as pd
import datetime

# Load data
with open(locals()['var_function-call-8714509910446930341'], 'r') as f:
    cases_raw = json.load(f)
with open(locals()['var_function-call-12405440511442738773'], 'r') as f:
    hist_raw = json.load(f)

df_cases = pd.DataFrame(cases_raw)
df_hist = pd.DataFrame(hist_raw)

# Clean IDs function
def clean_id(x):
    if isinstance(x, str):
        return x.strip().lstrip('#')
    return x

# Apply cleaning
df_cases['id_clean'] = df_cases['id'].apply(clean_id)
df_cases['owner_clean'] = df_cases['ownerid'].apply(clean_id)

df_hist['caseid_clean'] = df_hist['caseid__c'].apply(clean_id)
df_hist['newval_clean'] = df_hist['newvalue__c'].apply(clean_id)

# Filter Cases by Date Range
# Range: 2023-05-02 to 2023-09-02
start_date = pd.Timestamp("2023-05-02", tz="UTC")
end_date = pd.Timestamp("2023-09-02", tz="UTC")

# Parse dates
df_cases['closeddate_dt'] = pd.to_datetime(df_cases['closeddate'], errors='coerce')
df_cases['createddate_dt'] = pd.to_datetime(df_cases['createddate'], errors='coerce')

# Filter
# We need to make sure closeddate_dt is aware or tz-naive consistent. 
# The strings have +0000, so they are UTC.
relevant_cases = df_cases[
    (df_cases['closeddate_dt'] >= start_date) & 
    (df_cases['closeddate_dt'] <= end_date + pd.Timedelta(days=1)) # Include the end date fully? "In the past 4 months" usually means inclusive.
    # The prompt says "Today's date: 2023-09-02". "Past 4 months" -> May 2 to Sep 2.
    # Let's check strict inequality or inclusive. Usually inclusive.
    # Also strict upper bound if we want to exclude "future"? But 2023-09-02 is "Today".
    # I'll use <= end_date (end of day? The date is just YMD). 
    # If I use <= timestamp('2023-09-02'), it means 2023-09-02 00:00:00.
    # If a case closed at 14:00 on Sep 2, it should be included.
    # So I will use < start of next day (Sep 3).
]
relevant_cases = relevant_cases[relevant_cases['closeddate_dt'] < (end_date + pd.Timedelta(days=1))]

# Data structures for counting
agent_processed_counts = {} # AgentID -> Set of CaseIDs
agent_handle_times = {} # AgentID -> List of durations (seconds)

# Pre-group history
hist_groups = df_hist.groupby('caseid_clean')

for idx, row in relevant_cases.iterrows():
    case_id = row['id_clean']
    current_owner = row['owner_clean']
    
    # Get owners from history
    if case_id in hist_groups.groups:
        hist_owners = set(hist_groups.get_group(case_id)['newval_clean'].unique())
    else:
        hist_owners = set()
    
    # All owners for this case
    all_owners = hist_owners.copy()
    if current_owner:
        all_owners.add(current_owner)
    
    # Update Processed Counts
    for agent in all_owners:
        if agent not in agent_processed_counts:
            agent_processed_counts[agent] = set()
        agent_processed_counts[agent].add(case_id)
        
    # Handle Time Calculation
    # Only if Single Owner
    if len(all_owners) == 1:
        # Single owner
        owner = list(all_owners)[0]
        duration = (row['closeddate_dt'] - row['createddate_dt']).total_seconds()
        
        if duration < 0:
            continue # Should not happen, but safety check
            
        if owner not in agent_handle_times:
            agent_handle_times[owner] = []
        agent_handle_times[owner].append(duration)

# Calculate Averages and Filter
results = []
for agent, cases in agent_processed_counts.items():
    if len(cases) > 1: # Filter > 1 case
        if agent in agent_handle_times and len(agent_handle_times[agent]) > 0:
            avg_time = sum(agent_handle_times[agent]) / len(agent_handle_times[agent])
            results.append({'agent': agent, 'avg_time': avg_time, 'case_count': len(cases)})

# Find min
if not results:
    final_res = "No matching agents"
else:
    min_agent = min(results, key=lambda x: x['avg_time'])
    final_res = min_agent['agent']

print("__RESULT__:")
print(json.dumps(final_res))"""

env_args = {'var_function-call-2226308914537843042': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-18198891999226845478': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_function-call-1173095882525426615': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_function-call-8714509910446930341': 'file_storage/function-call-8714509910446930341.json', 'var_function-call-12526052071437487588': 75, 'var_function-call-12405440511442738773': 'file_storage/function-call-12405440511442738773.json'}

exec(code, env_args)
