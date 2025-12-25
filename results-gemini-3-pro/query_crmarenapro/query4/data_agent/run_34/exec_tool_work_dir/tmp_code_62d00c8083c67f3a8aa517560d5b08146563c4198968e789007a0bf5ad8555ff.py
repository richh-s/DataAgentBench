code = """import json
import pandas as pd
from datetime import datetime

# Load Case data
with open(locals()['var_function-call-5866975110549239295'], 'r') as f:
    cases = json.load(f)

# Load OrderItem data
with open(locals()['var_function-call-16846297581154012635'], 'r') as f:
    order_items = json.load(f)

target_product_id = '01tWt000006hVJdIAM'

# Filter OrderItems
relevant_order_item_ids = set()
for item in order_items:
    pid = item.get('Product2Id')
    if pid:
        clean_pid = pid.strip().lstrip('#')
        if clean_pid == target_product_id:
            oid = item.get('Id')
            if oid:
                clean_oid = oid.strip().lstrip('#')
                relevant_order_item_ids.add(clean_oid)

print(f"Found {len(relevant_order_item_ids)} relevant OrderItems.")

# Filter Cases
matches = []
for case in cases:
    raw_oid = case.get('orderitemid__c')
    if not raw_oid:
        continue
    cleaned_oid = raw_oid.strip().lstrip('#')
    
    if cleaned_oid in relevant_order_item_ids:
        # Date processing
        cdate_str = case['createddate']
        try:
            cdate_dt = datetime.strptime(cdate_str, "%Y-%m-%dT%H:%M:%S.%f%z")
            cdate = cdate_dt.date()
            
            # Range: 2020-06-10 to 2021-04-10
            start_date = datetime(2020, 6, 10).date()
            end_date = datetime(2021, 4, 10).date()
            
            if start_date <= cdate <= end_date:
                matches.append({
                    'month': cdate.strftime('%B'),
                    'year_month': cdate.strftime('%Y-%m'),
                    'date': cdate.strftime('%Y-%m-%d')
                })
        except ValueError:
            pass

df = pd.DataFrame(matches)
if not df.empty:
    counts = df['year_month'].value_counts().sort_index()
    counts_named = df['month'].value_counts()
    print("__RESULT__:")
    print(json.dumps({
        "counts_by_ym": counts.to_dict(),
        "counts_by_name": counts_named.to_dict(),
        "details": matches
    }))
else:
    print("__RESULT__:")
    print(json.dumps({"counts": {}, "details": []}))"""

env_args = {'var_function-call-2761220900479506085': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-2761220900479505406': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-5866975110549239295': 'file_storage/function-call-5866975110549239295.json', 'var_function-call-5866975110549240888': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}], 'var_function-call-7575201057824002274': {'counts_by_ym': {'2020-09': 1, '2020-11': 2, '2021-03': 1}, 'counts_by_name': {'November': 2, 'September': 1, 'March': 1}}, 'var_function-call-4228500991466225667': [{'case_id': '500Wt00000DDy8bIAD', 'createddate': '2020-11-05T08:19:00.000+0000', 'oid': '802Wt00000796qFIAQ'}, {'case_id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'oid': '802Wt00000798YdIAI'}, {'case_id': '500Wt00000DE00gIAD', 'createddate': '2020-09-29T01:59:00.000+0000', 'oid': '802Wt00000796bfIAA'}, {'case_id': '500Wt00000DE0AMIA1', 'createddate': '2021-03-07T11:25:00.000+0000', 'oid': '802Wt00000796qFIAQ'}, {'case_id': '500Wt00000DE0NFIA1', 'createddate': '2020-11-09T19:02:00.000+0000', 'oid': '802Wt00000796qFIAQ'}], 'var_function-call-14431728496812184382': [], 'var_function-call-16988956225792812766': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}], 'var_function-call-1567972343993841892': [{'count(*)': '689'}], 'var_function-call-16846297581154012635': 'file_storage/function-call-16846297581154012635.json'}

exec(code, env_args)
