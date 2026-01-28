code = """import json
# Access previous query results stored in variables
reviews = var_call_luccSrejt5jvcKkX5UMaUcda
businesses = var_call_oxP3bd8wdNLQXVVrnD3HcdyZ

# Convert review counts to int and build a mapping
count_map = {r['gmap_id']: int(r['high_count']) for r in reviews}
# Build mapping from gmap_id to business name
name_map = {b['gmap_id']: b['name'] for b in businesses}

# Combine into list of records with name and count for gmap_ids present in name_map
combined = []
for gid, cnt in count_map.items():
    name = name_map.get(gid)
    if name:
        combined.append({'gmap_id': gid, 'name': name, 'high_rating_review_count': cnt})

# Sort by count desc, then by name
combined_sorted = sorted(combined, key=lambda x: (-x['high_rating_review_count'], x['name']))
# Take top 3
top3 = combined_sorted[:3]

# Prepare JSON-serializable result
result = [{'name': r['name'], 'high_rating_review_count': r['high_rating_review_count']} for r in top3]

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_luccSrejt5jvcKkX5UMaUcda': [{'gmap_id': 'gmap_20', 'high_count': '8'}, {'gmap_id': 'gmap_53', 'high_count': '7'}, {'gmap_id': 'gmap_40', 'high_count': '6'}, {'gmap_id': 'gmap_35', 'high_count': '6'}, {'gmap_id': 'gmap_72', 'high_count': '5'}, {'gmap_id': 'gmap_62', 'high_count': '5'}, {'gmap_id': 'gmap_46', 'high_count': '5'}, {'gmap_id': 'gmap_17', 'high_count': '4'}, {'gmap_id': 'gmap_69', 'high_count': '3'}, {'gmap_id': 'gmap_56', 'high_count': '3'}], 'var_call_oxP3bd8wdNLQXVVrnD3HcdyZ': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_35', 'name': 'Encino Dermatology & Laser: Alex Khadavi MD'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
