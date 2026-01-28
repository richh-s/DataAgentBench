code = """import json
import pandas as pd

# Load the query result from the file
query_result_file = locals()['var_functions.query_db:2']

# Read the data
with open(query_result_file, 'r') as f:
    result = json.load(f)

# Create DataFrame
df = pd.DataFrame(result)

# Handle corrupted IDs - remove leading # and trailing whitespace
df['ownerid_clean'] = df['ownerid'].str.lstrip('#').str.strip()
df['oldvalue__c_clean'] = df['oldvalue__c'].str.lstrip('#').str.strip()

# Filter for last 4 quarters from 2022-04-10 onwards
filtered_df = df[pd.to_datetime(df['createddate']) >= pd.Timestamp('2022-04-10')].copy()

# Find all agents who handled cases (both initial and transferred)
all_agents = set(filtered_df['ownerid_clean'].unique())

# Identify transfer events (where oldvalue__c != 'None')
transfer_events = filtered_df[filtered_df['oldvalue__c'] != 'None'].copy()

# Count transfers per agent (oldvalue__c is the agent who transferred the case away)
if not transfer_events.empty:
    transfer_counts = transfer_events.groupby('oldvalue__c_clean').size().reset_index(name='transfer_count')
else:
    transfer_counts = pd.DataFrame(columns=['oldvalue__c_clean', 'transfer_count'])

# Filter to only include agents who handled cases
transfer_counts = transfer_counts[transfer_counts['oldvalue__c_clean'].isin(all_agents)]

# Include all agents (even those with 0 transfers)
all_agents_df = pd.DataFrame({'agent_id': list(all_agents)})
all_agents_df = all_agents_df.merge(transfer_counts, left_on='agent_id', right_on='oldvalue__c_clean', how='left')
all_agents_df['transfer_count'] = all_agents_df['transfer_count'].fillna(0)

# Find agent with minimum transfer count
min_count = all_agents_df['transfer_count'].min()
min_agents = all_agents_df[all_agents_df['transfer_count'] == min_count]

# Get the first agent_id with minimum transfers
result_agent_id = min_agents['agent_id'].iloc[0]

print('__RESULT__:')
print(json.dumps(str(result_agent_id)))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
