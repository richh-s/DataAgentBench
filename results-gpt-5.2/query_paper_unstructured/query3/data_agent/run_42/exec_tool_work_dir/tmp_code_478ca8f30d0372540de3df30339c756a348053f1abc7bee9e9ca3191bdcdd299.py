code = """import json, pandas as pd
cit = var_call_X5guGuxvn60u6azLsw8ZjZnj
if isinstance(cit, str):
    with open(cit,'r',encoding='utf-8') as f:
        cit = json.load(f)

cit_df = pd.DataFrame(cit)
print('__RESULT__:')
print(json.dumps({'columns': list(cit_df.columns), 'n': int(len(cit_df))}))"""

env_args = {'var_call_C8YeM5aHfGFgYH9W6E8Ej9My': 'file_storage/call_C8YeM5aHfGFgYH9W6E8Ej9My.json', 'var_call_X5guGuxvn60u6azLsw8ZjZnj': 'file_storage/call_X5guGuxvn60u6azLsw8ZjZnj.json', 'var_call_TazPQB4GwKJHrqXcBRWhQXOt': [{'cid': '0', 'name': 'id', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '1'}, {'cid': '1', 'name': 'title', 'type': 'TEXT', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'citation_count', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'citation_year', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}]}

exec(code, env_args)
