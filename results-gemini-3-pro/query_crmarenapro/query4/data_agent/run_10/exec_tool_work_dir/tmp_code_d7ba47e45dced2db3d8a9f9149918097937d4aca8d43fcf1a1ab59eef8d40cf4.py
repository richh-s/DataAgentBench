code = """import json
import pandas as pd

# Load data
with open(locals()['var_function-call-12271190876492238921'], 'r') as f:
    order_items = json.load(f)

with open(locals()['var_function-call-12271190876492240154'], 'r') as f:
    cases = json.load(f)

# Helper to clean IDs
def clean_id(x):
    if isinstance(x, str):
        return x.strip().lstrip('#')
    return x

# Target Product ID
target_product_id = '01tWt000006hVJdIAM'

# Filter OrderItems
target_order_item_ids = set()
for item in order_items:
    pid = clean_id(item.get('Product2Id'))
    if pid == target_product_id:
        oid = clean_id(item.get('Id'))
        if oid:
            target_order_item_ids.add(oid)

# Process Cases
case_counts = {}
relevant_cases = []

# Date range
start_date = pd.Timestamp('2020-06-01').tz_localize('UTC')
end_date = pd.Timestamp('2021-04-11').tz_localize('UTC')

for case in cases:
    oid = clean_id(case.get('orderitemid__c'))
    if oid in target_order_item_ids:
        cdate_str = case.get('createddate')
        if cdate_str:
            try:
                # Dates like "2023-07-02T11:00:00.000+0000"
                cdate = pd.to_datetime(cdate_str)
                # Ensure timezone awareness matches if needed, or compare as is if both aware
                # pd.to_datetime usually handles ISO8601
                
                # Check if within last 10 months (approx)
                # The user query is specific about "past 10 months".
                # Let's count ALL relevant cases and inspect dates.
                
                key = (cdate.year, cdate.month)
                case_counts[key] = case_counts.get(key, 0) + 1
                relevant_cases.append(cdate)
            except Exception as e:
                pass

# Sort and print
sorted_counts = sorted(case_counts.items())
print("__RESULT__:")
print(json.dumps(sorted_counts))"""

env_args = {'var_function-call-14757672430313574628': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-633523577645832216': [{'id': '500Wt00000DDDtTIAX', 'createddate': '2020-12-29T08:36:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDPM6IAP', 'createddate': '2020-09-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDRB2IAP', 'createddate': '2021-01-10T09:30:00.000+0000', 'orderitemid__c': '802Wt00000797axIAA'}, {'id': '500Wt00000DDRVzIAP', 'createddate': '2020-09-05T09:15:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDYpGIAX', 'createddate': '2021-03-31T11:41:00.000+0000', 'orderitemid__c': '802Wt00000798OvIAI'}, {'id': '#500Wt00000DDZmsIAH', 'createddate': '2020-07-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000795XwIAI'}, {'id': '500Wt00000DDeoCIAT', 'createddate': '2020-07-01T15:30:00.000+0000', 'orderitemid__c': '802Wt00000794bTIAQ'}, {'id': '#500Wt00000DDfvXIAT', 'createddate': '2021-03-24T18:04:00.000+0000', 'orderitemid__c': '802Wt00000796dGIAQ'}, {'id': '#500Wt00000DDg8QIAT', 'createddate': '2021-03-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDsG4IAL', 'createddate': '2020-11-05T11:00:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDt7HIAT', 'createddate': '2021-02-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}, {'id': '#500Wt00000DDxnbIAD', 'createddate': '2021-01-25T09:30:00.000+0000', 'orderitemid__c': '802Wt00000799o1IAA'}, {'id': '500Wt00000DDy8bIAD', 'createddate': '2020-11-05T08:19:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DDymuIAD', 'createddate': '2020-10-01T14:30:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDz6GIAT', 'createddate': '2020-09-03T14:45:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '#500Wt00000DDzKjIAL', 'createddate': '2020-10-22T03:55:00.000+0000', 'orderitemid__c': '802Wt00000796JtIAI'}, {'id': '500Wt00000DDzmAIAT', 'createddate': '2021-02-20T14:30:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DE00gIAD', 'createddate': '2020-09-29T01:59:00.000+0000', 'orderitemid__c': '802Wt00000796bfIAA'}, {'id': '500Wt00000DE05VIAT', 'createddate': '2021-01-03T15:30:00.000+0000', 'orderitemid__c': '802Wt00000799b7IAA'}, {'id': '500Wt00000DE0AMIA1', 'createddate': '2021-03-07T11:25:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0DZIA1', 'createddate': '2020-11-10T22:14:00.000+0000', 'orderitemid__c': '802Wt00000799uTIAQ'}, {'id': '500Wt00000DE0NFIA1', 'createddate': '2020-11-09T19:02:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0WwIAL', 'createddate': '2021-03-10T15:45:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}], 'var_function-call-77363065289227832': {'counts': [[[2020, 9, 'September'], 1], [[2020, 11, 'November'], 2], [[2021, 1, 'January'], 1], [[2021, 3, 'March'], 1]], 'total_matches': 5}, 'var_function-call-14928889524230315831': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro', 'External_ID__c': 'Data Analytics Platforms,Security and Compliance Modules_13'}], 'var_function-call-14928889524230315716': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-5117230080602577408': [{'count': '153'}], 'var_function-call-5117230080602578185': [{'orderitemid__c': '802Wt00000797r4IAA'}, {'orderitemid__c': '802Wt00000798aDIAQ'}, {'orderitemid__c': '802Wt00000792tiIAA'}, {'orderitemid__c': '802Wt00000797r3IAA'}, {'orderitemid__c': '802Wt00000797r5IAA'}, {'orderitemid__c': '802Wt00000792tiIAA'}, {'orderitemid__c': '802Wt0000078xAFIAY'}, {'orderitemid__c': '802Wt0000079ATyIAM'}, {'orderitemid__c': '802Wt00000794bXIAQ'}, {'orderitemid__c': '802Wt00000796yFIAQ'}, {'orderitemid__c': '802Wt000007988nIAA'}, {'orderitemid__c': '802Wt00000797axIAA'}, {'orderitemid__c': '802Wt00000797r5IAA'}, {'orderitemid__c': '802Wt0000079As9IAE'}, {'orderitemid__c': '802Wt000007983xIAA'}, {'orderitemid__c': '802Wt0000079ADpIAM'}, {'orderitemid__c': '802Wt000007928FIAQ'}, {'orderitemid__c': '802Wt0000079ATxIAM'}, {'orderitemid__c': '802Wt00000799EZIAY'}, {'orderitemid__c': '802Wt0000079ATxIAM'}], 'var_function-call-18273682006602143866': [{'Id': '802Wt00000798aDIAQ', 'OrderId': '801Wt00000PHLzOIAX', 'Product2Id': '01tWt000006hV58IAE', 'Quantity': '3.0', 'UnitPrice': '599.99', 'PriceBookEntryId': '01uWt0000027P5NIAU'}], 'var_function-call-15043664137983006632': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro', 'Description': 'Data analytics platform with enhanced focus on security and compliance.', 'IsActive': '1', 'External_ID__c': 'Data Analytics Platforms,Security and Compliance Modules_13'}], 'var_function-call-12271190876492238921': 'file_storage/function-call-12271190876492238921.json', 'var_function-call-12271190876492240154': 'file_storage/function-call-12271190876492240154.json'}

exec(code, env_args)
