code = """import pandas as pd
import json

# Load the query result from storage variable
records = var_call_pZlootUdALgLqI53J7A6baV8

# Create DataFrame
df = pd.DataFrame(records)

# Clean IDs: remove leading '#' and trim whitespace for owner_id
df['owner_id_clean'] = df['owner_id'].astype(str).str.strip().str.lstrip('#')

# Parse dates
# CreatedDate may include time and timezone; parse with pandas
df['created_dt'] = pd.to_datetime(df['created_date'], utc=True)
# CompanySignedDate may be date-only
df['company_signed_dt'] = pd.to_datetime(df['company_signed_date']).dt.tz_localize('UTC')

# Compute turnaround in days (as float days)
df['turnaround_days'] = (df['company_signed_dt'] - df['created_dt']).dt.total_seconds() / (24*3600)

# Group by owner and compute average turnaround
grouped = df.groupby('owner_id_clean', dropna=True)['turnaround_days'].mean().reset_index()

# Find owner with minimum average turnaround
min_row = grouped.loc[grouped['turnaround_days'].idxmin()]
agent_id = min_row['owner_id_clean']

# Print result in required format as JSON string
print("__RESULT__:")
print(json.dumps(agent_id))"""

env_args = {'var_call_pZlootUdALgLqI53J7A6baV8': [{'opp_id': '#006Wt000007BChmIAG', 'owner_id': '005Wt000003NJgAIAW', 'created_date': '2023-04-25T10:45:30.000+0000', 'company_signed_date': '2023-06-13'}, {'opp_id': '006Wt000007BDApIAO', 'owner_id': '005Wt000003NISMIA4', 'created_date': '2023-04-10T10:15:30.000+0000', 'company_signed_date': '2023-10-13'}, {'opp_id': '006Wt000007BHPhIAO', 'owner_id': '#005Wt000003NEa3IAG', 'created_date': '2023-04-15T09:12:34.000+0000', 'company_signed_date': '2023-09-30'}]}

exec(code, env_args)
