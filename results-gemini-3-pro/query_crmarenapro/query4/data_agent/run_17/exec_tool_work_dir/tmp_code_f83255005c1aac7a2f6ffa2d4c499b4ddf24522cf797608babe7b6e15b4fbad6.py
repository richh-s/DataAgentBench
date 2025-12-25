code = """import json
import pandas as pd

# Load order items
order_items = locals()['var_function-call-7422283301212900885']
# Clean IDs
target_order_item_ids = set()
for item in order_items:
    oid = item['Id']
    if oid:
        oid = oid.strip()
        if oid.startswith('#'):
            oid = oid[1:]
        target_order_item_ids.add(oid)

# Load cases
case_file_path = locals()['var_function-call-660718047220936255']
with open(case_file_path, 'r') as f:
    cases = json.load(f)

# Filter cases
relevant_cases = []
start_date = pd.to_datetime('2020-06-10').tz_localize('UTC')
end_date = pd.to_datetime('2021-04-10').tz_localize('UTC')

for case in cases:
    oid = case.get('orderitemid__c')
    if not oid:
        continue
    # Clean case oid
    oid = oid.strip()
    if oid.startswith('#'):
        oid = oid[1:]
    
    if oid in target_order_item_ids:
        cdate_str = case.get('createddate')
        if cdate_str:
            try:
                cdate = pd.to_datetime(cdate_str)
                if cdate.tzinfo is None:
                    cdate = cdate.tz_localize('UTC')
                else:
                    cdate = cdate.tz_convert('UTC')
                
                if start_date <= cdate <= end_date:
                    relevant_cases.append(cdate)
            except:
                pass

# Group by month
df = pd.DataFrame({'date': relevant_cases})
if df.empty:
    print('__RESULT__:')
    print(json.dumps({"error": "No cases found"}))
else:
    df['month'] = df['date'].dt.strftime('%B')
    df['year_month'] = df['date'].dt.strftime('%Y-%m')
    counts = df['year_month'].value_counts().sort_index()
    counts_name = df['month'].value_counts()
    
    result = {
        "by_year_month": counts.to_dict(),
        "by_month_name": counts_name.to_dict()
    }
    print('__RESULT__:')
    print(json.dumps(result))"""

env_args = {'var_function-call-7422283301212900885': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-660718047220936255': 'file_storage/function-call-660718047220936255.json', 'var_function-call-660718047220936438': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-14010267675844107626': {'by_year_month': {'2020-09': 1, '2020-11': 2, '2021-01': 1, '2021-03': 1}, 'by_month_name': {'November': 2, 'January': 1, 'September': 1, 'March': 1}}, 'var_function-call-6646528767966415556': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}], 'var_function-call-6646528767966415861': [{'count': '1'}]}

exec(code, env_args)
