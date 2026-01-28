code = """import json
import pandas as pd
import re

businesses_path = var_call_5kJVrgXIvN0Edazsc7HFYBgI
reviews_path = var_call_QYZaFbgIPmrqZ0Z5w0n7PI7g

with open(businesses_path, 'r') as f:
    businesses = json.load(f)
with open(reviews_path, 'r') as f:
    reviews = json.load(f)

# Prepare list for processed businesses
rows = []

keywords = [' in the category of ', ' offers a range of services in ', ' offers a diverse range of services and products in ', ' offers a range of services and products in ', ' in ', ' including ', ' offers ', ' provides services in ', ' offers a range of services in the fields of ']

for b in businesses:
    bid = b.get('business_id')
    desc = b.get('description') or ''
    desc = desc.strip()
    cat_segment = ''
    best_pos = -1
    best_kw = None
    for kw in keywords:
        pos = desc.lower().rfind(kw.strip())
        if pos > best_pos:
            best_pos = pos
            best_kw = kw
    if best_pos != -1:
        start = best_pos + len(best_kw.strip())
        # find first period after start in original desc (case-sensitive)
        m = re.search(r"[\.\!?]", desc[start:])
        end = start + m.start() if m else len(desc)
        cat_segment = desc[start:end]
    else:
        # fallback: try to find last dash and take after
        if ' - ' in desc:
            cat_segment = desc.split(' - ')[-1]
        else:
            # as last resort, take whole description
            cat_segment = desc

    # Clean cat_segment: remove leading phrases like 'this establishment offers a range of services including'
    # Already attempted with keywords; now split
    # Split by commas, ' and ', ' & ', ';', '/'
    parts = re.split(r',|\sand\s|\s&\s|;|/|\band\b', cat_segment)
    cats = []
    for p in parts:
        p = p.strip()
        # remove phrases like 'this facility offers a nurturing environment for young learners' heavy noise
        # discard if too long (>60 chars) and contains verbs
        if not p:
            continue
        if len(p) > 60 and re.search(r'\b(offers|provides|facility|establishment|located|located at)\b', p, re.IGNORECASE):
            continue
        # Remove trailing words like 'to meet all your travel and transportation needs' by cutting at ' to '
        if ' to ' in p.lower():
            p = p[:p.lower().find(' to ')].strip()
        # Remove leading 'the ' or 'a '
        p = re.sub(r"^(the |a )", '', p, flags=re.IGNORECASE).strip()
        # Remove surrounding quotes
        p = p.strip(" '\"")
        if p:
            cats.append(p)
    # If still empty, fallback to attributes categories? but attributes don't have categories
    rows.append({'business_id': bid, 'categories': cats})

# Create DataFrame
df = pd.DataFrame(rows)
# Explode
df_ex = df.explode('categories')
# Drop NaN categories
if 'categories' in df_ex.columns:
    df_ex = df_ex[df_ex['categories'].notna()]
else:
    df_ex = df_ex

# Trim
if not df_ex.empty:
    df_ex['categories'] = df_ex['categories'].str.strip()

# Count unique businesses per category
if df_ex.empty:
    result = {"category": None, "business_count": 0, "average_rating": None}
else:
    cat_counts = df_ex.groupby('categories')['business_id'].nunique().reset_index()
    cat_counts = cat_counts.rename(columns={'categories': 'category', 'business_id': 'business_count'})
    cat_counts = cat_counts.sort_values(by=['business_count', 'category'], ascending=[False, True])
    top = cat_counts.iloc[0]
    top_category = top['category']
    top_count = int(top['business_count'])

    # business ids in top category
    biz_ids = set(df_ex[df_ex['categories'] == top_category]['business_id'].unique())

    # Process reviews
    df_r = pd.DataFrame(reviews)
    if 'rating' in df_r.columns:
        df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
    else:
        df_r['rating'] = pd.Series(dtype='float')
    # convert business_ref
    def ref2id(r):
        if not isinstance(r, str):
            return None
        return r.replace('businessref_', 'businessid_')
    df_r['business_id'] = df_r['business_ref'].apply(ref2id)
    # filter
    df_r_cat = df_r[df_r['business_id'].isin(biz_ids)]
    if df_r_cat.empty:
        avg = None
    else:
        avg = round(float(df_r_cat['rating'].mean()), 2)

    result = {"category": top_category, "business_count": top_count, "average_rating": (None if avg is None else avg)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_NeumhbNtYh7RIqIMjxGLdY3e': ['checkin', 'business'], 'var_call_yJeK0J3aYKtbIkDeETPJZWaP': ['review', 'tip', 'user'], 'var_call_5kJVrgXIvN0Edazsc7HFYBgI': 'file_storage/call_5kJVrgXIvN0Edazsc7HFYBgI.json', 'var_call_QYZaFbgIPmrqZ0Z5w0n7PI7g': 'file_storage/call_QYZaFbgIPmrqZ0Z5w0n7PI7g.json', 'var_call_YjJC0VopQuMgq5f2rYcJ7a7n': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_5lJRX3ne1c6ql1kvUOPQTGXF': [], 'var_call_A9JencJUo1qHNPTfBWZ42ph7': 'file_storage/call_A9JencJUo1qHNPTfBWZ42ph7.json'}

exec(code, env_args)
