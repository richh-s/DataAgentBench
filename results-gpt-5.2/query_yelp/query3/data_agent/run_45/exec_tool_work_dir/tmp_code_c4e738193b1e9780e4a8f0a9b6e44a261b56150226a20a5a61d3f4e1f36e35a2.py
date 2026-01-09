code = """import json, pandas as pd
from pathlib import Path

# reviews in 2018 (distinct businesses)
rev = pd.DataFrame(var_call_bsM9Y0P4hSR4aAYy1dJQchSd)
rev_ids = set(rev['business_ref'].astype(str))

# businesses with parking attrs (load full json file)
path = Path(var_call_GIrEm7osfhR43sjNXMzlnzMK)
with path.open('r', encoding='utf-8') as f:
    biz = json.load(f)
biz_df = pd.DataFrame(biz)

# map businessid_X -> businessref_X
biz_df['business_ref'] = biz_df['business_id'].astype(str).str.replace('businessid_', 'businessref_', regex=False)

# interpret whether offers business parking or bike parking

def truthy(v):
    if v is None:
        return False
    if isinstance(v, bool):
        return v
    s = str(v).strip().lower()
    if s in {'true','t','1','yes','y'}:
        return True
    if s in {'false','f','0','no','n','none','null','nan',''}:
        return False
    return True

bp = []
bike = []
for attrs in biz_df.get('attributes', pd.Series([None]*len(biz_df))):
    if not isinstance(attrs, dict):
        bp.append(False)
        bike.append(False)
        continue
    bp.append(truthy(attrs.get('BusinessParking')))
    bike.append(truthy(attrs.get('BikeParking')))

biz_df['has_business_parking'] = bp
biz_df['has_bike_parking'] = bike
biz_df['has_either'] = biz_df['has_business_parking'] | biz_df['has_bike_parking']

eligible = set(biz_df.loc[biz_df['has_either'], 'business_ref'].astype(str))
count = len(rev_ids & eligible)

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_call_bsM9Y0P4hSR4aAYy1dJQchSd': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}], 'var_call_GIrEm7osfhR43sjNXMzlnzMK': 'file_storage/call_GIrEm7osfhR43sjNXMzlnzMK.json'}

exec(code, env_args)
