code = """import pandas as pd

order_item_ids_raw = locals()['var_function-call-9991420336842160724']
order_item_ids = [item['Id'].replace("#", "").strip() for item in order_item_ids_raw]

# Construct the WHERE clause for the SQL query
ids_str = ", ".join(f"'{id_}'" for id_ in order_item_ids)

# Adjusting the date range for the past 10 months from 2021-04-10
# This means from 2020-06-10 to 2021-04-10 (exclusive for the upper bound)
query = f'''SELECT createddate FROM "Case" WHERE orderitemid__c IN ({ids_str}) AND createddate >= '2020-06-10' AND createddate < '2021-04-10';'''

print("__RESULT__:")
print(query)"""

env_args = {'var_function-call-9991420336842160724': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)
