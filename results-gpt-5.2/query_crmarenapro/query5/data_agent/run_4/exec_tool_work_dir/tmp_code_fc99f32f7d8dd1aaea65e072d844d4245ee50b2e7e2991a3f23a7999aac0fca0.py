code = """import json, pandas as pd

orderitems = pd.DataFrame(var_call_YMfXWqyIEt5UsIJyb4YfG5TL)
orderitems['Id_clean'] = orderitems['Id'].str.replace('#','', regex=False)
orderitem_ids = set(orderitems['Id_clean'].tolist())

# pull cases in window with orderitemid and issueid
cases = pd.DataFrame(var_call_vjJauLSlazM4C5RemFBZG0B4)
# var_call_vj... is aggregated already; need raw cases instead
print('__RESULT__:')
print(json.dumps({'need_raw_cases': True}))"""

env_args = {'var_call_XF8tL1ZuLtGMla49DqUFvNVM': [{'createddate': '2023-07-02T11:00:00.000+0000', 'id': '#500Wt00000DDDfwIAH', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'orderitemid__c': '802Wt00000797r4IAA'}, {'createddate': '2020-12-29T08:36:00.000+0000', 'id': '500Wt00000DDDtTIAX', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'createddate': '2023-09-30T11:30:00.000+0000', 'id': '500Wt00000DDNYoIAP', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'orderitemid__c': '802Wt00000792tiIAA'}, {'createddate': '2022-08-05T14:30:00.000+0000', 'id': '500Wt00000DDPIsIAP', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'orderitemid__c': '802Wt00000797r3IAA'}, {'createddate': '2020-09-01T10:30:00.000+0000', 'id': '500Wt00000DDPM6IAP', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'orderitemid__c': '802Wt00000797r5IAA'}], 'var_call_k9VZxnPV1JPuDrFlBfgjNHGn': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_call_YMfXWqyIEt5UsIJyb4YfG5TL': [{'Id': '802Wt0000078wz5IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000078xAAIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000078yXgIAI', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt0000078yXiIAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000078ypSIAQ', 'Product2Id': '#01tWt000006hV8LIAU'}], 'var_call_ShoVVuZ46duuZX9XvSI8omPZ': [{'issue_id': 'a03Wt00000JqnHwIAJ', 'case_count': '4'}, {'issue_id': 'a03Wt00000JqmX6IAJ', 'case_count': '2'}, {'issue_id': 'a03Wt00000JqhItIAJ', 'case_count': '1'}, {'issue_id': 'a03Wt00000JqvNUIAZ', 'case_count': '1'}, {'issue_id': 'a03Wt00000JqxtvIAB', 'case_count': '1'}, {'issue_id': 'a03Wt00000JqzPSIAZ', 'case_count': '1'}], 'var_call_vjJauLSlazM4C5RemFBZG0B4': [{'issue_id': 'a03Wt00000JqnHwIAJ', 'case_count': '4'}, {'issue_id': 'a03Wt00000JqmX6IAJ', 'case_count': '2'}, {'issue_id': 'a03Wt00000JqhItIAJ', 'case_count': '1'}, {'issue_id': 'a03Wt00000JqvNUIAZ', 'case_count': '1'}, {'issue_id': 'a03Wt00000JqxtvIAB', 'case_count': '1'}, {'issue_id': 'a03Wt00000JqzPSIAZ', 'case_count': '1'}]}

exec(code, env_args)
