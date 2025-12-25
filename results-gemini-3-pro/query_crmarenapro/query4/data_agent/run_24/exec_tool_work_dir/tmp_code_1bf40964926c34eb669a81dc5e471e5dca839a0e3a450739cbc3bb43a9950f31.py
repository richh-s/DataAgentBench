code = """import json
import pandas as pd
from datetime import datetime

# Load OrderItems
order_items = locals()['var_function-call-9822237472880151234']
# Load Cases file
case_file_path = locals()['var_function-call-9822237472880150197']
with open(case_file_path, 'r') as f:
    cases = json.load(f)

# Normalize IDs function
def clean_id(x):
    if x and isinstance(x, str):
        return x.lstrip('#')
    return x

# Prepare target OrderItem IDs
target_oi_ids = set()
for oi in order_items:
    target_oi_ids.add(clean_id(oi['Id']))

# Filter Cases
relevant_cases = []
for c in cases:
    c_oid = clean_id(c.get('orderitemid__c'))
    if c_oid in target_oi_ids:
        relevant_cases.append(c)

# Create DataFrame
df = pd.DataFrame(relevant_cases)

# Check if empty
if df.empty:
    print('__RESULT__:')
    print(json.dumps({"message": "No relevant cases found"}))
else:
    # Convert createddate to datetime
    # Format example: "2023-07-02T11:00:00.000+0000"
    # Using mixed format inference or specifying format
    df['created_dt'] = pd.to_datetime(df['createddate'])

    # Filter date range
    # "Past 10 months" from 2021-04-10
    # Range: 2020-06-10 to 2021-04-10
    start_date = pd.Timestamp("2020-06-10").tz_localize('UTC')
    end_date = pd.Timestamp("2021-04-10").tz_localize('UTC')
    
    # Ensure timezone awareness matches
    if df['created_dt'].dt.tz is None:
         df['created_dt'] = df['created_dt'].dt.tz_localize('UTC')
    else:
         df['created_dt'] = df['created_dt'].dt.tz_convert('UTC')

    mask = (df['created_dt'] >= start_date) & (df['created_dt'] <= end_date)
    df_filtered = df[mask].copy()

    # Group by Month
    # We want to identify the month.
    df_filtered['month_year'] = df_filtered['created_dt'].dt.strftime('%Y-%m')
    df_filtered['month_name'] = df_filtered['created_dt'].dt.month_name()
    
    counts = df_filtered.groupby(['month_year', 'month_name']).size().reset_index(name='count')
    
    result = counts.to_dict(orient='records')
    print('__RESULT__:')
    print(json.dumps(result))"""

env_args = {'var_function-call-9822237472880151234': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-9822237472880150197': 'file_storage/function-call-9822237472880150197.json', 'var_function-call-14981807114117199014': [{'Product2Id': '01tWt000006hVJdIAM'}, {'Product2Id': '#01tWt000006hVJdIAM'}]}

exec(code, env_args)
