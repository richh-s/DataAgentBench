code = """import json, pandas as pd, ast

# load reviews 2018 distinct business_ref
reviews = pd.DataFrame(var_call_DiBv1XeiE5yrMJ1yueVPS37C)
review_ids = set(reviews['business_ref'].dropna().astype(str).tolist())

# load businesses with parking attributes from file
path = var_call_hZrZopHsoaPjfkw4tDUZqGje
with open(path, 'r') as f:
    businesses = json.load(f)

def has_parking(attrs):
    if not isinstance(attrs, dict):
        return False
    # BikeParking
    bp = attrs.get('BikeParking', None)
    bike_true = str(bp).strip().lower() == 'true'

    # BusinessParking can be dict, stringified dict, 'None', etc.
    bpar = attrs.get('BusinessParking', None)
    biz_true = False
    if isinstance(bpar, dict):
        biz_true = any(bool(v) for v in bpar.values())
    else:
        s = str(bpar)
        if s and s.lower() != 'none' and s.lower() != 'null':
            try:
                d = ast.literal_eval(s)
                if isinstance(d, dict):
                    biz_true = any(bool(v) for v in d.values())
            except Exception:
                biz_true = False
    return bike_true or biz_true

count = 0
for b in businesses:
    bid = b.get('business_id')
    if not bid:
        continue
    bref = 'businessref_' + str(bid).split('businessid_')[-1]
    if bref in review_ids and has_parking(b.get('attributes')):
        count += 1

result = json.dumps(count)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_DiBv1XeiE5yrMJ1yueVPS37C': [{'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}], 'var_call_DPQ5x16SzbnSXab80dcmhlEW': ['checkin', 'business'], 'var_call_hZrZopHsoaPjfkw4tDUZqGje': 'file_storage/call_hZrZopHsoaPjfkw4tDUZqGje.json'}

exec(code, env_args)
