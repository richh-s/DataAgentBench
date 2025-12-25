code = """import json
import pandas as pd

# Access variables from locals
order_items_data = locals()['var_function-call-3562023347462174956']
cases_file_path = locals()['var_function-call-7329632320469133909']

# Load OrderItem IDs
if isinstance(order_items_data, str):
    order_items = json.loads(order_items_data)
else:
    order_items = order_items_data

target_item_ids = set()
for item in order_items:
    if item.get('Id'):
        clean_id = str(item['Id']).lstrip('#').strip()
        target_item_ids.add(clean_id)

# Load Cases
with open(cases_file_path, 'r') as f:
    cases = json.load(f)

df = pd.DataFrame(cases)

if df.empty:
    print("__RESULT__:")
    print(json.dumps({}))
else:
    # Clean orderitemid__c
    df['clean_orderitemid'] = df['orderitemid__c'].astype(str).apply(lambda x: x.lstrip('#').strip())

    # Filter by target OrderItem IDs
    df_filtered = df[df['clean_orderitemid'].isin(target_item_ids)].copy()

    if df_filtered.empty:
        print("__RESULT__:")
        print(json.dumps({}))
    else:
        # Convert createddate to datetime
        df_filtered['created_dt'] = pd.to_datetime(df_filtered['createddate'])
        
        # Sort by date
        df_filtered = df_filtered.sort_values('created_dt')

        # Group by Year-Month
        df_filtered['year_month'] = df_filtered['created_dt'].dt.to_period('M')
        counts_ym = df_filtered.groupby('year_month')['id'].count()

        print("__RESULT__:")
        print(json.dumps({str(k): v for k, v in counts_ym.to_dict().items()}))"""

env_args = {'var_function-call-3562023347462174956': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-7329632320469133909': 'file_storage/function-call-7329632320469133909.json', 'var_function-call-10279842958367100034': {'counts_by_month_name': {'January': 1, 'March': 1, 'November': 2, 'September': 1}, 'counts_by_year_month': {'2020-09': 1, '2020-11': 2, '2021-01': 1, '2021-03': 1}}, 'var_function-call-2098960887653857239': [], 'var_function-call-2696260698802733294': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}]}

exec(code, env_args)
