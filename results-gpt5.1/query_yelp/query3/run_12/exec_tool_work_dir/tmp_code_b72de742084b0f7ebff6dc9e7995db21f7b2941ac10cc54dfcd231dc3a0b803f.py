code = """import json, pandas as pd, os

reviews_2018 = var_call_oauIL3MFSivS8ItMfqJYsPYj
# map businessref_X -> businessid_X
ids = [r['business_ref'].replace('businessref_', 'businessid_') for r in reviews_2018]
ids_set = set(ids)

# load full business attributes
path = var_call_nuIqgwuxg5WqsMfrqlmEHDvs
with open(path, 'r') as f:
    business = json.load(f)

count = 0
for b in business:
    bid = b.get('business_id')
    if bid not in ids_set:
        continue
    attrs = b.get('attributes')
    if not isinstance(attrs, dict):
        continue
    has_bike = attrs.get('BikeParking') == 'True'
    bp = attrs.get('BusinessParking')
    has_parking = False
    if isinstance(bp, str) and bp not in ('None', ''):
        try:
            d = eval(bp)
            if isinstance(d, dict) and any(d.values()):
                has_parking = True
        except Exception:
            pass
    if has_bike or has_parking:
        count += 1

result = json.dumps(count)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_0FqtAVCPv0jeDPiXlCKjJDlO': ['checkin', 'business'], 'var_call_oauIL3MFSivS8ItMfqJYsPYj': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}], 'var_call_nuIqgwuxg5WqsMfrqlmEHDvs': 'file_storage/call_nuIqgwuxg5WqsMfrqlmEHDvs.json'}

exec(code, env_args)
