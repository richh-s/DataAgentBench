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

# Convert createddate to datetime
df['createddate_dt'] = pd.to_datetime(df['createddate'])

# Calculate date ranges - last 4 quarters from 2023-04-10
# This means from 2022-04-10 to 2023-04-10
start_date = pd.Timestamp('2022-04-10', tz='UTC')
end_date = pd.Timestamp('2023-04-10', tz='UTC')

# Filter for last 4 quarters
filtered_df = df[(df['createddate_dt'] >= start_date) & (df['createddate_dt'] <= end_date)].copy()

# Find all agents who handled cases in this period
all_agents = set(filtered_df['ownerid_clean'].unique())

# For each case, count how many times it was transferred
case_transfers = filtered_df[filtered_df['oldvalue__c'] != 'None'].groupby('case_id').size().reset_index(name='transfer_times')

# For each transfer, get the old owner (the one who transferred away)
transfer_events = filtered_df[filtered_df['oldvalue__c'] != 'None'].copy()

# Count transfers per agent
if not transfer_events.empty:
    transfer_counts = transfer_events.groupby('oldvalue__c_clean').size().reset_index(name='transfer_count')
else:
    transfer_counts = pd.DataFrame(columns=['oldvalue__c_clean', 'transfer_count'])

# Filter to only include agents who handled cases during the period
transfer_counts = transfer_counts[transfer_counts['oldvalue__c_clean'].isin(all_agents)]

# Create a complete list of all agents and their transfer counts
all_agents_df = pd.DataFrame({'agent_id': list(all_agents)})
all_agents_df = all_agents_df.merge(transfer_counts, left_on='agent_id', right_on='oldvalue__c_clean', how='left')
all_agents_df['transfer_count'] = all_agents_df['transfer_count'].fillna(0)

# Find the agent(s) with the minimum transfer count
min_transfers = all_agents_df['transfer_count'].min()
min_agents = all_agents_df[all_agents_df['transfer_count'] == min_transfers]

# Return the first agent_id (in case of ties)
result_agent_id = min_agents['agent_id'].iloc[0]

print('__RESULT__:')
print(json.dumps(str(result_agent_id)))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
