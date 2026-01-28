code = """import json
with open(var_call_jZEL08NkDEmjwOrm2hls2Id8, 'r') as f:
    businesses = json.load(f)
# show first 30 descriptions and business_ids
out = []
for b in businesses[:30]:
    out.append({'business_id': b.get('business_id'), 'description': b.get('description')})
print('__RESULT__:')
import json
print(json.dumps(out))"""

env_args = {'var_call_jZEL08NkDEmjwOrm2hls2Id8': 'file_storage/call_jZEL08NkDEmjwOrm2hls2Id8.json', 'var_call_VHSQ4WPpBD7ghRgUueDxfic2': 'file_storage/call_VHSQ4WPpBD7ghRgUueDxfic2.json', 'var_call_5RpQqoTcTOoukUzuaAJIcCgW': {'state': None, 'total_reviews': 0, 'avg_review_rating': None, 'avg_business_rating': None}, 'var_call_bjGcfwAG1fa7paNezZrxJr6y': 'file_storage/call_bjGcfwAG1fa7paNezZrxJr6y.json', 'var_call_iQ9P3ePIhlt9yD0XaNEpH98V': {'state': None, 'total_reviews': 0, 'avg_review_rating': None, 'avg_business_average_rating': None}}

exec(code, env_args)
