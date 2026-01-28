code = """import json

with open(var_call_NAqUUrEjnmpiDdYHYZai6POw, 'r') as f:
    businesses = json.load(f)

sample = []
for b in businesses[:10]:
    entry = {
        'business_id': b.get('business_id'),
        'keys': list(b.keys()),
        'attributes_keys': list((b.get('attributes') or {}).keys()),
        'description_present': 'description' in b,
        'description_sample': (b.get('description')[:200] if isinstance(b.get('description'), str) else None)
    }
    sample.append(entry)

out = {'total_business_records': len(businesses), 'sample': sample}
import json
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_D7CD2DQCTa8jHGewhSkVZids': ['business', 'checkin'], 'var_call_oegT4QrYcZ0vHVix0AWApWFP': ['review', 'tip', 'user'], 'var_call_NAqUUrEjnmpiDdYHYZai6POw': 'file_storage/call_NAqUUrEjnmpiDdYHYZai6POw.json', 'var_call_ew33PuycLWh81QohJv7XOYLK': 'file_storage/call_ew33PuycLWh81QohJv7XOYLK.json', 'var_call_pyDZEAtTowFcGE2c5OZb7cI1': {'top_category': None, 'business_count': 0, 'avg_rating': None}, 'var_call_CSSBZ4Gi40C0nw1sqga3RIgt': [], 'var_call_0AmL1oCMuh1kFU62LZB4SpND': []}

exec(code, env_args)
