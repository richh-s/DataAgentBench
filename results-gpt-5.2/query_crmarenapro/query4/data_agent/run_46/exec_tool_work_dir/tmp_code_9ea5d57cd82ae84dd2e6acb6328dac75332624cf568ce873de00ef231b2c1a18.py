code = """import json
ids = [r['orderitem_id'] for r in var_call_jcFo6yqDN80gtmNXNvge7uPG]
# build SQL IN list
in_list = ','.join(["'"+i.replace("'","''")+"'" for i in ids])
query = f"""
SELECT date_trunc('month', createddate::timestamp) AS month_start, COUNT(*) AS case_count
FROM \"Case\"
WHERE createddate::date >= DATE '2020-06-10' AND createddate::date < DATE '2021-04-11'
  AND orderitemid__c IS NOT NULL
  AND REPLACE(TRIM(orderitemid__c), '#', '') IN ({in_list})
GROUP BY 1
ORDER BY 1;
"""
print('__RESULT__:')
print(json.dumps({'query': query}))"""

env_args = {'var_call_Ibe3S99tTPnmu2s6LdqzJftt': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_c8LRwg7NO0PfbWWYr6kXPrj0': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_call_ay3czsak9zJhSXvWgu3u1hDL': [{'cnt': '19'}], 'var_call_jcFo6yqDN80gtmNXNvge7uPG': [{'orderitem_id': '802Wt0000078yuGIAQ'}, {'orderitem_id': '802Wt00000790mOIAQ'}, {'orderitem_id': '802Wt00000790zGIAQ'}, {'orderitem_id': '802Wt00000794F2IAI'}, {'orderitem_id': '802Wt000007968eIAA'}, {'orderitem_id': '802Wt00000796bfIAA'}, {'orderitem_id': '802Wt00000796qFIAQ'}, {'orderitem_id': '802Wt0000079734IAA'}, {'orderitem_id': '802Wt00000797W5IAI'}, {'orderitem_id': '802Wt00000797awIAA'}, {'orderitem_id': '802Wt00000797z7IAA'}, {'orderitem_id': '802Wt00000798VPIAY'}, {'orderitem_id': '802Wt00000798YdIAI'}, {'orderitem_id': '802Wt00000798okIAA'}, {'orderitem_id': '802Wt00000799o1IAA'}, {'orderitem_id': '802Wt0000079A2bIAE'}, {'orderitem_id': '802Wt0000079ACGIA2'}, {'orderitem_id': '802Wt0000079B0EIAU'}, {'orderitem_id': '802Wt0000079B6gIAE'}]}

exec(code, env_args)
