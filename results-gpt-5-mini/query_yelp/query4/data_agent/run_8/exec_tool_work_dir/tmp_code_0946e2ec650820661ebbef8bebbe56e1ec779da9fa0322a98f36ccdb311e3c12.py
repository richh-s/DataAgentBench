code = """import json
import pandas as pd

# Load data
with open(var_call_1uii8pNZd1IBGrZIeeZbTb8Z, 'r') as f:
    businesses = json.load(f)
with open(var_call_4GZQ1vFcyPhN3EeL2n8BFb59, 'r') as f:
    reviews = json.load(f)

# Simple check for credit card acceptance
def accepts_cc(attr):
    if not attr or attr == 'None':
        return False
    if isinstance(attr, dict):
        v = attr.get('BusinessAcceptsCreditCards')
        if v is None:
            return False
        return str(v).lower() == 'true'
    s = str(attr)
    return ('BusinessAcceptsCreditCards' in s) and (('True' in s) or ("'True'" in s) or ('true' in s))

# Simple extract categories
def extract_categories(desc):
    if not desc:
        return []
    text = desc
    low = text.lower()
    pos = low.find(' in ')
    if pos == -1:
        pos = low.find('including ')
        if pos == -1:
            return []
        start = pos + len('including ')
    else:
        start = pos + len(' in ')
    sub = text[start:]
    if '.' in sub:
        sub = sub.split('.',1)[0]
    if ' to ' in sub:
        sub = sub.split(' to ',1)[0]
    sub = sub.replace(' and ', ',')
    parts = [p.strip().strip("'\"") for p in sub.split(',') if p.strip()]
    return parts

pairs = []
for b in businesses:
    bid = b.get('business_id')
    if not bid:
        continue
    if not accepts_cc(b.get('attributes')):
        continue
    cats = b.get('categories')
    cat_list = []
    if cats:
        if isinstance(cats, list):
            cat_list = cats
        elif isinstance(cats, str):
            cat_list = [c.strip() for c in cats.split(',') if c.strip()]
    if not cat_list:
        cat_list = extract_categories(b.get('description',''))
    for c in cat_list:
        if c:
            pairs.append({'business_ref': bid.replace('businessid_','businessref_'), 'category': c})

if not pairs:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    df = pd.DataFrame(pairs).drop_duplicates()
    counts = df.groupby('category')['business_ref'].nunique().reset_index().rename(columns={'business_ref':'business_count'})
    rev_df = pd.DataFrame(reviews)
    rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
    merged = rev_df.merge(df, on='business_ref', how='inner')
    avg = merged.groupby('category')['rating'].mean().reset_index().rename(columns={'rating':'avg_rating'})
    summary = counts.merge(avg, on='category', how='left')
    summary['avg_rating'] = summary['avg_rating'].round(2)
    max_count = int(summary['business_count'].max())
    top = summary[summary['business_count']==max_count].sort_values('avg_rating', ascending=False).iloc[0]
    result = {'category': top['category'], 'business_count': int(top['business_count']), 'average_rating': (None if pd.isna(top['avg_rating']) else float(top['avg_rating']))}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Ryydk2OydyICGOkK0fdQmodU': ['business', 'checkin'], 'var_call_s0HAPJstiC6duixg4yD27A9v': ['review', 'tip', 'user'], 'var_call_1uii8pNZd1IBGrZIeeZbTb8Z': 'file_storage/call_1uii8pNZd1IBGrZIeeZbTb8Z.json', 'var_call_4GZQ1vFcyPhN3EeL2n8BFb59': 'file_storage/call_4GZQ1vFcyPhN3EeL2n8BFb59.json', 'var_call_Da3AGLLQqDg6FPTJG5GiDHq9': {'ok': True}, 'var_call_cxEKNIAsWcPZVUPF4D6cpKde': {'n_businesses': 100, 'n_reviews': 2000}}

exec(code, env_args)
