code = """import pandas as pd
from datetime import datetime
import json
import re

# The result stored under the key is the raw string output from the tool
raw_tool_output_string = locals()['var_function-call-8720019229886834137']

# Extract the JSON array string from the raw_tool_output_string using regex
# This regex looks for the pattern '[...]' that contains the JSON data
json_match = re.search(r'\[.*\]', raw_tool_output_string, re.DOTALL)

if json_match:
    cases_json_str = json_match.group(0)
    # Parse the JSON string into a Python list of dictionaries
    cases = json.loads(cases_json_str)
else:
    # If no JSON array is found, initialize cases as an empty list
    cases = []

# Create a DataFrame from the list of case dictionaries
df = pd.DataFrame(cases)

# Proceed with data cleaning and analysis only if the DataFrame is not empty
if not df.empty:
    # Clean 'ownerid' and 'id' fields by removing '#' and stripping whitespace
    df['ownerid'] = df['ownerid'].astype(str).str.replace('#', '', regex=False).str.strip()
    df['id'] = df['id'].astype(str).str.replace('#', '', regex=False).str.strip()

    # Convert date fields to datetime objects
    df['createddate'] = pd.to_datetime(df['createddate'])
    df['closeddate'] = pd.to_datetime(df['closeddate'])

    # Calculate handle time in minutes
    df['handle_time_minutes'] = (df['closeddate'] - df['createddate']).dt.total_seconds() / 60

    # Filter out cases with non-positive handle time (in case of data issues)
    df = df[df['handle_time_minutes']] > 0

    # Group by ownerid, count cases, and calculate average handle time
    agent_stats = df.groupby('ownerid').agg(
        case_count=('id', 'count'),
        avg_handle_time=('handle_time_minutes', 'mean')
    ).reset_index()

    # Filter for agents processing more than one case
    filtered_agents = agent_stats[agent_stats['case_count']] > 1

    if not filtered_agents.empty:
        # Find the agent with the lowest average handle time
        lowest_avg_handle_time_agent = filtered_agents.sort_values(by='avg_handle_time', ascending=True).iloc[0]
        result = lowest_avg_handle_time_agent['ownerid']
    else:
        result = "No agents processed more than one case in the past four months."
else:
    result = "No cases found in the specified period."

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-8720019229886834137': [{'id': '500Wt00000DDNYoIAP', 'ownerid': '005Wt000003NIc3IAG', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000'}, {'id': '500Wt00000DDPSZIA5', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2023-10-02T14:15:00.000+0000', 'closeddate': '2023-10-02T14:45:22.000+0000'}, {'id': '500Wt00000DDU5iIAH', 'ownerid': '#005Wt000003NDqEIAW', 'createddate': '2023-10-15T09:15:47.000+0000', 'closeddate': '2023-10-15T14:23:52.000+0000'}, {'id': '500Wt00000DDYUGIA5', 'ownerid': '#005Wt000003NJ6gIAG', 'createddate': '2023-10-02T09:15:00.000+0000', 'closeddate': '2023-10-02T09:32:45.000+0000'}, {'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '#500Wt00000DDfFcIAL', 'ownerid': '005Wt000003NFKpIAO', 'createddate': '2023-09-22T08:28:00.000+0000', 'closeddate': '2023-09-22T08:43:27.000+0000'}, {'id': '500Wt00000DDnt6IAD', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-10-16T09:00:00.000+0000', 'closeddate': '2023-10-16T15:22:17.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDz6FIAT', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2023-09-03T10:15:00.000+0000', 'closeddate': '2023-09-08T16:25:49.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzW2IAL', 'ownerid': '005Wt000003NIk7IAG', 'createddate': '2023-10-05T09:45:00.000+0000', 'closeddate': '2023-10-05T16:02:30.000+0000'}, {'id': '#500Wt00000DDzpNIAT', 'ownerid': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'closeddate': '2023-09-07T16:45:30.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}, {'id': '#500Wt00000DE03tIAD', 'ownerid': '005Wt000003NHfzIAG', 'createddate': '2023-12-02T11:30:00.000+0000', 'closeddate': '2023-12-02T16:45:51.000+0000'}, {'id': '500Wt00000DE078IAD', 'ownerid': '005Wt000003NJTFIA4', 'createddate': '2023-09-16T15:30:00.000+0000', 'closeddate': '2023-09-16T21:27:33.000+0000'}, {'id': '500Wt00000DE0BxIAL', 'ownerid': '#005Wt000003NGwpIAG', 'createddate': '2023-11-02T10:00:00.000+0000', 'closeddate': '2023-11-02T14:10:33.000+0000'}, {'id': '500Wt00000DE0GnIAL', 'ownerid': '#005Wt000003NF1SIAW', 'createddate': '2023-09-18T09:45:00.000+0000', 'closeddate': '2023-09-18T09:53:18.000+0000'}, {'id': '500Wt00000DE0NGIA1', 'ownerid': '#005Wt000003NHpeIAG', 'createddate': '2023-09-25T10:30:00.000+0000', 'closeddate': '2023-09-26T12:20:45.000+0000'}], 'var_function-call-6570838578565936278': []}

exec(code, env_args)
