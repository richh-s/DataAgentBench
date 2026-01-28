code = """import json, re
complete_pat = re.compile(r'(?:construction\s+was\s+completed|complete\s+construction|completed)\b', re.IGNORECASE)
print('__RESULT__:')
print(json.dumps({'compiled': True, 'pattern': complete_pat.pattern}))"""

env_args = {'var_call_eCYT6mwb8a9Kpa5X4KBBvjMo': 'file_storage/call_eCYT6mwb8a9Kpa5X4KBBvjMo.json', 'var_call_wUAIQWHnhpnImBn34Zbk6oW2': 'file_storage/call_wUAIQWHnhpnImBn34Zbk6oW2.json', 'var_call_fwrAlLIXYuEkd3dLsbunT5gs': {'n_docs': 19, 'first_filename': 'malibucity_agenda_03222023-2060.txt', 'first_text_len': 9796}}

exec(code, env_args)
