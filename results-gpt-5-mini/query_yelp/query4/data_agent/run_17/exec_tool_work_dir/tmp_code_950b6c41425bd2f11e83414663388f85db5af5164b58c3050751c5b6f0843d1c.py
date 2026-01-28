code = """import json
import pandas as pd

# read the businesses with attributes
with open(var_call_4ZVQL7q75WID6ALIOttgioOn, 'r', encoding='utf-8') as f:
    businesses = json.load(f)

# read reviews
with open(var_call_oedosZ32xU5OrmgRvz9Fd1bh, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

# DataFrames
b = pd.DataFrame(businesses)
# ensure columns
for c in ['business_id','attributes','categories','name']:
    if c not in b.columns:
        b[c] = None

# detect accepts credit
import re

def accepts_credit(attr):
    if attr is None:
        return False
    if isinstance(attr, dict):
        v = attr.get('BusinessAcceptsCreditCards')
        if isinstance(v, bool):
            return v
        if isinstance(v, str):
            return v.strip().lower() == 'true'
        return False
    if isinstance(attr, str):
        s = attr
        if 'BusinessAcceptsCreditCards' in s:
            if re.search(r"BusinessAcceptsCreditCards\W*True", s, re.I):
                return True
            if re.search(r"BusinessAcceptsCreditCards\W*False", s, re.I):
                return False
            return False
        return False
    return False

b['accepts_cc'] = b['attributes'].apply(accepts_credit)

# parse categories

def parse_cats(c):
    if c is None:
        return []
    if isinstance(c, list):
        return [str(x).strip() for x in c if x]
    if isinstance(c, str):
        parts = [p.strip() for p in c.split(',')]
        return [p for p in parts if p]
    return []

b['category_list'] = b['categories'].apply(parse_cats)

bcc = b[b['accepts_cc']==True]

rows = []
for _, r in bcc.iterrows():
    bid = r['business_id']
    cats = r['category_list']
    if not cats:
        rows.append({'business_id': bid, 'category': 'Unknown'})
    else:
        for c in cats:
            rows.append({'business_id': bid, 'category': c})

if rows:
    catdf = pd.DataFrame(rows)
else:
    catdf = pd.DataFrame(columns=['business_id','category'])

if catdf.empty:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    grp = catdf.groupby('category').agg(business_count=('business_id', pd.Series.nunique)).reset_index()
    grp = grp.sort_values(['business_count','category'], ascending=[False, True])
    top = grp.iloc[0]
    top_cat = top['category']
    top_count = int(top['business_count'])

    # process reviews
    r = pd.DataFrame(reviews)
    for c in ['business_ref','rating']:
        if c not in r.columns:
            r[c]=None
    r['business_id'] = r['business_ref'].astype(str).str.replace('businessref_','businessid_')
    r['rating_num'] = pd.to_numeric(r['rating'], errors='coerce')

    bizids = set(catdf[catdf['category']==top_cat]['business_id'].unique())
    relevant = r[r['business_id'].isin(bizids) & r['rating_num'].notna()]
    if relevant.empty:
        avg = None
    else:
        avg = round(float(relevant['rating_num'].mean()), 2)
    result = {'category': top_cat, 'business_count': top_count, 'average_rating': avg}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_JnLluO3On3Gk0xm04Vc0e2av': ['business', 'checkin'], 'var_call_tz5knKhzNxFLrxjC90GMIKSe': ['review', 'tip', 'user'], 'var_call_KL7fiKyfNIubTLwwzh6YGblR': 'file_storage/call_KL7fiKyfNIubTLwwzh6YGblR.json', 'var_call_oedosZ32xU5OrmgRvz9Fd1bh': 'file_storage/call_oedosZ32xU5OrmgRvz9Fd1bh.json', 'var_call_cg0TVm2r0MuG68ryqkWrbUWf': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64'}, {'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}, {'_id': '6859a000fe8b31cd7362e2b4', 'business_id': 'businessid_29'}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10'}, {'_id': '6859a000fe8b31cd7362e2b6', 'business_id': 'businessid_61'}, {'_id': '6859a000fe8b31cd7362e2b7', 'business_id': 'businessid_54'}, {'_id': '6859a000fe8b31cd7362e2b8', 'business_id': 'businessid_8'}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91'}, {'_id': '6859a000fe8b31cd7362e2bb', 'business_id': 'businessid_83'}, {'_id': '6859a000fe8b31cd7362e2bc', 'business_id': 'businessid_93'}, {'_id': '6859a000fe8b31cd7362e2be', 'business_id': 'businessid_24'}, {'_id': '6859a000fe8b31cd7362e2bf', 'business_id': 'businessid_95'}, {'_id': '6859a000fe8b31cd7362e2c1', 'business_id': 'businessid_26'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84'}, {'_id': '6859a000fe8b31cd7362e2c3', 'business_id': 'businessid_89'}, {'_id': '6859a000fe8b31cd7362e2c4', 'business_id': 'businessid_32'}, {'_id': '6859a000fe8b31cd7362e2c7', 'business_id': 'businessid_71'}, {'_id': '6859a000fe8b31cd7362e2c8', 'business_id': 'businessid_97'}, {'_id': '6859a000fe8b31cd7362e2c9', 'business_id': 'businessid_14'}, {'_id': '6859a000fe8b31cd7362e2ca', 'business_id': 'businessid_3'}, {'_id': '6859a000fe8b31cd7362e2ce', 'business_id': 'businessid_27'}, {'_id': '6859a000fe8b31cd7362e2cf', 'business_id': 'businessid_75'}, {'_id': '6859a000fe8b31cd7362e2d1', 'business_id': 'businessid_2'}, {'_id': '6859a000fe8b31cd7362e2d3', 'business_id': 'businessid_48'}, {'_id': '6859a000fe8b31cd7362e2d4', 'business_id': 'businessid_67'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76'}, {'_id': '6859a000fe8b31cd7362e2d8', 'business_id': 'businessid_100'}, {'_id': '6859a000fe8b31cd7362e2da', 'business_id': 'businessid_63'}, {'_id': '6859a000fe8b31cd7362e2db', 'business_id': 'businessid_45'}, {'_id': '6859a000fe8b31cd7362e2dc', 'business_id': 'businessid_68'}, {'_id': '6859a000fe8b31cd7362e2dd', 'business_id': 'businessid_6'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2e1', 'business_id': 'businessid_66'}, {'_id': '6859a000fe8b31cd7362e2e2', 'business_id': 'businessid_55'}, {'_id': '6859a000fe8b31cd7362e2e3', 'business_id': 'businessid_30'}, {'_id': '6859a000fe8b31cd7362e2e5', 'business_id': 'businessid_15'}, {'_id': '6859a000fe8b31cd7362e2e6', 'business_id': 'businessid_96'}, {'_id': '6859a000fe8b31cd7362e2e7', 'business_id': 'businessid_11'}, {'_id': '6859a000fe8b31cd7362e2e8', 'business_id': 'businessid_73'}, {'_id': '6859a000fe8b31cd7362e2e9', 'business_id': 'businessid_4'}, {'_id': '6859a000fe8b31cd7362e2ea', 'business_id': 'businessid_77'}, {'_id': '6859a000fe8b31cd7362e2eb', 'business_id': 'businessid_18'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65'}, {'_id': '6859a000fe8b31cd7362e2ed', 'business_id': 'businessid_86'}, {'_id': '6859a000fe8b31cd7362e2ee', 'business_id': 'businessid_53'}, {'_id': '6859a000fe8b31cd7362e2ef', 'business_id': 'businessid_40'}, {'_id': '6859a000fe8b31cd7362e2f0', 'business_id': 'businessid_44'}, {'_id': '6859a000fe8b31cd7362e2f1', 'business_id': 'businessid_43'}, {'_id': '6859a000fe8b31cd7362e2f3', 'business_id': 'businessid_9'}, {'_id': '6859a000fe8b31cd7362e2f4', 'business_id': 'businessid_20'}, {'_id': '6859a000fe8b31cd7362e2f5', 'business_id': 'businessid_37'}, {'_id': '6859a000fe8b31cd7362e2f7', 'business_id': 'businessid_62'}, {'_id': '6859a000fe8b31cd7362e2f8', 'business_id': 'businessid_94'}, {'_id': '6859a000fe8b31cd7362e2fa', 'business_id': 'businessid_90'}, {'_id': '6859a000fe8b31cd7362e2fb', 'business_id': 'businessid_31'}, {'_id': '6859a000fe8b31cd7362e2fc', 'business_id': 'businessid_85'}, {'_id': '6859a000fe8b31cd7362e2fd', 'business_id': 'businessid_25'}, {'_id': '6859a000fe8b31cd7362e2fe', 'business_id': 'businessid_82'}, {'_id': '6859a000fe8b31cd7362e2ff', 'business_id': 'businessid_58'}, {'_id': '6859a000fe8b31cd7362e302', 'business_id': 'businessid_60'}, {'_id': '6859a000fe8b31cd7362e303', 'business_id': 'businessid_21'}, {'_id': '6859a000fe8b31cd7362e304', 'business_id': 'businessid_98'}, {'_id': '6859a000fe8b31cd7362e305', 'business_id': 'businessid_16'}, {'_id': '6859a000fe8b31cd7362e306', 'business_id': 'businessid_46'}, {'_id': '6859a000fe8b31cd7362e307', 'business_id': 'businessid_22'}, {'_id': '6859a000fe8b31cd7362e308', 'business_id': 'businessid_36'}, {'_id': '6859a000fe8b31cd7362e30b', 'business_id': 'businessid_38'}, {'_id': '6859a000fe8b31cd7362e30c', 'business_id': 'businessid_81'}, {'_id': '6859a000fe8b31cd7362e30d', 'business_id': 'businessid_13'}, {'_id': '6859a000fe8b31cd7362e30e', 'business_id': 'businessid_17'}], 'var_call_DjPGYI1h1LWCQdL8VCqPTO2J': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64'}, {'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}, {'_id': '6859a000fe8b31cd7362e2b4', 'business_id': 'businessid_29'}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10'}, {'_id': '6859a000fe8b31cd7362e2b6', 'business_id': 'businessid_61'}, {'_id': '6859a000fe8b31cd7362e2b7', 'business_id': 'businessid_54'}, {'_id': '6859a000fe8b31cd7362e2b8', 'business_id': 'businessid_8'}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91'}, {'_id': '6859a000fe8b31cd7362e2bb', 'business_id': 'businessid_83'}, {'_id': '6859a000fe8b31cd7362e2bc', 'business_id': 'businessid_93'}, {'_id': '6859a000fe8b31cd7362e2be', 'business_id': 'businessid_24'}, {'_id': '6859a000fe8b31cd7362e2bf', 'business_id': 'businessid_95'}, {'_id': '6859a000fe8b31cd7362e2c1', 'business_id': 'businessid_26'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84'}, {'_id': '6859a000fe8b31cd7362e2c3', 'business_id': 'businessid_89'}, {'_id': '6859a000fe8b31cd7362e2c4', 'business_id': 'businessid_32'}, {'_id': '6859a000fe8b31cd7362e2c7', 'business_id': 'businessid_71'}, {'_id': '6859a000fe8b31cd7362e2c8', 'business_id': 'businessid_97'}, {'_id': '6859a000fe8b31cd7362e2c9', 'business_id': 'businessid_14'}, {'_id': '6859a000fe8b31cd7362e2ca', 'business_id': 'businessid_3'}, {'_id': '6859a000fe8b31cd7362e2ce', 'business_id': 'businessid_27'}, {'_id': '6859a000fe8b31cd7362e2cf', 'business_id': 'businessid_75'}, {'_id': '6859a000fe8b31cd7362e2d1', 'business_id': 'businessid_2'}, {'_id': '6859a000fe8b31cd7362e2d3', 'business_id': 'businessid_48'}, {'_id': '6859a000fe8b31cd7362e2d4', 'business_id': 'businessid_67'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76'}, {'_id': '6859a000fe8b31cd7362e2d8', 'business_id': 'businessid_100'}, {'_id': '6859a000fe8b31cd7362e2da', 'business_id': 'businessid_63'}, {'_id': '6859a000fe8b31cd7362e2db', 'business_id': 'businessid_45'}, {'_id': '6859a000fe8b31cd7362e2dc', 'business_id': 'businessid_68'}, {'_id': '6859a000fe8b31cd7362e2dd', 'business_id': 'businessid_6'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2e1', 'business_id': 'businessid_66'}, {'_id': '6859a000fe8b31cd7362e2e2', 'business_id': 'businessid_55'}, {'_id': '6859a000fe8b31cd7362e2e3', 'business_id': 'businessid_30'}, {'_id': '6859a000fe8b31cd7362e2e5', 'business_id': 'businessid_15'}, {'_id': '6859a000fe8b31cd7362e2e6', 'business_id': 'businessid_96'}, {'_id': '6859a000fe8b31cd7362e2e7', 'business_id': 'businessid_11'}, {'_id': '6859a000fe8b31cd7362e2e8', 'business_id': 'businessid_73'}, {'_id': '6859a000fe8b31cd7362e2e9', 'business_id': 'businessid_4'}, {'_id': '6859a000fe8b31cd7362e2ea', 'business_id': 'businessid_77'}, {'_id': '6859a000fe8b31cd7362e2eb', 'business_id': 'businessid_18'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65'}, {'_id': '6859a000fe8b31cd7362e2ed', 'business_id': 'businessid_86'}, {'_id': '6859a000fe8b31cd7362e2ee', 'business_id': 'businessid_53'}, {'_id': '6859a000fe8b31cd7362e2ef', 'business_id': 'businessid_40'}, {'_id': '6859a000fe8b31cd7362e2f0', 'business_id': 'businessid_44'}, {'_id': '6859a000fe8b31cd7362e2f1', 'business_id': 'businessid_43'}, {'_id': '6859a000fe8b31cd7362e2f3', 'business_id': 'businessid_9'}, {'_id': '6859a000fe8b31cd7362e2f4', 'business_id': 'businessid_20'}, {'_id': '6859a000fe8b31cd7362e2f5', 'business_id': 'businessid_37'}, {'_id': '6859a000fe8b31cd7362e2f7', 'business_id': 'businessid_62'}, {'_id': '6859a000fe8b31cd7362e2f8', 'business_id': 'businessid_94'}, {'_id': '6859a000fe8b31cd7362e2fa', 'business_id': 'businessid_90'}, {'_id': '6859a000fe8b31cd7362e2fb', 'business_id': 'businessid_31'}, {'_id': '6859a000fe8b31cd7362e2fc', 'business_id': 'businessid_85'}, {'_id': '6859a000fe8b31cd7362e2fd', 'business_id': 'businessid_25'}, {'_id': '6859a000fe8b31cd7362e2fe', 'business_id': 'businessid_82'}, {'_id': '6859a000fe8b31cd7362e2ff', 'business_id': 'businessid_58'}, {'_id': '6859a000fe8b31cd7362e302', 'business_id': 'businessid_60'}, {'_id': '6859a000fe8b31cd7362e303', 'business_id': 'businessid_21'}, {'_id': '6859a000fe8b31cd7362e304', 'business_id': 'businessid_98'}, {'_id': '6859a000fe8b31cd7362e305', 'business_id': 'businessid_16'}, {'_id': '6859a000fe8b31cd7362e306', 'business_id': 'businessid_46'}, {'_id': '6859a000fe8b31cd7362e307', 'business_id': 'businessid_22'}, {'_id': '6859a000fe8b31cd7362e308', 'business_id': 'businessid_36'}, {'_id': '6859a000fe8b31cd7362e30b', 'business_id': 'businessid_38'}, {'_id': '6859a000fe8b31cd7362e30c', 'business_id': 'businessid_81'}, {'_id': '6859a000fe8b31cd7362e30d', 'business_id': 'businessid_13'}, {'_id': '6859a000fe8b31cd7362e30e', 'business_id': 'businessid_17'}], 'var_call_4ZVQL7q75WID6ALIOttgioOn': 'file_storage/call_4ZVQL7q75WID6ALIOttgioOn.json'}

exec(code, env_args)
