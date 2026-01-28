code = """import json
# var_call_D0nCvRBB0L6Qvs5tG4fvTRf7 and var_call_jJTBs6Cxr32wVWlKluxmo9tH are available from previous tool calls
reviews = var_call_D0nCvRBB0L6Qvs5tG4fvTRf7
businesses = var_call_jJTBs6Cxr32wVWlKluxmo9tH
# Convert review counts to int
for r in reviews:
    try:
        r['high_reviews'] = int(r['high_reviews'])
    except:
        r['high_reviews'] = int(r['high_reviews']) if isinstance(r['high_reviews'], str) and r['high_reviews'].isdigit() else r['high_reviews']
# Build dict for quick lookup of business names
biz_map = {b['gmap_id']: b['name'] for b in businesses}
# Prepare top 3 from reviews that we have names for
# Sort reviews by high_reviews desc
sorted_reviews = sorted(reviews, key=lambda x: x['high_reviews'], reverse=True)
result = []
count = 0
for r in sorted_reviews:
    gid = r['gmap_id']
    if gid in biz_map:
        result.append({'name': biz_map[gid], 'high_rating_review_count': r['high_reviews']})
        count += 1
        if count == 3:
            break
# Print in required format as JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_D0nCvRBB0L6Qvs5tG4fvTRf7': [{'gmap_id': 'gmap_20', 'high_reviews': '8'}, {'gmap_id': 'gmap_53', 'high_reviews': '7'}, {'gmap_id': 'gmap_40', 'high_reviews': '6'}, {'gmap_id': 'gmap_35', 'high_reviews': '6'}, {'gmap_id': 'gmap_72', 'high_reviews': '5'}, {'gmap_id': 'gmap_62', 'high_reviews': '5'}, {'gmap_id': 'gmap_46', 'high_reviews': '5'}, {'gmap_id': 'gmap_17', 'high_reviews': '4'}, {'gmap_id': 'gmap_69', 'high_reviews': '3'}, {'gmap_id': 'gmap_56', 'high_reviews': '3'}, {'gmap_id': 'gmap_2', 'high_reviews': '3'}, {'gmap_id': 'gmap_11', 'high_reviews': '3'}, {'gmap_id': 'gmap_7', 'high_reviews': '2'}, {'gmap_id': 'gmap_64', 'high_reviews': '2'}, {'gmap_id': 'gmap_59', 'high_reviews': '2'}, {'gmap_id': 'gmap_57', 'high_reviews': '2'}, {'gmap_id': 'gmap_5', 'high_reviews': '2'}, {'gmap_id': 'gmap_47', 'high_reviews': '2'}, {'gmap_id': 'gmap_3', 'high_reviews': '2'}, {'gmap_id': 'gmap_71', 'high_reviews': '1'}, {'gmap_id': 'gmap_65', 'high_reviews': '1'}, {'gmap_id': 'gmap_63', 'high_reviews': '1'}, {'gmap_id': 'gmap_58', 'high_reviews': '1'}, {'gmap_id': 'gmap_51', 'high_reviews': '1'}, {'gmap_id': 'gmap_34', 'high_reviews': '1'}, {'gmap_id': 'gmap_30', 'high_reviews': '1'}, {'gmap_id': 'gmap_29', 'high_reviews': '1'}, {'gmap_id': 'gmap_26', 'high_reviews': '1'}, {'gmap_id': 'gmap_16', 'high_reviews': '1'}, {'gmap_id': 'gmap_14', 'high_reviews': '1'}, {'gmap_id': 'gmap_13', 'high_reviews': '1'}], 'var_call_jJTBs6Cxr32wVWlKluxmo9tH': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
