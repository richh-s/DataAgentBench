code = """import json
biz_path = var_call_zenaF9gAgfmTXB50cZZX9sgh
with open(biz_path, 'r') as f:
    businesses = json.load(f)

# Analyze presence of 'categories' field and common keys
count_total = len(businesses)
count_with_categories = sum(1 for b in businesses if 'categories' in b and b.get('categories') not in (None, ''))
# collect sample businesses that accept credit cards
import ast

def parse_attributes(attr):
    if attr is None:
        return {}
    if isinstance(attr, dict):
        return attr
    if isinstance(attr, str):
        s = attr.strip()
        if s.lower() == 'none' or s == '':
            return {}
        try:
            parsed = ast.literal_eval(s)
            if isinstance(parsed, dict):
                return parsed
            else:
                return {}
        except Exception:
            return {}
    return {}

samples = []
for b in businesses:
    attrs = parse_attributes(b.get('attributes'))
    val = attrs.get('BusinessAcceptsCreditCards')
    accepts = False
    if isinstance(val, bool):
        accepts = val
    elif isinstance(val, str) and val.strip().lower() == 'true':
        accepts = True
    if accepts:
        samples.append({
            'business_id': b.get('business_id'),
            'name': b.get('name'),
            'categories': b.get('categories'),
            'attributes': b.get('attributes')
        })
        if len(samples) >= 10:
            break

out = {'total_businesses': count_total, 'with_categories_count': count_with_categories, 'sample_accepts_credit_cards': samples}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_0QTDBTRd8H2RpxhSyMvftFu1': ['checkin', 'business'], 'var_call_VJcMYyiV5SnGv91Ebp3eBv6h': ['review', 'tip', 'user'], 'var_call_zenaF9gAgfmTXB50cZZX9sgh': 'file_storage/call_zenaF9gAgfmTXB50cZZX9sgh.json', 'var_call_qlkHo3dF8SjDijFURBwJADSJ': 'file_storage/call_qlkHo3dF8SjDijFURBwJADSJ.json', 'var_call_nEII5g43LY0Blwe2Q4EG9evd': {'category': None, 'business_count': 0, 'average_rating': None}}

exec(code, env_args)
