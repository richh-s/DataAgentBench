code = """import json
# load the result file from previous execute_python
path = var_call_axVHWtR2B6vfCQTIIHYLeBLc
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
# data has 'pairs' and 'codes'
codes = sorted(set(data.get('codes',[])))
pairs = data.get('pairs',[])
# Prepare output
out = {'codes': codes, 'pairs': pairs}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_gsWxlXamH0bH8ljehePMHHM6': ['publicationinfo'], 'var_call_weqzvfBrnc60cyw9FtEWIR77': ['cpc_definition'], 'var_call_tjsA3rOynI5Mzn4kWRCLheXY': 'file_storage/call_tjsA3rOynI5Mzn4kWRCLheXY.json', 'var_call_uSj2XJbyd96rb50wTleyhl2b': 'file_storage/call_uSj2XJbyd96rb50wTleyhl2b.json', 'var_call_kYlzlUWo5eXA7pqnDn7VJWw3': {'pairs': [], 'codes': []}, 'var_call_axVHWtR2B6vfCQTIIHYLeBLc': 'file_storage/call_axVHWtR2B6vfCQTIIHYLeBLc.json'}

exec(code, env_args)
