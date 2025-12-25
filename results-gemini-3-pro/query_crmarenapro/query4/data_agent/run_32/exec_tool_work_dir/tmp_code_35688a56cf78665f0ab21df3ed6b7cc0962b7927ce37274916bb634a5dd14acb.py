code = """import pandas as pd
import json

# Load OrderItems
order_items_file = locals()['var_function-call-2610723034945138776']
with open(order_items_file, 'r') as f:
    order_items_data = json.load(f)

target_product_id = '01tWt000006hVJdIAM'
valid_order_item_ids = set()

# Process OrderItems to find matching IDs
for item in order_items_data:
    pid = item.get('Product2Id', '')
    if not pid: continue
    
    clean_pid = pid.strip()
    if clean_pid.startswith('#'):
        clean_pid = clean_pid[1:]
        
    if clean_pid == target_product_id:
        # If product matches, add the OrderItem Id to set
        oid = item.get('Id', '')
        if oid:
            clean_oid = oid.strip()
            if clean_oid.startswith('#'):
                clean_oid = clean_oid[1:]
            valid_order_item_ids.add(clean_oid)

print(f"DEBUG: Found {len(valid_order_item_ids)} matching OrderItem IDs.")

# Load Cases
cases_file_path = locals()['var_function-call-1046338226553717698']
with open(cases_file_path, 'r') as f:
    cases_data = json.load(f)

relevant_cases = []
for case in cases_data:
    raw_oid = case.get('orderitemid__c')
    if not raw_oid: continue
    
    clean_oid = raw_oid.strip()
    if clean_oid.startswith('#'):
        clean_oid = clean_oid[1:]
        
    if clean_oid in valid_order_item_ids:
        relevant_cases.append(case)

print(f"DEBUG: Found {len(relevant_cases)} relevant cases before date filter.")

df = pd.DataFrame(relevant_cases)
if df.empty:
    print('__RESULT__:')
    print(json.dumps([]))
else:
    df['created_date'] = pd.to_datetime(df['createddate'], utc=True)
    
    end_date = pd.Timestamp('2021-04-10').tz_localize('UTC')
    start_date = end_date - pd.DateOffset(months=10)
    
    mask = (df['created_date'] >= start_date) & (df['created_date'] <= end_date)
    df_filtered = df.loc[mask].copy()
    
    print(f"DEBUG: Found {len(df_filtered)} cases in date range.")
    
    if df_filtered.empty:
        print('__RESULT__:')
        print(json.dumps([]))
    else:
        df_filtered['month_name'] = df_filtered['created_date'].dt.strftime('%B')
        counts = df_filtered.groupby('month_name')['orderitemid__c'].count().reset_index(name='count')
        counts = counts.sort_values(by='count', ascending=False)
        print('__RESULT__:')
        print(counts.to_json(orient='records'))"""

env_args = {'var_function-call-4782762988492548461': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-1046338226553717698': 'file_storage/function-call-1046338226553717698.json', 'var_function-call-4732369327275654210': [{'month_name': 'November', 'count': 2}, {'month_name': 'January', 'count': 1}, {'month_name': 'March', 'count': 1}, {'month_name': 'September', 'count': 1}], 'var_function-call-2610723034945138776': 'file_storage/function-call-2610723034945138776.json'}

exec(code, env_args)
