code = """import json
from collections import Counter

with open(locals()['var_function-call-6182685443246566889'], 'r') as f:
    cases_data = json.load(f)

# Check non-empty orderitemid__c
oids = [c.get('orderitemid__c') for c in cases_data if c.get('orderitemid__c')]
print(f"Total cases with orderitemid: {len(oids)}")
print(f"Sample orderitemids: {oids[:5]}")

# Check my target IDs from previous step
order_items_data = locals()['var_function-call-6182685443246565004']
target_ids_raw = [item['Id'] for item in order_items_data]
print(f"Target OrderItem IDs (raw): {target_ids_raw}")

# Check for matches with looser logic (e.g. contains)
count = 0
for o in oids:
    for t in target_ids_raw:
        if t in o or o in t: # simplistic match
            count += 1
            break
print(f"Approximate matches found: {count}")"""

env_args = {'var_function-call-5668392397130027000': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-5668392397130026911': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-6182685443246565004': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-6182685443246566889': 'file_storage/function-call-6182685443246566889.json', 'var_function-call-4677988440214606885': {'January': 1, 'November': 2, 'September': 1, 'March': 1}, 'var_function-call-2583504869033761794': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}]}

exec(code, env_args)
