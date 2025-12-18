code = """import pandas as pd
opportunities = locals()['var_function-call-4002710651754569137']
df_opportunities = pd.DataFrame(opportunities)
opportunity_ids = df_opportunities['Id'].tolist()
print('__RESULT__:')
print(pd.Series(opportunity_ids).to_json())"""

env_args = {'var_function-call-14047255255173712402': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-5188543164553168510': [], 'var_function-call-4002710651754569137': [{'Id': '006Wt000007B0g2IAC', 'AccountId': '001Wt00000PGXrNIAX'}, {'Id': '006Wt000007B7TcIAK', 'AccountId': '001Wt00000PGXrNIAX'}]}

exec(code, env_args)
