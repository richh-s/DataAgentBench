code = """import json
from datetime import datetime

# Load OrderItem IDs
order_items = locals()['var_function-call-3420856295872642531']
target_order_item_ids = set()
for item in order_items:
    oid = item['Id']
    if oid:
        oid = oid.strip() # Strip whitespace
        if oid.startswith('#'):
            oid = oid[1:]
        target_order_item_ids.add(oid)

# Load Cases
cases_file = locals()['var_function-call-3420856295872639120']
with open(cases_file, 'r') as f:
    cases = json.load(f)

# Filter and Count
case_counts = {}
start_date = datetime(2020, 6, 10)
end_date = datetime(2021, 4, 10)

filtered_cases = []

for case in cases:
    # Clean OrderItemId
    oid_c = case.get('orderitemid__c')
    if not oid_c:
        continue
    
    oid_c = oid_c.strip() # Strip whitespace
    if oid_c.startswith('#'):
        oid_c = oid_c[1:]
    
    # Check if related to target product
    if oid_c in target_order_item_ids:
        # Check date
        cdate_str = case['createddate']
        try:
            cdate_dt = datetime.strptime(cdate_str[:10], "%Y-%m-%d")
            if start_date <= cdate_dt <= end_date:
                month_name = cdate_dt.strftime("%B")
                case_counts[month_name] = case_counts.get(month_name, 0) + 1
                filtered_cases.append(case)
        except ValueError:
            continue

print("__RESULT__:")
print(json.dumps(case_counts))"""

env_args = {'var_function-call-530338849428747900': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-530338849428749193': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-3420856295872642531': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-3420856295872639120': 'file_storage/function-call-3420856295872639120.json', 'var_function-call-14800394706308198195': {'January': 1, 'November': 2, 'September': 1, 'March': 1}, 'var_function-call-13992762942569951089': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro', 'External_ID__c': 'Data Analytics Platforms,Security and Compliance Modules_13'}], 'var_function-call-17688011455540546709': ['2021-01-25T09:30:00.000+0000', '2020-11-05T08:19:00.000+0000', '2023-06-30T13:03:00.000+0000', '2020-09-29T01:59:00.000+0000', '2021-03-07T11:25:00.000+0000', '2020-11-09T19:02:00.000+0000'], 'var_function-call-1051271700341571764': [{'Id': '802Wt0000078wz3IAA', 'OrderId': '801Wt00000PGSYIIA5', 'Product2Id': '#01tWt000006hVTJIA2', 'Quantity': '15.0', 'UnitPrice': '476.991', 'PriceBookEntryId': '01uWt0000027Pa1IAE'}, {'Id': '802Wt0000078wz4IAA', 'OrderId': '801Wt00000PHVkDIAX', 'Product2Id': '01tWt000006hVDBIA2', 'Quantity': '3.0', 'UnitPrice': '549.99', 'PriceBookEntryId': '01uWt0000027PF3IAM'}, {'Id': '802Wt0000078wz5IAA', 'OrderId': '801Wt00000PHQuFIAX', 'Product2Id': '01tWt000006hV8LIAU', 'Quantity': '9.0', 'UnitPrice': '503.4905', 'PriceBookEntryId': '01uWt0000027P8cIAE'}, {'Id': '802Wt0000078xAAIAY', 'OrderId': '801Wt00000PGHg7IAH', 'Product2Id': '01tWt000006hV8LIAU', 'Quantity': '10.0', 'UnitPrice': '476.991', 'PriceBookEntryId': '01uWt0000027P8cIAE'}, {'Id': '#802Wt0000078xABIAY', 'OrderId': '801Wt00000PHVicIAH', 'Product2Id': '01tWt000006hVMrIAM', 'Quantity': '1.0', 'UnitPrice': '299.99', 'PriceBookEntryId': '01uWt0000027POjIAM'}], 'var_function-call-1051271700341573851': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027P3mIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVhpIAE', 'UnitPrice': '489.99'}, {'Id': '01uWt0000027P5NIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hV58IAE', 'UnitPrice': '599.99'}, {'Id': '#01uWt0000027P6zIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hTUkIAM', 'UnitPrice': '399.99'}, {'Id': '#01uWt0000027P8bIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV6jIAE', 'UnitPrice': '349.99'}], 'var_function-call-11363536213205745924': [{'Id': '01uWt0000027PJtIAM'}], 'var_function-call-18109756787802840435': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-17463913523078601579': [{'id': '#500Wt00000DDxnbIAD', 'createddate': '2021-01-25T09:30:00.000+0000'}, {'id': '500Wt00000DDy8bIAD', 'createddate': '2020-11-05T08:19:00.000+0000'}, {'id': '500Wt00000DE00gIAD', 'createddate': '2020-09-29T01:59:00.000+0000'}, {'id': '500Wt00000DE0AMIA1', 'createddate': '2021-03-07T11:25:00.000+0000'}, {'id': '500Wt00000DE0NFIA1', 'createddate': '2020-11-09T19:02:00.000+0000'}], 'var_function-call-17533078027490655287': [], 'var_function-call-9094339139192889946': [{'id': '#500Wt00000DDxnbIAD', 'createddate': '2021-01-25T09:30:00.000+0000', 'subject': 'ROI Metrics Clarification  '}, {'id': '500Wt00000DDy8bIAD', 'createddate': '2020-11-05T08:19:00.000+0000', 'subject': 'Update Alerts Absent'}, {'id': '500Wt00000DE00gIAD', 'createddate': '2020-09-29T01:59:00.000+0000', 'subject': 'SecureAnalytics Compliance Concern'}, {'id': '500Wt00000DE0AMIA1', 'createddate': '2021-03-07T11:25:00.000+0000', 'subject': 'No Feature Update Notices'}, {'id': '500Wt00000DE0NFIA1', 'createddate': '2020-11-09T19:02:00.000+0000', 'subject': 'Missing Feature Notifications'}]}

exec(code, env_args)
