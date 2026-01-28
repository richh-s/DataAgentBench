code = """import json
import re

# Get the OrderItem IDs for the product
order_items_data = var_functions.query_db:4
# This is a list of dictionaries with 'Id' key
order_item_ids = {item['Id'].strip() for item in order_items_data}

# Get the cases data
cases_data = var_functions.query_db:6

# Filter cases to only include those with orderitemid__c in our product's order items
filtered_cases = [case for case in cases_data if case.get('orderitemid__c') and case['orderitemid__c'].strip() in order_item_ids]

# Count occurrences of each issueid__c
issue_counts = {}
for case in filtered_cases:
    issue_id = case.get('issueid__c')
    if issue_id:
        issue_id = issue_id.strip()
        issue_counts[issue_id] = issue_counts.get(issue_id, 0) + 1

# Sort by count descending and get the most frequent issue
most_frequent_issues = sorted(issue_counts.items(), key=lambda x: x[1], reverse=True)

# Prepare result for printing
result_data = {
    'most_frequent_issues': most_frequent_issues[:5],  # Top 5 for debugging
    'total_filtered_cases': len(filtered_cases),
    'total_unique_issues': len(issue_counts)
}

# Print result
print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:4': [{'Id': '802Wt0000078wz5IAA'}, {'Id': '802Wt0000078xAAIAY'}, {'Id': '802Wt0000078yXiIAI'}, {'Id': '#802Wt00000790WEIAY'}, {'Id': '802Wt00000792gDIAQ'}, {'Id': '802Wt00000792zTIAQ'}, {'Id': '#802Wt0000079315IAA'}, {'Id': '802Wt00000793sTIAQ'}, {'Id': '802Wt00000794F3IAI'}, {'Id': '802Wt00000794F4IAI'}, {'Id': '#802Wt00000794JmIAI'}, {'Id': '#802Wt00000794YFIAY'}, {'Id': '802Wt00000794YJIAY'}, {'Id': '802Wt000007959OIAQ'}, {'Id': '802Wt00000795akIAA'}, {'Id': '802Wt00000795ywIAA'}, {'Id': '802Wt000007962JIAQ'}, {'Id': '802Wt000007968hIAA'}, {'Id': '802Wt000007968iIAA'}, {'Id': '802Wt00000796F5IAI'}, {'Id': '#802Wt00000796N7IAI'}, {'Id': '802Wt00000796NAIAY'}, {'Id': '802Wt00000796RzIAI'}, {'Id': '802Wt00000796S0IAI'}, {'Id': '802Wt00000796S1IAI'}, {'Id': '802Wt00000796VDIAY'}, {'Id': '802Wt00000796YPIAY'}, {'Id': '802Wt00000796YQIAY'}, {'Id': '802Wt00000796a1IAA'}, {'Id': '802Wt00000796dFIAQ'}, {'Id': '#802Wt00000796dIIAQ'}, {'Id': '#802Wt00000796jiIAA'}, {'Id': '802Wt00000796myIAA'}, {'Id': '802Wt00000796oaIAA'}, {'Id': '802Wt00000796rlIAA'}, {'Id': '802Wt00000796tTIAQ'}, {'Id': '802Wt00000796v0IAA'}, {'Id': '802Wt00000796wbIAA'}, {'Id': '802Wt00000796wcIAA'}, {'Id': '802Wt00000797FxIAI'}, {'Id': '802Wt00000797MQIAY'}, {'Id': '#802Wt00000797O5IAI'}, {'Id': '#802Wt00000797axIAA'}, {'Id': '802Wt00000797e9IAA'}, {'Id': '802Wt00000797hNIAQ'}, {'Id': '802Wt00000797j0IAA'}, {'Id': '#802Wt00000797mDIAQ'}, {'Id': '802Wt00000797nsIAA'}, {'Id': '#802Wt00000797pSIAQ'}, {'Id': '802Wt00000797sfIAA'}, {'Id': '802Wt00000797z8IAA'}, {'Id': '802Wt000007982LIAQ'}, {'Id': '802Wt00000798IUIAY'}, {'Id': '802Wt00000798IVIAY'}, {'Id': '802Wt00000798NKIAY'}, {'Id': '#802Wt00000798S9IAI'}, {'Id': '#802Wt00000798nBIAQ'}, {'Id': '802Wt00000798rxIAA'}, {'Id': '802Wt00000798wpIAA'}, {'Id': '802Wt000007991dIAA'}, {'Id': '802Wt0000079987IAA'}, {'Id': '802Wt00000799EZIAY'}, {'Id': '802Wt00000799HoIAI'}, {'Id': '#802Wt00000799JPIAY'}, {'Id': '802Wt00000799T3IAI'}, {'Id': '802Wt00000799ckIAA'}, {'Id': '#802Wt00000799fxIAA'}, {'Id': '802Wt00000799srIAA'}, {'Id': '802Wt00000799w5IAA'}, {'Id': '#802Wt0000079A0wIAE'}, {'Id': '802Wt0000079A2aIAE'}, {'Id': '802Wt0000079A49IAE'}, {'Id': '802Wt0000079AU1IAM'}, {'Id': '802Wt0000079AgrIAE'}, {'Id': '802Wt0000079AqXIAU'}, {'Id': '802Wt0000079As9IAE'}], 'var_functions.query_db:6': [{'issueid__c': 'a03Wt00000JqmX6IAJ', 'orderitemid__c': '802Wt00000790mNIAQ'}, {'issueid__c': 'a03Wt00000JqzPSIAZ', 'orderitemid__c': '802Wt00000799mPIAQ'}, {'issueid__c': 'a03Wt00000JqvNUIAZ', 'orderitemid__c': '802Wt00000798K5IAI'}, {'issueid__c': 'a03Wt00000JqhItIAJ', 'orderitemid__c': '802Wt00000793bTIAQ'}, {'issueid__c': 'a03Wt00000JqnHwIAJ', 'orderitemid__c': '802Wt00000790WEIAY'}, {'issueid__c': 'a03Wt00000JqnHwIAJ', 'orderitemid__c': '802Wt00000790WEIAY'}, {'issueid__c': 'a03Wt00000JqxtvIAB', 'orderitemid__c': '802Wt000007928FIAQ'}, {'issueid__c': 'a03Wt00000JqmX6IAJ', 'orderitemid__c': '802Wt0000079A4AIAU'}, {'issueid__c': 'a03Wt00000JqnHwIAJ', 'orderitemid__c': '802Wt00000798olIAA'}, {'issueid__c': 'a03Wt00000JqnHwIAJ', 'orderitemid__c': '802Wt00000798olIAA'}]}

exec(code, env_args)
