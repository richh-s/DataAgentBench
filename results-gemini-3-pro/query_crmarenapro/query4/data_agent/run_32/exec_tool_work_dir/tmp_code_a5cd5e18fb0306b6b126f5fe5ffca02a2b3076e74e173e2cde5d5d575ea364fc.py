code = """import pandas as pd
import json

# Load OrderItem IDs
order_items_data = locals()['var_function-call-4782762988492548461']

# Load Cases data
cases_file_path = locals()['var_function-call-1046338226553717698']
with open(cases_file_path, 'r') as f:
    cases_data = json.load(f)

# Create sets for OrderItem IDs for faster lookup
target_ids = set()
for item in order_items_data:
    raw_id = item['Id']
    if raw_id:
        clean_id = raw_id.strip()
        if clean_id.startswith('#'):
            clean_id = clean_id[1:]
        target_ids.add(clean_id)

# Filter Cases
relevant_cases = []
for case in cases_data:
    raw_oid = case.get('orderitemid__c')
    if not raw_oid:
        continue
    clean_oid = raw_oid.strip()
    if clean_oid.startswith('#'):
        clean_oid = clean_oid[1:]
    
    if clean_oid in target_ids:
        relevant_cases.append(case)

# Create DataFrame
df = pd.DataFrame(relevant_cases)
if df.empty:
    print('__RESULT__:')
    print(json.dumps({"error": "No relevant cases found"}))
else:
    # Convert createddate to datetime, handling UTC
    df['created_date'] = pd.to_datetime(df['createddate'], utc=True)
    
    # Filter for past 10 months
    # Today: 2021-04-10. We assume end of day or just the date. 
    # Let's align with UTC.
    end_date = pd.Timestamp('2021-04-10').tz_localize('UTC')
    # If the user implies inclusive of 2021-04-10, we should perhaps set time to end of day, but usually "past 10 months" implies looking back.
    # I'll use exact timestamp 00:00:00 for simplicity or cover the whole day if needed. 
    # Given the granularity is usually by month, exact time matters less unless it's on the boundary.
    start_date = end_date - pd.DateOffset(months=10)
    
    mask = (df['created_date'] >= start_date) & (df['created_date'] <= end_date)
    df_filtered = df.loc[mask].copy()
    
    if df_filtered.empty:
        print('__RESULT__:')
        print(json.dumps({"error": "No cases in the date range", "start": str(start_date), "end": str(end_date)}))
    else:
        # Extract Month Name
        df_filtered['month_name'] = df_filtered['created_date'].dt.strftime('%B')
        
        # Group by Month
        counts = df_filtered.groupby('month_name')['orderitemid__c'].count().reset_index(name='count')
        
        # Sort by count desc
        counts = counts.sort_values(by='count', ascending=False)
        
        print('__RESULT__:')
        print(counts.to_json(orient='records'))"""

env_args = {'var_function-call-4782762988492548461': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-1046338226553717698': 'file_storage/function-call-1046338226553717698.json'}

exec(code, env_args)
