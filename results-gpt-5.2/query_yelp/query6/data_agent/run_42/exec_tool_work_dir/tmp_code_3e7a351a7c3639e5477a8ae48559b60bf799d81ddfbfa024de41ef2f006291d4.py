code = """import json, re
row = var_call_Dkj5vWQd7GLlELYM7onp8Nmz[0]
desc = row.get('description','') or ''
# Extract categories after 'featuring'
cat_str = ''
m = re.search(r'featuring\s+([^,]+(?:,\s*[^,]+)*)\s*,\s*perfect', desc)
if m:
    cat_str = m.group(1)
else:
    # fallback: take between 'featuring' and 'perfect' if present
    m = re.search(r'featuring\s+(.*?)\s*perfect', desc)
    if m:
        cat_str = m.group(1)
# split categories
cats = [c.strip() for c in cat_str.split(',') if c.strip()]
result = {
    'business_id': row.get('business_id'),
    'name': row.get('name'),
    'categories': cats
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_zFDsOZYLJxXEfW9yI9UZaH9u': [{'business_ref': 'businessref_9', 'avg_rating': '4.285714285714286', 'review_cnt': '7'}], 'var_call_Dkj5vWQd7GLlELYM7onp8Nmz': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
