code = """import pandas as pd

order_item_ids_raw = locals()['var_function-call-15292278472913030167']['results']
order_item_ids = [item['Id'].replace("#", "").strip() for item in order_item_ids_raw]

# Prepare the list of IDs for the SQL IN clause
order_item_ids_str = ", ".join([f"'{item}'" for item in order_item_ids])

query = f'''
SELECT createddate
FROM "Case"
WHERE orderitemid__c IN ({order_item_ids_str})
AND createddate >= '2020-06-10'
AND createddate <= '2021-04-10';
'''
print("__RESULT__:")
print(query)"""

env_args = {'var_function-call-15292278472913030167': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)
