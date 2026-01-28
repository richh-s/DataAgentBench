code = """import json
import pandas as pd

# Load results
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

merged = pd.merge(df_rev, df_bus, on='business_id', how='left')

import re
from collections import defaultdict

def extract_categories(desc):
    if not isinstance(desc, str) or desc.strip() == '' or desc.lower() == 'none':
        return []
    text = desc.replace('\n', ' ').strip()
    low = text.lower()
    # find likely start of categories by common phrases
    markers = ['offers a diverse range of services and products in the fields of',
               'offers a diverse range of services and products in',
               'offers a diverse range of services in',
               'offers a range of services in',
               'offers a range of services, including',
               'offers a range of services and dining options, including',
               'offers a variety of services, including',
               'offers a delightful selection of',
               'offers a delightful array of options',
               'this establishment offers',
               'this facility offers',
               'offers',
               'provides essential services in the categories of',
               'provides a range of services in',
               'specializes in',
               'in the categories of',
               'in the category of',
               'including',
               'offering']
    pos = -1
    marker = None
    for m in markers:
        p = low.find(m)
        if p != -1 and p > pos:
            pos = p
            marker = m
    if pos != -1:
        start = pos + len(marker)
        candidate = text[start:]
    else:
        # fallback: after last 'located at' or take whole
        p = low.rfind('located at')
        if p != -1:
            candidate = text[p+len('located at'):]
        else:
            candidate = text
    # split by commas, semicolons, ' and ', '&'
    parts = re.split(',|;| and | & ', candidate)
    cleaned = []
    for p in parts:
        t = p.strip()
        # remove leading common words
        t = re.sub('^(offers|including|offering|the|a|this|provides|specializes in)\s+', '', t, flags=re.I)
        # remove trailing explanatory fragments
        t = re.sub('\s+for.*$', '', t, flags=re.I)
        t = t.strip(' ."\'')
        if t == '':
            continue
        # skip things with digits (likely addresses)
        if re.search('\d', t):
            continue
        # limit length
        if len(t) > 100:
            continue
        cleaned.append(re.sub('\s+', ' ', t).strip())
    # deduplicate
    seen = set()
    out = []
    for c in cleaned:
        key = c.lower()
        if key not in seen:
            seen.add(key)
            out.append(c)
    return out

cat_counts = defaultdict(int)
for _, row in merged.iterrows():
    desc = row.get('description', '')
    cats = extract_categories(desc)
    cnt = int(row.get('review_count', 0) or 0)
    for c in cats:
        cat_counts[c] += cnt

items = sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)
result = [{'category': k, 'review_count': v} for k, v in items[:5]]

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_D2kJ0Y9gE3yR8RliD60BLhuV': ['checkin', 'business'], 'var_call_FBGO4FivMrShNLULYWnaVrfB': ['review', 'tip', 'user'], 'var_call_bPBGrBk40upm3qZvV8dYbzzo': 'file_storage/call_bPBGrBk40upm3qZvV8dYbzzo.json', 'var_call_SwMEsOwMOr2TdxYrqiUUXsxF': [{'user_id': 'userid_746'}, {'user_id': 'userid_1109'}, {'user_id': 'userid_1950'}, {'user_id': 'userid_1316'}, {'user_id': 'userid_1182'}, {'user_id': 'userid_151'}, {'user_id': 'userid_1158'}, {'user_id': 'userid_508'}, {'user_id': 'userid_435'}, {'user_id': 'userid_958'}, {'user_id': 'userid_1879'}, {'user_id': 'userid_308'}, {'user_id': 'userid_1179'}, {'user_id': 'userid_324'}, {'user_id': 'userid_863'}, {'user_id': 'userid_100'}, {'user_id': 'userid_1333'}, {'user_id': 'userid_1636'}, {'user_id': 'userid_1850'}, {'user_id': 'userid_711'}, {'user_id': 'userid_729'}, {'user_id': 'userid_1505'}, {'user_id': 'userid_1315'}, {'user_id': 'userid_1708'}, {'user_id': 'userid_1661'}, {'user_id': 'userid_850'}, {'user_id': 'userid_1675'}, {'user_id': 'userid_227'}, {'user_id': 'userid_577'}, {'user_id': 'userid_257'}, {'user_id': 'userid_598'}, {'user_id': 'userid_847'}, {'user_id': 'userid_673'}, {'user_id': 'userid_1856'}, {'user_id': 'userid_384'}, {'user_id': 'userid_935'}, {'user_id': 'userid_210'}, {'user_id': 'userid_1101'}, {'user_id': 'userid_945'}, {'user_id': 'userid_842'}, {'user_id': 'userid_1351'}, {'user_id': 'userid_230'}, {'user_id': 'userid_593'}, {'user_id': 'userid_1431'}, {'user_id': 'userid_686'}, {'user_id': 'userid_527'}, {'user_id': 'userid_244'}, {'user_id': 'userid_393'}, {'user_id': 'userid_1178'}, {'user_id': 'userid_526'}, {'user_id': 'userid_90'}, {'user_id': 'userid_238'}, {'user_id': 'userid_1105'}], 'var_call_hDC0ciInAZpFuFr2mcpU2nuI': [{'business_ref': 'businessref_13', 'review_count': '1'}, {'business_ref': 'businessref_79', 'review_count': '1'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_6', 'review_count': '1'}, {'business_ref': 'businessref_15', 'review_count': '1'}, {'business_ref': 'businessref_33', 'review_count': '2'}, {'business_ref': 'businessref_36', 'review_count': '2'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_12', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_57', 'review_count': '2'}, {'business_ref': 'businessref_86', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '1'}, {'business_ref': 'businessref_37', 'review_count': '1'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_26', 'review_count': '1'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}, {'business_ref': 'businessref_45', 'review_count': '3'}, {'business_ref': 'businessref_96', 'review_count': '2'}, {'business_ref': 'businessref_98', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}], 'var_call_ooMcmBtwkcWJHwP8c2dMIWun': 'file_storage/call_ooMcmBtwkcWJHwP8c2dMIWun.json'}

exec(code, env_args)
