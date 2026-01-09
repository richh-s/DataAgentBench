code = """import json
path = var_call_lQCE5ZVtUBOwMqBecJ1jBBLy
with open(path,'r',encoding='utf-8') as f:
    obj=json.load(f)
print('__RESULT__:')
print(json.dumps(obj['query']))"""

env_args = {'var_call_wlQQ57s4e1fd96riyNOnezMK': 'file_storage/call_wlQQ57s4e1fd96riyNOnezMK.json', 'var_call_lQCE5ZVtUBOwMqBecJ1jBBLy': 'file_storage/call_lQCE5ZVtUBOwMqBecJ1jBBLy.json'}

exec(code, env_args)
