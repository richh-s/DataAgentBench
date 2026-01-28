code = """import json
import re
from datetime import datetime

# Get the query results
opportunities = var_functions.query_db:2

# Function to clean IDs and data
def clean_id(id_str):
    if not id_str:
        return None
    return str(id_str).replace('#', '').strip()

# Process the data
turnaround_data = []

for opp in opportunities:
    # Clean IDs
    owner_id = clean_id(opp['OwnerId'])
    
    # Skip if missing key data
    if not owner_id or not opp['CreatedDate'] or not opp['CompanySignedDate']:
        continue
    
    # Parse dates
    try:
        created_date = datetime.fromisoformat(opp['CreatedDate'].replace('Z', '+00:00'))
        # CompanySignedDate seems to be in YYYY-MM-DD format
        signed_date = datetime.strptime(opp['CompanySignedDate'], '%Y-%m-%d')
        signed_date = signed_date.replace(tzinfo=created_date.tzinfo)
        
        # Calculate turnaround days
        turnaround_days = (signed_date - created_date).days
        
        turnaround_data.append({
            'OwnerId': owner_id,
            'OpportunityId': clean_id(opp['OpportunityId']),
            'TurnaroundDays': turnaround_days,
            'CreatedDate': opp['CreatedDate'],
            'CompanySignedDate': opp['CompanySignedDate']
        })
    except (ValueError, TypeError) as e:
        print(f"Error processing opportunity {opp.get('OpportunityId', 'unknown')}: {e}")
        continue

# Group by OwnerId and calculate average turnaround
from collections import defaultdict

owner_turnarounds = defaultdict(list)
for data in turnaround_data:
    owner_turnarounds[data['OwnerId']].append(data['TurnaroundDays'])

# Calculate average for each owner
owner_averages = {}
for owner_id, turnarounds in owner_turnarounds.items():
    avg_turnaround = sum(turnarounds) / len(turnarounds)
    owner_averages[owner_id] = {
        'average_turnaround': avg_turnaround,
        'opportunity_count': len(turnarounds)
    }

# Find the owner with the minimum average turnaround
if owner_averages:
    quickest_owner = min(owner_averages.keys(), key=lambda x: owner_averages[x]['average_turnaround'])
    
    result = {
        'quickest_owner_id': quickest_owner,
        'average_turnaround_days': owner_averages[quickest_owner]['average_turnaround'],
        'opportunity_count': owner_averages[quickest_owner]['opportunity_count'],
        'all_owner_averages': owner_averages
    }
else:
    result = {'error': 'No valid opportunities found'}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': [{'OpportunityId': '006Wt000007BDApIAO', 'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'CompanySignedDate': '2023-10-13'}, {'OpportunityId': '006Wt000007BHPhIAO', 'OwnerId': '#005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'CompanySignedDate': '2023-09-30'}]}

exec(code, env_args)
