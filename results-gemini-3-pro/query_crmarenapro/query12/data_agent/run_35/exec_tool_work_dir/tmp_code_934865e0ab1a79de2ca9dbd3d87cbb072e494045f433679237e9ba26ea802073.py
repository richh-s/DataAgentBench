code = """import json
import pandas as pd
from datetime import datetime

# Load data
with open(locals()['var_function-call-8504362619409159086'], 'r') as f:
    opportunities = json.load(f)

with open(locals()['var_function-call-8504362619409159979'], 'r') as f:
    contracts = json.load(f)

# Helper to clean ID
def clean_id(x):
    if not isinstance(x, str):
        return x
    x = x.strip()
    if x.startswith('#'):
        return x[1:]
    return x

# Process Contracts
contract_data = {}
for c in contracts:
    c_id = clean_id(c.get('Id'))
    signed_date = c.get('CompanySignedDate')
    if c_id and signed_date:
        # Check if in April 2023
        try:
            dt = datetime.strptime(signed_date, "%Y-%m-%d")
            if dt.year == 2023 and dt.month == 4:
                contract_data[c_id] = dt
        except ValueError:
            continue

# Process Opportunities and Calculate Cycle
agent_cycles = {} # OwnerId -> list of cycle days

for opp in opportunities:
    contract_id = clean_id(opp.get('ContractID__c'))
    owner_id = clean_id(opp.get('OwnerId'))
    created_date_str = opp.get('CreatedDate')
    
    if contract_id in contract_data and created_date_str:
        signed_date = contract_data[contract_id]
        
        # Parse CreatedDate
        # Format: "2023-09-05T11:32:46.000+0000"
        # We only care about the date part for day difference usually
        try:
            # Taking first 10 chars for YYYY-MM-DD
            created_date = datetime.strptime(created_date_str[:10], "%Y-%m-%d")
            
            days_diff = (signed_date - created_date).days
            
            if owner_id not in agent_cycles:
                agent_cycles[owner_id] = []
            agent_cycles[owner_id].append(days_diff)
            
        except ValueError:
            continue

# Calculate averages
results = []
for agent, cycles in agent_cycles.items():
    avg_cycle = sum(cycles) / len(cycles)
    results.append({'AgentId': agent, 'AvgCycle': avg_cycle, 'Count': len(cycles)})

# Sort by AvgCycle ascending
results.sort(key=lambda x: x['AvgCycle'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-8504362619409159086': 'file_storage/function-call-8504362619409159086.json', 'var_function-call-8504362619409159979': 'file_storage/function-call-8504362619409159979.json'}

exec(code, env_args)
