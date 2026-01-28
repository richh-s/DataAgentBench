code = """import json
fp = var_call_v3rckjqRhhiiQmkMiPmwu2pg
with open(fp, 'r', encoding='utf-8') as f:
    recs = json.load(f)

# Convert ratings to ints and compute average
ratings = []
for r in recs:
    try:
        ratings.append(int(r['rating']))
    except:
        pass
avg = sum(ratings)/len(ratings) if ratings else None
out = {'num_review_rows': len(recs), 'num_ratings': len(ratings), 'avg_rating_all_reviews': avg}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ogAXyUAbzhdfA7wxn0QSesde': ['business', 'checkin'], 'var_call_GKBL2knORpUCjBgP3uUpLRSi': ['review', 'tip', 'user'], 'var_call_jMnTfOXhNhOpuKrxHpCUinQp': 'file_storage/call_jMnTfOXhNhOpuKrxHpCUinQp.json', 'var_call_ziEaYqeT6TC1A7rcoT0DSCoC': [{'business_id': 'businessid_64', 'business_ref': 'businessref_64', 'state': 'MO', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_54', 'business_ref': 'businessref_54', 'state': 'FL', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_91', 'business_ref': 'businessref_91', 'state': 'LA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_93', 'business_ref': 'businessref_93', 'state': 'IL', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_26', 'business_ref': 'businessref_26', 'state': 'FL', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_89', 'business_ref': 'businessref_89', 'state': 'PA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_97', 'business_ref': 'businessref_97', 'state': 'PA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_67', 'business_ref': 'businessref_67', 'state': 'PA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_51', 'business_ref': 'businessref_51', 'state': 'FL', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_6', 'business_ref': 'businessref_6', 'state': 'NV', 'wifi_raw': "'free'"}, {'business_id': 'businessid_55', 'business_ref': 'businessref_55', 'state': 'FL', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_77', 'business_ref': 'businessref_77', 'state': 'PA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_86', 'business_ref': 'businessref_86', 'state': 'PA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_40', 'business_ref': 'businessref_40', 'state': 'PA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_44', 'business_ref': 'businessref_44', 'state': 'PA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_43', 'business_ref': 'businessref_43', 'state': 'IN', 'wifi_raw': "'free'"}, {'business_id': 'businessid_20', 'business_ref': 'businessref_20', 'state': 'FL', 'wifi_raw': "'free'"}, {'business_id': 'businessid_25', 'business_ref': 'businessref_25', 'state': 'ID', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_82', 'business_ref': 'businessref_82', 'state': 'PA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_12', 'business_ref': 'businessref_12', 'state': 'AB', 'wifi_raw': "u'paid'"}, {'business_id': 'businessid_16', 'business_ref': 'businessref_16', 'state': 'IN', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_46', 'business_ref': 'businessref_46', 'state': 'MO', 'wifi_raw': "u'free'"}], 'var_call_OLsOHKIorWQvxndanMI0STcv': {'top_state': 'PA', 'count': 8, 'business_refs': ['businessref_89', 'businessref_97', 'businessref_67', 'businessref_77', 'businessref_86', 'businessref_40', 'businessref_44', 'businessref_82']}, 'var_call_v3rckjqRhhiiQmkMiPmwu2pg': 'file_storage/call_v3rckjqRhhiiQmkMiPmwu2pg.json'}

exec(code, env_args)
