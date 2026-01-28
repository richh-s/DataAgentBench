code = """import json
import pandas as pd
import string
from collections import defaultdict

# Load data
reviews = var_call_hDC0ciInAZpFuFr2mcpU2nuI
business_file = var_call_ooMcmBtwkcWJHwP8c2dMIWun
with open(business_file, 'r', encoding='utf-8') as f:
    businesses = json.load(f)

# DataFrames
df_rev = pd.DataFrame(reviews)
if not df_rev.empty:
    df_rev['review_count'] = df_rev['review_count'].astype(int)
    df_rev['business_id'] = df_rev['business_ref'].apply(lambda x: x.replace('businessref_', 'businessid_'))
else:
    df_rev = pd.DataFrame(columns=['business_ref', 'review_count', 'business_id'])

df_bus = pd.DataFrame(businesses)
if 'description' not in df_bus.columns:
    df_bus['description'] = ''

merged = pd.merge(df_rev, df_bus[['business_id', 'description']], on='business_id', how='left')

# Token extraction without regex
def extract_tokens(desc):
    if not isinstance(desc, str):
        return []
    s = ' '.join(desc.splitlines()).strip()
    if not s:
        return []
    # try to find a part after keywords that often precede categories
    low = s.lower()
    keywords = ['offers a range of services', 'offers a diverse range', 'offers a variety of', 'offers a delightful', 'this establishment offers', 'this facility offers', 'offers', 'specializes in', 'in the category of', 'in the categories of', 'provides a range of services']
    pos = -1
    for k in keywords:
        idx = low.find(k)
        if idx != -1 and idx > pos:
            pos = idx
    if pos != -1:
        # take substring after the keyword position
        start = pos
        # find the first comma after start
        sub = s[start:]
    else:
        sub = s
    # Normalize separators
    sub = sub.replace('&', ',')
    sub = sub.replace(' and ', ',')
    parts = [p.strip() for p in sub.split(',') if p.strip()]
    tokens = []
    for p in parts:
        # remove punctuation
        p_clean = p.translate(str.maketrans('', '', string.punctuation))
        p_clean = p_clean.strip()
        if not p_clean:
            continue
        # skip if contains digits
        if any(ch.isdigit() for ch in p_clean):
            continue
        if len(p_clean) < 2:
            continue
        # skip very long
        if len(p_clean) > 120:
            continue
        tokens.append(' '.join(p_clean.split()))
    # deduplicate
    seen = set()
    out = []
    for t in tokens:
        key = t.lower()
        if key not in seen:
            seen.add(key)
            out.append(t)
    return out

cat_counts = defaultdict(int)
for _, row in merged.iterrows():
    desc = row.get('description', '')
    cnt = int(row.get('review_count', 0) or 0)
    toks = extract_tokens(desc)
    for t in toks:
        cat_counts[t] += cnt

items = sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)
result = [{'category': k, 'review_count': v} for k, v in items[:5]]

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_D2kJ0Y9gE3yR8RliD60BLhuV': ['checkin', 'business'], 'var_call_FBGO4FivMrShNLULYWnaVrfB': ['review', 'tip', 'user'], 'var_call_bPBGrBk40upm3qZvV8dYbzzo': 'file_storage/call_bPBGrBk40upm3qZvV8dYbzzo.json', 'var_call_SwMEsOwMOr2TdxYrqiUUXsxF': [{'user_id': 'userid_746'}, {'user_id': 'userid_1109'}, {'user_id': 'userid_1950'}, {'user_id': 'userid_1316'}, {'user_id': 'userid_1182'}, {'user_id': 'userid_151'}, {'user_id': 'userid_1158'}, {'user_id': 'userid_508'}, {'user_id': 'userid_435'}, {'user_id': 'userid_958'}, {'user_id': 'userid_1879'}, {'user_id': 'userid_308'}, {'user_id': 'userid_1179'}, {'user_id': 'userid_324'}, {'user_id': 'userid_863'}, {'user_id': 'userid_100'}, {'user_id': 'userid_1333'}, {'user_id': 'userid_1636'}, {'user_id': 'userid_1850'}, {'user_id': 'userid_711'}, {'user_id': 'userid_729'}, {'user_id': 'userid_1505'}, {'user_id': 'userid_1315'}, {'user_id': 'userid_1708'}, {'user_id': 'userid_1661'}, {'user_id': 'userid_850'}, {'user_id': 'userid_1675'}, {'user_id': 'userid_227'}, {'user_id': 'userid_577'}, {'user_id': 'userid_257'}, {'user_id': 'userid_598'}, {'user_id': 'userid_847'}, {'user_id': 'userid_673'}, {'user_id': 'userid_1856'}, {'user_id': 'userid_384'}, {'user_id': 'userid_935'}, {'user_id': 'userid_210'}, {'user_id': 'userid_1101'}, {'user_id': 'userid_945'}, {'user_id': 'userid_842'}, {'user_id': 'userid_1351'}, {'user_id': 'userid_230'}, {'user_id': 'userid_593'}, {'user_id': 'userid_1431'}, {'user_id': 'userid_686'}, {'user_id': 'userid_527'}, {'user_id': 'userid_244'}, {'user_id': 'userid_393'}, {'user_id': 'userid_1178'}, {'user_id': 'userid_526'}, {'user_id': 'userid_90'}, {'user_id': 'userid_238'}, {'user_id': 'userid_1105'}], 'var_call_hDC0ciInAZpFuFr2mcpU2nuI': [{'business_ref': 'businessref_13', 'review_count': '1'}, {'business_ref': 'businessref_79', 'review_count': '1'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_6', 'review_count': '1'}, {'business_ref': 'businessref_15', 'review_count': '1'}, {'business_ref': 'businessref_33', 'review_count': '2'}, {'business_ref': 'businessref_36', 'review_count': '2'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_12', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_57', 'review_count': '2'}, {'business_ref': 'businessref_86', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '1'}, {'business_ref': 'businessref_37', 'review_count': '1'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_26', 'review_count': '1'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}, {'business_ref': 'businessref_45', 'review_count': '3'}, {'business_ref': 'businessref_96', 'review_count': '2'}, {'business_ref': 'businessref_98', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}], 'var_call_ooMcmBtwkcWJHwP8c2dMIWun': 'file_storage/call_ooMcmBtwkcWJHwP8c2dMIWun.json'}

exec(code, env_args)
