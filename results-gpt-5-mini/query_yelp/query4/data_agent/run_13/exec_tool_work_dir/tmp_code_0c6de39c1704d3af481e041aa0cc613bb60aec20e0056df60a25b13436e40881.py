code = """import json
import pandas as pd

# Load data from storage file paths
with open(var_call_vnholAlQfSuOZwpTOHWQ58az, 'r') as f:
    businesses = json.load(f)
with open(var_call_HtFv3W3KxYFSOrMluWeDO78n, 'r') as f:
    reviews = json.load(f)

# Create DataFrames
bdf = pd.DataFrame(businesses)
rdf = pd.DataFrame(reviews)

# Ensure fields
bdf = bdf[['business_id', 'name', 'description']].dropna()

# Function to extract categories from description
import re

def extract_categories(desc):
    if not isinstance(desc, str):
        return []
    s = desc
    # Try to take part after last 'in '
    part = s.rsplit(' in ', 1)[-1]
    # Remove leading common phrases
    part = re.sub(r"^(the )?(categories|category|fields|range of services|range|selection|offers a diverse range of services and products in the fields of|offers a diverse selection of|offers a range of services, including|offers a range of services in the categories of)", '', part, flags=re.I)
    # Remove trailing location mentions if any (like ending with a period)
    part = part.strip().strip('.')
    # Split by commas or ' and ' or '/' or '&'
    tokens = re.split(r",|/| & | and | &|\u2013|-|;", part)
    # Clean tokens
    cats = []
    for t in tokens:
        tt = t.strip()
        if not tt:
            continue
        # Remove leading phrases like 'this establishment offers a wide range of services, including'
        tt = re.sub(r"^(offers a .* of |including |such as |for all your .*|a range of |offering a range of |offering a diverse range of )", '', tt, flags=re.I).strip()
        # Remove trailing words like 'services' or 'products'
        tt = re.sub(r"(services|products|options)$", '', tt, flags=re.I).strip()
        # Remove stray location words
        tt = tt.strip()
        # Remove trailing 'for' fragments
        tt = tt.rstrip('.')
        if tt:
            cats.append(tt)
    # Further split tokens that contain ' & ' inside
    final = []
    for c in cats:
        parts = re.split(r" & | and |/", c)
        for p in parts:
            p2 = p.strip()
            if p2:
                final.append(p2)
    # Deduplicate while preserving order
    seen = set()
    out = []
    for c in final:
        if c not in seen:
            seen.add(c)
            out.append(c)
    return out

bdf['categories'] = bdf['description'].apply(extract_categories)

# Map business_id 'businessid_49' -> 'businessref_49' to join with reviews
bdf['business_ref'] = bdf['business_id'].str.replace('businessid_', 'businessref_')

# Process reviews: ensure rating numeric
rdf = rdf[['business_ref', 'rating']].dropna()
# Convert rating to numeric (some may be strings)
rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')

# Filter reviews to only those business_refs present in bdf
valid_refs = set(bdf['business_ref'])
rdf = rdf[rdf['business_ref'].isin(valid_refs)]

# Compute average rating per business_ref (use all reviews)
avg_by_business = rdf.groupby('business_ref', as_index=False)['rating'].mean()
avg_by_business.rename(columns={'rating':'avg_rating'}, inplace=True)

# Merge avg rating back to businesses
bdf = bdf.merge(avg_by_business, on='business_ref', how='left')

# For counting, expand categories so each row per category
exploded = bdf.explode('categories')
exploded = exploded[exploded['categories'].notna()]

# Count unique businesses per category (business_id unique)
counts = exploded.groupby('categories')['business_id'].nunique().reset_index()
counts.rename(columns={'business_id':'business_count'}, inplace=True)

# Identify top category by business_count
if counts.empty:
    result = {"category": None, "business_count": 0, "average_rating": None}
else:
    top = counts.sort_values(['business_count','categories'], ascending=[False, True]).iloc[0]
    top_cat = top['categories']
    top_count = int(top['business_count'])
    # For average rating: consider all reviews for businesses in this category
    bizs_in_cat = exploded[exploded['categories']==top_cat]['business_ref'].unique().tolist()
    reviews_in_cat = rdf[rdf['business_ref'].isin(bizs_in_cat)]
    if len(reviews_in_cat)==0:
        avg_rating = None
    else:
        avg_rating = float(reviews_in_cat['rating'].mean())
    result = {"category": top_cat, "business_count": top_count, "average_rating": round(avg_rating, 2) if avg_rating is not None else None}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_aPkwVXTW75C3e0z8RiVJa404': ['checkin', 'business'], 'var_call_xb1zsaH1iQ82P7HA69qxYAte': ['review', 'tip', 'user'], 'var_call_Fx9qv8ELJNmT8Beifel8PrsZ': 'file_storage/call_Fx9qv8ELJNmT8Beifel8PrsZ.json', 'var_call_vnholAlQfSuOZwpTOHWQ58az': 'file_storage/call_vnholAlQfSuOZwpTOHWQ58az.json', 'var_call_HtFv3W3KxYFSOrMluWeDO78n': 'file_storage/call_HtFv3W3KxYFSOrMluWeDO78n.json'}

exec(code, env_args)
