code = """import json
etf_path = var_call_UpHwLqrnxP6jMvmuilhtHEYp
tables_path = var_call_HViMBQGu5fIjjUvgP8uMwvKu
with open(etf_path, 'r') as f:
    etfs = json.load(f)
with open(tables_path, 'r') as f:
    tables = json.load(f)
symbols = [r['Symbol'] for r in etfs]
common = sorted([s for s in symbols if s in tables])
output = {'count': len(common), 'sample_first_50': common[:50]}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_UpHwLqrnxP6jMvmuilhtHEYp': 'file_storage/call_UpHwLqrnxP6jMvmuilhtHEYp.json', 'var_call_HViMBQGu5fIjjUvgP8uMwvKu': 'file_storage/call_HViMBQGu5fIjjUvgP8uMwvKu.json'}

exec(code, env_args)
