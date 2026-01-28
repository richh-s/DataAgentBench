code = """import json
path = var_call_5I4DtjpcM4Fv7fjmRPlhswNj
with open(path, 'r') as f:
    data = json.load(f)
# Prepare small sample
sample = []
for i, rec in enumerate(data[:8]):
    sample.append({
        'rowid': rec.get('rowid'),
        'Patents_info': rec.get('Patents_info')[:200] if rec.get('Patents_info') else None,
        'cpc': rec.get('cpc'),
        'citation_count': len(rec.get('citation') or [])
    })
import json
print("__RESULT__:")
print(json.dumps(sample))"""

env_args = {'var_call_5I4DtjpcM4Fv7fjmRPlhswNj': 'file_storage/call_5I4DtjpcM4Fv7fjmRPlhswNj.json'}

exec(code, env_args)
