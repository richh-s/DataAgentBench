code = """import json
import re
from datetime import datetime, timedelta

# Get the data from storage
cases_data_key = 'var_functions.query_db:5'
accounts_data_key = 'var_functions.query_db:12'

# Load the data - check if they're strings (file paths) or already loaded data
cases_result = locals().get(cases_data_key, [])
accounts_result = locals().get(accounts_data_key, [])

# Load from file if needed
case_records = []
account_records = []

if isinstance(cases_result, str) and cases_result.endswith('.json'):
    with open(cases_result, 'r') as f:
        case_records = json.load(f)
elif isinstance(cases_result, list):
    case_records = cases_result

if isinstance(accounts_result, str) and accounts_result.endswith('.json'):
    with open(accounts_result, 'r') as f:
        account_records = json.load(f)
elif isinstance(accounts_result, list):
    account_records = accounts_result

# Clean ID function (remove leading #)
def clean_id(id_str):
    if isinstance(id_str, str):
        return id_str.lstrip('#').strip()
    return str(id_str).strip() if id_str else ''

# Parse date function
def parse_date(date_str):
    if not date_str or date_str == 'None':
        return None
    try:
        date_str = str(date_str).strip()
        # Handle the format: 2023-09-30T16:03:45.000+0000
        if '.' in date_str:
            parts = date_str.split('.')
            if len(parts) == 2:
                # Remove milliseconds but keep timezone
                time_part = parts[1]
                if '+' in time_part:
                    tz_part = time_part.split('+')[1]
                    date_str = parts[0] + '+' + tz_part
                elif 'Z' in time_part:
                    date_str = parts[0] + '+00:00'
        return datetime.fromisoformat(date_str.replace('Z', '+00:00'))
    except Exception as e:
        return None

# Process cases: calculate closure time, filter by date
# Today's date: 2022-10-26, so 6 quarters = 18 months back
cutoff_date = datetime(2022, 10, 26, 0, 0, 0).replace(tzinfo=None) - timedelta(days=18*30)

processed_cases = []
for case in case_records:
    # Clean status (remove trailing whitespace)
    status = str(case.get('status', '')).strip()
    
    # Only consider closed cases
    if 'closed' not in status.lower():
        continue
        
    # Parse dates
    created_date = parse_date(case.get('createddate'))
    closed_date = parse_date(case.get('closeddate'))
    
    if not created_date or not closed_date:
        continue
        
    # Remove timezone info for comparison (some dates might not have timezone)
    created_date_naive = created_date.replace(tzinfo=None)
    
    # Filter for past 6 quarters (approx last 18 months from 2022-10-26)
    if created_date_naive < cutoff_date:
        continue
        
    # Calculate closure time in hours
    closure_hours = (closed_date - created_date).total_seconds() / 3600
    
    # Clean account ID
    account_id = clean_id(case.get('accountid', ''))
    
    processed_cases.append({
        'case_id': clean_id(case.get('id', '')),
        'account_id': account_id,
        'created_date': created_date,
        'closed_date': closed_date,
        'closure_hours': closure_hours
    })

# Build account state map (clean IDs)
account_state_map = {}
for account in account_records:
    account_id = clean_id(account.get('Id', ''))
    state = str(account.get('ShippingState', '')).strip() if account.get('ShippingState') else ''
    if state and account_id:
        account_state_map[account_id] = state

# Join cases with state and calculate average closure time by state
state_closure_times = {}

for case in processed_cases:
    account_id = case['account_id']
    if account_id in account_state_map:
        state = account_state_map[account_id]
        if state not in state_closure_times:
            state_closure_times[state] = []
        state_closure_times[state].append(case['closure_hours'])

# Calculate average closure time per state
state_avg_closure = {}
for state, times in state_closure_times.items():
    if len(times) >= 2:  # Only states with at least 2 cases for reliability
        state_avg_closure[state] = sum(times) / len(times)

# Find state with quickest closure time
quickest_state = None
min_hours = None
if state_avg_closure:
    quickest_state = min(state_avg_closure, key=state_avg_closure.get)
    min_hours = state_avg_closure[quickest_state]

# Sort states by average closure time
sorted_states = sorted(state_avg_closure.items(), key=lambda x: x[1])

result = {
    'quickest_state': quickest_state,
    'quickest_avg_hours': round(min_hours, 2) if min_hours else None,
    'total_states': len(state_avg_closure),
    'states_ranking': [(state, round(hours, 2)) for state, hours in sorted_states[:10]],
    'cases_processed': len(processed_cases)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}, {'id': '500Wt00000DDPSZIA5', 'priority': 'Medium', 'subject': 'Slow Reply from Support Team', 'description': "The delay in obtaining a prompt response from the TechPulse support team is causing frustration and hindering our team's efficiency.", 'status': 'Closed', 'contactid': '003Wt00000JqqVtIAJ', 'createddate': '2023-10-02T14:15:00.000+0000', 'closeddate': '2023-10-02T14:45:22.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '#001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NJhlIAG'}, {'id': '500Wt00000DDPZ0IAP', 'priority': 'Low', 'subject': 'Scaling Difficulties ', 'description': 'We are struggling to effectively scale the AI DesignShift solution, affecting our operational expansion, and we require assistance.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000Jqv0zIAB', 'createddate': '2022-04-18T10:30:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt0000078xAFIAY', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PGdzxIAD', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '500Wt00000DDPsOIAX', 'priority': 'Medium', 'subject': 'EcoPCB Data Integration Error', 'description': 'I am facing issues integrating EcoPCB Creator with third-party applications, which is causing disruptions in project workflows.', 'status': 'Working', 'contactid': '003Wt00000JqyEtIAJ', 'createddate': '2021-07-06T14:30:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt0000079ATyIAM', 'issueid__c': 'a03Wt00000JqzKcIAJ', 'accountid': '001Wt00000PHRF9IAP', 'ownerid': '005Wt000003NIk7IAG'}, {'id': '500Wt00000DDPsPIAX', 'priority': 'Medium', 'subject': 'Customization Issue', 'description': "I find it difficult to adapt the AI Cirku-Tech platform to my company's very specialized circuit design requirements despite the customization features available.", 'status': 'Closed', 'contactid': '003Wt00000Jqy0PIAR', 'createddate': '2023-04-05T17:51:00.000+0000', 'closeddate': '2023-04-06T11:30:54.000+0000', 'orderitemid__c': '802Wt00000794bXIAQ', 'issueid__c': 'a03Wt00000JqmX6IAJ', 'accountid': '#001Wt00000PGHsyIAH', 'ownerid': '005Wt000003NJ8HIAW'}, {'id': '500Wt00000DDQRsIAP', 'priority': 'Medium', 'subject': 'Scalability Issue', 'description': "I am facing challenges in scaling the OptiPower Manager to meet my organization's growing demands, hindering our expansion efforts.", 'status': 'Closed', 'contactid': '#003Wt00000Jqwg6IAB', 'createddate': '2023-03-08T06:49:00.000+0000', 'closeddate': '2023-03-08T07:07:30.000+0000', 'orderitemid__c': '802Wt00000796yFIAQ', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PGzM9IAL', 'ownerid': '#005Wt000003NFKoIAO'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['User', 'Account', 'Contact'], 'var_functions.query_db:12': [{'Id': '001Wt00000PFj4zIAD', 'ShippingState': 'FL'}, {'Id': '001Wt00000PFj50IAD', 'ShippingState': 'TX'}, {'Id': '#001Wt00000PFluoIAD', 'ShippingState': 'AZ'}, {'Id': '#001Wt00000PFlupIAD', 'ShippingState': 'CA'}, {'Id': '001Wt00000PFrk1IAD', 'ShippingState': 'MO'}, {'Id': '001Wt00000PFsjMIAT', 'ShippingState': 'OH'}, {'Id': '001Wt00000PFsjOIAT', 'ShippingState': 'NY'}, {'Id': '001Wt00000PFsmZIAT', 'ShippingState': 'CO'}, {'Id': '001Wt00000PFsmaIAD', 'ShippingState': 'MI'}, {'Id': '001Wt00000PFsmbIAD', 'ShippingState': 'NV'}, {'Id': '#001Wt00000PFsmcIAD', 'ShippingState': 'MN'}, {'Id': '001Wt00000PFsmdIAD', 'ShippingState': 'MA'}, {'Id': '001Wt00000PFt7TIAT', 'ShippingState': 'CO'}, {'Id': '#001Wt00000PFttwIAD', 'ShippingState': 'CA'}, {'Id': '001Wt00000PGGTtIAP', 'ShippingState': 'CA'}, {'Id': '#001Wt00000PGGTuIAP', 'ShippingState': 'CA'}, {'Id': '#001Wt00000PGHsyIAH', 'ShippingState': 'FL'}, {'Id': '001Wt00000PGQzcIAH', 'ShippingState': 'WA'}, {'Id': '001Wt00000PGR63IAH', 'ShippingState': 'WA'}, {'Id': '001Wt00000PGRnYIAX', 'ShippingState': 'IA'}, {'Id': '001Wt00000PGRqjIAH', 'ShippingState': 'CA'}, {'Id': '001Wt00000PGSwYIAX', 'ShippingState': 'IA'}, {'Id': '001Wt00000PGSwZIAX', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PGXrKIAX', 'ShippingState': 'WA'}, {'Id': '#001Wt00000PGXrLIAX', 'ShippingState': 'NY'}, {'Id': '001Wt00000PGXrMIAX', 'ShippingState': 'NY'}, {'Id': '001Wt00000PGXrNIAX', 'ShippingState': 'WA'}, {'Id': '#001Wt00000PGYgxIAH', 'ShippingState': 'OR'}, {'Id': '001Wt00000PGYx4IAH', 'ShippingState': 'NY'}, {'Id': '#001Wt00000PGYx5IAH', 'ShippingState': 'MA'}, {'Id': '001Wt00000PGZZnIAP', 'ShippingState': 'TX'}, {'Id': '001Wt00000PGZZoIAP', 'ShippingState': 'OR'}, {'Id': '001Wt00000PGZgHIAX', 'ShippingState': 'UT'}, {'Id': '#001Wt00000PGZmeIAH', 'ShippingState': 'TX'}, {'Id': '001Wt00000PGZmfIAH', 'ShippingState': 'MI'}, {'Id': '001Wt00000PGaHIIA1', 'ShippingState': 'NV'}, {'Id': '001Wt00000PGaNjIAL', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGaNkIAL', 'ShippingState': 'VA'}, {'Id': '#001Wt00000PGaZCIA1', 'ShippingState': 'OR'}, {'Id': '001Wt00000PGaZDIA1', 'ShippingState': 'CA'}, {'Id': '#001Wt00000PGb5MIAT', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PGb5NIAT', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGb5OIAT', 'ShippingState': 'IL'}, {'Id': '#001Wt00000PGcFxIAL', 'ShippingState': 'MI'}, {'Id': '001Wt00000PGccRIAT', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGcpMIAT', 'ShippingState': 'MO'}, {'Id': '#001Wt00000PGdBuIAL', 'ShippingState': 'WA'}, {'Id': '#001Wt00000PGdwiIAD', 'ShippingState': 'WA'}, {'Id': '#001Wt00000PGdzxIAD', 'ShippingState': 'FL'}, {'Id': '001Wt00000PGeJIIA1', 'ShippingState': 'MA'}, {'Id': '001Wt00000PGoAaIAL', 'ShippingState': 'NJ'}, {'Id': '#001Wt00000PGovMIAT', 'ShippingState': 'CO'}, {'Id': '001Wt00000PGtdJIAT', 'ShippingState': 'IL'}, {'Id': '001Wt00000PGtdKIAT', 'ShippingState': 'VA'}, {'Id': '001Wt00000PGtmwIAD', 'ShippingState': 'IL'}, {'Id': '001Wt00000PGtmxIAD', 'ShippingState': 'TX'}, {'Id': '001Wt00000PGyTIIA1', 'ShippingState': 'CO'}, {'Id': '001Wt00000PGyv0IAD', 'ShippingState': 'MA'}, {'Id': '001Wt00000PGz2nIAD', 'ShippingState': 'CO'}, {'Id': '001Wt00000PGzM9IAL', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGzSaIAL', 'ShippingState': 'WA'}, {'Id': '001Wt00000PGzSbIAL', 'ShippingState': 'FL'}, {'Id': '001Wt00000PGzVpIAL', 'ShippingState': 'TX'}, {'Id': '001Wt00000PGzsMIAT', 'ShippingState': 'CA'}, {'Id': '001Wt00000PH90cIAD', 'ShippingState': 'MA'}, {'Id': '#001Wt00000PH9DRIA1', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PH9ITIA1', 'ShippingState': 'TX'}, {'Id': '#001Wt00000PHHXXIA5', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHR75IAH', 'ShippingState': 'OR'}, {'Id': '#001Wt00000PHR8gIAH', 'ShippingState': 'AZ'}, {'Id': '001Wt00000PHRF8IAP', 'ShippingState': 'NY'}, {'Id': '001Wt00000PHRF9IAP', 'ShippingState': 'WA'}, {'Id': '001Wt00000PHRTeIAP', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PHRTfIAP', 'ShippingState': 'FL'}, {'Id': '001Wt00000PHRVGIA5', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHRVHIA5', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHRVIIA5', 'ShippingState': 'NY'}, {'Id': '001Wt00000PHRbiIAH', 'ShippingState': 'GA'}, {'Id': '001Wt00000PHVaUIAX', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHVaVIAX', 'ShippingState': 'NY'}, {'Id': '#001Wt00000PHVdhIAH', 'ShippingState': 'TX'}, {'Id': '#001Wt00000PHVfJIAX', 'ShippingState': 'MN'}, {'Id': '001Wt00000PHVgvIAH', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHViXIAX', 'ShippingState': 'NC'}, {'Id': '001Wt00000PHViYIAX', 'ShippingState': 'MD'}, {'Id': '#001Wt00000PHViZIAX', 'ShippingState': 'PA'}, {'Id': '001Wt00000PHViaIAH', 'ShippingState': 'CO'}, {'Id': '001Wt00000PHVk9IAH', 'ShippingState': 'NY'}, {'Id': '#001Wt00000PHVkAIAX', 'ShippingState': 'VA'}, {'Id': '001Wt00000PHVllIAH', 'ShippingState': 'FL'}, {'Id': '001Wt00000PHVnNIAX', 'ShippingState': 'SC'}, {'Id': '001Wt00000PHVnOIAX', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHVozIAH', 'ShippingState': 'NY'}, {'Id': '001Wt00000PHVqbIAH', 'ShippingState': 'GA'}, {'Id': '001Wt00000PHVqdIAH', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHVsDIAX', 'ShippingState': 'OR'}, {'Id': '001Wt00000PHVtpIAH', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHVvRIAX', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHVx3IAH', 'ShippingState': 'AZ'}, {'Id': '#001Wt00000PHVyfIAH', 'ShippingState': 'NC'}, {'Id': '001Wt00000PHW0HIAX', 'ShippingState': 'NY'}]}

exec(code, env_args)
