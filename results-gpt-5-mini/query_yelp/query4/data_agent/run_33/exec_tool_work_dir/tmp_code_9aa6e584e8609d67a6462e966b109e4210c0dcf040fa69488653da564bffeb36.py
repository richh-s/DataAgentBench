code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
with open(var_call_By0YsQSKO0TUH7HYGOuh2IE3, 'r') as f:
    businesses = json.load(f)
with open(var_call_TlPasEwRwrpoipslO3NtzTX9, 'r') as f:
    reviews = json.load(f)

# Create DataFrames
df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews)

# Ensure expected columns exist
if 'categories' not in df_b.columns:
    df_b['categories'] = None

# Function to detect if BusinessAcceptsCreditCards is True
def accepts_credit(attrs):
    if attrs is None:
        return False
    # If it's already a dict
    if isinstance(attrs, dict):
        v = attrs.get('BusinessAcceptsCreditCards')
        if v is None:
            return False
        return 'true' in str(v).lower()
    # Otherwise treat as string
    s = str(attrs).lower()
    if 'businessacceptscreditcards' in s and 'true' in s:
        return True
    return False

# Apply detection
df_b['accepts_cc'] = df_b['attributes'].apply(accepts_credit)

# Normalize categories into list
def split_categories(x):
    if x is None:
        return []
    if isinstance(x, list):
        return [str(i).strip() for i in x if str(i).strip()!='']
    s = str(x)
    if s.lower() == 'none' or s.strip() == '':
        return []
    # Some categories may already be a list-like string, split by comma
    parts = [p.strip() for p in s.split(',')]
    parts = [p for p in parts if p!='']
    return parts

df_b['category_list'] = df_b['categories'].apply(split_categories)

# Create business_ref to match reviews table
def to_ref(bid):
    if not isinstance(bid, str):
        return None
    return bid.replace('businessid_', 'businessref_')

df_b['business_ref'] = df_b['business_id'].apply(to_ref)

# Filter businesses that accept credit cards
df_acc = df_b[df_b['accepts_cc'] == True].copy()

# Explode categories so each row = business-category
df_expl = df_acc.explode('category_list')
# Remove empty categories
df_expl = df_expl[df_expl['category_list'].notna() & (df_expl['category_list'] != '')]

# If no categories after filtering, return empty result
if df_expl.empty:
    result = {"category": None, "business_count": 0, "average_rating": None}
else:
    # Count unique businesses per category
    counts = df_expl.groupby('category_list')['business_id'].nunique()
    top_cat = counts.idxmax()
    top_count = int(counts.max())

    # Get business_refs in that category
    refs_in_top = set(df_expl[df_expl['category_list'] == top_cat]['business_ref'].dropna().tolist())

    # Prepare reviews: ensure rating numeric
    if not df_r.empty:
        df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
    else:
        df_r['rating'] = pd.Series(dtype=float)

    # Filter reviews for those business_refs
    df_sel = df_r[df_r['business_ref'].isin(refs_in_top)]

    if len(df_sel) > 0:
        avg_rating = float(df_sel['rating'].mean())
        avg_rating = round(avg_rating, 2)
    else:
        avg_rating = None

    result = {"category": top_cat, "business_count": top_count, "average_rating": avg_rating}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_zYWWfxdtpjIy5owlOM4SaGDn': ['business', 'checkin'], 'var_call_mHA3vgr16eyfCZYaS9qPg3uP': ['review', 'tip', 'user'], 'var_call_By0YsQSKO0TUH7HYGOuh2IE3': 'file_storage/call_By0YsQSKO0TUH7HYGOuh2IE3.json', 'var_call_TlPasEwRwrpoipslO3NtzTX9': 'file_storage/call_TlPasEwRwrpoipslO3NtzTX9.json'}

exec(code, env_args)
