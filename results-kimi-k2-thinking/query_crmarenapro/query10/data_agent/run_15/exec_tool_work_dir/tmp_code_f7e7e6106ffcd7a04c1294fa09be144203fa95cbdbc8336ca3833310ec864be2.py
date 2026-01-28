code = """import json
import pandas as pd
from datetime import datetime

# Load results from previous queries
cases = locals().get('var_functions.query_db:2', [])
history = locals().get('var_functions.query_db:8', [])

print(f"Number of cases loaded: {len(cases)}")
print(f"Number of history records loaded: {len(history)}")

# Clean case data
cleaned_cases = []
for case in cases:
    clean_case = {
        'id': case['id'].lstrip('#'),
        'ownerid': case['ownerid'].lstrip('#'),
        'createddate': case['createddate'],
        'closeddate': case['closeddate']
    }
    cleaned_cases.append(clean_case)

# Clean history data
cleaned_history = []
for hist in history:
    clean_hist = {
        'caseid__c': hist['caseid__c'].lstrip('#'),
        'oldvalue__c': hist['oldvalue__c'].lstrip('#'),
        'newvalue__c': hist['newvalue__c'].lstrip('#'),
        'createddate': hist['createddate']
    }
    cleaned_history.append(clean_hist)

cases_df = pd.DataFrame(cleaned_cases)
history_df = pd.DataFrame(cleaned_history)

# Parse dates
if not cases_df.empty:
    cases_df['createddate'] = pd.to_datetime(cases_df['createddate'])
    cases_df['closeddate'] = pd.to_datetime(cases_df['closeddate'])
    cases_df['handle_time_hours'] = (cases_df['closeddate'] - cases_df['createddate']).dt.total_seconds() / 3600

# Check which cases are in both datasets
case_ids_in_cases = set(cases_df['id'].unique())
case_ids_in_history = set(history_df['caseid__c'].unique())
common_cases = case_ids_in_cases.intersection(case_ids_in_history)

print(f"Unique cases in cases table: {len(case_ids_in_cases)}")
print(f"Unique cases in history table: {len(case_ids_in_history)}")
print(f"Common cases: {len(common_cases)}")
print(f"Cases in cases table but not in history: {len(case_ids_in_cases - case_ids_in_history)}")

# Check if history_df is empty
if history_df.empty:
    print("No history data available. Will use case table ownerid as the agent.")
    print(f"Cases sample: {cases_df.head()}")
    agents_multiple_cases = cases_df.groupby('ownerid').filter(lambda x: len(x) > 1)['ownerid'].unique()
    print(f"Agents with multiple cases: {len(agents_multiple_cases)}")
    print("__RESULT__:")
    print(json.dumps(None))
else:
    # Find cases with multiple owner assignments
    case_assignment_counts = history_df.groupby('caseid__c').size().reset_index(name='assignment_count')
    cases_with_single_assignment = case_assignment_counts[case_assignment_counts['assignment_count'] == 1]['caseid__c'].tolist()
    
    # Filter for non-transferred cases
    non_transferred_data = cases_df[cases_df['id'].isin(cases_with_single_assignment)].copy()
    
    # Add original agent from history
    initial_assignments = history_df.sort_values('createddate').groupby('caseid__c').first().reset_index()
    merged_data = non_transferred_data.merge(initial_assignments[['caseid__c', 'newvalue__c']], left_on='id', right_on='caseid__c', how='left')
    merged_data['original_agent'] = merged_data['newvalue__c'].fillna(merged_data['ownerid'])
    
    print(f"Non-transferred cases: {len(non_transferred_data)}")
    print(f"Cases after merge: {len(merged_data)}")
    
    # Count cases per agent
    if not merged_data.empty:
        case_counts = merged_data.groupby('original_agent').size().reset_index(name='case_count')
        agents_multiple_cases = case_counts[case_counts['case_count'] > 1]['original_agent'].tolist()
        
        print(f"Agents with > 1 case: {len(agents_multiple_cases)}")
        print(f"Final data to analyze: {len(merged_data)}")
        
        if len(agents_multiple_cases) > 0:
            filtered_data = merged_data[merged_data['original_agent'].isin(agents_multiple_cases)]
            avg_time = filtered_data.groupby('original_agent')['handle_time_hours'].mean().reset_index()
            avg_time = avg_time.sort_values('handle_time_hours')
            
            print(f"Available agents: {avg_time.head()}")
            if not avg_time.empty:
                lowest_agent_id = avg_time.iloc[0]['original_agent']
                lowest_hours = avg_time.iloc[0]['handle_time_hours']
                print(f"Agent with lowest AHT: {lowest_agent_id} ({lowest_hours:.2f} hours)")
                print("__RESULT__:")
                print(json.dumps(lowest_agent_id))
            else:
                print("No agents found with multiple cases")
                print("__RESULT__:")
                print(json.dumps(None))
        else:
            print("No agents processed more than one case")
            print("__RESULT__:")
            print(json.dumps(None))
    else:
        print("No non-transferred cases to analyze")
        print("__RESULT__:")
        print(json.dumps(None))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_functions.query_db:5': [], 'var_functions.query_db:6': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_functions.query_db:8': [{'id': 'a04Wt00000538O1IAI', 'caseid__c': '500Wt00000DDDfwIAH', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NH3GIAW', 'field__c': 'Owner Assignment', 'createddate': '2023-07-02T11:00:00.000+0000'}, {'id': 'a04Wt00000539QTIAY', 'caseid__c': '500Wt00000DDDfwIAH', 'oldvalue__c': '005Wt000003NH3GIAW', 'newvalue__c': '005Wt000003NJ0DIAW', 'field__c': 'Owner Assignment', 'createddate': '2023-07-02T11:30:02.000+0000'}, {'id': 'a04Wt00000538O3IAI', 'caseid__c': '500Wt00000DDTxbIAH', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIfFIAW', 'field__c': 'Owner Assignment', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'id': '#a04Wt00000537LUIAY', 'caseid__c': '500Wt00000DDepmIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJufIAG', 'field__c': 'Owner Assignment', 'createddate': '2023-07-01T10:30:00.000+0000'}, {'id': 'a04Wt00000538mAIAQ', 'caseid__c': '500Wt00000DDflsIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NF1SIAW', 'field__c': 'Owner Assignment', 'createddate': '2023-06-12T09:45:00.000+0000'}, {'id': 'a04Wt00000537YNIAY', 'caseid__c': '500Wt00000DDflsIAD', 'oldvalue__c': '005Wt000003NF1SIAW', 'newvalue__c': '005Wt000003NJppIAG', 'field__c': 'Owner Assignment', 'createddate': '2023-06-12T10:00:06.000+0000'}, {'id': 'a04Wt00000538FtIAI', 'caseid__c': '500Wt00000DDsG3IAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NI5mIAG', 'field__c': 'Owner Assignment', 'createddate': '2023-08-10T14:20:00.000+0000'}, {'id': '#a04Wt00000538r0IAA', 'caseid__c': '500Wt00000DDyzpIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJGLIA4', 'field__c': 'Owner Assignment', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'id': 'a04Wt00000537baIAA', 'caseid__c': '500Wt00000DDzUPIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'field__c': 'Owner Assignment', 'createddate': '2023-05-10T14:45:00.000+0000'}, {'id': '#a04Wt00000537zlIAA', 'caseid__c': '500Wt00000DDzXdIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJUrIAO', 'field__c': 'Owner Assignment', 'createddate': '2023-06-22T11:00:00.000+0000'}, {'id': 'a04Wt00000536Z5IAI', 'caseid__c': '500Wt00000DDzZHIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'field__c': 'Owner Assignment', 'createddate': '2023-07-02T09:30:00.000+0000'}, {'id': 'a04Wt00000538pNIAQ', 'caseid__c': '500Wt00000DDzivIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'field__c': 'Owner Assignment', 'createddate': '2023-06-05T11:15:00.000+0000'}, {'id': 'a04Wt00000538hKIAQ', 'caseid__c': '500Wt00000DDzkXIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'field__c': 'Owner Assignment', 'createddate': '2023-06-19T14:30:00.000+0000'}, {'id': 'a04Wt00000537ZzIAI', 'caseid__c': '500Wt00000DDzr0IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcvIAG', 'field__c': 'Owner Assignment', 'createddate': '2023-08-01T10:00:00.000+0000'}, {'id': 'a04Wt00000538scIAA', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO', 'field__c': 'Owner Assignment', 'createddate': '2023-06-30T13:03:00.000+0000'}, {'id': 'a04Wt00000532s4IAA', 'caseid__c': '500Wt00000DDzscIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'field__c': 'Owner Assignment', 'createddate': '2023-05-02T23:55:00.000+0000'}, {'id': 'a04Wt00000538hMIAQ', 'caseid__c': '500Wt00000DDzuEIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJJaIAO', 'field__c': 'Owner Assignment', 'createddate': '2023-06-02T09:30:00.000+0000'}, {'id': 'a04Wt00000539BxIAI', 'caseid__c': '500Wt00000DE02HIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIddIAG', 'field__c': 'Owner Assignment', 'createddate': '2023-06-03T14:45:00.000+0000'}], 'var_functions.execute_python:12': None}

exec(code, env_args)
