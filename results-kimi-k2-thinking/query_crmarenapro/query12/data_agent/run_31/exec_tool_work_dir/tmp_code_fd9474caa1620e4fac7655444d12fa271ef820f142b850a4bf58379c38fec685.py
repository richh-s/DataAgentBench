code = """import json
import re
from datetime import datetime

# Get the query result
query_result = locals()['var_functions.query_db:2']

# Parse dates and calculate turnaround time
turnaround_data = []

for record in query_result:
    # Parse CreatedDate (ISO format with time)
    created_match = re.match(r'(\d{4}-\d{2}-\d{2})', record['CreatedDate'])
    if created_match:
        created_date = datetime.strptime(created_match.group(1), '%Y-%m-%d').date()
    else:
        continue
    
    # Parse CompanySignedDate (should be YYYY-MM-DD format)
    try:
        signed_date = datetime.strptime(record['CompanySignedDate'], '%Y-%m-%d').date()
    except:
        continue
    
    # Calculate turnaround days
    turnaround_days = (signed_date - created_date).days
    
    turnaround_data.append({
        'OwnerId': record['OwnerId'],
        'turnaround_days': turnaround_days
    })

# Group by OwnerId and calculate average turnaround
from collections import defaultdict

owner_turnarounds = defaultdict(list)
for item in turnaround_data:
    owner_turnarounds[item['OwnerId']].append(item['turnaround_days'])

# Calculate average for each owner
owner_averages = {}
for owner_id, days_list in owner_turnarounds.items():
    owner_averages[owner_id] = sum(days_list) / len(days_list)

# Find owner with minimum average turnaround
if owner_averages:
    quickest_owner = min(owner_averages.items(), key=lambda x: x[1])[0]
else:
    quickest_owner = None

# Print result
print('__RESULT__:')
print(json.dumps(quickest_owner))"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': [{'OpportunityId': '006Wt000007BI41IAG', 'OwnerId': '005Wt000003NDEBIA4', 'CreatedDate': '2022-06-15T10:20:30.000+0000', 'CompanySignedDate': '2023-04-15'}]}

exec(code, env_args)
