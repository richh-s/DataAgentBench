code = """import json
import pandas as pd
from datetime import datetime

# Load Order Items
file_path_oi = locals()['var_function-call-5457444856085881988']
with open(file_path_oi, 'r') as f:
    order_items = json.load(f)

# Target Product ID
target_product_id = '01tWt000006hVJdIAM'

# Build a set of OrderItem IDs that match the product
target_order_item_ids = set()

for item in order_items:
    # Clean Product2Id
    p2id = item.get('Product2Id')
    if not p2id:
        continue
    p2id_clean = p2id.strip()
    if p2id_clean.startswith('#'):
        p2id_clean = p2id_clean[1:]
    
    if p2id_clean == target_product_id:
        # Clean OrderItem Id
        oid = item.get('Id')
        if oid:
            oid_clean = oid.strip()
            if oid_clean.startswith('#'):
                oid_clean = oid_clean[1:]
            target_order_item_ids.add(oid_clean)

# Load Cases
file_path_cases = locals()['var_function-call-1872938474651528192']
with open(file_path_cases, 'r') as f:
    cases = json.load(f)

# Filter Cases
filtered_cases = []
start_date_str = '2020-06-01' # Approx 10 months ago
end_date_str = '2021-04-10'

for case in cases:
    c_oid = case.get('orderitemid__c')
    if not c_oid:
        continue
    # Clean Case OrderItem Id
    c_oid_clean = c_oid.strip()
    if c_oid_clean.startswith('#'):
        c_oid_clean = c_oid_clean[1:]
    
    if c_oid_clean in target_order_item_ids:
        c_date = case.get('createddate')
        if c_date and c_date >= start_date_str and c_date <= end_date_str: # String comparison works for ISO format
             filtered_cases.append({'date': c_date})

# Analyze
if filtered_cases:
    df = pd.DataFrame(filtered_cases)
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.month_name()
    df['year'] = df['date'].dt.year
    df['month_year'] = df['date'].dt.strftime('%Y-%B')
    
    counts = df['month_year'].value_counts().sort_index()
    print('__RESULT__:')
    print(counts.to_json())
else:
    print('__RESULT__:')
    print(json.dumps({}))"""

env_args = {'var_function-call-7545720086494888731': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-538766658491964125': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-1872938474651528192': 'file_storage/function-call-1872938474651528192.json', 'var_function-call-3473821976030577614': {'2020-November': 2, '2020-September': 1, '2021-January': 1, '2021-March': 1}, 'var_function-call-11445797233741824167': [], 'var_function-call-11618045494959090199': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}], 'var_function-call-18231925582358357544': [{'createddate': '2021-01-25T09:30:00.000+0000'}, {'createddate': '2020-11-05T08:19:00.000+0000'}, {'createddate': '2020-09-29T01:59:00.000+0000'}, {'createddate': '2021-03-07T11:25:00.000+0000'}, {'createddate': '2020-11-09T19:02:00.000+0000'}], 'var_function-call-16069975660508162232': [{'orderitemid__c': '802Wt00000797r4IAA'}, {'orderitemid__c': '802Wt00000798aDIAQ'}, {'orderitemid__c': '802Wt00000792tiIAA'}, {'orderitemid__c': '802Wt00000797r3IAA'}, {'orderitemid__c': '802Wt00000797r5IAA'}, {'orderitemid__c': '802Wt00000792tiIAA'}, {'orderitemid__c': '802Wt0000078xAFIAY'}, {'orderitemid__c': '802Wt0000079ATyIAM'}, {'orderitemid__c': '802Wt00000794bXIAQ'}, {'orderitemid__c': '802Wt00000796yFIAQ'}, {'orderitemid__c': '802Wt000007988nIAA'}, {'orderitemid__c': '802Wt00000797axIAA'}, {'orderitemid__c': '802Wt00000797r5IAA'}, {'orderitemid__c': '802Wt0000079As9IAE'}, {'orderitemid__c': '802Wt000007983xIAA'}, {'orderitemid__c': '802Wt0000079ADpIAM'}, {'orderitemid__c': '802Wt000007928FIAQ'}, {'orderitemid__c': '802Wt0000079ATxIAM'}, {'orderitemid__c': '802Wt00000799EZIAY'}, {'orderitemid__c': '802Wt0000079ATxIAM'}], 'var_function-call-259118688776744588': [{'count(*)': '689'}], 'var_function-call-5457444856085881988': 'file_storage/function-call-5457444856085881988.json', 'var_function-call-3268359730895990783': []}

exec(code, env_args)
