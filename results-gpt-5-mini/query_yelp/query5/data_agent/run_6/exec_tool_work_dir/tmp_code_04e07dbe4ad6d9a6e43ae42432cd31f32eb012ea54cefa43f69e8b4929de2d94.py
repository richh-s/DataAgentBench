code = """import json

# Load the avg ratings from the SQL query result
ratings = var_call_BTnpdoaRyaN0H6iVYM9yQOqK

# Ensure proper types
for r in ratings:
    r['avg_rating'] = float(r['avg_rating'])

# Compute overall average rating across these businesses
vals = [r['avg_rating'] for r in ratings]
overall_avg = sum(vals)/len(vals) if vals else None

result = {'state': 'PA', 'business_count': len(vals), 'average_rating': overall_avg}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_2WlZ388LhmZXZkp6DMJW9hWz': 'file_storage/call_2WlZ388LhmZXZkp6DMJW9hWz.json', 'var_call_TaOnEhAoB1Sb6u68swYExP0N': [{'business_id': 'businessid_64', 'business_ref': 'businessref_64', 'state': 'MO', 'wifi_value': "u'free'"}, {'business_id': 'businessid_54', 'business_ref': 'businessref_54', 'state': 'FL', 'wifi_value': "u'free'"}, {'business_id': 'businessid_91', 'business_ref': 'businessref_91', 'state': 'LA', 'wifi_value': "u'free'"}, {'business_id': 'businessid_93', 'business_ref': 'businessref_93', 'state': 'IL', 'wifi_value': "u'free'"}, {'business_id': 'businessid_26', 'business_ref': 'businessref_26', 'state': 'FL', 'wifi_value': "u'free'"}, {'business_id': 'businessid_89', 'business_ref': 'businessref_89', 'state': 'PA', 'wifi_value': "u'free'"}, {'business_id': 'businessid_97', 'business_ref': 'businessref_97', 'state': 'PA', 'wifi_value': "u'free'"}, {'business_id': 'businessid_67', 'business_ref': 'businessref_67', 'state': 'PA', 'wifi_value': "u'free'"}, {'business_id': 'businessid_51', 'business_ref': 'businessref_51', 'state': 'FL', 'wifi_value': "u'free'"}, {'business_id': 'businessid_6', 'business_ref': 'businessref_6', 'state': 'NV', 'wifi_value': "'free'"}, {'business_id': 'businessid_55', 'business_ref': 'businessref_55', 'state': 'FL', 'wifi_value': "u'free'"}, {'business_id': 'businessid_77', 'business_ref': 'businessref_77', 'state': 'PA', 'wifi_value': "u'free'"}, {'business_id': 'businessid_86', 'business_ref': 'businessref_86', 'state': 'PA', 'wifi_value': "u'free'"}, {'business_id': 'businessid_40', 'business_ref': 'businessref_40', 'state': 'PA', 'wifi_value': "u'free'"}, {'business_id': 'businessid_44', 'business_ref': 'businessref_44', 'state': 'PA', 'wifi_value': "u'free'"}, {'business_id': 'businessid_43', 'business_ref': 'businessref_43', 'state': 'IN', 'wifi_value': "'free'"}, {'business_id': 'businessid_20', 'business_ref': 'businessref_20', 'state': 'FL', 'wifi_value': "'free'"}, {'business_id': 'businessid_25', 'business_ref': 'businessref_25', 'state': 'ID', 'wifi_value': "u'free'"}, {'business_id': 'businessid_82', 'business_ref': 'businessref_82', 'state': 'PA', 'wifi_value': "u'free'"}, {'business_id': 'businessid_12', 'business_ref': 'businessref_12', 'state': 'AB', 'wifi_value': "u'paid'"}, {'business_id': 'businessid_16', 'business_ref': 'businessref_16', 'state': 'IN', 'wifi_value': "u'free'"}, {'business_id': 'businessid_46', 'business_ref': 'businessref_46', 'state': 'MO', 'wifi_value': "u'free'"}], 'var_call_2V0njM9lnd67gzYHotprUOno': {'top_state': 'PA', 'business_refs': ['businessref_89', 'businessref_97', 'businessref_67', 'businessref_77', 'businessref_86', 'businessref_40', 'businessref_44', 'businessref_82'], 'count': 8}, 'var_call_BTnpdoaRyaN0H6iVYM9yQOqK': [{'business_ref': 'businessref_67', 'avg_rating': '3.3260869565217392'}, {'business_ref': 'businessref_77', 'avg_rating': '2.5476190476190474'}, {'business_ref': 'businessref_86', 'avg_rating': '3.739130434782609'}, {'business_ref': 'businessref_97', 'avg_rating': '4.294117647058823'}, {'business_ref': 'businessref_44', 'avg_rating': '2.9285714285714284'}, {'business_ref': 'businessref_89', 'avg_rating': '3.04'}, {'business_ref': 'businessref_82', 'avg_rating': '4.309523809523809'}, {'business_ref': 'businessref_40', 'avg_rating': '4.476190476190476'}]}

exec(code, env_args)
