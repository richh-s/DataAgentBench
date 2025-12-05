code = """import json
ids = [r['Id'].lstrip('#') for r in var_call_yAPP8N6dbIOwUcyiaj8R6AOy]
ids_list = "','".join(ids)
query = f"SELECT date_trunc('month', createddate)::date AS month_start, COUNT(*) AS case_count FROM \"Case\" WHERE orderitemid__c IN ('{ids_list}') AND createddate >= (DATE '2021-04-10' - INTERVAL '10 months') AND createddate < DATE '2021-04-10' GROUP BY month_start ORDER BY month_start;"
result = json.dumps(query)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_hCyFoZ9IS3tnyuANTc0RP9dU': [{'table_name': 'Case'}, {'table_name': 'knowledge__kav'}, {'table_name': 'issue__c'}, {'table_name': 'casehistory__c'}, {'table_name': 'emailmessage'}, {'table_name': 'livechattranscript'}], 'var_call_wN70IYFk0BbOt5xULER7yQP6': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_call_yAPP8N6dbIOwUcyiaj8R6AOy': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)
