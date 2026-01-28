code = """import json
import pandas as pd
from datetime import datetime

# Read case data from file
case_data_file = var_functions.query_db:6
with open(case_data_file, 'r') as f:
    case_records = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(case_records)

# Clean IDs (remove leading # and trailing whitespace)
def clean_id(id_val):
    if id_val is None or id_val == 'None':
        return None
    id_str = str(id_val).strip()
    if id_str.startswith('#'):
        id_str = id_str[1:]
    return id_str

df['clean_case_id'] = df['id'].apply(clean_id)
df['clean_owner_id'] = df['ownerid'].apply(clean_id)

# Filter out invalid rows
df = df[df['clean_case_id'].notna() & (df['clean_case_id'] != '') &
        df['clean_owner_id'].notna() & (df['clean_owner_id'] != '')]

# Parse dates
def parse_date(date_str):
    if date_str is None or date_str == 'None' or date_str == '':
        return None
    try:
        return pd.to_datetime(date_str)
    except:
        return None

df['created_date'] = df['createddate'].apply(parse_date)
df['closed_date'] = df['closeddate'].apply(parse_date)
df['assignment_date'] = df['assignment_date'].apply(parse_date)

# Filter cases in past 4 months (created >= 2023-05-02)
df_filtered = df[(df['created_date'] >= '2023-05-02') & 
                 (df['closed_date'].notna()) & 
                 (df['clean_case_id'] != '')].copy()

# For each case, count number of Owner Assignment entries to identify transfers
transfer_counts = df_filtered[df_filtered['field__c'] == 'Owner Assignment'].groupby('clean_case_id').size()
case_transfer_counts = transfer_counts.to_dict()

# Identify cases that were transferred (more than 1 Owner Assignment entry)
transferred_cases = {case_id for case_id, count in case_transfer_counts.items() if count > 1}

# For non-transferred cases, get handle time (closed - created) for the final owner
non_transferred_cases = []
for case_id in df_filtered['clean_case_id'].unique():
    if case_id not in transferred_cases:
        # Get the row with Case Closed to get final owner
        case_rows = df_filtered[df_filtered['clean_case_id'] == case_id]
        closed_row = case_rows[case_rows['field__c'] == 'Case Closed']
        if not closed_row.empty and len(closed_row) == 1:
            owner_id = closed_row.iloc[0]['clean_owner_id']
            created_date = closed_row.iloc[0]['created_date']
            closed_date = closed_row.iloc[0]['closed_date']
            
            if owner_id and created_date and closed_date:
                handle_time_hours = (closed_date - created_date).total_seconds() / 3600
                non_transferred_cases.append({
                    'case_id': case_id,
                    'owner_id': owner_id,
                    'handle_time_hours': handle_time_hours
                })

# Create DataFrame of non-transferred cases
if non_transferred_cases:
    df_non_transferred = pd.DataFrame(non_transferred_cases)
    
    # Count cases per agent
    agent_case_counts = df_non_transferred.groupby('owner_id').size()
    
    # Filter agents who processed more than one case
    agents_multiple_cases = agent_case_counts[agent_case_counts > 1].index.tolist()
    
    # Calculate average handle time for these agents
    agent_avg_handle_time = df_non_transferred[df_non_transferred['owner_id'].isin(agents_multiple_cases)].groupby('owner_id')['handle_time_hours'].mean()
    
    # Find agent with lowest average handle time
    if not agent_avg_handle_time.empty:
        best_agent_id = agent_avg_handle_time.idxmin()
        result = best_agent_id
    else:
        result = None
else:
    result = None

# Print result
print(f"__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_functions.query_db:5': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
