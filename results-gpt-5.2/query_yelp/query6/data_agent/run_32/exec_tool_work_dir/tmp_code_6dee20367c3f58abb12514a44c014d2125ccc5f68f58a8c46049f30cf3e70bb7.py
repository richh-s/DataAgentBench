code = """import json, re
row = var_call_38xh2770YfbH7pfy0PDUriss[0]
desc = row.get('description') or ''
# extract categories after 'featuring'
m = re.search(r"featuring\s+(.+?)\s*,\s*perfect", desc, flags=re.IGNORECASE)
cat = None
if m:
    cat = m.group(1).strip()
else:
    # fallback: take text after 'menu' or 'offers'
    cat = None
out = {
    'business_id': row.get('business_id'),
    'name': row.get('name'),
    'category': cat,
    'avg_rating': float(var_call_QjRXNAK7tH0KxLUg6Rmb4ys5[0]['avg_rating']),
    'review_count_in_period': int(var_call_QjRXNAK7tH0KxLUg6Rmb4ys5[0]['review_ct'])
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_QjRXNAK7tH0KxLUg6Rmb4ys5': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'review_ct': '5'}], 'var_call_38xh2770YfbH7pfy0PDUriss': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
