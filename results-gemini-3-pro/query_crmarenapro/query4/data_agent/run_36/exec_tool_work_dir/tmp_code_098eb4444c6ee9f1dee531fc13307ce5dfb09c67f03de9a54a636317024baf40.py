code = """import pandas as pd
import json

# Target Product ID
target_product_id = "01tWt000006hVJdIAM"

# Load ALL OrderItems
order_items_file = locals()['var_function-call-15969494074762132251']
with open(order_items_file, 'r') as f:
    order_items_data = json.load(f)

# Identify valid OrderItem IDs
valid_order_item_ids = set()
for item in order_items_data:
    raw_pid = item.get('Product2Id')
    raw_oid = item.get('Id')
    if raw_pid and raw_oid:
        # Clean Product ID
        clean_pid = raw_pid.lstrip('#').strip()
        if clean_pid == target_product_id:
            # Clean OrderItem ID and add to set
            clean_oid = raw_oid.lstrip('#').strip()
            valid_order_item_ids.add(clean_oid)

# Load Cases
cases_file = locals()['var_function-call-14591549845299595368']
with open(cases_file, 'r') as f:
    cases_data = json.load(f)

# Filter Cases
relevant_cases = []
current_date = pd.Timestamp('2021-04-10').tz_localize('UTC')
start_date = current_date - pd.DateOffset(months=10)

for case in cases_data:
    # Clean orderitemid__c
    raw_oid = case.get('orderitemid__c')
    if not raw_oid:
        continue
    clean_oid = raw_oid.lstrip('#').strip()
    
    if clean_oid in valid_order_item_ids:
        cdate_str = case.get('createddate')
        if cdate_str:
            try:
                cdate = pd.to_datetime(cdate_str)
                if cdate.tz is None:
                    cdate = cdate.tz_localize('UTC')
                else:
                    cdate = cdate.tz_convert('UTC')
                
                # Check date range (inclusive of start, up to end of current day)
                if start_date <= cdate <= (current_date + pd.Timedelta(days=1)):
                    relevant_cases.append({'month_name': cdate.strftime('%B'), 'year': cdate.year, 'month_year': cdate.strftime('%Y-%m')})
            except:
                pass

df = pd.DataFrame(relevant_cases)
result = {}
if not df.empty:
    # Group by month_year to distinguish months
    counts = df.groupby('month_year').size().sort_values(ascending=False)
    # Also get the month name of the top one
    top_month = counts.index[0]
    top_count = int(counts.iloc[0])
    
    # Prepare result for printing
    result = {
        "counts": counts.to_dict(),
        "top_month_key": top_month,
        "top_count": top_count,
        "month_name": df[df['month_year'] == top_month].iloc[0]['month_name']
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-8667889600301125328': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-7738091277095320761': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}], 'var_function-call-12493228435165791799': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-2130935510497008485': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-14591549845299595368': 'file_storage/function-call-14591549845299595368.json', 'var_function-call-4837108201200954273': {'November 2020': 2, 'January 2021': 1, 'March 2021': 1, 'September 2020': 1}, 'var_function-call-378961959093618944': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}], 'var_function-call-5065899491344346018': [{'COUNT(*)': '689'}], 'var_function-call-15969494074762132251': 'file_storage/function-call-15969494074762132251.json'}

exec(code, env_args)
