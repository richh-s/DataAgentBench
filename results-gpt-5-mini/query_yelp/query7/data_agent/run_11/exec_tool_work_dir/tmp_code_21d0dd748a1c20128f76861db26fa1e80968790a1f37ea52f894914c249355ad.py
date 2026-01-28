code = """import json
import pandas as pd

# Load tool results
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

# Category extraction without regex to avoid escape issues
markers = [
    'offers a diverse range of services and products in the fields of',
    'offers a diverse range of services and products in',
    'offers a diverse range of services in',
    'offers a range of services in',
    'offers a range of services, including',
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
    'offering'
]

def extract_categories(desc):
    if not isinstance(desc, str):
        return []
    txt = desc.replace('\n', ' ').strip()
    if not txt:
        return []
    low = txt.lower()
    pos = -1
    used = None
    for m in markers:
        p = low.find(m)
        if p != -1 and p > pos:
            pos = p
            used = m
    if pos != -1:
        start = pos + len(used)
        candidate = txt[start:]
    else:
        p = low.rfind('located at')
        if p != -1:
            candidate = txt[p+len('located at'):]
        else:
            candidate = txt
    # Normalize separators
    cand = candidate.replace('&', ',')
    cand = cand.replace(' and ', ',')
    cand = cand.replace(';', ',')
    cand = cand.replace('.', ',')
    parts = [p.strip() for p in cand.split(',') if p.strip()]
    cleaned = []
    lead_words = set(['offers', 'including', 'offering', 'the', 'a', 'this', 'provides', 'specializes in'])
    for p in parts:
        # remove leading word if present
        words = p.split()
        if not words:
            continue
        if words[0].lower() in lead_words:
            words = words[1:]
        t = ' '.join(words).strip()
        # remove trailing phrase starting with 'for'
        idx = t.lower().find(' for ')
        if idx != -1:
            t = t[:idx]
        # skip if contains digits
        if any(ch.isdigit() for ch in t):
            continue
        if len(t) < 2:
            continue
        if len(t) > 120:
            continue
        cleaned.append(' '.join(t.split()))
    # deduplicate preserving order
    seen = set()
    out = []
    for c in cleaned:
        key = c.lower()
        if key not in seen:
            seen.add(key)
            out.append(c)
    return out

from collections import defaultdict
cat_counts = defaultdict(int)
for _, row in merged.iterrows():
    desc = row.get('description', '')
    cnt = int(row.get('review_count', 0) or 0)
    cats = extract_categories(desc)
    for c in cats:
        cat_counts[c] += cnt

items = sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)
result = []
for k, v in items[:5]:
    result.append({'category': k, 'review_count': v})

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_D2kJ0Y9gE3yR8RliD60BLhuV': ['checkin', 'business'], 'var_call_FBGO4FivMrShNLULYWnaVrfB': ['review', 'tip', 'user'], 'var_call_bPBGrBk40upm3qZvV8dYbzzo': 'file_storage/call_bPBGrBk40upm3qZvV8dYbzzo.json', 'var_call_SwMEsOwMOr2TdxYrqiUUXsxF': [{'user_id': 'userid_746'}, {'user_id': 'userid_1109'}, {'user_id': 'userid_1950'}, {'user_id': 'userid_1316'}, {'user_id': 'userid_1182'}, {'user_id': 'userid_151'}, {'user_id': 'userid_1158'}, {'user_id': 'userid_508'}, {'user_id': 'userid_435'}, {'user_id': 'userid_958'}, {'user_id': 'userid_1879'}, {'user_id': 'userid_308'}, {'user_id': 'userid_1179'}, {'user_id': 'userid_324'}, {'user_id': 'userid_863'}, {'user_id': 'userid_100'}, {'user_id': 'userid_1333'}, {'user_id': 'userid_1636'}, {'user_id': 'userid_1850'}, {'user_id': 'userid_711'}, {'user_id': 'userid_729'}, {'user_id': 'userid_1505'}, {'user_id': 'userid_1315'}, {'user_id': 'userid_1708'}, {'user_id': 'userid_1661'}, {'user_id': 'userid_850'}, {'user_id': 'userid_1675'}, {'user_id': 'userid_227'}, {'user_id': 'userid_577'}, {'user_id': 'userid_257'}, {'user_id': 'userid_598'}, {'user_id': 'userid_847'}, {'user_id': 'userid_673'}, {'user_id': 'userid_1856'}, {'user_id': 'userid_384'}, {'user_id': 'userid_935'}, {'user_id': 'userid_210'}, {'user_id': 'userid_1101'}, {'user_id': 'userid_945'}, {'user_id': 'userid_842'}, {'user_id': 'userid_1351'}, {'user_id': 'userid_230'}, {'user_id': 'userid_593'}, {'user_id': 'userid_1431'}, {'user_id': 'userid_686'}, {'user_id': 'userid_527'}, {'user_id': 'userid_244'}, {'user_id': 'userid_393'}, {'user_id': 'userid_1178'}, {'user_id': 'userid_526'}, {'user_id': 'userid_90'}, {'user_id': 'userid_238'}, {'user_id': 'userid_1105'}], 'var_call_hDC0ciInAZpFuFr2mcpU2nuI': [{'business_ref': 'businessref_13', 'review_count': '1'}, {'business_ref': 'businessref_79', 'review_count': '1'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_6', 'review_count': '1'}, {'business_ref': 'businessref_15', 'review_count': '1'}, {'business_ref': 'businessref_33', 'review_count': '2'}, {'business_ref': 'businessref_36', 'review_count': '2'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_12', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_57', 'review_count': '2'}, {'business_ref': 'businessref_86', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '1'}, {'business_ref': 'businessref_37', 'review_count': '1'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_26', 'review_count': '1'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}, {'business_ref': 'businessref_45', 'review_count': '3'}, {'business_ref': 'businessref_96', 'review_count': '2'}, {'business_ref': 'businessref_98', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}], 'var_call_ooMcmBtwkcWJHwP8c2dMIWun': 'file_storage/call_ooMcmBtwkcWJHwP8c2dMIWun.json'}

exec(code, env_args)
