code = """import json, re, pandas as pd

def load_records(maybe_path):
    if isinstance(maybe_path, str) and maybe_path.endswith('.json'):
        with open(maybe_path, 'r') as f:
            return json.load(f)
    return maybe_path

biz = load_records(var_call_dxH3ZaVrO5kpAUXl7q603S3X)
rev = load_records(var_call_hCyjCZ7GLM4nSogB9BTRfbJm)

biz_df = pd.DataFrame(biz)
state_pat = re.compile(r'\b([A-Z]{2})\b')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # prefer pattern ' in <City>, ST' or ' in <City>, ST,'
    m = re.findall(r'\b([A-Z]{2})\b', desc)
    if not m:
        return None
    # last 2-letter token often state abbreviation
    return m[-1]

biz_df['state'] = biz_df.get('description').map(extract_state)
# keep only known US state abbreviations
us_states = set('AL AK AZ AR CA CO CT DE FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY DC'.split())
biz_df.loc[~biz_df['state'].isin(us_states), 'state'] = None
biz_df['review_count'] = pd.to_numeric(biz_df.get('review_count'), errors='coerce').fillna(0).astype(int)

state_totals = biz_df.dropna(subset=['state']).groupby('state')['review_count'].sum().sort_values(ascending=False)

if state_totals.empty:
    out = {'error':'Could not parse any state from business.description'}
else:
    top_state = state_totals.index[0]
    top_total_reviews = int(state_totals.iloc[0])

    rev_df = pd.DataFrame(rev)
    rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
    rev_df['business_id'] = rev_df['business_ref'].astype(str).str.replace('businessref_', 'businessid_', regex=False)
    joined = rev_df.merge(biz_df[['business_id','state']], on='business_id', how='left')
    avg_rating = joined.loc[joined['state']==top_state, 'rating'].mean()

    out = {
        'state': top_state,
        'total_reviews': top_total_reviews,
        'average_rating': None if pd.isna(avg_rating) else float(round(avg_rating, 4))
    }

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_dxH3ZaVrO5kpAUXl7q603S3X': 'file_storage/call_dxH3ZaVrO5kpAUXl7q603S3X.json', 'var_call_hCyjCZ7GLM4nSogB9BTRfbJm': 'file_storage/call_hCyjCZ7GLM4nSogB9BTRfbJm.json'}

exec(code, env_args)
