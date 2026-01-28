code = """import json
import pandas as pd
# load query result from storage
records = var_call_oqbn7CdM77RnwGKnYAn9fpZ8
# Create DataFrame
df = pd.DataFrame(records)
# Parse createddate
df['createddate'] = pd.to_datetime(df['createddate'], errors='coerce')
# Extract month name
df['month'] = df['createddate'].dt.strftime('%B')
# Count per month
counts = df['month'].value_counts()
# Determine if a particular month significantly exceeds others
# Define 'significantly exceeds' as having a strictly greater count than every other month
if counts.empty:
    result = None
else:
    max_count = counts.max()
    top_months = counts[counts == max_count].index.tolist()
    if len(top_months) == 1:
        # ensure it's strictly greater than others (already true since unique)
        result = top_months[0]
    else:
        result = None
# Print result in required format as JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_SGCKhSXdV4l3D75JsbitHJrj': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}], 'var_call_oqbn7CdM77RnwGKnYAn9fpZ8': [{'createddate': '2020-11-05T08:19:00.000+0000'}, {'createddate': '2020-09-29T01:59:00.000+0000'}, {'createddate': '2021-03-07T11:25:00.000+0000'}, {'createddate': '2020-11-09T19:02:00.000+0000'}]}

exec(code, env_args)
