code = """import json
from collections import defaultdict
path = var_call_bC8pABsUSjz4LtTsWdS3euDX
with open(path, 'r') as f:
    businesses = json.load(f)

cat_map = defaultdict(list)
for b in businesses:
    attrs = b.get('attributes') or {}
    if not isinstance(attrs, dict):
        continue
    bac = attrs.get('BusinessAcceptsCreditCards')
    if not (isinstance(bac, str) and bac.strip().lower() == 'true'):
        continue
    bid = b.get('business_id')
    if not bid:
        continue
    bref = bid.replace('businessid_','businessref_')
    cats = b.get('categories')
    if not cats:
        continue
    if isinstance(cats, list):
        items = cats
    else:
        items = [c.strip() for c in str(cats).split(',') if c.strip()]
    for c in items:
        cat_map[c].append(bref)

# deduplicate
cat_map = {k: sorted(list(set(v))) for k,v in cat_map.items()}
# find top category
top_cat = None
top_count = 0
for k,v in cat_map.items():
    if len(v) > top_count:
        top_count = len(v)
        top_cat = k

out = {'top_category': top_cat, 'count': top_count, 'business_refs': cat_map.get(top_cat, [])}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_o0m9KMh4DDuBhn2XVu2q6QDi': ['business', 'checkin'], 'var_call_lsdmMUuJCJNnxnXhv8E45hwq': ['review', 'tip', 'user'], 'var_call_bC8pABsUSjz4LtTsWdS3euDX': 'file_storage/call_bC8pABsUSjz4LtTsWdS3euDX.json', 'var_call_KrKrgIK7d0zousRvavha9ypB': {'business_refs': ['businessref_10', 'businessref_100', 'businessref_11', 'businessref_13', 'businessref_14', 'businessref_15', 'businessref_16', 'businessref_17', 'businessref_18', 'businessref_2', 'businessref_20', 'businessref_21', 'businessref_22', 'businessref_24', 'businessref_25', 'businessref_26', 'businessref_27', 'businessref_29', 'businessref_3', 'businessref_30', 'businessref_31', 'businessref_32', 'businessref_33', 'businessref_36', 'businessref_37', 'businessref_38', 'businessref_4', 'businessref_40', 'businessref_43', 'businessref_44', 'businessref_45', 'businessref_46', 'businessref_47', 'businessref_48', 'businessref_49', 'businessref_52', 'businessref_53', 'businessref_54', 'businessref_55', 'businessref_58', 'businessref_6', 'businessref_60', 'businessref_61', 'businessref_62', 'businessref_63', 'businessref_64', 'businessref_65', 'businessref_66', 'businessref_67', 'businessref_68', 'businessref_71', 'businessref_73', 'businessref_75', 'businessref_76', 'businessref_77', 'businessref_8', 'businessref_81', 'businessref_82', 'businessref_83', 'businessref_84', 'businessref_85', 'businessref_86', 'businessref_87', 'businessref_88', 'businessref_89', 'businessref_9', 'businessref_90', 'businessref_91', 'businessref_92', 'businessref_93', 'businessref_94', 'businessref_95', 'businessref_96', 'businessref_97', 'businessref_98'], 'category_to_business_refs': {}}, 'var_call_Dk0ET2yVFOnW8tU64FBYrvzr': [{'business_id': 'businessid_49'}, {'business_id': 'businessid_47'}, {'business_id': 'businessid_88'}, {'business_id': 'businessid_33'}, {'business_id': 'businessid_92'}, {'business_id': 'businessid_64'}, {'business_id': 'businessid_52'}, {'business_id': 'businessid_29'}, {'business_id': 'businessid_10'}, {'business_id': 'businessid_61'}, {'business_id': 'businessid_54'}, {'business_id': 'businessid_8'}, {'business_id': 'businessid_91'}, {'business_id': 'businessid_83'}, {'business_id': 'businessid_93'}, {'business_id': 'businessid_24'}, {'business_id': 'businessid_95'}, {'business_id': 'businessid_26'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_89'}, {'business_id': 'businessid_32'}, {'business_id': 'businessid_71'}, {'business_id': 'businessid_97'}, {'business_id': 'businessid_14'}, {'business_id': 'businessid_3'}, {'business_id': 'businessid_27'}, {'business_id': 'businessid_75'}, {'business_id': 'businessid_2'}, {'business_id': 'businessid_48'}, {'business_id': 'businessid_67'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_100'}, {'business_id': 'businessid_63'}, {'business_id': 'businessid_45'}, {'business_id': 'businessid_68'}, {'business_id': 'businessid_6'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_66'}, {'business_id': 'businessid_55'}, {'business_id': 'businessid_30'}, {'business_id': 'businessid_15'}, {'business_id': 'businessid_96'}, {'business_id': 'businessid_11'}, {'business_id': 'businessid_73'}, {'business_id': 'businessid_4'}, {'business_id': 'businessid_77'}, {'business_id': 'businessid_18'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_86'}, {'business_id': 'businessid_53'}, {'business_id': 'businessid_40'}, {'business_id': 'businessid_44'}, {'business_id': 'businessid_43'}, {'business_id': 'businessid_9'}, {'business_id': 'businessid_20'}, {'business_id': 'businessid_37'}, {'business_id': 'businessid_62'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_31'}, {'business_id': 'businessid_85'}, {'business_id': 'businessid_25'}, {'business_id': 'businessid_82'}, {'business_id': 'businessid_58'}, {'business_id': 'businessid_60'}, {'business_id': 'businessid_21'}, {'business_id': 'businessid_98'}, {'business_id': 'businessid_16'}, {'business_id': 'businessid_46'}, {'business_id': 'businessid_22'}, {'business_id': 'businessid_36'}, {'business_id': 'businessid_38'}, {'business_id': 'businessid_81'}, {'business_id': 'businessid_13'}, {'business_id': 'businessid_17'}]}

exec(code, env_args)
