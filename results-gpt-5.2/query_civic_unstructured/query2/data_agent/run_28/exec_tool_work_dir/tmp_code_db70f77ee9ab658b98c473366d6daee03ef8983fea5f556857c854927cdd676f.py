code = """import json, re

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

print('__RESULT__:')
print(json.dumps({'ok': True}))"""

env_args = {'var_call_VcSoEbEV11tJzvrjgzmhULMm': ['Funding'], 'var_call_B0V2TRekCl6vrNeq0NVAjjNk': ['civic_docs'], 'var_call_zl52m9mn8D1cMBUR9ENZQ8n5': 'file_storage/call_zl52m9mn8D1cMBUR9ENZQ8n5.json', 'var_call_XVHE2S4YMwyqfgnXLhph61QL': 'file_storage/call_XVHE2S4YMwyqfgnXLhph61QL.json'}

exec(code, env_args)
