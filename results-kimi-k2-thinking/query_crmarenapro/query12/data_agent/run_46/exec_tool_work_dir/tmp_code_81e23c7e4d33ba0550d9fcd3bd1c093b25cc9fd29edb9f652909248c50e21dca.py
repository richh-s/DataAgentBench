code = """import json
import pandas as pd
from datetime import datetime

# Load the data from file
file_path = locals()['var_functions.query_db:5']
with open(file_path, 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Filter opportunities created in April 2023
df['OpportunityCreatedDate'] = pd.to_datetime(df['OpportunityCreatedDate'])
mask = (df['OpportunityCreatedDate'] >= '2023-04-01') & (df['OpportunityCreatedDate'] < '2023-05-01')
df_april = df[mask].copy()

# Clean dates
df_april['CompanySignedDate'] = pd.to_datetime(df_april['CompanySignedDate'])

# Calculate turnaround days
df_april['turnaround_days'] = (df_april['CompanySignedDate'] - df_april['OpportunityCreatedDate']).dt.days

# Clean OwnerId (remove leading #)
df_april['OwnerId_clean'] = df_april['OwnerId'].str.replace('^#', '', regex=True)

# Group by agent and calculate average turnaround
agent_stats = df_april.groupby('OwnerId_clean').agg(
    avg_turnaround=('turnaround_days', 'mean'),
    opportunity_count=('turnaround_days', 'count')
).reset_index()

# Remove agents with only one opportunity (less reliable average)
agent_stats = agent_stats[agent_stats['opportunity_count'] > 1]

# Find agent with lowest average turnaround
if not agent_stats.empty:
    best_agent = agent_stats.loc[agent_stats['avg_turnaround'].idxmin()]
    result = best_agent['OwnerId_clean']
else:
    result = None

print('__RESULT__:')
print(json.dumps({'best_agent_id': result}))"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
