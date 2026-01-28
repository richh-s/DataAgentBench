code = """import json
import pandas as pd
from datetime import datetime

# Load the query result
query_result_file = var_query_result_1
result = []
with open(query_result_file, 'r') as f:
    result = json.load(f)

# Create DataFrame
df = pd.DataFrame(result)

# Today's date is 2023-04-10, last 4 quarters means from 2022-04-10 onwards
start_date = '2022-04-10'

df_createdate = pd.to_datetime(df['createddate'])
# Filter for last 4 quarters
mask = df_createdate >= pd.Timestamp(start_date)
filtered_df = df[mask].copy()

# Group by case_id and count assignments to identify transfers
case_assignments = filtered_df.groupby('case_id').agg({
    'createddate': ['count', 'min', 'max'],
    'oldvalue__c': 'first',
    'newvalue__c': 'last'
}).reset_index()

case_assignments.columns = ['case_id', 'assignment_count', 'first_assignment_date', 'last_assignment_date', 'first_owner', 'last_owner']
case_assignments['was_transferred'] = case_assignments['assignment_count'] > 1

# Get all distinct agents who handled cases in the last 4 quarters
agents_with_cases = set(filtered_df['ownerid'].unique())

# Filter for transfer events (where oldvalue__c != 'None')
transfer_events = filtered_df[filtered_df['oldvalue__c'] != 'None'].copy()

# Calculate transfer counts per agent
# Each transfer has an oldvalue__c (agent giving away) and newvalue__c (agent receiving)
transfer_counts = transfer_events.groupby('oldvalue__c').size().reset_index(name='transfer_count')

# Handle the # prefix and trailing whitespace issue from hints
transfer_counts['oldvalue__c_clean'] = transfer_counts['oldvalue__c'].str.lstrip('#').str.strip()

transfer_counts_clean = transfer_counts.groupby('oldvalue__c_clean')['transfer_count'].sum().reset_index()
transfer_counts_clean.columns = ['agent_id', 'transfer_count']

# Filter to only include agents who have handled cases
# First, get a clean list of agents
agents_clean = {str(agent).lstrip('#').strip() for agent in agents_with_cases}

transfer_counts_clean = transfer_counts_clean[transfer_counts_clean['agent_id'].isin(agents_clean)]

# Find the agent with the fewest transfer counts (minimum > 0 if we exclude 0, but we want among those who handled > 0 cases)
# Include agents with 0 transfers too since they handled cases
all_agents = pd.DataFrame({'agent_id': list(agents_clean)})
all_agents = all_agents.merge(transfer_counts_clean, on='agent_id', how='left')
all_agents['transfer_count'] = all_agents['transfer_count'].fillna(0)

# Find the agent(s) with minimum transfer count
min_transfers = all_agents['transfer_count'].min()
agents_min_transfers = all_agents[all_agents['transfer_count'] == min_transfers]

# Convert to JSON serializable format
result_data = {
    'agent_id': agents_min_transfers['agent_id'].iloc[0],
    'transfer_count': int(agents_min_transfers['transfer_count'].iloc[0])
}

answer = result_data['agent_id']

print('__RESULT__:')
print(json.dumps(str(answer)))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
