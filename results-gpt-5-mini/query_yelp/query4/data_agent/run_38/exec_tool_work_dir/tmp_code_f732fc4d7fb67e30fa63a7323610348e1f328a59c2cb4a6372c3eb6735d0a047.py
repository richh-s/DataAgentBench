code = """import json
import pandas as pd
with open(var_call_5vnOh8AuoRlDoxaH2LJA4BnY,'r') as f:
    businesses = json.load(f)

# Build dataframe
df = pd.DataFrame(businesses)

# Extract categories from description field (comma-separated categories at end after location)
# Heuristic: description contains 'offers a range of services in X, Y, Z.' or 'offers a range of services including A, B, C.'
import re

def extract_cats(desc):
    if not isinstance(desc, str):
        return []
    # Attempt to find the part after 'offers a range of services in' or 'offers a range of services including' or 'offers a range of services in the category of'
    m = re.search(r'offers a range of services in (.+?)(\.|$)', desc, flags=re.IGNORECASE)
    if not m:
        m = re.search(r'offers a range of services including (.+?)(\.|$)', desc, flags=re.IGNORECASE)
    if not m:
        m = re.search(r'category of (.+?)(\.|$)', desc, flags=re.IGNORECASE)
    if not m:
        # fallback: look after 'offering a range of services' phrase
        m = re.search(r'offering a range of services (?:in|including)? (.+?)(\.|$)', desc, flags=re.IGNORECASE)
    if not m:
        return []
    cats_str = m.group(1)
    # split by commas
    parts = [p.strip() for p in re.split(r',| and | & |;|/', cats_str) if p.strip()]
    # Remove location-like phrases (like 'Food', 'Shopping' might be valid though). We'll keep all.
    return parts

# Apply extraction
df['categories_list'] = df['description'].apply(extract_cats)
# Check counts
num_with_cats = int(df['categories_list'].apply(lambda x: len(x)>0).sum())

res = {'total_businesses': len(df), 'businesses_with_extracted_categories': num_with_cats}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_hXzUi1HOyrj3924Zuuu4nlzl': ['business', 'checkin'], 'var_call_Vx7f3xeQCmMRh0NWNG3HKaZW': ['review', 'tip', 'user'], 'var_call_O9KyZjGrIpkwN2nC1wIjqtqU': 'file_storage/call_O9KyZjGrIpkwN2nC1wIjqtqU.json', 'var_call_VFqrAgjYogQR7lq5ElNsE2Jt': 'file_storage/call_VFqrAgjYogQR7lq5ElNsE2Jt.json', 'var_call_HPQ5bAnzRSDUt6FM5hMjLm5U': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_BDiaUSol9ihcL5p6YpXrFGSA': {'columns': ['business_id', 'name', 'attributes'], 'col_counts': {'business_id': 100, 'name': 100, 'attributes': 100}, 'categories_nonempty_count': 0, 'attributes_nonempty_count': 100, 'total_businesses': 100}, 'var_call_5vnOh8AuoRlDoxaH2LJA4BnY': 'file_storage/call_5vnOh8AuoRlDoxaH2LJA4BnY.json'}

exec(code, env_args)
