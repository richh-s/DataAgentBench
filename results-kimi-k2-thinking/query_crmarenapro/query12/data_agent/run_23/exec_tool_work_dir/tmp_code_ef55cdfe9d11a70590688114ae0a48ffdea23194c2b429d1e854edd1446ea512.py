code = """import json
from datetime import datetime

# Get the opportunities with signed contracts
opportunities = locals()['var_functions.query_db:10']

# Clean and process the data
cleaned_data = []
for opp in opportunities:
    # Clean OwnerId (remove leading # and trailing spaces)
    owner_id = opp['OwnerId'].replace('#', '').strip()
    
    # Parse dates - created_date is ISO format, signed_date is YYYY-MM-DD
    created_date_str = opp['CreatedDate']
    if 'T' in created_date_str:
        created_date = datetime.fromisoformat(created_date_str.replace('Z', '+00:00')).date()
    else:
        created_date = datetime.strptime(created_date_str, '%Y-%m-%d').date()
    
    # CompanySignedDate is in YYYY-MM-DD format
    signed_date = datetime.strptime(opp['CompanySignedDate'], '%Y-%m-%d').date()
    
    # Calculate turnaround days
    turnaround_days = (signed_date - created_date).days
    
    cleaned_data.append({
        'OwnerId': owner_id,
        'TurnaroundDays': turnaround_days
    })

# Group by OwnerId and calculate average turnaround
from collections import defaultdict

owner_stats = defaultdict(list)
for item in cleaned_data:
    owner_stats[item['OwnerId']].append(item['TurnaroundDays'])

# Calculate averages
owner_averages = {}
for owner_id, days_list in owner_stats.items():
    owner_averages[owner_id] = sum(days_list) / len(days_list)

# Find agent with quickest average turnaround
quickest_agent = min(owner_averages, key=owner_averages.get)

print("__RESULT__:")
print(json.dumps(quickest_agent))"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': [{'opp_count': '30'}], 'var_functions.query_db:5': [{'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'CompanySignedDate': '2023-10-13', 'Status': 'Activated'}, {'OwnerId': '#005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'CompanySignedDate': '2023-09-30', 'Status': 'Activated '}, {'OwnerId': '#005Wt000003NBylIAG', 'CreatedDate': '2023-04-15T09:00:34.000+0000', 'CompanySignedDate': 'None', 'Status': 'None'}, {'OwnerId': '005Wt000003NIs9IAG', 'CreatedDate': '2023-04-25T14:32:51.000+0000', 'CompanySignedDate': 'None', 'Status': 'None'}, {'OwnerId': '005Wt000003NJZhIAO', 'CreatedDate': '2023-04-04T10:15:30.000+0000', 'CompanySignedDate': 'None', 'Status': 'None'}, {'OwnerId': '#005Wt000003NJMnIAO', 'CreatedDate': '2023-04-25T09:45:30.000+0000', 'CompanySignedDate': 'None', 'Status': 'None'}, {'OwnerId': '005Wt000003NIfGIAW', 'CreatedDate': '2023-04-15T10:20:30.000+0000', 'CompanySignedDate': 'None', 'Status': 'None'}, {'OwnerId': '#005Wt000003NEdJIAW', 'CreatedDate': '2023-04-15T10:30:45.000+0000', 'CompanySignedDate': 'None', 'Status': 'None'}, {'OwnerId': '005Wt000003NInKIAW', 'CreatedDate': '2023-04-15T09:30:45.000+0000', 'CompanySignedDate': 'None', 'Status': 'None'}, {'OwnerId': '005Wt000003NIovIAG', 'CreatedDate': '2023-04-15T10:30:15.000+0000', 'CompanySignedDate': 'None', 'Status': 'None'}, {'OwnerId': '005Wt000003NF9WIAW', 'CreatedDate': '2023-04-02T10:15:30.000+0000', 'CompanySignedDate': 'None', 'Status': 'None'}, {'OwnerId': '005Wt000003NDEBIA4', 'CreatedDate': '2023-04-01T14:47:23.000+0000', 'CompanySignedDate': 'None', 'Status': 'None'}, {'OwnerId': '#005Wt000003NFhPIAW', 'CreatedDate': '2023-04-19T15:30:45.000+0000', 'CompanySignedDate': 'None', 'Status': 'None'}, {'OwnerId': '005Wt000003NJxtIAG', 'CreatedDate': '2023-04-15T10:15:32.000+0000', 'CompanySignedDate': 'None', 'Status': 'None'}, {'OwnerId': '005Wt000003NJ1pIAG', 'CreatedDate': '2023-04-10T10:30:15.000+0000', 'CompanySignedDate': 'None', 'Status': 'None'}, {'OwnerId': '005Wt000003NEtPIAW', 'CreatedDate': '2023-04-15T10:14:32.000+0000', 'CompanySignedDate': 'None', 'Status': 'None'}, {'OwnerId': '005Wt000003NJBVIA4', 'CreatedDate': '2023-04-27T11:22:30.000+0000', 'CompanySignedDate': 'None', 'Status': 'None'}, {'OwnerId': '#005Wt000003NBcBIAW', 'CreatedDate': '2023-04-20T11:15:33.000+0000', 'CompanySignedDate': 'None', 'Status': 'None'}, {'OwnerId': '005Wt000003NJgAIAW', 'CreatedDate': '2023-04-25T10:45:30.000+0000', 'CompanySignedDate': 'None', 'Status': 'None'}, {'OwnerId': '005Wt000003NJ0EIAW', 'CreatedDate': '2023-04-15T10:45:00.000+0000', 'CompanySignedDate': 'None', 'Status': 'None'}, {'OwnerId': '005Wt000003NIAbIAO', 'CreatedDate': '2023-04-15T10:32:45.000+0000', 'CompanySignedDate': 'None', 'Status': 'None'}, {'OwnerId': '005Wt000003NEtPIAW', 'CreatedDate': '2023-04-15T10:30:15.000+0000', 'CompanySignedDate': 'None', 'Status': 'None'}, {'OwnerId': '#005Wt000003NJjNIAW', 'CreatedDate': '2023-04-20T11:34:22.000+0000', 'CompanySignedDate': 'None', 'Status': 'None'}, {'OwnerId': '005Wt000003NFRKIA4', 'CreatedDate': '2023-04-05T14:23:45.000+0000', 'CompanySignedDate': 'None', 'Status': 'None'}, {'OwnerId': '005Wt000003NHpdIAG', 'CreatedDate': '2023-04-05T10:15:30.000+0000', 'CompanySignedDate': 'None', 'Status': 'None'}, {'OwnerId': '005Wt000003NIdeIAG', 'CreatedDate': '2023-04-11T12:45:33.000+0000', 'CompanySignedDate': 'None', 'Status': 'None'}, {'OwnerId': '005Wt000003NBcBIAW', 'CreatedDate': '2023-04-10T11:20:45.000+0000', 'CompanySignedDate': 'None', 'Status': 'None'}, {'OwnerId': '005Wt000003NIaPIAW', 'CreatedDate': '2023-04-10T14:25:30.000+0000', 'CompanySignedDate': 'None', 'Status': 'None'}, {'OwnerId': '005Wt000003NIqXIAW', 'CreatedDate': '2023-04-17T14:37:45.000+0000', 'CompanySignedDate': 'None', 'Status': 'None'}, {'OwnerId': '005Wt000003NIfGIAW', 'CreatedDate': '2023-04-01T09:45:23.000+0000', 'CompanySignedDate': 'None', 'Status': 'None'}], 'var_functions.execute_python:8': {'opportunity_count': '30', 'sample_opportunities': [{'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'CompanySignedDate': '2023-10-13', 'Status': 'Activated'}, {'OwnerId': '#005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'CompanySignedDate': '2023-09-30', 'Status': 'Activated '}, {'OwnerId': '#005Wt000003NBylIAG', 'CreatedDate': '2023-04-15T09:00:34.000+0000', 'CompanySignedDate': 'None', 'Status': 'None'}]}, 'var_functions.query_db:10': [{'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'CompanySignedDate': '2023-10-13'}, {'OwnerId': '#005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'CompanySignedDate': '2023-09-30'}]}

exec(code, env_args)
