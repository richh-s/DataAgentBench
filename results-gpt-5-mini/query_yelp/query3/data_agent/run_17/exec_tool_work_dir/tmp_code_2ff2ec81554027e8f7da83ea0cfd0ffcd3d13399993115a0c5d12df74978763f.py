code = """import json, ast
# Load business collection data (may be large)
with open(var_call_yq94tfmbSSKtjbOKLCWtF0to, 'r') as f:
    businesses = json.load(f)

# Load review business refs from 2018
review_refs = [d['business_ref'] for d in var_call_bSh5OQJmxIRs8Kq0mdTQtRJo]
review_bids = set(r.replace('businessref_', 'businessid_') for r in review_refs)

count = 0
matched = []
present_bids = set()
import re
for b in businesses:
    bid = b.get('business_id')
    if bid in review_bids:
        present_bids.add(bid)
        attrs = b.get('attributes') or {}
        has_bike = False
        has_bus = False
        # BikeParking check
        bp = attrs.get('BikeParking')
        if bp is not None:
            if isinstance(bp, bool):
                has_bike = bp
            else:
                s = str(bp)
                if 'true' in s.lower():
                    has_bike = True
        # BusinessParking check
        busp = attrs.get('BusinessParking')
        if busp is not None:
            if isinstance(busp, dict):
                for v in busp.values():
                    if v is True or (isinstance(v, str) and 'true' in v.lower()):
                        has_bus = True
                        break
            else:
                s = str(busp)
                # normalize unicode prefixes
                s = s.replace("u'", "'").replace('u"', '"')
                # try to literal_eval to dict
                try:
                    d = ast.literal_eval(s)
                    if isinstance(d, dict):
                        for v in d.values():
                            if v is True or (isinstance(v, str) and 'true' in v.lower()):
                                has_bus = True
                                break
                except Exception:
                    # fallback: look for 'true' or 'True' in string
                    if 'true' in s.lower():
                        has_bus = True
        if has_bike or has_bus:
            count += 1
            matched.append(bid)

missing = sorted(list(review_bids - present_bids))
result = {'count': count, 'matched_business_ids': sorted(matched), 'missing_business_ids_from_business_collection': missing}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_xGu3TbsbetmewRGsrvOEhHxY': ['business', 'checkin'], 'var_call_ggquAZZk0HIg8Js6o3twPwCe': ['review', 'tip', 'user'], 'var_call_yq94tfmbSSKtjbOKLCWtF0to': 'file_storage/call_yq94tfmbSSKtjbOKLCWtF0to.json', 'var_call_bSh5OQJmxIRs8Kq0mdTQtRJo': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}]}

exec(code, env_args)
