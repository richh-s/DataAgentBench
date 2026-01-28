code = """import json
import pandas as pd
from datetime import datetime

# Load the data from storage
opp_data = locals()['var_functions.query_db:0']
contract_data = locals()['var_functions.query_db:2']

# Read the full data from the JSON files
with open(opp_data, 'r') as f:
    opportunities = json.load(f)

with open(contract_data, 'r') as f:
    contracts = json.load(f)

# Convert to DataFrames
opp_df = pd.DataFrame(opportunities)
contract_df = pd.DataFrame(contracts)

# Data cleaning
# Remove leading '#' from IDs and trailing whitespace
opp_df['Id'] = opp_df['Id'].str.replace('#', '').str.strip()
opp_df['OwnerId'] = opp_df['OwnerId'].str.replace('#', '').str.strip()
opp_df['ContractID__c'] = opp_df['ContractID__c'].str.replace('#', '').str.strip()

contract_df['Id'] = contract_df['Id'].str.replace('#', '').str.strip()

# Convert dates
opp_df['CreatedDate'] = pd.to_datetime(opp_df['CreatedDate'])
contract_df['CompanySignedDate'] = pd.to_datetime(contract_df['CompanySignedDate'])

# Filter for opportunities in April 2023
opp_df['CreatedYear'] = opp_df['CreatedDate'].dt.year
opp_df['CreatedMonth'] = opp_df['CreatedDate'].dt.month

april_2023_opps = opp_df[(opp_df['CreatedYear'] == 2023) & (opp_df['CreatedMonth'] == 4)]

# Join with contracts to get the signed dates
merged_df = april_2023_opps.merge(
    contract_df[['Id', 'CompanySignedDate']], 
    left_on='ContractID__c', 
    right_on='Id', 
    suffixes=('_opp', '_contract')
)

# Calculate turnaround days (from opportunity creation to contract signing)
merged_df['TurnaroundDays'] = (merged_df['CompanySignedDate'] - merged_df['CreatedDate']).dt.days

# Group by agent (OwnerId) and calculate average turnaround
agent_stats = merged_df.groupby('OwnerId').agg({
    'TurnaroundDays': ['mean', 'count']
}).round(2)

agent_stats.columns = ['AvgTurnaroundDays', 'OpportunityCount']
agent_stats = agent_stats.reset_index()

# Filter agents with at least 2 opportunities (for statistical significance)
qualified_agents = agent_stats[agent_stats['OpportunityCount'] >= 2]

# Find the agent with the quickest average turnaround
if not qualified_agents.empty:
    quickest_agent = qualified_agents.loc[qualified_agents['AvgTurnaroundDays'].idxmin()]
    result = {
        'AgentId': quickest_agent['OwnerId'],
        'AvgTurnaroundDays': quickest_agent['AvgTurnaroundDays'],
        'OpportunityCount': quickest_agent['OpportunityCount']
    }
else:
    # If no agent has 2+ opportunities, find the one with 1 opportunity and quickest turnaround
    if not agent_stats.empty:
        quickest_agent = agent_stats.loc[agent_stats['AvgTurnaroundDays'].idxmin()]
        result = {
            'AgentId': quickest_agent['OwnerId'],
            'AvgTurnaroundDays': quickest_agent['AvgTurnaroundDays'],
            'OpportunityCount': quickest_agent['OpportunityCount']
        }
    else:
        result = {'error': 'No data found'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': 'Attempting to load data', 'var_functions.execute_python:14': 'Checking variable access', 'var_functions.execute_python:16': 'Data loaded successfully'}

exec(code, env_args)
