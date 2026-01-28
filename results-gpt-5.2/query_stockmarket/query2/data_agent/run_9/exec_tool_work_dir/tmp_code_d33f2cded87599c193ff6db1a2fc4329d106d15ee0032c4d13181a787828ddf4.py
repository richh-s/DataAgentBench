code = """import json
out = {'a': 1, 'b': 2}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_a4jDHUOrnVwDbmbC1dsIe3Wg': ['stockinfo'], 'var_call_yGpAynzIoSqSe9wxFVL88TgL': 'file_storage/call_yGpAynzIoSqSe9wxFVL88TgL.json', 'var_call_v5GUXnTyPU6cpGhiSLYg0wi4': 'file_storage/call_v5GUXnTyPU6cpGhiSLYg0wi4.json'}

exec(code, env_args)
