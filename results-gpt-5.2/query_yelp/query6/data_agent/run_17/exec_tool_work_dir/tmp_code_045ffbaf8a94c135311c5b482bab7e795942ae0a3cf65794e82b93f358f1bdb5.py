code = """import json, re
rec = var_call_FrIaBoDOJXSqNnXbKAlWTtPV[0]
desc = rec.get('description','')
# categories appear as a comma-separated list after 'featuring'
m = re.search(r'featuring\s+([^,]+(?:,\s*[^,]+)*)', desc, flags=re.IGNORECASE)
cat = None
if m:
    cats = [c.strip().rstrip('.') for c in m.group(1).split(',') if c.strip()]
    cat = cats[0] if cats else None
out = {
    'business_id': rec.get('business_id'),
    'name': rec.get('name'),
    'category': cat
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_LKDrWoK7rqK5ICeJ9I5fIHlM': [{'business_ref': 'businessref_9', 'avg_rating': '4.285714285714286', 'review_cnt': '7'}], 'var_call_FrIaBoDOJXSqNnXbKAlWTtPV': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
