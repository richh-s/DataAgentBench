code = """import json
import pandas as pd
import re

# Load data
with open(var_call_By0YsQSKO0TUH7HYGOuh2IE3, 'r') as f:
    businesses = json.load(f)
with open(var_call_TlPasEwRwrpoipslO3NtzTX9, 'r') as f:
    reviews = json.load(f)

df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews)

# Helper: accepts credit cards
def accepts_credit(attrs):
    if attrs is None:
        return False
    if isinstance(attrs, dict):
        v = attrs.get('BusinessAcceptsCreditCards')
        if v is None:
            return False
        return 'true' in str(v).lower()
    s = str(attrs).lower()
    return ('businessacceptscreditcards' in s and 'true' in s)

# Apply
if 'attributes' not in df_b.columns:
    df_b['attributes'] = None

df_b['accepts_cc'] = df_b['attributes'].apply(accepts_credit)

# Function to extract categories
patterns = [
    r"offers .* in (.+?)(?:\.|$)",
    r"offers .* in the category of (.+?)(?:\.|$)",
    r"offers .* in the categories? of (.+?)(?:\.|$)",
    r"offers .* including (.+?)(?:\.|$)",
    r"offers .* offering (.+?)(?:\.|$)",
]

def extract_from_description(desc):
    if not isinstance(desc, str):
        return []
    s = desc
    for pat in patterns:
        m = re.search(pat, s, flags=re.IGNORECASE)
        if m:
            grp = m.group(1)
            # Remove leading location phrases if any
            # Split by common separators
            parts = re.split(r",|/|\band\b|\&|;", grp)
            parts = [p.strip().strip("'\"") for p in parts if p.strip()]
            # Further clean trailing words like '.'
            cleaned = []
            for p in parts:
                # Remove phrases like 'Food' trailing 'Food' keep as is
                # Remove extra words like 'and' handled
                cleaned.append(p)
            return cleaned
    return []

# Build category list from 'categories' field if present, else from description
if 'categories' not in df_b.columns:
    df_b['categories'] = None

def categories_list(row):
    c = row.get('categories')
    if c and not (isinstance(c, str) and c.lower()=='none'):
        if isinstance(c, list):
            parts = [str(x).strip() for x in c if str(x).strip()]
            return parts
        s = str(c)
        parts = [p.strip() for p in s.split(',') if p.strip()]
        return parts
    # fallback to description
    return extract_from_description(row.get('description'))

# Apply
df_b['category_list'] = df_b.apply(categories_list, axis=1)

# Create business_ref
def to_ref(bid):
    if not isinstance(bid, str):
        return None
    return bid.replace('businessid_', 'businessref_')

df_b['business_ref'] = df_b['business_id'].apply(to_ref)

# Filter businesses that accept CC
df_acc = df_b[df_b['accepts_cc']==True].copy()

# Explode
df_expl = df_acc.explode('category_list')
if 'category_list' not in df_expl.columns:
    df_expl['category_list'] = None

# Clean category entries
df_expl['category_list'] = df_expl['category_list'].apply(lambda x: x.strip() if isinstance(x, str) else x)

df_expl = df_expl[df_expl['category_list'].notna() & (df_expl['category_list']!='')]

result = {"category": None, "business_count": 0, "average_rating": None}

if not df_expl.empty:
    counts = df_expl.groupby('category_list')['business_id'].nunique()
    counts = counts.sort_values(ascending=False)
    top_cat = counts.index[0]
    top_count = int(counts.iloc[0])

    refs_in_top = set(df_expl[df_expl['category_list']==top_cat]['business_ref'].dropna().tolist())

    # Prepare reviews df
    if not df_r.empty:
        df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
    else:
        df_r['rating'] = pd.Series(dtype=float)

    df_sel = df_r[df_r['business_ref'].isin(refs_in_top)]
    if len(df_sel)>0:
        avg_rating = round(float(df_sel['rating'].mean()),2)
    else:
        avg_rating = None

    result = {"category": top_cat, "business_count": top_count, "average_rating": avg_rating}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_zYWWfxdtpjIy5owlOM4SaGDn': ['business', 'checkin'], 'var_call_mHA3vgr16eyfCZYaS9qPg3uP': ['review', 'tip', 'user'], 'var_call_By0YsQSKO0TUH7HYGOuh2IE3': 'file_storage/call_By0YsQSKO0TUH7HYGOuh2IE3.json', 'var_call_TlPasEwRwrpoipslO3NtzTX9': 'file_storage/call_TlPasEwRwrpoipslO3NtzTX9.json', 'var_call_y3E5KsRHzfEDIvVCCDQoNDKU': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_4EyBBhMx0IX87GBMEIVF9q5X': 'file_storage/call_4EyBBhMx0IX87GBMEIVF9q5X.json'}

exec(code, env_args)
