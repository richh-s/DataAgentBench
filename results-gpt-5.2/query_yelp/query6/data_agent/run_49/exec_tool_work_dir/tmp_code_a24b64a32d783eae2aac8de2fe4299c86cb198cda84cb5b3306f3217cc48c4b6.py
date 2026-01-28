code = """import json, re
rec = var_call_wVWrgxkUNRlJZLiTdAsZ9ccI[0]
desc = rec.get('description') or ''
# extract categories after 'featuring'
cat = None
m = re.search(r'featuring\s+(.+?),\s*perfect for', desc, flags=re.IGNORECASE)
if m:
    cat = m.group(1).strip()
else:
    # fallback: take part after 'menu featuring'
    m2 = re.search(r'featuring\s+(.+?)(?:\.|$)', desc, flags=re.IGNORECASE)
    if m2:
        cat = m2.group(1).strip()
out = {
    'business_id':'businessid_9',
    'business_ref':'businessref_9',
    'name':rec.get('name'),
    'category':cat
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_4j6N5I2k8dmLYXZLxcFRx03O': [{'business_ref': 'businessref_9', 'avg_rating': '4.285714285714286', 'review_cnt': '7'}], 'var_call_wVWrgxkUNRlJZLiTdAsZ9ccI': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
