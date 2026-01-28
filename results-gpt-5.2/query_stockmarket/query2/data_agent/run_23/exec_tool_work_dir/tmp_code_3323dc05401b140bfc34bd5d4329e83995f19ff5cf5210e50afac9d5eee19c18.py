code = """import json
print('__RESULT__:')
print(json.dumps({'note':'skip python build; will query per symbol'}))"""

env_args = {'var_call_L7ddSgvG4pwxWupzI6Jilkxd': 'file_storage/call_L7ddSgvG4pwxWupzI6Jilkxd.json', 'var_call_h8spSELnHicwBjN3VuyEck6c': 'file_storage/call_h8spSELnHicwBjN3VuyEck6c.json', 'var_call_wERm2QHfA2RBc64TBAhT7uxH': {'ok': True}, 'var_call_AWJg34e7rBqyftomAJ8IkUFQ': [{'name': 'AAAU'}], 'var_call_4mAtZaLzNVFHo1lAqNHCJ4kZ': [{'Symbol': 'AAAU'}, {'Symbol': 'AADR'}, {'Symbol': 'AAME'}, {'Symbol': 'AAWW'}, {'Symbol': 'AAXJ'}]}

exec(code, env_args)
