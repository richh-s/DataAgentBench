code = """import json

# Read the file from the query
file_path = locals()['var_functions.query_db:14']

with open(file_path, 'r') as f:
    all_cases = json.load(f)

# Get order item IDs for our product
order_items_result = locals()['var_functions.query_db:12']
order_item_ids = set([item['Id'] for item in order_items_result])

# Also create a set without the '#' prefix for matching
order_item_ids_clean = set([item.lstrip('#') for item in order_item_ids])
order_item_ids_normalized = {}
for item_id in order_item_ids:
    clean_id = item_id.lstrip('#')
    order_item_ids_normalized[clean_id] = item_id

# Filter cases that match our order items (handling the '#' corruption)
filtered_cases = []
for case in all_cases:
    case_order_item = case.get('orderitemid__c', '')
    if case_order_item:
        # Normalize the case's order item ID by removing leading '#'
        case_order_item_clean = case_order_item.lstrip('#')
        if case_order_item_clean in order_item_ids_normalized:
            filtered_cases.append(case)

# Count frequency of issue IDs
issue_counts = {}
for case in filtered_cases:
    issue_id = case.get('issueid__c')
    if issue_id:
        issue_counts[issue_id] = issue_counts.get(issue_id, 0) + 1

# Find the most frequent issue
most_frequent_issue = max(issue_counts.items(), key=lambda x: x[1]) if issue_counts else None

result = {
    'filtered_cases_count': len(filtered_cases),
    'issue_counts': issue_counts,
    'most_frequent_issue': most_frequent_issue[0] if most_frequent_issue else None,
    'most_frequent_issue_count': most_frequent_issue[1] if most_frequent_issue else 0
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'Id': '802Wt0000078wz5IAA', 'OrderId': '801Wt00000PHQuFIAX', 'Product2Id': '01tWt000006hV8LIAU', 'Quantity': '9.0', 'UnitPrice': '503.4905', 'PriceBookEntryId': '01uWt0000027P8cIAE'}, {'Id': '802Wt0000078xAAIAY', 'OrderId': '801Wt00000PGHg7IAH', 'Product2Id': '01tWt000006hV8LIAU', 'Quantity': '10.0', 'UnitPrice': '476.991', 'PriceBookEntryId': '01uWt0000027P8cIAE'}, {'Id': '802Wt0000078yXiIAI', 'OrderId': '#801Wt00000PGjNsIAL', 'Product2Id': '01tWt000006hV8LIAU', 'Quantity': '10.0', 'UnitPrice': '476.991', 'PriceBookEntryId': '01uWt0000027P8cIAE'}, {'Id': '#802Wt00000790WEIAY', 'OrderId': '801Wt00000PHLzNIAX', 'Product2Id': '01tWt000006hV8LIAU', 'Quantity': '12.0', 'UnitPrice': '476.991', 'PriceBookEntryId': '01uWt0000027P8cIAE'}, {'Id': '802Wt00000792gDIAQ', 'OrderId': '801Wt00000PGbDQIA1', 'Product2Id': '01tWt000006hV8LIAU', 'Quantity': '10.0', 'UnitPrice': '476.991', 'PriceBookEntryId': '01uWt0000027P8cIAE'}], 'var_functions.query_db:5': [{'Id': '802Wt0000078wz5IAA'}, {'Id': '802Wt0000078xAAIAY'}, {'Id': '802Wt0000078yXiIAI'}, {'Id': '#802Wt00000790WEIAY'}, {'Id': '802Wt00000792gDIAQ'}, {'Id': '802Wt00000792zTIAQ'}, {'Id': '#802Wt0000079315IAA'}, {'Id': '802Wt00000793sTIAQ'}, {'Id': '802Wt00000794F3IAI'}, {'Id': '802Wt00000794F4IAI'}, {'Id': '#802Wt00000794JmIAI'}, {'Id': '#802Wt00000794YFIAY'}, {'Id': '802Wt00000794YJIAY'}, {'Id': '802Wt000007959OIAQ'}, {'Id': '802Wt00000795akIAA'}, {'Id': '802Wt00000795ywIAA'}, {'Id': '802Wt000007962JIAQ'}, {'Id': '802Wt000007968hIAA'}, {'Id': '802Wt000007968iIAA'}, {'Id': '802Wt00000796F5IAI'}, {'Id': '#802Wt00000796N7IAI'}, {'Id': '802Wt00000796NAIAY'}, {'Id': '802Wt00000796RzIAI'}, {'Id': '802Wt00000796S0IAI'}, {'Id': '802Wt00000796S1IAI'}, {'Id': '802Wt00000796VDIAY'}, {'Id': '802Wt00000796YPIAY'}, {'Id': '802Wt00000796YQIAY'}, {'Id': '802Wt00000796a1IAA'}, {'Id': '802Wt00000796dFIAQ'}, {'Id': '#802Wt00000796dIIAQ'}, {'Id': '#802Wt00000796jiIAA'}, {'Id': '802Wt00000796myIAA'}, {'Id': '802Wt00000796oaIAA'}, {'Id': '802Wt00000796rlIAA'}, {'Id': '802Wt00000796tTIAQ'}, {'Id': '802Wt00000796v0IAA'}, {'Id': '802Wt00000796wbIAA'}, {'Id': '802Wt00000796wcIAA'}, {'Id': '802Wt00000797FxIAI'}, {'Id': '802Wt00000797MQIAY'}, {'Id': '#802Wt00000797O5IAI'}, {'Id': '#802Wt00000797axIAA'}, {'Id': '802Wt00000797e9IAA'}, {'Id': '802Wt00000797hNIAQ'}, {'Id': '802Wt00000797j0IAA'}, {'Id': '#802Wt00000797mDIAQ'}, {'Id': '802Wt00000797nsIAA'}, {'Id': '#802Wt00000797pSIAQ'}, {'Id': '802Wt00000797sfIAA'}, {'Id': '802Wt00000797z8IAA'}, {'Id': '802Wt000007982LIAQ'}, {'Id': '802Wt00000798IUIAY'}, {'Id': '802Wt00000798IVIAY'}, {'Id': '802Wt00000798NKIAY'}, {'Id': '#802Wt00000798S9IAI'}, {'Id': '#802Wt00000798nBIAQ'}, {'Id': '802Wt00000798rxIAA'}, {'Id': '802Wt00000798wpIAA'}, {'Id': '802Wt000007991dIAA'}, {'Id': '802Wt0000079987IAA'}, {'Id': '802Wt00000799EZIAY'}, {'Id': '802Wt00000799HoIAI'}, {'Id': '#802Wt00000799JPIAY'}, {'Id': '802Wt00000799T3IAI'}, {'Id': '802Wt00000799ckIAA'}, {'Id': '#802Wt00000799fxIAA'}, {'Id': '802Wt00000799srIAA'}, {'Id': '802Wt00000799w5IAA'}, {'Id': '#802Wt0000079A0wIAE'}, {'Id': '802Wt0000079A2aIAE'}, {'Id': '802Wt0000079A49IAE'}, {'Id': '802Wt0000079AU1IAM'}, {'Id': '802Wt0000079AgrIAE'}, {'Id': '802Wt0000079AqXIAU'}, {'Id': '802Wt0000079As9IAE'}], 'var_functions.query_db:8': [{'id': '500Wt00000DDU5iIAH', 'issueid__c': 'a03Wt00000JqzUHIAZ', 'orderitemid__c': '802Wt00000799EZIAY', 'createddate': '2023-10-15T09:15:47.000+0000'}, {'id': '#500Wt00000DDfYwIAL', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'orderitemid__c': '802Wt000007968iIAA', 'createddate': '2024-05-02T09:30:00.000+0000'}, {'id': '500Wt00000DDgLKIA1', 'issueid__c': 'a03Wt00000JqnHwIAJ', 'orderitemid__c': '802Wt00000799ckIAA', 'createddate': '2023-11-03T11:30:00.000+0000'}, {'id': '500Wt00000DDxSdIAL', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'orderitemid__c': '802Wt000007968iIAA', 'createddate': '2024-05-15T14:45:00.000+0000'}, {'id': '500Wt00000DDzqzIAD', 'issueid__c': 'a03Wt00000JqzR3IAJ', 'orderitemid__c': '802Wt00000794F3IAI', 'createddate': '2023-01-17T09:30:00.000+0000'}], 'var_functions.execute_python:10': 'a03Wt00000JqzSfIAJ', 'var_functions.query_db:12': [{'Id': '802Wt0000078wz5IAA'}, {'Id': '802Wt0000078xAAIAY'}, {'Id': '802Wt0000078yXiIAI'}, {'Id': '#802Wt00000790WEIAY'}, {'Id': '802Wt00000792gDIAQ'}, {'Id': '802Wt00000792zTIAQ'}, {'Id': '#802Wt0000079315IAA'}, {'Id': '802Wt00000793sTIAQ'}, {'Id': '802Wt00000794F3IAI'}, {'Id': '802Wt00000794F4IAI'}, {'Id': '#802Wt00000794JmIAI'}, {'Id': '#802Wt00000794YFIAY'}, {'Id': '802Wt00000794YJIAY'}, {'Id': '802Wt000007959OIAQ'}, {'Id': '802Wt00000795akIAA'}, {'Id': '802Wt00000795ywIAA'}, {'Id': '802Wt000007962JIAQ'}, {'Id': '802Wt000007968hIAA'}, {'Id': '802Wt000007968iIAA'}, {'Id': '802Wt00000796F5IAI'}, {'Id': '#802Wt00000796N7IAI'}, {'Id': '802Wt00000796NAIAY'}, {'Id': '802Wt00000796RzIAI'}, {'Id': '802Wt00000796S0IAI'}, {'Id': '802Wt00000796S1IAI'}, {'Id': '802Wt00000796VDIAY'}, {'Id': '802Wt00000796YPIAY'}, {'Id': '802Wt00000796YQIAY'}, {'Id': '802Wt00000796a1IAA'}, {'Id': '802Wt00000796dFIAQ'}, {'Id': '#802Wt00000796dIIAQ'}, {'Id': '#802Wt00000796jiIAA'}, {'Id': '802Wt00000796myIAA'}, {'Id': '802Wt00000796oaIAA'}, {'Id': '802Wt00000796rlIAA'}, {'Id': '802Wt00000796tTIAQ'}, {'Id': '802Wt00000796v0IAA'}, {'Id': '802Wt00000796wbIAA'}, {'Id': '802Wt00000796wcIAA'}, {'Id': '802Wt00000797FxIAI'}, {'Id': '802Wt00000797MQIAY'}, {'Id': '#802Wt00000797O5IAI'}, {'Id': '#802Wt00000797axIAA'}, {'Id': '802Wt00000797e9IAA'}, {'Id': '802Wt00000797hNIAQ'}, {'Id': '802Wt00000797j0IAA'}, {'Id': '#802Wt00000797mDIAQ'}, {'Id': '802Wt00000797nsIAA'}, {'Id': '#802Wt00000797pSIAQ'}, {'Id': '802Wt00000797sfIAA'}, {'Id': '802Wt00000797z8IAA'}, {'Id': '802Wt000007982LIAQ'}, {'Id': '802Wt00000798IUIAY'}, {'Id': '802Wt00000798IVIAY'}, {'Id': '802Wt00000798NKIAY'}, {'Id': '#802Wt00000798S9IAI'}, {'Id': '#802Wt00000798nBIAQ'}, {'Id': '802Wt00000798rxIAA'}, {'Id': '802Wt00000798wpIAA'}, {'Id': '802Wt000007991dIAA'}, {'Id': '802Wt0000079987IAA'}, {'Id': '802Wt00000799EZIAY'}, {'Id': '802Wt00000799HoIAI'}, {'Id': '#802Wt00000799JPIAY'}, {'Id': '802Wt00000799T3IAI'}, {'Id': '802Wt00000799ckIAA'}, {'Id': '#802Wt00000799fxIAA'}, {'Id': '802Wt00000799srIAA'}, {'Id': '802Wt00000799w5IAA'}, {'Id': '#802Wt0000079A0wIAE'}, {'Id': '802Wt0000079A2aIAE'}, {'Id': '802Wt0000079A49IAE'}, {'Id': '802Wt0000079AU1IAM'}, {'Id': '802Wt0000079AgrIAE'}, {'Id': '802Wt0000079AqXIAU'}, {'Id': '802Wt0000079As9IAE'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': ['802Wt0000078wz5IAA', '802Wt0000078xAAIAY', '802Wt0000078yXiIAI', '#802Wt00000790WEIAY', '802Wt00000792gDIAQ', '802Wt00000792zTIAQ', '#802Wt0000079315IAA', '802Wt00000793sTIAQ', '802Wt00000794F3IAI', '802Wt00000794F4IAI', '#802Wt00000794JmIAI', '#802Wt00000794YFIAY', '802Wt00000794YJIAY', '802Wt000007959OIAQ', '802Wt00000795akIAA', '802Wt00000795ywIAA', '802Wt000007962JIAQ', '802Wt000007968hIAA', '802Wt000007968iIAA', '802Wt00000796F5IAI', '#802Wt00000796N7IAI', '802Wt00000796NAIAY', '802Wt00000796RzIAI', '802Wt00000796S0IAI', '802Wt00000796S1IAI', '802Wt00000796VDIAY', '802Wt00000796YPIAY', '802Wt00000796YQIAY', '802Wt00000796a1IAA', '802Wt00000796dFIAQ', '#802Wt00000796dIIAQ', '#802Wt00000796jiIAA', '802Wt00000796myIAA', '802Wt00000796oaIAA', '802Wt00000796rlIAA', '802Wt00000796tTIAQ', '802Wt00000796v0IAA', '802Wt00000796wbIAA', '802Wt00000796wcIAA', '802Wt00000797FxIAI', '802Wt00000797MQIAY', '#802Wt00000797O5IAI', '#802Wt00000797axIAA', '802Wt00000797e9IAA', '802Wt00000797hNIAQ', '802Wt00000797j0IAA', '#802Wt00000797mDIAQ', '802Wt00000797nsIAA', '#802Wt00000797pSIAQ', '802Wt00000797sfIAA', '802Wt00000797z8IAA', '802Wt000007982LIAQ', '802Wt00000798IUIAY', '802Wt00000798IVIAY', '802Wt00000798NKIAY', '#802Wt00000798S9IAI', '#802Wt00000798nBIAQ', '802Wt00000798rxIAA', '802Wt00000798wpIAA', '802Wt000007991dIAA', '802Wt0000079987IAA', '802Wt00000799EZIAY', '802Wt00000799HoIAI', '#802Wt00000799JPIAY', '802Wt00000799T3IAI', '802Wt00000799ckIAA', '#802Wt00000799fxIAA', '802Wt00000799srIAA', '802Wt00000799w5IAA', '#802Wt0000079A0wIAE', '802Wt0000079A2aIAE', '802Wt0000079A49IAE', '802Wt0000079AU1IAM', '802Wt0000079AgrIAE', '802Wt0000079AqXIAU', '802Wt0000079As9IAE'], 'var_functions.execute_python:18': {'total_cases': 72, 'order_item_ids_count': 76, 'order_item_ids_sample': ['802Wt00000796S0IAI', '802Wt00000799w5IAA', '802Wt0000078xAAIAY', '802Wt00000794F4IAI', '802Wt00000796a1IAA']}}

exec(code, env_args)
