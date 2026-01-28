code = """import json
all_tables = json.load(open(var_call_rL51DkgtzdOWrf1cILYO8Xv8))
candidates = ['SPY','IVV','VOO','VGT','QQQ','DIA','VOOG','VTI','IWM','GLD','GDX']
present = [s for s in candidates if s in all_tables]
print('__RESULT__:')
print(json.dumps(present))"""

env_args = {'var_call_pioxFm3HMNADNVHF9KBLRTjt': 'file_storage/call_pioxFm3HMNADNVHF9KBLRTjt.json', 'var_call_rL51DkgtzdOWrf1cILYO8Xv8': 'file_storage/call_rL51DkgtzdOWrf1cILYO8Xv8.json', 'var_call_q7gL9hCr9JspmaMEoJRADFkT': 'file_storage/call_q7gL9hCr9JspmaMEoJRADFkT.json'}

exec(code, env_args)
