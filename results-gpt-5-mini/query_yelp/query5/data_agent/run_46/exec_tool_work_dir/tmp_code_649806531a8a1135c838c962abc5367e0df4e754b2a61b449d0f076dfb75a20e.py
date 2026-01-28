code = """import json
# var_call_Q9H20kVTfSdCLao8r4mq4Ehd contains the SQL query result as list of dicts
rows = var_call_Q9H20kVTfSdCLao8r4mq4Ehd
# map businessref_XX to businessid_XX
ratings = {}
for r in rows:
    bref = r['business_ref']
    # extract numeric id
    m = bref.replace('businessref_','')
    bid = 'businessid_' + m
    ratings[bid] = float(r['avg_rating'])

# business ids from previous python call
top_business_ids = var_call_HSqtIpLLoy43fl59N8DMLrh7
bids = top_business_ids['business_ids']
# compute average rating across these businesses weighted equally (average of business averages)
vals = [ratings[b] for b in bids if b in ratings]
if vals:
    avg_of_businesses = sum(vals)/len(vals)
else:
    avg_of_businesses = None

out = {
    'state': top_business_ids['top_state'],
    'business_with_wifi_count': top_business_ids['count'],
    'average_rating_for_those_businesses': avg_of_businesses,
    'per_business_avg_ratings': ratings
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_x07oAuhWTqZMIy5fdjuj9v1q': ['business', 'checkin'], 'var_call_qKmdSTOXMctGRxPO6QYPOUue': ['review', 'tip', 'user'], 'var_call_V6QpZLl9ysxbV2KLsfJ9j8CZ': 'file_storage/call_V6QpZLl9ysxbV2KLsfJ9j8CZ.json', 'var_call_lNKkfWJJX4LCo0BjC4JwWfAK': 'file_storage/call_lNKkfWJJX4LCo0BjC4JwWfAK.json', 'var_call_HSqtIpLLoy43fl59N8DMLrh7': {'top_state': 'PA', 'count': 8, 'business_ids': ['businessid_89', 'businessid_97', 'businessid_67', 'businessid_77', 'businessid_86', 'businessid_40', 'businessid_44', 'businessid_82']}, 'var_call_Q9H20kVTfSdCLao8r4mq4Ehd': [{'business_ref': 'businessref_44', 'avg_rating': '2.9285714285714284', 'review_count': '42'}, {'business_ref': 'businessref_67', 'avg_rating': '3.3260869565217392', 'review_count': '46'}, {'business_ref': 'businessref_89', 'avg_rating': '3.04', 'review_count': '25'}, {'business_ref': 'businessref_86', 'avg_rating': '3.739130434782609', 'review_count': '46'}, {'business_ref': 'businessref_97', 'avg_rating': '4.294117647058823', 'review_count': '17'}, {'business_ref': 'businessref_40', 'avg_rating': '4.476190476190476', 'review_count': '21'}, {'business_ref': 'businessref_82', 'avg_rating': '4.309523809523809', 'review_count': '42'}, {'business_ref': 'businessref_77', 'avg_rating': '2.5476190476190474', 'review_count': '42'}]}

exec(code, env_args)
