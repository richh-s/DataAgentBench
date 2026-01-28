code = """import json
import pandas as pd

# Load data files from previous tool calls
with open(var_call_5u72CFr6RYHT6MZ5xk6hTNx, 'r') as f:
    businesses = json.load(f)
with open(var_call_pPOFbEeTYqEA9ypm58fbm9eV, 'r') as f:
    reviews = json.load(f)

bdf = pd.DataFrame(businesses)
rdf = pd.DataFrame(reviews)

# Determine credit card acceptance
def accepts_credit(attrs):
    if attrs is None:
        return False
    if isinstance(attrs, dict):
        val = attrs.get('BusinessAcceptsCreditCards')
        if val is None:
            return False
        s = str(val).strip().lower()
        return s == 'true'
    s = str(attrs).lower()
    return ('businessacceptscreditcards' in s) and ('true' in s)

bdf['_accepts_cc'] = bdf.get('attributes').apply(accepts_credit)

# Categories parsing
def parse_categories(c):
    if c is None:
        return []
    if isinstance(c, list):
        return [str(x).strip() for x in c if x]
    s = str(c)
    if s.strip() == '' or s.lower() == 'none':
        return []
    return [p.strip() for p in s.split(',') if p.strip()]

if 'categories' not in bdf.columns:
    bdf['categories'] = None

bdf['_categories_list'] = bdf['categories'].apply(parse_categories)

# Expand only businesses that accept credit cards
acc_df = bdf[bdf['_accepts_cc'] == True].copy()
acc_expanded = acc_df[['business_id','name','_categories_list']].explode('_categories_list')
acc_expanded = acc_expanded.rename(columns={'_categories_list':'category'})
acc_expanded = acc_expanded[acc_expanded['category'].notna()]

# Count unique businesses per category
cat_counts = acc_expanded.groupby('category')['business_id'].nunique().reset_index(name='business_count')

if cat_counts.empty:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    top_row = cat_counts.sort_values(['business_count','category'], ascending=[False, True]).iloc[0]
    top_category = top_row['category']
    top_count = int(top_row['business_count'])

    # Map review business_ref to business_id
    def ref_to_bid(ref):
        if ref is None:
            return None
        return str(ref).replace('businessref_','businessid_')

    rdf['business_id'] = rdf['business_ref'].apply(ref_to_bid)
    rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')

    top_bids = set(acc_expanded[acc_expanded['category']==top_category]['business_id'].unique())
    relevant = rdf[rdf['business_id'].isin(top_bids) & rdf['rating'].notna()]
    if relevant.empty:
        avg = None
    else:
        avg = round(float(relevant['rating'].mean()), 2)
    result = {'category': top_category, 'business_count': top_count, 'average_rating': avg}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_33tJdYSKyPvqCFR6GBOv64VT': ['checkin', 'business'], 'var_call_0RUxKzrFEwaCMBIFUgyyM9Wi': ['review', 'tip', 'user'], 'var_call_5u72CFr6RYHT6MZ5xk6hTNxq': 'file_storage/call_5u72CFr6RYHT6MZ5xk6hTNxq.json', 'var_call_pPOFbEeTYqEA9ypm58fbm9eV': 'file_storage/call_pPOFbEeTYqEA9ypm58fbm9eV.json'}

exec(code, env_args)
