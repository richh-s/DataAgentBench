code = """import json
from datetime import datetime

# Load case data from the file
cases_file = locals()['var_functions.query_db:2']
with open(cases_file, 'r') as f:
    cases = json.load(f)

# Load account data
accounts = locals()['var_functions.query_db:6']

# Create account mapping with both # and non-# versions
account_state_map = {}
for acc in accounts:
    account_id = acc['Id']
    state = acc['ShippingState']
    account_state_map[account_id] = state
    if account_id.startswith('#'):
        account_state_map[account_id[1:]] = state
    else:
        account_state_map['#' + account_id] = state

# Define target quarters based on the prompt: past 6 quarters from today 2022-10-26
target_quarters = [
    ('Q3-2021', datetime(2021, 7, 1), datetime(2021, 9, 30)),
    ('Q4-2021', datetime(2021, 10, 1), datetime(2021, 12, 31)),
    ('Q1-2022', datetime(2022, 1, 1), datetime(2022, 3, 31)),
    ('Q2-2022', datetime(2022, 4, 1), datetime(2022, 6, 30)),
    ('Q3-2022', datetime(2022, 7, 1), datetime(2022, 9, 30)),
    ('Q4-2022', datetime(2022, 10, 1), datetime(2022, 10, 26))
]

# Process cases in target date range
cases_by_state = {}
for case in cases:
    try:
        # Parse the exact format: 2023-09-30T11:30:00.000+0000
        created_str = case['createddate']
        # Extract until the dot before milliseconds
        if '.' in created_str:
            created_base = created_str.split('.')[0]
            created = datetime.fromisoformat(created_base)
        else:
            created = datetime.fromisoformat(created_str.replace('Z', '+00:00'))
        
        # Check if in target quarters
        in_target = False
        for q_name, start, end in target_quarters:
            if start <= created <= end:
                in_target = True
                break
        
        if not in_target:
            continue
        
        # Parse closed date
        closed_str = case['closeddate']
        if '.' in closed_str:
            closed_base = closed_str.split('.')[0]
            closed = datetime.fromisoformat(closed_base)
        else:
            closed = datetime.fromisoformat(closed_str.replace('Z', '+00:00'))
        
        # Calculate closure time in hours
        closure_hours = (closed - created).total_seconds() / 3600
        
        # Get account ID and state
        account_id = case['accountid']
        state = account_state_map.get(account_id)
        if not state:
            if account_id.startswith('#'):
                alt_id = account_id[1:]
            else:
                alt_id = '#' + account_id
            state = account_state_map.get(alt_id)
        
        if state:
            if state not in cases_by_state:
                cases_by_state[state] = []
            cases_by_state[state].append(closure_hours)
        
    except Exception as e:
        continue

# Calculate average closure time for each state with at least 2 cases
state_averages = {}
for state, hours_list in cases_by_state.items():
    if len(hours_list) >= 2:
        state_averages[state] = sum(hours_list) / len(hours_list)

# Find state with minimum average closure time
result = "No data"
if state_averages:
    best_state = min(state_averages.items(), key=lambda x: x[1])
    result = best_state[0]

print('__RESULT__:')
print(json.dumps({
    'states_with_cases': len(cases_by_state),
    'states_eligible': len(state_averages),
    'best_state': result,
    'debug': state_averages
}))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['User', 'Account', 'Contact'], 'var_functions.query_db:6': [{'Id': '001Wt00000PFj4zIAD', 'ShippingState': 'FL'}, {'Id': '001Wt00000PFj50IAD', 'ShippingState': 'TX'}, {'Id': '#001Wt00000PFluoIAD', 'ShippingState': 'AZ'}, {'Id': '#001Wt00000PFlupIAD', 'ShippingState': 'CA'}, {'Id': '001Wt00000PFrk1IAD', 'ShippingState': 'MO'}, {'Id': '001Wt00000PFsjMIAT', 'ShippingState': 'OH'}, {'Id': '001Wt00000PFsjOIAT', 'ShippingState': 'NY'}, {'Id': '001Wt00000PFsmZIAT', 'ShippingState': 'CO'}, {'Id': '001Wt00000PFsmaIAD', 'ShippingState': 'MI'}, {'Id': '001Wt00000PFsmbIAD', 'ShippingState': 'NV'}, {'Id': '#001Wt00000PFsmcIAD', 'ShippingState': 'MN'}, {'Id': '001Wt00000PFsmdIAD', 'ShippingState': 'MA'}, {'Id': '001Wt00000PFt7TIAT', 'ShippingState': 'CO'}, {'Id': '#001Wt00000PFttwIAD', 'ShippingState': 'CA'}, {'Id': '001Wt00000PGGTtIAP', 'ShippingState': 'CA'}, {'Id': '#001Wt00000PGGTuIAP', 'ShippingState': 'CA'}, {'Id': '#001Wt00000PGHsyIAH', 'ShippingState': 'FL'}, {'Id': '001Wt00000PGQzcIAH', 'ShippingState': 'WA'}, {'Id': '001Wt00000PGR63IAH', 'ShippingState': 'WA'}, {'Id': '001Wt00000PGRnYIAX', 'ShippingState': 'IA'}, {'Id': '001Wt00000PGRqjIAH', 'ShippingState': 'CA'}, {'Id': '001Wt00000PGSwYIAX', 'ShippingState': 'IA'}, {'Id': '001Wt00000PGSwZIAX', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PGXrKIAX', 'ShippingState': 'WA'}, {'Id': '#001Wt00000PGXrLIAX', 'ShippingState': 'NY'}, {'Id': '001Wt00000PGXrMIAX', 'ShippingState': 'NY'}, {'Id': '001Wt00000PGXrNIAX', 'ShippingState': 'WA'}, {'Id': '#001Wt00000PGYgxIAH', 'ShippingState': 'OR'}, {'Id': '001Wt00000PGYx4IAH', 'ShippingState': 'NY'}, {'Id': '#001Wt00000PGYx5IAH', 'ShippingState': 'MA'}, {'Id': '001Wt00000PGZZnIAP', 'ShippingState': 'TX'}, {'Id': '001Wt00000PGZZoIAP', 'ShippingState': 'OR'}, {'Id': '001Wt00000PGZgHIAX', 'ShippingState': 'UT'}, {'Id': '#001Wt00000PGZmeIAH', 'ShippingState': 'TX'}, {'Id': '001Wt00000PGZmfIAH', 'ShippingState': 'MI'}, {'Id': '001Wt00000PGaHIIA1', 'ShippingState': 'NV'}, {'Id': '001Wt00000PGaNjIAL', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGaNkIAL', 'ShippingState': 'VA'}, {'Id': '#001Wt00000PGaZCIA1', 'ShippingState': 'OR'}, {'Id': '001Wt00000PGaZDIA1', 'ShippingState': 'CA'}, {'Id': '#001Wt00000PGb5MIAT', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PGb5NIAT', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGb5OIAT', 'ShippingState': 'IL'}, {'Id': '#001Wt00000PGcFxIAL', 'ShippingState': 'MI'}, {'Id': '001Wt00000PGccRIAT', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGcpMIAT', 'ShippingState': 'MO'}, {'Id': '#001Wt00000PGdBuIAL', 'ShippingState': 'WA'}, {'Id': '#001Wt00000PGdwiIAD', 'ShippingState': 'WA'}, {'Id': '#001Wt00000PGdzxIAD', 'ShippingState': 'FL'}, {'Id': '001Wt00000PGeJIIA1', 'ShippingState': 'MA'}, {'Id': '001Wt00000PGoAaIAL', 'ShippingState': 'NJ'}, {'Id': '#001Wt00000PGovMIAT', 'ShippingState': 'CO'}, {'Id': '001Wt00000PGtdJIAT', 'ShippingState': 'IL'}, {'Id': '001Wt00000PGtdKIAT', 'ShippingState': 'VA'}, {'Id': '001Wt00000PGtmwIAD', 'ShippingState': 'IL'}, {'Id': '001Wt00000PGtmxIAD', 'ShippingState': 'TX'}, {'Id': '001Wt00000PGyTIIA1', 'ShippingState': 'CO'}, {'Id': '001Wt00000PGyv0IAD', 'ShippingState': 'MA'}, {'Id': '001Wt00000PGz2nIAD', 'ShippingState': 'CO'}, {'Id': '001Wt00000PGzM9IAL', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGzSaIAL', 'ShippingState': 'WA'}, {'Id': '001Wt00000PGzSbIAL', 'ShippingState': 'FL'}, {'Id': '001Wt00000PGzVpIAL', 'ShippingState': 'TX'}, {'Id': '001Wt00000PGzsMIAT', 'ShippingState': 'CA'}, {'Id': '001Wt00000PH90cIAD', 'ShippingState': 'MA'}, {'Id': '#001Wt00000PH9DRIA1', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PH9ITIA1', 'ShippingState': 'TX'}, {'Id': '#001Wt00000PHHXXIA5', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHR75IAH', 'ShippingState': 'OR'}, {'Id': '#001Wt00000PHR8gIAH', 'ShippingState': 'AZ'}, {'Id': '001Wt00000PHRF8IAP', 'ShippingState': 'NY'}, {'Id': '001Wt00000PHRF9IAP', 'ShippingState': 'WA'}, {'Id': '001Wt00000PHRTeIAP', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PHRTfIAP', 'ShippingState': 'FL'}, {'Id': '001Wt00000PHRVGIA5', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHRVHIA5', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHRVIIA5', 'ShippingState': 'NY'}, {'Id': '001Wt00000PHRbiIAH', 'ShippingState': 'GA'}, {'Id': '001Wt00000PHVaUIAX', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHVaVIAX', 'ShippingState': 'NY'}, {'Id': '#001Wt00000PHVdhIAH', 'ShippingState': 'TX'}, {'Id': '#001Wt00000PHVfJIAX', 'ShippingState': 'MN'}, {'Id': '001Wt00000PHVgvIAH', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHViXIAX', 'ShippingState': 'NC'}, {'Id': '001Wt00000PHViYIAX', 'ShippingState': 'MD'}, {'Id': '#001Wt00000PHViZIAX', 'ShippingState': 'PA'}, {'Id': '001Wt00000PHViaIAH', 'ShippingState': 'CO'}, {'Id': '001Wt00000PHVk9IAH', 'ShippingState': 'NY'}, {'Id': '#001Wt00000PHVkAIAX', 'ShippingState': 'VA'}, {'Id': '001Wt00000PHVllIAH', 'ShippingState': 'FL'}, {'Id': '001Wt00000PHVnNIAX', 'ShippingState': 'SC'}, {'Id': '001Wt00000PHVnOIAX', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHVozIAH', 'ShippingState': 'NY'}, {'Id': '001Wt00000PHVqbIAH', 'ShippingState': 'GA'}, {'Id': '001Wt00000PHVqdIAH', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHVsDIAX', 'ShippingState': 'OR'}, {'Id': '001Wt00000PHVtpIAH', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHVvRIAX', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHVx3IAH', 'ShippingState': 'AZ'}, {'Id': '#001Wt00000PHVyfIAH', 'ShippingState': 'NC'}, {'Id': '001Wt00000PHW0HIAX', 'ShippingState': 'NY'}], 'var_functions.execute_python:10': {'cases_count': 64, 'accounts_count': 101, 'sample_cases': [{'id': '500Wt00000DDNYoIAP', 'accountid': '001Wt00000PGZZoIAP', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDPM6IAP', 'accountid': '001Wt00000PGzSaIAL', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDPSZIA5', 'accountid': '#001Wt00000PGZZoIAP', 'createddate': '2023-10-02T14:15:00.000+0000', 'closeddate': '2023-10-02T14:45:22.000+0000', 'status': 'Closed'}], 'sample_accounts': [{'Id': '001Wt00000PFj4zIAD', 'ShippingState': 'FL'}, {'Id': '001Wt00000PFj50IAD', 'ShippingState': 'TX'}, {'Id': '#001Wt00000PFluoIAD', 'ShippingState': 'AZ'}]}, 'var_functions.execute_python:12': {'cases_parsed': 0, 'sample_cases': []}, 'var_functions.execute_python:14': {'earliest_created': '2020-07-05T09:45:00+00:00', 'latest_created': '2023-12-02T11:30:00+00:00', 'total_cases': 64}, 'var_functions.execute_python:16': 'No data found', 'var_functions.execute_python:18': {'total_cases': 64, 'date_range': {'min': '2020-07-05T09:45:00+00:00', 'max': '2023-12-02T11:30:00+00:00'}, 'sample_dates': ['2023-09-22T08:28:00+00:00', '2023-09-25T10:30:00+00:00', '2023-09-30T11:30:00+00:00', '2023-10-02T09:15:00+00:00', '2023-10-02T14:15:00+00:00', '2023-10-05T09:45:00+00:00', '2023-10-15T09:15:47+00:00', '2023-10-16T09:00:00+00:00', '2023-11-02T10:00:00+00:00', '2023-12-02T11:30:00+00:00'], 'account_mappings': {'total_unique_accounts': 41, 'mapped_accounts': 41}}, 'var_functions.execute_python:20': {'total_cases': 64, 'date_range': '2020-07-05 09:45:00+00:00 to 2023-12-02 11:30:00+00:00', 'all_quarters': {'Q3-2020': 4, 'Q4-2020': 5, 'Q1-2021': 4, 'Q2-2021': 1, 'Q3-2021': 5, 'Q4-2021': 2, 'Q1-2022': 7, 'Q2-2022': 3, 'Q3-2022': 4, 'Q4-2022': 1, 'Q1-2023': 8, 'Q2-2023': 6, 'Q3-2023': 7, 'Q4-2023': 7}, 'filtered_cases_count': 0, 'sample_filtered': []}}

exec(code, env_args)
