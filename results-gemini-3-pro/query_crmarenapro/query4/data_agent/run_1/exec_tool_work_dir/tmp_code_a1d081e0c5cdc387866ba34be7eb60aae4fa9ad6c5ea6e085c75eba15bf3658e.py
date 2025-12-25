code = """import json
import pandas as pd

# Load order items
order_items = locals()['var_function-call-10158223557989843011']
# Load cases
cases_path = locals()['var_function-call-8293248890011068619']
with open(cases_path, 'r') as f:
    cases = json.load(f)

# Create sets of valid OrderItem IDs (clean them)
valid_ids = set()
for item in order_items:
    id_val = item['Id']
    if id_val:
        # Remove leading #
        if id_val.startswith('#'):
            id_val = id_val[1:]
        # Strip whitespace
        id_val = id_val.strip()
        valid_ids.add(id_val)

# Process cases
case_data = []
for c in cases:
    oid = c.get('orderitemid__c')
    cdate = c.get('createddate')
    if oid and cdate:
        # Clean oid
        if oid.startswith('#'):
            oid = oid[1:]
        oid = oid.strip()
        
        if oid in valid_ids:
            case_data.append({'createddate': cdate})

df = pd.DataFrame(case_data)
if not df.empty:
    df['createddate'] = pd.to_datetime(df['createddate'])
    # Filter for past 10 months from 2021-04-10
    end_date = pd.Timestamp('2021-04-10')
    start_date = end_date - pd.DateOffset(months=10)
    
    df = df[(df['createddate'] >= start_date) & (df['createddate'] <= end_date)]
    
    # Extract month name
    df['month'] = df['createddate'].dt.strftime('%B')
    df['year_month'] = df['createddate'].dt.to_period('M')
    
    counts = df.groupby('year_month')['month'].count()
    counts_named = df.groupby('month')['month'].count()
    
    print("__RESULT__:")
    print(json.dumps({
        "counts_by_period": {str(k): v for k, v in counts.items()},
        "counts_by_name": counts_named.to_dict()
    }))
else:
    print("__RESULT__:")
    print(json.dumps({"message": "No matching cases found"}))"""

env_args = {'var_function-call-10158223557989843011': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}], 'var_function-call-8293248890011068619': 'file_storage/function-call-8293248890011068619.json'}

exec(code, env_args)
