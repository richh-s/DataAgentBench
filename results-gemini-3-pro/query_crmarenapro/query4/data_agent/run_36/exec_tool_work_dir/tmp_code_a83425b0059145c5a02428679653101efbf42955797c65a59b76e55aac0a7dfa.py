code = """import pandas as pd
import json

# Load OrderItem IDs
order_items_data = locals()['var_function-call-12493228435165791799']
# Clean OrderItem IDs
valid_order_item_ids = set()
for item in order_items_data:
    oid = item['Id']
    if oid:
        # remove leading # and whitespace
        clean_id = oid.lstrip('#').strip()
        valid_order_item_ids.add(clean_id)

# Load Cases
cases_file_path = locals()['var_function-call-14591549845299595368']
with open(cases_file_path, 'r') as f:
    cases_data = json.load(f)

# Process cases
relevant_cases = []
# Current date 2021-04-10
current_date = pd.Timestamp('2021-04-10').tz_localize('UTC')
# Past 10 months: Start from roughly 2020-06-10.
# I'll be inclusive.
start_date = current_date - pd.DateOffset(months=10)

for case in cases_data:
    # Clean orderitemid__c
    raw_oid = case.get('orderitemid__c')
    if not raw_oid:
        continue
    clean_oid = raw_oid.lstrip('#').strip()
    
    if clean_oid in valid_order_item_ids:
        # Check date
        cdate_str = case.get('createddate')
        if cdate_str:
            # Parse date
            try:
                cdate = pd.to_datetime(cdate_str)
                # Ensure UTC
                if cdate.tz is None:
                    cdate = cdate.tz_localize('UTC')
                else:
                    cdate = cdate.tz_convert('UTC')
                
                # Check range (using strictly < current_date + 1 day to include all of today)
                if start_date <= cdate <= (current_date + pd.Timedelta(days=1)):
                    relevant_cases.append({'month': cdate.strftime('%B %Y'), 'id': case['id']})
            except Exception as e:
                pass

df = pd.DataFrame(relevant_cases)
result = {}
if not df.empty:
    counts = df.groupby('month').size().sort_values(ascending=False)
    result = counts.to_dict()

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-8667889600301125328': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-7738091277095320761': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}], 'var_function-call-12493228435165791799': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-2130935510497008485': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-14591549845299595368': 'file_storage/function-call-14591549845299595368.json'}

exec(code, env_args)
