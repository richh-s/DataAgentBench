code = """# load summarized result and produce a concise JSON with just the total
import json
with open(var_call_xNqDgALckZoPveyIzvmob58j, 'r', encoding='utf-8') as f:
    data = json.load(f)
output = {'total_funding_disaster_started_2022': data.get('total_funding_disaster_started_2022', 0)}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_cI8eVt0Fkg4l6hxMsjm3hTmf': ['civic_docs'], 'var_call_wSFEHvsJf7lq3Z9DXUZQqQqP': ['Funding'], 'var_call_qCk3641LXIXN5enTFFze5lZV': 'file_storage/call_qCk3641LXIXN5enTFFze5lZV.json', 'var_call_Y9DOQHC3dDmseXvmGYGNgAg8': 'file_storage/call_Y9DOQHC3dDmseXvmGYGNgAg8.json', 'var_call_L2m8vqRYvrbcbG1cz2xQ1tD9': 'file_storage/call_L2m8vqRYvrbcbG1cz2xQ1tD9.json', 'var_call_xNqDgALckZoPveyIzvmob58j': 'file_storage/call_xNqDgALckZoPveyIzvmob58j.json'}

exec(code, env_args)
