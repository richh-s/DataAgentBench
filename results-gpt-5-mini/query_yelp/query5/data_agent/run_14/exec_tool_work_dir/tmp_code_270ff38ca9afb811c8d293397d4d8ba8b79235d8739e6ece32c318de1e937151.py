code = """import json
with open(var_call_aKmeMSOPHs2Xdn1V2kvfjWlK, 'r') as f:
    reviews = json.load(f)
# Convert ratings to ints and compute average per business and overall average for the businesses in PA
from collections import defaultdict
per_business = defaultdict(list)
for r in reviews:
    br = r['business_ref']
    try:
        rating = int(r['rating'])
    except:
        continue
    per_business[br].append(rating)
# Calculate average per business
avg_per_business = {br: sum(vals)/len(vals) for br,vals in per_business.items()}
# Now average across the businesses (mean of business averages)
businesses = sorted(avg_per_business.keys())
if businesses:
    avg_across_businesses = sum(avg_per_business[b] for b in businesses)/len(businesses)
else:
    avg_across_businesses = None
result = {'avg_per_business': avg_per_business, 'avg_across_businesses': avg_across_businesses}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_64XhkT1xjnWS5IJk13AjtdSC': ['checkin', 'business'], 'var_call_2mQZXksl33KcC0GbmzZKG5d3': 'file_storage/call_2mQZXksl33KcC0GbmzZKG5d3.json', 'var_call_GA2ZbbgiIX6go1wcdFD5Qkxf': {'count_wifi_businesses': 22, 'wifi_businesses': [{'business_id': 'businessid_64', 'business_ref': 'businessref_64', 'state': 'MO', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_54', 'business_ref': 'businessref_54', 'state': 'FL', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_91', 'business_ref': 'businessref_91', 'state': 'LA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_93', 'business_ref': 'businessref_93', 'state': 'IL', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_26', 'business_ref': 'businessref_26', 'state': 'FL', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_89', 'business_ref': 'businessref_89', 'state': 'PA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_97', 'business_ref': 'businessref_97', 'state': 'PA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_67', 'business_ref': 'businessref_67', 'state': 'PA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_51', 'business_ref': 'businessref_51', 'state': 'FL', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_6', 'business_ref': 'businessref_6', 'state': 'NV', 'wifi_raw': "'free'"}, {'business_id': 'businessid_55', 'business_ref': 'businessref_55', 'state': 'FL', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_77', 'business_ref': 'businessref_77', 'state': 'PA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_86', 'business_ref': 'businessref_86', 'state': 'PA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_40', 'business_ref': 'businessref_40', 'state': 'PA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_44', 'business_ref': 'businessref_44', 'state': 'PA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_43', 'business_ref': 'businessref_43', 'state': 'IN', 'wifi_raw': "'free'"}, {'business_id': 'businessid_20', 'business_ref': 'businessref_20', 'state': 'FL', 'wifi_raw': "'free'"}, {'business_id': 'businessid_25', 'business_ref': 'businessref_25', 'state': 'ID', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_82', 'business_ref': 'businessref_82', 'state': 'PA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_12', 'business_ref': 'businessref_12', 'state': 'AB', 'wifi_raw': "u'paid'"}, {'business_id': 'businessid_16', 'business_ref': 'businessref_16', 'state': 'IN', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_46', 'business_ref': 'businessref_46', 'state': 'MO', 'wifi_raw': "u'free'"}]}, 'var_call_NgF2xHlIx0ZxpJJNSdKQ67m2': {'top_state': 'PA', 'count': 8, 'business_refs': ['businessref_89', 'businessref_97', 'businessref_67', 'businessref_77', 'businessref_86', 'businessref_40', 'businessref_44', 'businessref_82']}, 'var_call_KJ74v0k1zlYrOXfaUUNkm4En': ['review', 'tip', 'user'], 'var_call_aKmeMSOPHs2Xdn1V2kvfjWlK': 'file_storage/call_aKmeMSOPHs2Xdn1V2kvfjWlK.json'}

exec(code, env_args)
