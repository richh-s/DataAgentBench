code = """import json
# load variables from previous query results
business_records = var_call_NHmCNDyLJbT6hXlrtwJyGxxB
review_aggs = var_call_FZU2mYmG5GIuCmlMeG7oQXPA

# build mapping from gmap_id to business name
name_map = {b['gmap_id']: b.get('name') for b in business_records}

results = []
for r in review_aggs:
    gid = r.get('gmap_id')
    try:
        avg = float(r.get('avg_rating'))
    except Exception:
        continue
    if avg >= 4.0 and gid in name_map:
        results.append({'name': name_map[gid], 'gmap_id': gid, 'avg_rating': round(avg, 2)})

# sort by avg_rating descending
results = sorted(results, key=lambda x: x['avg_rating'], reverse=True)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_0hPny6ZoxfpxIUVlIddxprRc': [], 'var_call_kAYmo9555LLOOEdFeW7dI77v': ['business_description'], 'var_call_NHmCNDyLJbT6hXlrtwJyGxxB': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage'}], 'var_call_FZU2mYmG5GIuCmlMeG7oQXPA': [{'gmap_id': 'gmap_20', 'avg_rating': '4.18', 'num_reviews': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.93', 'num_reviews': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.33', 'num_reviews': '6'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.88', 'num_reviews': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'num_reviews': '1'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.88', 'num_reviews': '8'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.13', 'num_reviews': '8'}]}

exec(code, env_args)
