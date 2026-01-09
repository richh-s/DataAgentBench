code = """import json, re
row = var_call_m42wM2aXUEZ1Iq7Qp7AjAdN7[0]
desc = row.get('description') or ''
# extract categories after 'featuring'
cat = None
m = re.search(r"featuring\s+([^,]+(?:,\s*[^,]+)*)\s*,\s*perfect", desc)
if m:
    cat = m.group(1).strip()
else:
    # fallback: take part after 'featuring'
    m2 = re.search(r"featuring\s+(.+)$", desc)
    if m2:
        cat = m2.group(1).strip().rstrip('.')
result = {
    "business_id": row.get('business_id'),
    "name": row.get('name'),
    "category": cat
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_lfSO9ooy278TVLNDyppwSnd0': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'review_cnt': '5'}], 'var_call_m42wM2aXUEZ1Iq7Qp7AjAdN7': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
