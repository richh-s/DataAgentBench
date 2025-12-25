code = """import json

clean_ids = locals()['var_function-call-4512183450764435327']

# Construct SQL IN clause
ids_str = "', '".join(clean_ids)
query = f"SELECT createddate FROM Case WHERE REPLACE(orderitemid__c, '#', '') IN ('{ids_str}')"

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-8128570514379634743': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-11721698262061313310': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-4512183450764435327': ['802Wt00000797awIAA', '802Wt00000794F2IAI', '802Wt00000798YdIAI', '802Wt000007968eIAA', '802Wt0000079B6gIAE', '802Wt0000079A2bIAE', '802Wt00000790zGIAQ', '802Wt00000796qFIAQ', '802Wt00000797z7IAA', '802Wt0000079ACGIA2', '802Wt0000079B0EIAU', '802Wt00000798okIAA', '802Wt00000798VPIAY', '802Wt00000799o1IAA', '802Wt00000796bfIAA', '802Wt0000079734IAA', '802Wt00000790mOIAQ', '802Wt00000797W5IAI', '802Wt0000078yuGIAQ']}

exec(code, env_args)
