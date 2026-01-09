code = """import json, pandas as pd

# load review business_refs from duckdb result
review_refs = [r['business_ref'] for r in var_call_GHN6UPs3hzD61u68nZQVSuFS]
review_ids = set(ref.replace('businessref_','businessid_') for ref in review_refs)

# load businesses with parking attributes from mongo result file
path = var_call_1mjTp4izjaZc1jl0gKWWYwc8
with open(path, 'r') as f:
    biz_recs = json.load(f)

# Determine if business offers business parking (any True in parsed dict or string) or bike parking true
import ast

def truthy(val):
    if val is True: return True
    if isinstance(val, (int,float)) and val==1: return True
    if isinstance(val, str):
        return val.strip().lower() in {'true','1','yes','y'}
    return False

def has_business_parking(attr):
    if attr is None: return False
    v = attr.get('BusinessParking') if isinstance(attr, dict) else None
    if v is None:
        return False
    if isinstance(v, dict):
        return any(truthy(x) for x in v.values())
    if isinstance(v, str):
        s=v.strip()
        if s.lower()=='none':
            return False
        # try parse python dict-like strings
        try:
            parsed = ast.literal_eval(s.replace('u\'','\'').replace('u"','"'))
            if isinstance(parsed, dict):
                return any(truthy(x) for x in parsed.values())
        except Exception:
            pass
        # fallback: if string contains 'True'
        return 'true' in s.lower()
    return truthy(v)

def has_bike_parking(attr):
    if not isinstance(attr, dict):
        return False
    v = attr.get('BikeParking')
    return truthy(v)

parking_biz_ids=set()
for r in biz_recs:
    bid = r.get('business_id')
    attrs = r.get('attributes')
    if bid is None: continue
    if has_business_parking(attrs) or has_bike_parking(attrs):
        parking_biz_ids.add(bid)

answer = len(review_ids & parking_biz_ids)
print('__RESULT__:')
print(json.dumps({'count': answer}))"""

env_args = {'var_call_GHN6UPs3hzD61u68nZQVSuFS': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}], 'var_call_1mjTp4izjaZc1jl0gKWWYwc8': 'file_storage/call_1mjTp4izjaZc1jl0gKWWYwc8.json'}

exec(code, env_args)
