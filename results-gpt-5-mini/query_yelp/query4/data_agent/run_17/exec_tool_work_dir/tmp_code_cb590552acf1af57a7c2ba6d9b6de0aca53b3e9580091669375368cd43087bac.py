code = """import json
import pandas as pd

with open(var_call_KL7fiKyfNIubTLwwzh6YGblR, 'r', encoding='utf-8') as f:
    businesses = json.load(f)
with open(var_call_oedosZ32xU5OrmgRvz9Fd1bh, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

# DataFrames
DfB = pd.DataFrame(businesses)
for col in ['business_id','attributes','categories','name']:
    if col not in DfB.columns:
        DfB[col] = None

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
            if re.search(r"BusinessAcceptsCreditCards\s*[:=]\s*['\"]?True['\"]?", s, re.I):
                return True
            if re.search(r"BusinessAcceptsCreditCards\s*[:=]\s*['\"]?False['\"]?", s, re.I):
                return False
            # if contains key and the word True
            if 'true' in s.lower():
                return True
            return False
        return False
    return False

DfB['accepts_cc'] = DfB['attributes'].apply(accepts_credit)

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

DfB['category_list'] = DfB['categories'].apply(parse_cats)

DfCC = DfB[DfB['accepts_cc']==True].copy()

rows = []
for _, r in DfCC.iterrows():
    bid = r.get('business_id')
    cats = r.get('category_list') or []
    if not cats:
        rows.append({'business_id': bid, 'category': 'Unknown'})
    else:
        for c in cats:
            rows.append({'business_id': bid, 'category': c})

if rows:
    DfCat = pd.DataFrame(rows)
else:
    DfCat = pd.DataFrame(columns=['business_id','category'])

if DfCat.empty:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    grp = DfCat.groupby('category').agg(business_count=('business_id', pd.Series.nunique)).reset_index()
    if grp.empty:
        result = {'category': None, 'business_count': 0, 'average_rating': None}
    else:
        max_count = int(grp['business_count'].max())
        candidates = grp[grp['business_count']==max_count].sort_values('category')
        top_row = candidates.iloc[0]
        top_category = top_row['category']
        top_count = int(top_row['business_count'])

        # process reviews
        DfR = pd.DataFrame(reviews)
        for col in ['business_ref','rating']:
            if col not in DfR.columns:
                DfR[col] = None
        DfR['business_id'] = DfR['business_ref'].astype(str).str.replace('businessref_','businessid_')
        DfR['rating_num'] = pd.to_numeric(DfR['rating'], errors='coerce')

        biz_in_top = set(DfCat[DfCat['category']==top_category]['business_id'].unique())
        relevant = DfR[DfR['business_id'].isin(biz_in_top) & DfR['rating_num'].notna()]
        if relevant.empty:
            avg = None
        else:
            avg = round(float(relevant['rating_num'].mean()), 2)
        result = {'category': top_category, 'business_count': top_count, 'average_rating': avg}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_JnLluO3On3Gk0xm04Vc0e2av': ['business', 'checkin'], 'var_call_tz5knKhzNxFLrxjC90GMIKSe': ['review', 'tip', 'user'], 'var_call_KL7fiKyfNIubTLwwzh6YGblR': 'file_storage/call_KL7fiKyfNIubTLwwzh6YGblR.json', 'var_call_oedosZ32xU5OrmgRvz9Fd1bh': 'file_storage/call_oedosZ32xU5OrmgRvz9Fd1bh.json'}

exec(code, env_args)
