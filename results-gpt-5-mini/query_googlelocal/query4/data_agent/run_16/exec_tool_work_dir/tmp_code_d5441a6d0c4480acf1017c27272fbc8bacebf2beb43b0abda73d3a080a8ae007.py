code = """import json
# read the top3 result and business names
top3 = var_call_GU9DnH5gm3zeSWix1ob2fBw6
names = var_call_gfIamnAT4Z0bo2lhlWcd6QEh
# create mapping from gmap_id to name
name_map = {d['gmap_id']: d['name'] for d in names}
# attach names to top3
for rec in top3:
    rec['name'] = name_map.get(rec['gmap_id'], None)
# prepare final output list with name and count
final = [{'name': r['name'], 'high_rating_count': r['high_rating_count']} for r in top3]
print('__RESULT__:')
print(json.dumps(final))"""

env_args = {'var_call_H0L4Ia9iTMVchL4vCqUCubBR': [{'gmap_id': 'gmap_11', 'high_rating_count': '3'}, {'gmap_id': 'gmap_13', 'high_rating_count': '1'}, {'gmap_id': 'gmap_14', 'high_rating_count': '1'}, {'gmap_id': 'gmap_16', 'high_rating_count': '1'}, {'gmap_id': 'gmap_17', 'high_rating_count': '4'}, {'gmap_id': 'gmap_2', 'high_rating_count': '3'}, {'gmap_id': 'gmap_20', 'high_rating_count': '8'}, {'gmap_id': 'gmap_26', 'high_rating_count': '1'}, {'gmap_id': 'gmap_29', 'high_rating_count': '1'}, {'gmap_id': 'gmap_3', 'high_rating_count': '2'}, {'gmap_id': 'gmap_30', 'high_rating_count': '1'}, {'gmap_id': 'gmap_34', 'high_rating_count': '1'}, {'gmap_id': 'gmap_35', 'high_rating_count': '6'}, {'gmap_id': 'gmap_40', 'high_rating_count': '6'}, {'gmap_id': 'gmap_46', 'high_rating_count': '5'}, {'gmap_id': 'gmap_47', 'high_rating_count': '2'}, {'gmap_id': 'gmap_5', 'high_rating_count': '2'}, {'gmap_id': 'gmap_51', 'high_rating_count': '1'}, {'gmap_id': 'gmap_53', 'high_rating_count': '7'}, {'gmap_id': 'gmap_56', 'high_rating_count': '3'}, {'gmap_id': 'gmap_57', 'high_rating_count': '2'}, {'gmap_id': 'gmap_58', 'high_rating_count': '1'}, {'gmap_id': 'gmap_59', 'high_rating_count': '2'}, {'gmap_id': 'gmap_62', 'high_rating_count': '5'}, {'gmap_id': 'gmap_63', 'high_rating_count': '1'}, {'gmap_id': 'gmap_64', 'high_rating_count': '2'}, {'gmap_id': 'gmap_65', 'high_rating_count': '1'}, {'gmap_id': 'gmap_69', 'high_rating_count': '3'}, {'gmap_id': 'gmap_7', 'high_rating_count': '2'}, {'gmap_id': 'gmap_71', 'high_rating_count': '1'}, {'gmap_id': 'gmap_72', 'high_rating_count': '5'}], 'var_call_GU9DnH5gm3zeSWix1ob2fBw6': [{'gmap_id': 'gmap_20', 'high_rating_count': 8}, {'gmap_id': 'gmap_53', 'high_rating_count': 7}, {'gmap_id': 'gmap_35', 'high_rating_count': 6}], 'var_call_gfIamnAT4Z0bo2lhlWcd6QEh': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_35', 'name': 'Encino Dermatology & Laser: Alex Khadavi MD'}]}

exec(code, env_args)
