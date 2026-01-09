code = """import json, re
row = var_call_kswwbNFBfACjTLQqgtS8ovbN[0]
biz = var_call_MK1EOpoqHJlkrSYWzY4Px62u[0]
desc = biz.get('description') or ''
# extract categories after 'featuring'
cat = None
m = re.search(r'featuring\s+(.+?),\s*perfect for', desc, flags=re.IGNORECASE)
if m:
    cat = m.group(1).strip()
result = {
    'business_id': biz['business_id'],
    'name': biz['name'],
    'category': cat,
    'avg_rating': float(row['avg_rating']),
    'review_count_in_period': int(row['review_cnt']),
    'period': '2016-01-01 to 2016-06-30'
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_kswwbNFBfACjTLQqgtS8ovbN': [{'business_ref': 'businessref_9', 'avg_rating': '4.545454545454546', 'review_cnt': '11'}], 'var_call_MK1EOpoqHJlkrSYWzY4Px62u': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
