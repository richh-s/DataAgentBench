code = """import json
import pandas as pd

# Load data
with open(locals()['var_function-call-15237146713433936160'], 'r') as f:
    cases_data = json.load(f)

order_items_data = locals()['var_function-call-15237146713433937959']

df_cases = pd.DataFrame(cases_data)
df_order_items = pd.DataFrame(order_items_data)

def clean_id(x):
    if isinstance(x, str):
        return x.strip().lstrip('#')
    return x

df_order_items['Id_clean'] = df_order_items['Id'].apply(clean_id)
df_order_items['Product2Id_clean'] = df_order_items['Product2Id'].apply(clean_id)

target_product_id = '01tWt000006hVJdIAM'
valid_order_items = df_order_items[df_order_items['Product2Id_clean'] == target_product_id]['Id_clean'].tolist()

df_cases['orderitemid_clean'] = df_cases['orderitemid__c'].apply(clean_id)
df_cases['createddate'] = pd.to_datetime(df_cases['createddate'], utc=True)

# Precise date range
# Today: 2021-04-10. End of day.
end_date = pd.Timestamp('2021-04-10 23:59:59.999999').tz_localize('UTC')
start_date = pd.Timestamp('2020-06-10 00:00:00').tz_localize('UTC')

df_cases_filtered = df_cases[(df_cases['createddate'] >= start_date) & (df_cases['createddate'] <= end_date)]

# Match
df_matched = df_cases_filtered[df_cases_filtered['orderitemid_clean'].isin(valid_order_items)].copy()

# Print details
df_matched['MonthName'] = df_matched['createddate'].dt.month_name()
print("__RESULT__:")
print(json.dumps(df_matched[['createddate', 'MonthName']].astype(str).to_dict(orient='records')))"""

env_args = {'var_function-call-5222737157604988371': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-5222737157604988016': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-15237146713433936160': 'file_storage/function-call-15237146713433936160.json', 'var_function-call-15237146713433937959': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-10118077612135579648': [{'MonthName': 'September', 'Count': 1, 'MonthYearStr': '2020-09'}, {'MonthName': 'November', 'Count': 2, 'MonthYearStr': '2020-11'}, {'MonthName': 'January', 'Count': 1, 'MonthYearStr': '2021-01'}, {'MonthName': 'March', 'Count': 1, 'MonthYearStr': '2021-03'}], 'var_function-call-17633396882460631336': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}], 'var_function-call-16070226681690940678': [{'id': '#500Wt00000DDxnbIAD', 'createddate': '2021-01-25T09:30:00.000+0000', 'subject': 'ROI Metrics Clarification  '}, {'id': '500Wt00000DDy8bIAD', 'createddate': '2020-11-05T08:19:00.000+0000', 'subject': 'Update Alerts Absent'}, {'id': '500Wt00000DE00gIAD', 'createddate': '2020-09-29T01:59:00.000+0000', 'subject': 'SecureAnalytics Compliance Concern'}, {'id': '500Wt00000DE0AMIA1', 'createddate': '2021-03-07T11:25:00.000+0000', 'subject': 'No Feature Update Notices'}, {'id': '500Wt00000DE0NFIA1', 'createddate': '2020-11-09T19:02:00.000+0000', 'subject': 'Missing Feature Notifications'}]}

exec(code, env_args)
