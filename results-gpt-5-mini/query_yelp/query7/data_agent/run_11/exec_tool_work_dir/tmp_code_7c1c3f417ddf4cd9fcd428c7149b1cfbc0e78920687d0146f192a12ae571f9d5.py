code = """import json
import pandas as pd

# Load tool results from storage variables
reviews = var_call_hDC0ciInAZpFuFr2mcpU2nuI  # list of dicts from SQL query
# business collection result stored in a .json file path string
business_file = var_call_ooMcmBtwkcWJHwP8c2dMIWun

# Read full business JSON file
with open(business_file, 'r', encoding='utf-8') as f:
    businesses = json.load(f)

# Create DataFrames
df_rev = pd.DataFrame(reviews)
if not df_rev.empty:
    df_rev['review_count'] = df_rev['review_count'].astype(int)
    # Map businessref_ -> businessid_
    df_rev['business_id'] = df_rev['business_ref'].str.replace('businessref_', 'businessid_')
else:
    df_rev['business_id'] = []

# business df
df_bus = pd.DataFrame(businesses)
# Ensure description exists
if 'description' not in df_bus.columns:
    df_bus['description'] = ''

# Merge
df = pd.merge(df_rev, df_bus, on='business_id', how='left')

# Helper to extract categories from description
import re

def extract_categories(desc):
    if not isinstance(desc, str) or desc.strip()=='' or desc.lower()=='none':
        return []
    desc = desc.replace('\n',' ').strip()
    # Candidate phrases before category list
    phrases = [
        'offers a diverse range of services and products in the fields of',
        'offers a diverse range of services and products in',
        'offers a diverse range of services in',
        'offers a range of services in',
        'offers a range of services, including',
        'offers a range of services and dining options, including',
        'offers a range of services and dining options',
        'offers a variety of services, including',
        'offers a delightful selection of',
        'offers a delightful array of options ranging from',
        'offers a delightful array of options ranging from',
        'offers a delightful array of options',
        'offers a delightful array of options ranging from',
        'offers a delightful array of options ranging',
        'this establishment offers',
        'this facility offers',
        'offers',
        'provides essential services in the categories of',
        'provides essential services in the categories',
        'provides essential services in',
        'provides a range of services in',
        'specializes in',
        'specializes in the categories of',
        'in the categories of',
        'in the category of',
        "in the category of '",
        'including',
        'offering'
    ]
    lower = desc.lower()
    idx = -1
    phrase_used = None
    for ph in phrases:
        pos = lower.find(ph)
        if pos!=-1:
            # choose earliest occurrence of these indicator phrases that probably precede categories
            if idx==-1 or pos>idx:
                idx = pos
                phrase_used = ph
    if idx!=-1:
        # take substring after the phrase used
        start = idx + len(phrase_used)
        candidate = desc[start:]
    else:
        # fallback: try to find ' in ' after the address part; find the last ' in '
        pos = lower.rfind(' in ')
        if pos!=-1:
            candidate = desc[pos+4:]
        else:
            # as ultimate fallback, take whole description
            candidate = desc
    # Now split candidate by commas
    parts = [p.strip() for p in re.split(',|;|\\.|\\band\\b|\\&', candidate) if p.strip()]
    cleaned = []
    for p in parts:
        # remove leading words like 'the', 'a', 'offers', 'this', 'including'
        p = re.sub('^the\s+','',p, flags=re.I)
        p = re.sub('^a\s+','',p, flags=re.I)
        p = re.sub('^offers\s+','',p, flags=re.I)
        p = re.sub('^including\s+','',p, flags=re.I)
        p = p.strip(' "\'')
        # remove trailing words that are not category-like
        p = re.sub('\s+for.*$','',p)
        p = re.sub('\s+to.*$','',p)
        # ignore short tokens
        if len(p)>=2:
            cleaned.append(p)
    # Further filter tokens that look like addresses or sentences
    # Keep tokens that contain letters
    final = []
    for c in cleaned:
        # skip if looks like an address (contains digits and street abbreviations)
        if re.search('\d', c):
            continue
        # skip if too long (>100)
        if len(c)>100:
            continue
        final.append(c.strip())
    # Normalize whitespace
    final = [re.sub('\s+',' ',f).strip() for f in final]
    return final

# Aggregate counts by category
from collections import defaultdict
cat_counts = defaultdict(int)

for _, row in df.iterrows():
    desc = row.get('description','')
    cats = extract_categories(desc)
    cnt = int(row.get('review_count',0))
    if not cats:
        # try using 'name' as category fallback? skip
        continue
    for c in cats:
        cat_counts[c] += cnt

# Prepare top 5
items = sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)
top5 = items[:5]
# Build result list
result = []
for cat, cnt in top5:
    result.append({'category': cat, 'review_count': cnt})

# If no categories found (edge case), return empty list
out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_D2kJ0Y9gE3yR8RliD60BLhuV': ['checkin', 'business'], 'var_call_FBGO4FivMrShNLULYWnaVrfB': ['review', 'tip', 'user'], 'var_call_bPBGrBk40upm3qZvV8dYbzzo': 'file_storage/call_bPBGrBk40upm3qZvV8dYbzzo.json', 'var_call_SwMEsOwMOr2TdxYrqiUUXsxF': [{'user_id': 'userid_746'}, {'user_id': 'userid_1109'}, {'user_id': 'userid_1950'}, {'user_id': 'userid_1316'}, {'user_id': 'userid_1182'}, {'user_id': 'userid_151'}, {'user_id': 'userid_1158'}, {'user_id': 'userid_508'}, {'user_id': 'userid_435'}, {'user_id': 'userid_958'}, {'user_id': 'userid_1879'}, {'user_id': 'userid_308'}, {'user_id': 'userid_1179'}, {'user_id': 'userid_324'}, {'user_id': 'userid_863'}, {'user_id': 'userid_100'}, {'user_id': 'userid_1333'}, {'user_id': 'userid_1636'}, {'user_id': 'userid_1850'}, {'user_id': 'userid_711'}, {'user_id': 'userid_729'}, {'user_id': 'userid_1505'}, {'user_id': 'userid_1315'}, {'user_id': 'userid_1708'}, {'user_id': 'userid_1661'}, {'user_id': 'userid_850'}, {'user_id': 'userid_1675'}, {'user_id': 'userid_227'}, {'user_id': 'userid_577'}, {'user_id': 'userid_257'}, {'user_id': 'userid_598'}, {'user_id': 'userid_847'}, {'user_id': 'userid_673'}, {'user_id': 'userid_1856'}, {'user_id': 'userid_384'}, {'user_id': 'userid_935'}, {'user_id': 'userid_210'}, {'user_id': 'userid_1101'}, {'user_id': 'userid_945'}, {'user_id': 'userid_842'}, {'user_id': 'userid_1351'}, {'user_id': 'userid_230'}, {'user_id': 'userid_593'}, {'user_id': 'userid_1431'}, {'user_id': 'userid_686'}, {'user_id': 'userid_527'}, {'user_id': 'userid_244'}, {'user_id': 'userid_393'}, {'user_id': 'userid_1178'}, {'user_id': 'userid_526'}, {'user_id': 'userid_90'}, {'user_id': 'userid_238'}, {'user_id': 'userid_1105'}], 'var_call_hDC0ciInAZpFuFr2mcpU2nuI': [{'business_ref': 'businessref_13', 'review_count': '1'}, {'business_ref': 'businessref_79', 'review_count': '1'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_6', 'review_count': '1'}, {'business_ref': 'businessref_15', 'review_count': '1'}, {'business_ref': 'businessref_33', 'review_count': '2'}, {'business_ref': 'businessref_36', 'review_count': '2'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_12', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_57', 'review_count': '2'}, {'business_ref': 'businessref_86', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '1'}, {'business_ref': 'businessref_37', 'review_count': '1'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_26', 'review_count': '1'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}, {'business_ref': 'businessref_45', 'review_count': '3'}, {'business_ref': 'businessref_96', 'review_count': '2'}, {'business_ref': 'businessref_98', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}], 'var_call_ooMcmBtwkcWJHwP8c2dMIWun': 'file_storage/call_ooMcmBtwkcWJHwP8c2dMIWun.json'}

exec(code, env_args)
