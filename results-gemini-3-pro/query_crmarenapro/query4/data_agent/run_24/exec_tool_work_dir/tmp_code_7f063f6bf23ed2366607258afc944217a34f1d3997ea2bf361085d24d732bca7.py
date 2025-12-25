code = """import json
import pandas as pd

# Load OrderItems (list of dicts)
order_items = locals()['var_function-call-9822237472880151234']
# Load Cases file
case_file_path = locals()['var_function-call-9822237472880150197']
with open(case_file_path, 'r') as f:
    cases = json.load(f)

# Improved clean function
def clean_id(x):
    if isinstance(x, str):
        return x.strip().lstrip('#')
    return str(x) if x else None

# Prepare target OrderItem IDs
target_oi_ids = set()
for oi in order_items:
    val = clean_id(oi.get('Id'))
    if val:
        target_oi_ids.add(val)

print(f"Target OrderItem IDs count: {len(target_oi_ids)}")

# Filter Cases
relevant_cases = []
for c in cases:
    c_oid = clean_id(c.get('orderitemid__c'))
    if c_oid and c_oid in target_oi_ids:
        relevant_cases.append(c)

print(f"Found {len(relevant_cases)} relevant cases.")

# Create DataFrame
if not relevant_cases:
    print('__RESULT__:')
    print(json.dumps([]))
else:
    df = pd.DataFrame(relevant_cases)
    df['created_dt'] = pd.to_datetime(df['createddate'])
    
    # Date filtering
    # Past 10 months from 2021-04-10
    start_date = pd.Timestamp("2020-06-10").tz_localize('UTC')
    end_date = pd.Timestamp("2021-04-10").tz_localize('UTC')
    
    if df['created_dt'].dt.tz is None:
         df['created_dt'] = df['created_dt'].dt.tz_localize('UTC')
    else:
         df['created_dt'] = df['created_dt'].dt.tz_convert('UTC')

    mask = (df['created_dt'] >= start_date) & (df['created_dt'] <= end_date)
    df_filtered = df[mask].copy()
    
    print(f"Filtered cases in range: {len(df_filtered)}")

    if len(df_filtered) > 0:
        df_filtered['month_year'] = df_filtered['created_dt'].dt.strftime('%Y-%m')
        df_filtered['month_name'] = df_filtered['created_dt'].dt.month_name()
        
        counts = df_filtered.groupby(['month_year', 'month_name']).size().reset_index(name='count')
        result = counts.to_dict(orient='records')
        print('__RESULT__:')
        print(json.dumps(result))
    else:
        print('__RESULT__:')
        print(json.dumps([]))"""

env_args = {'var_function-call-9822237472880151234': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-9822237472880150197': 'file_storage/function-call-9822237472880150197.json', 'var_function-call-14981807114117199014': [{'Product2Id': '01tWt000006hVJdIAM'}, {'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-2763364339123918824': [{'month_year': '2020-09', 'month_name': 'September', 'count': 1}, {'month_year': '2020-11', 'month_name': 'November', 'count': 2}, {'month_year': '2021-01', 'month_name': 'January', 'count': 1}, {'month_year': '2021-03', 'month_name': 'March', 'count': 1}], 'var_function-call-7145074624251064754': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}], 'var_function-call-7145074624251066043': [{'Count(*)': '689'}], 'var_function-call-8649526282731093157': [{'id': '#500Wt00000DDxnbIAD', 'createddate': '2021-01-25T09:30:00.000+0000'}, {'id': '500Wt00000DDy8bIAD', 'createddate': '2020-11-05T08:19:00.000+0000'}, {'id': '500Wt00000DE00gIAD', 'createddate': '2020-09-29T01:59:00.000+0000'}, {'id': '500Wt00000DE0AMIA1', 'createddate': '2021-03-07T11:25:00.000+0000'}, {'id': '500Wt00000DE0NFIA1', 'createddate': '2020-11-09T19:02:00.000+0000'}], 'var_function-call-8204222968077973088': [{'id': '#500Wt00000DDxnbIAD', 'createddate': '2021-01-25T09:30:00.000+0000', 'subject': 'ROI Metrics Clarification  '}, {'id': '500Wt00000DDy8bIAD', 'createddate': '2020-11-05T08:19:00.000+0000', 'subject': 'Update Alerts Absent'}, {'id': '500Wt00000DE00gIAD', 'createddate': '2020-09-29T01:59:00.000+0000', 'subject': 'SecureAnalytics Compliance Concern'}, {'id': '500Wt00000DE0AMIA1', 'createddate': '2021-03-07T11:25:00.000+0000', 'subject': 'No Feature Update Notices'}, {'id': '500Wt00000DE0NFIA1', 'createddate': '2020-11-09T19:02:00.000+0000', 'subject': 'Missing Feature Notifications'}], 'var_function-call-6436880395090780845': [{'Count(*)': '0'}], 'var_function-call-6436880395090781588': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}]}

exec(code, env_args)
