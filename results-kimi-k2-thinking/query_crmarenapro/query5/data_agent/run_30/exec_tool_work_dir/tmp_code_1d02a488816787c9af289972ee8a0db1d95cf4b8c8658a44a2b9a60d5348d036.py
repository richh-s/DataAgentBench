code = """import json

# Access the results from the previous queries using locals()
cases_data = locals()['var_functions.query_db:0']
order_items_data = locals()['var_functions.query_db:2']

# Clean IDs by removing leading # and trailing whitespace
def clean_id(id_value):
    if isinstance(id_value, str):
        return id_value.replace('#', '').strip()
    return id_value

# Clean the order item IDs
order_item_ids = [clean_id(item['Id']) for item in order_items_data]

# Filter cases to find those related to the product (within the past 5 months)
# and group by issue ID to find the most frequent one
issue_counts = {}

for case in cases_data:
    orderitem_id = clean_id(case.get('orderitemid__c', ''))
    issue_id = clean_id(case.get('issueid__c', ''))
    
    if orderitem_id in order_item_ids and issue_id:
        issue_counts[issue_id] = issue_counts.get(issue_id, 0) + 1

# Find the most frequent issue ID
most_frequent_issue = None
max_count = 0

for issue_id, count in issue_counts.items():
    if count > max_count:
        max_count = count
        most_frequent_issue = issue_id

result = most_frequent_issue

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'id': '#500Wt00000DDYpHIAX', 'issueid__c': 'a03Wt00000JqmX6IAJ', 'orderitemid__c': '802Wt00000790mNIAQ', 'createddate': '2022-09-05T11:15:00.000+0000'}, {'id': '#500Wt00000DDZtKIAX', 'issueid__c': 'a03Wt00000JqzPSIAZ', 'orderitemid__c': '802Wt00000799mPIAQ', 'createddate': '2023-01-04T08:47:00.000+0000'}, {'id': '500Wt00000DDfx8IAD', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'orderitemid__c': '802Wt00000798K5IAI', 'createddate': '2023-01-03T10:15:00.000+0000'}, {'id': '500Wt00000DDg20IAD', 'issueid__c': 'a03Wt00000JqhItIAJ', 'orderitemid__c': '802Wt00000793bTIAQ', 'createddate': '2022-12-01T10:00:00.000+0000'}, {'id': '500Wt00000DDxScIAL', 'issueid__c': 'a03Wt00000JqnHwIAJ', 'orderitemid__c': '802Wt00000790WEIAY', 'createddate': '2022-10-01T14:45:00.000+0000'}, {'id': '500Wt00000DDxduIAD', 'issueid__c': 'a03Wt00000JqnHwIAJ', 'orderitemid__c': '802Wt00000790WEIAY', 'createddate': '2022-09-16T09:30:00.000+0000'}, {'id': '#500Wt00000DDyznIAD', 'issueid__c': 'a03Wt00000JqxtvIAB', 'orderitemid__c': '802Wt000007928FIAQ', 'createddate': '2022-09-22T19:28:00.000+0000'}, {'id': '#500Wt00000DDzJ8IAL', 'issueid__c': 'a03Wt00000JqmX6IAJ', 'orderitemid__c': '802Wt0000079A4AIAU', 'createddate': '2022-09-03T15:30:00.000+0000'}, {'id': '#500Wt00000DDzXeIAL', 'issueid__c': 'a03Wt00000JqnHwIAJ', 'orderitemid__c': '802Wt00000798olIAA', 'createddate': '2022-09-05T14:45:00.000+0000'}, {'id': '500Wt00000DE0K1IAL', 'issueid__c': 'a03Wt00000JqnHwIAJ', 'orderitemid__c': '802Wt00000798olIAA', 'createddate': '2022-10-15T11:00:00.000+0000'}], 'var_functions.query_db:2': [{'Id': '802Wt0000078wz5IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000078xAAIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000078yXiIAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000790WEIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000792gDIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000792zTIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt0000079315IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000793sTIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000794F3IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000794F4IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000794JmIAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000794YFIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000794YJIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007959OIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000795akIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000795ywIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007962JIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007968hIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007968iIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796F5IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000796N7IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796NAIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796RzIAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796S0IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796S1IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796VDIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796YPIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796YQIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796a1IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796dFIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000796dIIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000796jiIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796myIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796oaIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796rlIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796tTIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796v0IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796wbIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000796wcIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797FxIAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797MQIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000797O5IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000797axIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797e9IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797hNIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797j0IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000797mDIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797nsIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000797pSIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797sfIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000797z8IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007982LIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000798IUIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000798IVIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000798NKIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000798S9IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000798nBIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000798rxIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000798wpIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt000007991dIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000079987IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000799EZIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000799HoIAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000799JPIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000799T3IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000799ckIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000799fxIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000799srIAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000799w5IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt0000079A0wIAE', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000079A2aIAE', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000079A49IAE', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000079AU1IAM', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000079AgrIAE', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000079AqXIAU', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000079As9IAE', 'Product2Id': '01tWt000006hV8LIAU'}]}

exec(code, env_args)
