code = """import json
from collections import Counter

# Get the results from previous queries
cases_data = var_functions.query_db_2
order_items_data = var_functions.query_db_5

# Extract OrderItem IDs for the product
order_item_ids = set()
for item in order_items_data:
    order_item_id = item['Id']
    # Clean up the ID (remove leading # if present)
    clean_id = order_item_id.lstrip('#')
    order_item_ids.add(clean_id)
    # Also add the original with # for matching
    order_item_ids.add(order_item_id)

# Filter cases that match these OrderItem IDs and collect issue IDs
issue_ids = []
for case in cases_data:
    orderitem_id = case.get('orderitemid__c', '')
    if orderitem_id:
        # Clean up for matching
        clean_orderitem_id = orderitem_id.lstrip('#')
        if clean_orderitem_id in order_item_ids:
            issue_id = case.get('issueid__c')
            if issue_id:
                issue_ids.append(issue_id)

# Count occurrences of each issue ID
issue_counts = Counter(issue_ids)

# Find the most common issue ID
if issue_counts:
    most_common_issue_id = issue_counts.most_common(1)[0][0]
else:
    most_common_issue_id = None

# Print result in the required format
print('__RESULT__:')
print(json.dumps(most_common_issue_id))"""

env_args = {'var_functions.list_db:0': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_functions.query_db:2': [{'id': '#500Wt00000DDYpHIAX', 'orderitemid__c': '802Wt00000790mNIAQ', 'issueid__c': 'a03Wt00000JqmX6IAJ'}, {'id': '#500Wt00000DDZtKIAX', 'orderitemid__c': '802Wt00000799mPIAQ', 'issueid__c': 'a03Wt00000JqzPSIAZ'}, {'id': '500Wt00000DDfx8IAD', 'orderitemid__c': '802Wt00000798K5IAI', 'issueid__c': 'a03Wt00000JqvNUIAZ'}, {'id': '500Wt00000DDg20IAD', 'orderitemid__c': '802Wt00000793bTIAQ', 'issueid__c': 'a03Wt00000JqhItIAJ'}, {'id': '500Wt00000DDxScIAL', 'orderitemid__c': '802Wt00000790WEIAY', 'issueid__c': 'a03Wt00000JqnHwIAJ'}, {'id': '500Wt00000DDxduIAD', 'orderitemid__c': '802Wt00000790WEIAY', 'issueid__c': 'a03Wt00000JqnHwIAJ'}, {'id': '#500Wt00000DDyznIAD', 'orderitemid__c': '802Wt000007928FIAQ', 'issueid__c': 'a03Wt00000JqxtvIAB'}, {'id': '#500Wt00000DDzJ8IAL', 'orderitemid__c': '802Wt0000079A4AIAU', 'issueid__c': 'a03Wt00000JqmX6IAJ'}, {'id': '#500Wt00000DDzXeIAL', 'orderitemid__c': '802Wt00000798olIAA', 'issueid__c': 'a03Wt00000JqnHwIAJ'}, {'id': '500Wt00000DE0K1IAL', 'orderitemid__c': '802Wt00000798olIAA', 'issueid__c': 'a03Wt00000JqnHwIAJ'}], 'var_functions.query_db:5': [{'Id': '802Wt0000078wz5IAA'}, {'Id': '802Wt0000078xAAIAY'}, {'Id': '802Wt0000078yXiIAI'}, {'Id': '#802Wt00000790WEIAY'}, {'Id': '802Wt00000792gDIAQ'}, {'Id': '802Wt00000792zTIAQ'}, {'Id': '#802Wt0000079315IAA'}, {'Id': '802Wt00000793sTIAQ'}, {'Id': '802Wt00000794F3IAI'}, {'Id': '802Wt00000794F4IAI'}, {'Id': '#802Wt00000794JmIAI'}, {'Id': '#802Wt00000794YFIAY'}, {'Id': '802Wt00000794YJIAY'}, {'Id': '802Wt000007959OIAQ'}, {'Id': '802Wt00000795akIAA'}, {'Id': '802Wt00000795ywIAA'}, {'Id': '802Wt000007962JIAQ'}, {'Id': '802Wt000007968hIAA'}, {'Id': '802Wt000007968iIAA'}, {'Id': '802Wt00000796F5IAI'}, {'Id': '#802Wt00000796N7IAI'}, {'Id': '802Wt00000796NAIAY'}, {'Id': '802Wt00000796RzIAI'}, {'Id': '802Wt00000796S0IAI'}, {'Id': '802Wt00000796S1IAI'}, {'Id': '802Wt00000796VDIAY'}, {'Id': '802Wt00000796YPIAY'}, {'Id': '802Wt00000796YQIAY'}, {'Id': '802Wt00000796a1IAA'}, {'Id': '802Wt00000796dFIAQ'}, {'Id': '#802Wt00000796dIIAQ'}, {'Id': '#802Wt00000796jiIAA'}, {'Id': '802Wt00000796myIAA'}, {'Id': '802Wt00000796oaIAA'}, {'Id': '802Wt00000796rlIAA'}, {'Id': '802Wt00000796tTIAQ'}, {'Id': '802Wt00000796v0IAA'}, {'Id': '802Wt00000796wbIAA'}, {'Id': '802Wt00000796wcIAA'}, {'Id': '802Wt00000797FxIAI'}, {'Id': '802Wt00000797MQIAY'}, {'Id': '#802Wt00000797O5IAI'}, {'Id': '#802Wt00000797axIAA'}, {'Id': '802Wt00000797e9IAA'}, {'Id': '802Wt00000797hNIAQ'}, {'Id': '802Wt00000797j0IAA'}, {'Id': '#802Wt00000797mDIAQ'}, {'Id': '802Wt00000797nsIAA'}, {'Id': '#802Wt00000797pSIAQ'}, {'Id': '802Wt00000797sfIAA'}, {'Id': '802Wt00000797z8IAA'}, {'Id': '802Wt000007982LIAQ'}, {'Id': '802Wt00000798IUIAY'}, {'Id': '802Wt00000798IVIAY'}, {'Id': '802Wt00000798NKIAY'}, {'Id': '#802Wt00000798S9IAI'}, {'Id': '#802Wt00000798nBIAQ'}, {'Id': '802Wt00000798rxIAA'}, {'Id': '802Wt00000798wpIAA'}, {'Id': '802Wt000007991dIAA'}, {'Id': '802Wt0000079987IAA'}, {'Id': '802Wt00000799EZIAY'}, {'Id': '802Wt00000799HoIAI'}, {'Id': '#802Wt00000799JPIAY'}, {'Id': '802Wt00000799T3IAI'}, {'Id': '802Wt00000799ckIAA'}, {'Id': '#802Wt00000799fxIAA'}, {'Id': '802Wt00000799srIAA'}, {'Id': '802Wt00000799w5IAA'}, {'Id': '#802Wt0000079A0wIAE'}, {'Id': '802Wt0000079A2aIAE'}, {'Id': '802Wt0000079A49IAE'}, {'Id': '802Wt0000079AU1IAM'}, {'Id': '802Wt0000079AgrIAE'}, {'Id': '802Wt0000079AqXIAU'}, {'Id': '802Wt0000079As9IAE'}]}

exec(code, env_args)
