code = """import pandas as pd
import json

order_item_ids_raw = json.loads(locals()['var_function-call-14427941967854933840']['results'][0])
order_item_ids = [item['Id'].replace('#', '').strip() for item in order_item_ids_raw]

# Construct the query for the support database
# Since it's PostgreSQL, need to use IN clause and wrap column names in double quotes
query_parts = [f"'{id}'" for id in order_item_ids]
query_string = f"SELECT createddate FROM \"Case\" WHERE orderitemid__c IN ({', '.join(query_parts)});"

print('__RESULT__:')
print(json.dumps(query_string))"""

env_args = {'var_function-call-14427941967854933840': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)
