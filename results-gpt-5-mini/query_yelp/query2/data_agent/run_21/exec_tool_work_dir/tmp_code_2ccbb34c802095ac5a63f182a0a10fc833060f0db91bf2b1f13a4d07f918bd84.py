code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
with open(var_call_K4j5EdaGbvL0F2JZCDZlMfb4, 'r') as f:
    businesses = json.load(f)
with open(var_call_MC5PA2iXmKvLohsxZOLzSr5l, 'r') as f:
    reviews = json.load(f)

# Create DataFrames
df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews)

# Clean and convert review_count to integer
if 'review_count' in df_b.columns:
    df_b['review_count'] = pd.to_numeric(df_b['review_count'], errors='coerce').fillna(0).astype(int)
else:
    df_b['review_count'] = 0

# Extract US state from description by finding the last occurrence of a comma followed by two uppercase letters
state_pattern = re.compile(r',\s*([A-Z]{2})\b')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    matches = state_pattern.findall(desc)
    return matches[-1] if matches else None

df_b['state'] = df_b.get('description', None).apply(extract_state)

# Aggregate total reviews per state using business.review_count
state_reviews = df_b.dropna(subset=['state']).groupby('state', as_index=False)['review_count'].sum()

if state_reviews.empty:
    result = {"state": None, "total_reviews": 0, "average_rating": None}
else:
    # State with highest number of reviews
    top = state_reviews.sort_values('review_count', ascending=False).iloc[0]
    top_state = top['state']
    top_reviews = int(top['review_count'])

    # Prepare reviews dataframe: map businessref_X -> businessid_X
    if 'business_ref' in df_r.columns:
        df_r['business_id'] = df_r['business_ref'].astype(str).str.replace('businessref_', 'businessid_', regex=False)
    else:
        df_r['business_id'] = None

    # Ensure numeric ratings
    if 'rating' in df_r.columns:
        df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
    else:
        df_r['rating'] = pd.NA

    # Merge to get state for each review
    df_merged = pd.merge(df_r, df_b[['business_id','state']], on='business_id', how='left')

    # Compute average rating for the top state across all reviews associated with businesses in that state
    ratings_top_state = df_merged[df_merged['state'] == top_state]['rating'].dropna()
    if len(ratings_top_state) == 0:
        avg_rating = None
    else:
        avg_rating = float(ratings_top_state.mean())

    # Round average rating to 2 decimals if not None
    avg_rating_rounded = round(avg_rating, 2) if avg_rating is not None else None

    result = {"state": top_state, "total_reviews": top_reviews, "average_rating": avg_rating_rounded}

# Print in required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_G8hOykkC4hAZtPhL6yZt1uZ4': ['checkin', 'business'], 'var_call_G7tiMa5ecVnpHmEVAStpmLgn': ['review', 'tip', 'user'], 'var_call_K4j5EdaGbvL0F2JZCDZlMfb4': 'file_storage/call_K4j5EdaGbvL0F2JZCDZlMfb4.json', 'var_call_MC5PA2iXmKvLohsxZOLzSr5l': 'file_storage/call_MC5PA2iXmKvLohsxZOLzSr5l.json'}

exec(code, env_args)
