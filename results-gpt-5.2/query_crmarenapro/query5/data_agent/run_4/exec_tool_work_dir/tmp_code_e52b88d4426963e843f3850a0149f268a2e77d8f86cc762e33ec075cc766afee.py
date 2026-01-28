code = """import json, pandas as pd

orderitems = pd.DataFrame(var_call_YMfXWqyIEt5UsIJyb4YfG5TL)
orderitems['orderitem_id'] = orderitems['Id'].str.replace('#','', regex=False)
orderitem_ids = set(orderitems['orderitem_id'].tolist())

cases = pd.DataFrame(var_call_Fwe0xxyLWdivXX5aDVAd8xse)
cases['orderitem_id_clean'] = cases['orderitem_id'].str.replace('#','', regex=False)
filtered = cases[cases['orderitem_id_clean'].isin(orderitem_ids)]

counts = (filtered.groupby('issue_id').size().sort_values(ascending=False))
issue_id = counts.index[0] if len(counts) else None

print('__RESULT__:')
print(json.dumps(issue_id))"""

env_args = {'var_call_XF8tL1ZuLtGMla49DqUFvNVM': [{'createddate': '2023-07-02T11:00:00.000+0000', 'id': '#500Wt00000DDDfwIAH', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'orderitemid__c': '802Wt00000797r4IAA'}, {'createddate': '2020-12-29T08:36:00.000+0000', 'id': '500Wt00000DDDtTIAX', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'createddate': '2023-09-30T11:30:00.000+0000', 'id': '500Wt00000DDNYoIAP', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'orderitemid__c': '802Wt00000792tiIAA'}, {'createddate': '2022-08-05T14:30:00.000+0000', 'id': '500Wt00000DDPIsIAP', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'orderitemid__c': '802Wt00000797r3IAA'}, {'createddate': '2020-09-01T10:30:00.000+0000', 'id': '500Wt00000DDPM6IAP', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'orderitemid__c': '802Wt00000797r5IAA'}], 'var_call_k9VZxnPV1JPuDrFlBfgjNHGn': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_call_YMfXWqyIEt5UsIJyb4YfG5TL': [{'Id': '802Wt0000078wz5IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000078xAAIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000078yXgIAI', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt0000078yXiIAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000078ypSIAQ', 'Product2Id': '#01tWt000006hV8LIAU'}], 'var_call_ShoVVuZ46duuZX9XvSI8omPZ': [{'issue_id': 'a03Wt00000JqnHwIAJ', 'case_count': '4'}, {'issue_id': 'a03Wt00000JqmX6IAJ', 'case_count': '2'}, {'issue_id': 'a03Wt00000JqhItIAJ', 'case_count': '1'}, {'issue_id': 'a03Wt00000JqvNUIAZ', 'case_count': '1'}, {'issue_id': 'a03Wt00000JqxtvIAB', 'case_count': '1'}, {'issue_id': 'a03Wt00000JqzPSIAZ', 'case_count': '1'}], 'var_call_vjJauLSlazM4C5RemFBZG0B4': [{'issue_id': 'a03Wt00000JqnHwIAJ', 'case_count': '4'}, {'issue_id': 'a03Wt00000JqmX6IAJ', 'case_count': '2'}, {'issue_id': 'a03Wt00000JqhItIAJ', 'case_count': '1'}, {'issue_id': 'a03Wt00000JqvNUIAZ', 'case_count': '1'}, {'issue_id': 'a03Wt00000JqxtvIAB', 'case_count': '1'}, {'issue_id': 'a03Wt00000JqzPSIAZ', 'case_count': '1'}], 'var_call_TY9YY5U7yVAEOGQGNn19sZXu': {'need_raw_cases': True}, 'var_call_Fwe0xxyLWdivXX5aDVAd8xse': [{'issue_id': 'a03Wt00000JqmX6IAJ', 'orderitem_id': '802Wt00000790mNIAQ'}, {'issue_id': 'a03Wt00000JqzPSIAZ', 'orderitem_id': '802Wt00000799mPIAQ'}, {'issue_id': 'a03Wt00000JqvNUIAZ', 'orderitem_id': '802Wt00000798K5IAI'}, {'issue_id': 'a03Wt00000JqhItIAJ', 'orderitem_id': '802Wt00000793bTIAQ'}, {'issue_id': 'a03Wt00000JqnHwIAJ', 'orderitem_id': '802Wt00000790WEIAY'}, {'issue_id': 'a03Wt00000JqnHwIAJ', 'orderitem_id': '802Wt00000790WEIAY'}, {'issue_id': 'a03Wt00000JqxtvIAB', 'orderitem_id': '802Wt000007928FIAQ'}, {'issue_id': 'a03Wt00000JqmX6IAJ', 'orderitem_id': '802Wt0000079A4AIAU'}, {'issue_id': 'a03Wt00000JqnHwIAJ', 'orderitem_id': '802Wt00000798olIAA'}, {'issue_id': 'a03Wt00000JqnHwIAJ', 'orderitem_id': '802Wt00000798olIAA'}]}

exec(code, env_args)
