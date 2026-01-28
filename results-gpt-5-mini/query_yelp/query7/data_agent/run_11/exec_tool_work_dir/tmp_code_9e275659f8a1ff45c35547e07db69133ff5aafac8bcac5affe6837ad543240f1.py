code = """import json
import pandas as pd

# Load tool results from storage variables
reviews = var_call_hDC0ciInAZpFuFr2mcpU2nuI
business_file = var_call_ooMcmBtwkcWJHwP8c2dMIWun

with open(business_file, 'r', encoding='utf-8') as f:
    businesses = json.load(f)

# DataFrames
df_rev = pd.DataFrame(reviews)
if not df_rev.empty:
    df_rev['review_count'] = df_rev['review_count'].astype(int)
    df_rev['business_id'] = df_rev['business_ref'].str.replace('businessref_', 'businessid_')
else:
    df_rev['business_id'] = []

df_bus = pd.DataFrame(businesses)
if 'description' not in df_bus.columns:
    df_bus['description'] = ''

# Merge
merged = pd.merge(df_rev, df_bus, on='business_id', how='left')

import re
from collections import defaultdict

def extract_categories(desc):
    if not isinstance(desc, str) or desc.strip() == '' or desc.lower() == 'none':
        return []
    desc = desc.replace('\n', ' ').strip()
    lower = desc.lower()
    # Common markers preceding category lists
    markers = [
        'offers a diverse range of services and products in the fields of',
        'offers a diverse range of services and products in the fields',
        'offers a diverse range of services and products in',
        'offers a diverse range of services in',
        'offers a range of services in',
        'offers a range of services, including',
        'offers a range of services and dining options, including',
        'offers a range of services and dining options',
        'offers a variety of services, including',
        'offers a delightful selection of',
        'offers a delightful array of options ranging from',
        'offers a delightful array of options',
        'this establishment offers',
        'this facility offers',
        'offers',
        'provides essential services in the categories of',
        'provides essential services in the categories',
        'provides essential services in',
        'provides a range of services in',
        'specializes in',
        'in the categories of',
        'in the category of',
        "in the category of '",
        'including',
        'offering'
    ]
    pos = -1
    marker_used = None
    for m in markers:
        p = lower.find(m)
        if p != -1:
            # choose the last occurring marker (more likely right before categories)
            if p > pos:
                pos = p
                marker_used = m
    if pos != -1:
        start = pos + len(marker_used)
        candidate = desc[start:]
    else:
        # fallback: try after last 'this establishment' or after last 'located at'
        p = lower.rfind('this establishment')
        if p!=-1:
            candidate = desc[p+len('this establishment'):]
        else:
            # fallback whole description
            candidate = desc
    # Split candidate into tokens by commas, semicolons, ' and ', ' & '
    parts = [t.strip() for t in re.split(',|;|\band\b|\&', candidate) if t.strip()]
    cleaned = []
    for t in parts:
        # remove leading connector words
        t2 = re.sub('^(offers|including|offering|the|a|this|provides|specializes in)\s+', '', t, flags=re.I)
        # remove trailing phrases like 'for all your ...' or location-like fragments
        t2 = re.sub('\s+for.*$', '', t2, flags=re.I)
        t2 = t2.strip(' \"\'')
        # skip if contains digits (likely an address)
        if re.search('\d', t2):
            continue
        if len(t2) < 2:
            continue
        # normalize spaces
        t2 = re.sub('\s+', ' ', t2).strip()
        cleaned.append(t2)
    # Deduplicate maintaining order
    seen = set()
    final = []
    for c in cleaned:
        cc = c.strip()
        if cc.lower() not in seen:
            seen.add(cc.lower())
            final.append(cc)
    return final

cat_counts = defaultdict(int)
for _, r in merged.iterrows():
    desc = r.get('description', '')
    cats = extract_categories(desc)
    cnt = int(r.get('review_count', 0) or 0)
    for c in cats:
        cat_counts[c] += cnt

items = sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)
top5 = items[:5]
result = []
for cat, cnt in top5:
    result.append({'category': cat, 'review_count': cnt})

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_D2kJ0Y9gE3yR8RliD60BLhuV': ['checkin', 'business'], 'var_call_FBGO4FivMrShNLULYWnaVrfB': ['review', 'tip', 'user'], 'var_call_bPBGrBk40upm3qZvV8dYbzzo': 'file_storage/call_bPBGrBk40upm3qZvV8dYbzzo.json', 'var_call_SwMEsOwMOr2TdxYrqiUUXsxF': [{'user_id': 'userid_746'}, {'user_id': 'userid_1109'}, {'user_id': 'userid_1950'}, {'user_id': 'userid_1316'}, {'user_id': 'userid_1182'}, {'user_id': 'userid_151'}, {'user_id': 'userid_1158'}, {'user_id': 'userid_508'}, {'user_id': 'userid_435'}, {'user_id': 'userid_958'}, {'user_id': 'userid_1879'}, {'user_id': 'userid_308'}, {'user_id': 'userid_1179'}, {'user_id': 'userid_324'}, {'user_id': 'userid_863'}, {'user_id': 'userid_100'}, {'user_id': 'userid_1333'}, {'user_id': 'userid_1636'}, {'user_id': 'userid_1850'}, {'user_id': 'userid_711'}, {'user_id': 'userid_729'}, {'user_id': 'userid_1505'}, {'user_id': 'userid_1315'}, {'user_id': 'userid_1708'}, {'user_id': 'userid_1661'}, {'user_id': 'userid_850'}, {'user_id': 'userid_1675'}, {'user_id': 'userid_227'}, {'user_id': 'userid_577'}, {'user_id': 'userid_257'}, {'user_id': 'userid_598'}, {'user_id': 'userid_847'}, {'user_id': 'userid_673'}, {'user_id': 'userid_1856'}, {'user_id': 'userid_384'}, {'user_id': 'userid_935'}, {'user_id': 'userid_210'}, {'user_id': 'userid_1101'}, {'user_id': 'userid_945'}, {'user_id': 'userid_842'}, {'user_id': 'userid_1351'}, {'user_id': 'userid_230'}, {'user_id': 'userid_593'}, {'user_id': 'userid_1431'}, {'user_id': 'userid_686'}, {'user_id': 'userid_527'}, {'user_id': 'userid_244'}, {'user_id': 'userid_393'}, {'user_id': 'userid_1178'}, {'user_id': 'userid_526'}, {'user_id': 'userid_90'}, {'user_id': 'userid_238'}, {'user_id': 'userid_1105'}], 'var_call_hDC0ciInAZpFuFr2mcpU2nuI': [{'business_ref': 'businessref_13', 'review_count': '1'}, {'business_ref': 'businessref_79', 'review_count': '1'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_6', 'review_count': '1'}, {'business_ref': 'businessref_15', 'review_count': '1'}, {'business_ref': 'businessref_33', 'review_count': '2'}, {'business_ref': 'businessref_36', 'review_count': '2'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_12', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_57', 'review_count': '2'}, {'business_ref': 'businessref_86', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '1'}, {'business_ref': 'businessref_37', 'review_count': '1'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_26', 'review_count': '1'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}, {'business_ref': 'businessref_45', 'review_count': '3'}, {'business_ref': 'businessref_96', 'review_count': '2'}, {'business_ref': 'businessref_98', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}], 'var_call_ooMcmBtwkcWJHwP8c2dMIWun': 'file_storage/call_ooMcmBtwkcWJHwP8c2dMIWun.json'}

exec(code, env_args)
