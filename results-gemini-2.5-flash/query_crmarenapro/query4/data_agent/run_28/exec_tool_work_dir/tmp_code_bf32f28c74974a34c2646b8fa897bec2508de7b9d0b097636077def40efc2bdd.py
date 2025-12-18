code = """import json
order_item_ids_raw = locals()['var_function-call-16377467498839735633']
order_item_ids = [item['Id'].replace('#', '') for item in order_item_ids_raw]
print('__RESULT__:')
print(json.dumps(order_item_ids))"""

env_args = {'var_function-call-362352720963237849': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-362352720963237218': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-1843966017507684069': [], 'var_function-call-7840849210289834778': [{'Id': '#01tWt000006hVJdIAM'}], 'var_function-call-16377467498839735633': [{'Id': '802Wt00000797awIAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B6gIAE'}]}

exec(code, env_args)
