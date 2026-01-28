code = """import json
import pandas as pd
import re

# Load data
with open(var_call_K4j5EdaGbvL0F2JZCDZlMfb4, 'r') as f:
    businesses = json.load(f)
with open(var_call_MC5PA2iXmKvLohsxZOLzSr5l, 'r') as f:
    reviews = json.load(f)

# US state codes
states = set(['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','DC'])

# Function to extract state by finding any token matching state codes
pattern = re.compile(r'\b([A-Z]{2})\b')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # find all two-letter uppercase tokens
    toks = pattern.findall(desc)
    # return the first token that is a valid state code scanning from end to start
    for t in reversed(toks):
        if t in states:
            return t
    return None

# Build DataFrame
df_b = pd.DataFrame(businesses)
if 'review_count' in df_b.columns:
    df_b['review_count'] = pd.to_numeric(df_b['review_count'], errors='coerce').fillna(0).astype(int)
else:
    df_b['review_count'] = 0

# Extract state
df_b['state'] = df_b.get('description', '').apply(extract_state)

# Aggregate total reviews per state
state_reviews = df_b.dropna(subset=['state']).groupby('state', as_index=False)['review_count'].sum()

if state_reviews.empty:
    result = {"state": None, "total_reviews": 0, "average_rating": None}
else:
    top = state_reviews.sort_values('review_count', ascending=False).iloc[0]
    top_state = top['state']
    top_reviews = int(top['review_count'])

    # Prepare reviews df
    df_r = pd.DataFrame(reviews)
    if 'business_ref' in df_r.columns:
        df_r['business_id'] = df_r['business_ref'].astype(str).str.replace('businessref_','businessid_', regex=False)
    else:
        df_r['business_id'] = None
    df_r['rating'] = pd.to_numeric(df_r.get('rating', []), errors='coerce')

    # Merge to attach state
    df_merged = pd.merge(df_r, df_b[['business_id','state']], on='business_id', how='left')
    ratings_top_state = df_merged[df_merged['state']==top_state]['rating'].dropna()
    if len(ratings_top_state)==0:
        avg_rating = None
    else:
        avg_rating = round(float(ratings_top_state.mean()),2)

    result = {"state": top_state, "total_reviews": top_reviews, "average_rating": avg_rating}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_G8hOykkC4hAZtPhL6yZt1uZ4': ['checkin', 'business'], 'var_call_G7tiMa5ecVnpHmEVAStpmLgn': ['review', 'tip', 'user'], 'var_call_K4j5EdaGbvL0F2JZCDZlMfb4': 'file_storage/call_K4j5EdaGbvL0F2JZCDZlMfb4.json', 'var_call_MC5PA2iXmKvLohsxZOLzSr5l': 'file_storage/call_MC5PA2iXmKvLohsxZOLzSr5l.json', 'var_call_AFjWY94ENbetQ3HDcnvZ5AGH': {'state': None, 'total_reviews': 0, 'average_rating': None}, 'var_call_bGOAEWagOaMhgtQBKmBYp7ip': 'file_storage/call_bGOAEWagOaMhgtQBKmBYp7ip.json'}

exec(code, env_args)
