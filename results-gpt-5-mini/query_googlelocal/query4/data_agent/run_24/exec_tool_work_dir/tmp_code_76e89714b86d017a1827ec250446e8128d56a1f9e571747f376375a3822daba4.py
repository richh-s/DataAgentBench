code = """import json
# var_call_qVNmWVC87ZDJLphicpjRQhvz and var_call_HT1N6fo7lkqwlpBOaUaIt9RE are available from previous tool calls
records = var_call_qVNmWVC87ZDJLphicpjRQhvz
biz = var_call_HT1N6fo7lkqwlpBOaUaIt9RE
# Build count map (ensure integers)
counts = {r['gmap_id']: int(r['high_reviews']) for r in records}
# Get top 3 by count
top3 = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:3]
# Map gmap_id to business name
name_map = {b['gmap_id']: b['name'] for b in biz}
output = []
for gid, cnt in top3:
    output.append({
        'name': name_map.get(gid, gid),
        'gmap_id': gid,
        'high_reviews': cnt
    })
result = json.dumps(output)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_qVNmWVC87ZDJLphicpjRQhvz': [{'gmap_id': 'gmap_20', 'high_reviews': '8'}, {'gmap_id': 'gmap_53', 'high_reviews': '7'}, {'gmap_id': 'gmap_40', 'high_reviews': '6'}, {'gmap_id': 'gmap_35', 'high_reviews': '6'}, {'gmap_id': 'gmap_72', 'high_reviews': '5'}, {'gmap_id': 'gmap_62', 'high_reviews': '5'}, {'gmap_id': 'gmap_46', 'high_reviews': '5'}, {'gmap_id': 'gmap_17', 'high_reviews': '4'}, {'gmap_id': 'gmap_69', 'high_reviews': '3'}, {'gmap_id': 'gmap_56', 'high_reviews': '3'}], 'var_call_HT1N6fo7lkqwlpBOaUaIt9RE': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
