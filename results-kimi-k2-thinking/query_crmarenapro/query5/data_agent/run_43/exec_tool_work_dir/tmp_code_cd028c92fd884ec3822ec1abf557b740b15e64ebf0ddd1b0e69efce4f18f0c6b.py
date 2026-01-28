code = """import json

# Load the OrderItem IDs for the product
order_items_file = var_functions.query_db_2
if isinstance(order_items_file, str) and order_items_file.endswith('.json'):
    with open(order_items_file, 'r') as f:
        product_order_items = json.load(f)
else:
    product_order_items = var_functions.query_db_2

# Load the cases from the last 5 months
cases_file = var_functions.query_db_6
if isinstance(cases_file, str) and cases_file.endswith('.json'):
    with open(cases_file, 'r') as f:
        cases = json.load(f)
else:
    cases = var_functions.query_db_6

# Create a set of OrderItem IDs (cleaned) for the product
product_orderitem_ids = set()
for item in product_order_items:
    orderitem_id = item['Id']
    # Remove leading # if present
    if orderitem_id.startswith('#'):
        orderitem_id = orderitem_id[1:]
    product_orderitem_ids.add(orderitem_id)

# Find matching cases and count issues
issue_counts = {}
matching_cases = []

for case in cases:
    case_orderitem_id = case['orderitemid__c']
    # Remove leading # if present
    if case_orderitem_id and case_orderitem_id.startswith('#'):
        case_orderitem_id = case_orderitem_id[1:]
    
    # Check if this case is for our product
    if case_orderitem_id in product_orderitem_ids:
        issue_id = case['issueid__c']
        issue_counts[issue_id] = issue_counts.get(issue_id, 0) + 1
        matching_cases.append(case)

# Find the most frequent issue
most_frequent_issue = None
max_count = 0
for issue_id, count in issue_counts.items():
    if count > max_count:
        max_count = count
        most_frequent_issue = issue_id

print('__RESULT__:')
print(json.dumps(most_frequent_issue))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'Id': '802Wt0000078wz5IAA'}, {'Id': '802Wt0000078xAAIAY'}, {'Id': '802Wt0000078yXiIAI'}, {'Id': '#802Wt00000790WEIAY'}, {'Id': '802Wt00000792gDIAQ'}, {'Id': '802Wt00000792zTIAQ'}, {'Id': '#802Wt0000079315IAA'}, {'Id': '802Wt00000793sTIAQ'}, {'Id': '802Wt00000794F3IAI'}, {'Id': '802Wt00000794F4IAI'}, {'Id': '#802Wt00000794JmIAI'}, {'Id': '#802Wt00000794YFIAY'}, {'Id': '802Wt00000794YJIAY'}, {'Id': '802Wt000007959OIAQ'}, {'Id': '802Wt00000795akIAA'}, {'Id': '802Wt00000795ywIAA'}, {'Id': '802Wt000007962JIAQ'}, {'Id': '802Wt000007968hIAA'}, {'Id': '802Wt000007968iIAA'}, {'Id': '802Wt00000796F5IAI'}, {'Id': '#802Wt00000796N7IAI'}, {'Id': '802Wt00000796NAIAY'}, {'Id': '802Wt00000796RzIAI'}, {'Id': '802Wt00000796S0IAI'}, {'Id': '802Wt00000796S1IAI'}, {'Id': '802Wt00000796VDIAY'}, {'Id': '802Wt00000796YPIAY'}, {'Id': '802Wt00000796YQIAY'}, {'Id': '802Wt00000796a1IAA'}, {'Id': '802Wt00000796dFIAQ'}, {'Id': '#802Wt00000796dIIAQ'}, {'Id': '#802Wt00000796jiIAA'}, {'Id': '802Wt00000796myIAA'}, {'Id': '802Wt00000796oaIAA'}, {'Id': '802Wt00000796rlIAA'}, {'Id': '802Wt00000796tTIAQ'}, {'Id': '802Wt00000796v0IAA'}, {'Id': '802Wt00000796wbIAA'}, {'Id': '802Wt00000796wcIAA'}, {'Id': '802Wt00000797FxIAI'}, {'Id': '802Wt00000797MQIAY'}, {'Id': '#802Wt00000797O5IAI'}, {'Id': '#802Wt00000797axIAA'}, {'Id': '802Wt00000797e9IAA'}, {'Id': '802Wt00000797hNIAQ'}, {'Id': '802Wt00000797j0IAA'}, {'Id': '#802Wt00000797mDIAQ'}, {'Id': '802Wt00000797nsIAA'}, {'Id': '#802Wt00000797pSIAQ'}, {'Id': '802Wt00000797sfIAA'}, {'Id': '802Wt00000797z8IAA'}, {'Id': '802Wt000007982LIAQ'}, {'Id': '802Wt00000798IUIAY'}, {'Id': '802Wt00000798IVIAY'}, {'Id': '802Wt00000798NKIAY'}, {'Id': '#802Wt00000798S9IAI'}, {'Id': '#802Wt00000798nBIAQ'}, {'Id': '802Wt00000798rxIAA'}, {'Id': '802Wt00000798wpIAA'}, {'Id': '802Wt000007991dIAA'}, {'Id': '802Wt0000079987IAA'}, {'Id': '802Wt00000799EZIAY'}, {'Id': '802Wt00000799HoIAI'}, {'Id': '#802Wt00000799JPIAY'}, {'Id': '802Wt00000799T3IAI'}, {'Id': '802Wt00000799ckIAA'}, {'Id': '#802Wt00000799fxIAA'}, {'Id': '802Wt00000799srIAA'}, {'Id': '802Wt00000799w5IAA'}, {'Id': '#802Wt0000079A0wIAE'}, {'Id': '802Wt0000079A2aIAE'}, {'Id': '802Wt0000079A49IAE'}, {'Id': '802Wt0000079AU1IAM'}, {'Id': '802Wt0000079AgrIAE'}, {'Id': '802Wt0000079AqXIAU'}, {'Id': '802Wt0000079As9IAE'}], 'var_functions.query_db:6': [{'id': '#500Wt00000DDYpHIAX', 'issueid__c': 'a03Wt00000JqmX6IAJ', 'orderitemid__c': '802Wt00000790mNIAQ', 'createddate': '2022-09-05T11:15:00.000+0000'}, {'id': '#500Wt00000DDZtKIAX', 'issueid__c': 'a03Wt00000JqzPSIAZ', 'orderitemid__c': '802Wt00000799mPIAQ', 'createddate': '2023-01-04T08:47:00.000+0000'}, {'id': '500Wt00000DDfx8IAD', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'orderitemid__c': '802Wt00000798K5IAI', 'createddate': '2023-01-03T10:15:00.000+0000'}, {'id': '500Wt00000DDg20IAD', 'issueid__c': 'a03Wt00000JqhItIAJ', 'orderitemid__c': '802Wt00000793bTIAQ', 'createddate': '2022-12-01T10:00:00.000+0000'}, {'id': '500Wt00000DDxScIAL', 'issueid__c': 'a03Wt00000JqnHwIAJ', 'orderitemid__c': '802Wt00000790WEIAY', 'createddate': '2022-10-01T14:45:00.000+0000'}, {'id': '500Wt00000DDxduIAD', 'issueid__c': 'a03Wt00000JqnHwIAJ', 'orderitemid__c': '802Wt00000790WEIAY', 'createddate': '2022-09-16T09:30:00.000+0000'}, {'id': '#500Wt00000DDyznIAD', 'issueid__c': 'a03Wt00000JqxtvIAB', 'orderitemid__c': '802Wt000007928FIAQ', 'createddate': '2022-09-22T19:28:00.000+0000'}, {'id': '#500Wt00000DDzJ8IAL', 'issueid__c': 'a03Wt00000JqmX6IAJ', 'orderitemid__c': '802Wt0000079A4AIAU', 'createddate': '2022-09-03T15:30:00.000+0000'}, {'id': '#500Wt00000DDzXeIAL', 'issueid__c': 'a03Wt00000JqnHwIAJ', 'orderitemid__c': '802Wt00000798olIAA', 'createddate': '2022-09-05T14:45:00.000+0000'}, {'id': '500Wt00000DE0K1IAL', 'issueid__c': 'a03Wt00000JqnHwIAJ', 'orderitemid__c': '802Wt00000798olIAA', 'createddate': '2022-10-15T11:00:00.000+0000'}]}

exec(code, env_args)
