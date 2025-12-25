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
    # Convert createddate to datetime
    # The format in preview looks like "2023-07-02T11:00:00.000+0000"
    df['created_date'] = pd.to_datetime(df['createddate'])
    
    # Filter for past 10 months
    # Today: 2021-04-10
    end_date = pd.Timestamp('2021-04-10')
    start_date = end_date - pd.DateOffset(months=10)
    
    mask = (df['created_date'] >= start_date) & (df['created_date'] <= end_date)
    df_filtered = df.loc[mask].copy()
    
    if df_filtered.empty:
        print('__RESULT__:')
        print(json.dumps({"error": "No cases in the date range", "debug_dates": [str(start_date), str(end_date)], "sample_dates": df['created_date'].head().dt.strftime('%Y-%m-%d').tolist()}))
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
