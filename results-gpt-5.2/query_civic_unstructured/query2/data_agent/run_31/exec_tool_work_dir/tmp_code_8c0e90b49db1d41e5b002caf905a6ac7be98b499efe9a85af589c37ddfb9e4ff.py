code = """import json
src = var_call_eCYT6mwb8a9Kpa5X4KBBvjMo
if isinstance(src, str):
    docs = json.load(open(src, 'r', encoding='utf-8'))
else:
    docs = src

print('__RESULT__:')
print(json.dumps({'n_docs': len(docs), 'first_filename': docs[0].get('filename'), 'first_text_len': len(docs[0].get('text',''))}))"""

env_args = {'var_call_eCYT6mwb8a9Kpa5X4KBBvjMo': 'file_storage/call_eCYT6mwb8a9Kpa5X4KBBvjMo.json', 'var_call_wUAIQWHnhpnImBn34Zbk6oW2': 'file_storage/call_wUAIQWHnhpnImBn34Zbk6oW2.json'}

exec(code, env_args)
