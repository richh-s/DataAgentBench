code = """import json, re
row = var_call_07uWejPOBH30hYXDYQ9Lda4F[0]
biz = var_call_2MHaflrh3L7p2TzYXDtoArJi[0]
# Extract categories list from description after 'featuring'
desc = biz.get('description') or ''
cat = None
m = re.search(r"featuring\s+(.+?)(?:,\s*perfect|\.|$)", desc, flags=re.IGNORECASE)
if m:
    cat = m.group(1).strip()
result = {
    "business": biz.get('name'),
    "category": cat,
    "avg_rating": float(row['avg_rating']),
    "review_count_in_period": int(row['review_cnt']),
    "business_ref": row['business_ref']
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_07uWejPOBH30hYXDYQ9Lda4F': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'review_cnt': '5'}], 'var_call_2MHaflrh3L7p2TzYXDtoArJi': [{'name': 'Coffee House Too Cafe', 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
