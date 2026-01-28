code = """import json
from datetime import datetime

# Load the data from the storage variable
data = locals()['var_functions.query_db:0']

# Parse dates and calculate sales cycle in days
def calculate_sales_cycle(created_date, signed_date):
    # Parse ISO format dates
    created = datetime.fromisoformat(created_date.replace('Z', '+00:00'))
    signed = datetime.fromisoformat(signed_date.replace('Z', '+00:00')) if isinstance(signed_date, str) else signed_date
    # Calculate days difference
    return (signed - created).days

# Process each record and calculate sales cycle
processed_data = []
for record in data:
    try:
        days = calculate_sales_cycle(record['CreatedDate'], record['CompanySignedDate'])
        processed_data.append({
            'OwnerId': record['OwnerId'],
            'SalesCycleDays': days
        })
    except Exception as e:
        print(f"Error processing record: {e}")

# Group by OwnerId and calculate average sales cycle
from collections import defaultdict

agent_cycles = defaultdict(list)
for item in processed_data:
    agent_cycles[item['OwnerId']].append(item['SalesCycleDays'])

# Calculate averages
agent_averages = []
for owner_id, cycles in agent_cycles.items():
    avg_days = sum(cycles) / len(cycles)
    agent_averages.append({
        'OwnerId': owner_id,
        'AverageSalesCycle': avg_days,
        'OpportunityCount': len(cycles)
    })

# Sort by average sales cycle and get the agent with the quickest turnaround
default_sorted = sorted(agent_averages, key=lambda x: x['AverageSalesCycle'])

# Prepare result - the OwnerId of the agent with the quickest average turnaround
result = default_sorted[0]['OwnerId'] if default_sorted else None

# Print in required format
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'OwnerId': '005Wt000003NDEBIA4', 'CreatedDate': '2022-06-15T10:20:30.000+0000', 'CompanySignedDate': '2023-04-15'}]}

exec(code, env_args)
