code = """import pandas as pd
order_item_ids_raw = [item['Id'] for item in locals()['var_function-call-10806200677987939836']]
order_item_ids = [item.replace('#', '') for item in order_item_ids_raw]
print('__RESULT__:')
print(order_item_ids)"""

env_args = {'var_function-call-10806200677987939836': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)
