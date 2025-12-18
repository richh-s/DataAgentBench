code = """import pandas as pd
import json

order_item_ids = json.loads(locals()['var_function-call-8876751307380815954'])['results']
cleaned_ids = [item['Id'].replace('#', '').strip() for item in order_item_ids]

# Prepare the list of IDs for the SQL query
ids_str = ', '.join([f"'{_id}'" for _id in cleaned_ids])

print("__RESULT__:")
print(json.dumps(ids_str))"""

env_args = {'var_function-call-8876751307380815954': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)
