code = """import json
import pandas as pd
with open(var_call_uM66o8gfxRMsPZNM2Vbl26Cj, 'r') as f:
    businesses = json.load(f)

bdf = pd.DataFrame(businesses)

# Inspect keys
all_keys = set()
for d in businesses:
    all_keys.update(d.keys())

# Count total and presence of 'categories'
total = len(bdf)
has_categories = bdf['categories'].notnull().sum() if 'categories' in bdf.columns else 0

# Sample values for categories
sample_cats = []
if 'categories' in bdf.columns:
    sample_cats = bdf['categories'].dropna().head(20).tolist()

# Also check attributes types and how many have BusinessAcceptsCreditCards
from collections import Counter
attr_vals = bdf['attributes'].dropna().head(20).tolist() if 'attributes' in bdf.columns else []

# Count values for BusinessAcceptsCreditCards occurrences in attributes (string search)
count_accepts_key = 0
count_accepts_true = 0
for a in bdf.get('attributes', []):
    if a is None:
        continue
    # string or dict
    if isinstance(a, dict):
        if any(k.lower()=='businessacceptscreditcards' for k in a.keys()):
            count_accepts_key += 1
            val = a.get('BusinessAcceptsCreditCards') or a.get('businessacceptscreditcards')
            if isinstance(val, str) and val.strip().lower()=='true':
                count_accepts_true += 1
            if isinstance(val, bool) and val:
                count_accepts_true += 1
    elif isinstance(a, str):
        if 'BusinessAcceptsCreditCards' in a or 'businessacceptscreditcards' in a:
            count_accepts_key += 1
            if "'True'" in a or 'True' in a or 'true' in a:
                count_accepts_true += 1

res = {
    'total_businesses': total,
    'has_categories_count': int(has_categories),
    'sample_categories_values': sample_cats,
    'sample_attributes_values': attr_vals,
    'count_attributes_with_accepts_key': int(count_accepts_key),
    'count_attributes_with_accepts_true': int(count_accepts_true),
    'all_keys_sample': list(sorted(all_keys))[:50]
}
print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_call_qKe6K9xSeTMnrKra3a4TBAVv': ['checkin', 'business'], 'var_call_x5ANzylX9WGMppdPR142hyW8': ['review', 'tip', 'user'], 'var_call_uM66o8gfxRMsPZNM2Vbl26Cj': 'file_storage/call_uM66o8gfxRMsPZNM2Vbl26Cj.json', 'var_call_rx4eFEGYXvzUp1nrbfdgwYXF': 'file_storage/call_rx4eFEGYXvzUp1nrbfdgwYXF.json', 'var_call_3NobthWtPD6itKMVABbgkr5p': {'category': None, 'business_count': 0, 'average_rating': None}}

exec(code, env_args)
