code = """import json
from pathlib import Path

rows = var_call_reFUsvQL7R9CK3Q1T4BDtsln
sym_data = json.loads(Path(var_call_mV5GgMaIkHOvl5GPQJwMAdy8).read_text())
name_map = sym_data['name_map']

names = [name_map.get(r['symbol'], r['symbol']) for r in rows]

print('__RESULT__:')
print(json.dumps(names))"""

env_args = {'var_call_TWmoaj5nxzkNWCttpzyMj9Oo': 'file_storage/call_TWmoaj5nxzkNWCttpzyMj9Oo.json', 'var_call_oIR00k72R1HbHiVAZ5Jsi8oa': 'file_storage/call_oIR00k72R1HbHiVAZ5Jsi8oa.json', 'var_call_7Pp9E0aiz2wVfAj9focr1xtx': 'file_storage/call_7Pp9E0aiz2wVfAj9focr1xtx.json', 'var_call_mV5GgMaIkHOvl5GPQJwMAdy8': 'file_storage/call_mV5GgMaIkHOvl5GPQJwMAdy8.json', 'var_call_reFUsvQL7R9CK3Q1T4BDtsln': [{'symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0', 'net_up': '42.0'}, {'symbol': 'MTD', 'up_days': '143.0', 'down_days': '108.0', 'net_up': '35.0'}, {'symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0', 'net_up': '31.0'}, {'symbol': 'KMB', 'up_days': '140.0', 'down_days': '111.0', 'net_up': '29.0'}, {'symbol': 'HRB', 'up_days': '135.0', 'down_days': '111.0', 'net_up': '24.0'}]}

exec(code, env_args)
