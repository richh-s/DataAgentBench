code = """import json, pandas as pd
from collections import defaultdict

# Load the full result from the JSON file path
file_path = var_call_9eeFg4DvN4LPmUFHSsZcmrdg
with open(file_path, 'r') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# For each (System, Name) keep the row with the latest UpstreamPublishedAt if available, otherwise max Version lexicographically
# But our query didn't include UpstreamPublishedAt, so we'll just take the first occurrence per Name since ordered by UpstreamPublishedAt DESC
# Group by Name and take the first row
latest_df = df.groupby(['System','Name'], as_index=False).first()[['System','Name','Version']]

result = latest_df.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_9eeFg4DvN4LPmUFHSsZcmrdg': 'file_storage/call_9eeFg4DvN4LPmUFHSsZcmrdg.json', 'var_call_NFjIoKmOhFgffSzw4MH8k63g': ['project_info', 'project_packageversion']}

exec(code, env_args)
