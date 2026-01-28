code = """import json
import pandas as pd
import re

with open(var_call_jZEL08NkDEmjwOrm2hls2Id8, 'r') as f:
    businesses = json.load(f)
with open(var_call_VHSQ4WPpBD7ghRgUueDxfic2, 'r') as f:
    reviews = json.load(f)

# DataFrames
df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews)

# Ensure columns
if 'business_id' not in df_b.columns:
    df_b['business_id'] = None
if 'description' not in df_b.columns:
    df_b['description'] = ''

# Uppercase descriptions for matching
df_b['description_up'] = df_b['description'].fillna('').astype(str).str.upper()

state_list = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','DC']
state_pattern = re.compile(r'\b(' + '|'.join(state_list) + r')\b')

def extract_state(desc_up):
    if not desc_up:
        return None
    m = state_pattern.search(desc_up)
    if m:
        return m.group(1)
    return None

df_b['state'] = df_b['description_up'].apply(extract_state)

# construct business_ref
if 'business_id' in df_b.columns:
    df_b['business_ref'] = df_b['business_id'].astype(str).str.replace('businessid_', 'businessref_')
else:
    df_b['business_ref'] = None

# Clean ratings
if 'rating' in df_r.columns:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
else:
    df_r['rating'] = pd.NA

# Merge
df_merged = pd.merge(df_r, df_b[['business_ref','state','business_id']], on='business_ref', how='left')

# Drop missing states
df_merged = df_merged.dropna(subset=['state'])

# If no data
if df_merged.empty:
    out = {"state": None, "total_reviews": 0, "avg_review_rating": None, "avg_business_average_rating": None}
else:
    counts = df_merged.groupby('state').size()
    state_max = counts.idxmax()
    total_reviews = int(counts.max())
    avg_review_rating = df_merged.loc[df_merged['state']==state_max, 'rating'].mean()
    biz_avg = df_merged[df_merged['state']==state_max].groupby('business_ref')['rating'].mean()
    avg_business_avg = biz_avg.mean() if not biz_avg.empty else None
    out = {"state": state_max, "total_reviews": int(total_reviews), "avg_review_rating": round(float(avg_review_rating),4) if avg_review_rating is not None and not pd.isna(avg_review_rating) else None, "avg_business_average_rating": round(float(avg_business_avg),4) if avg_business_avg is not None and not pd.isna(avg_business_avg) else None}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_jZEL08NkDEmjwOrm2hls2Id8': 'file_storage/call_jZEL08NkDEmjwOrm2hls2Id8.json', 'var_call_VHSQ4WPpBD7ghRgUueDxfic2': 'file_storage/call_VHSQ4WPpBD7ghRgUueDxfic2.json', 'var_call_5RpQqoTcTOoukUzuaAJIcCgW': {'state': None, 'total_reviews': 0, 'avg_review_rating': None, 'avg_business_rating': None}, 'var_call_bjGcfwAG1fa7paNezZrxJr6y': 'file_storage/call_bjGcfwAG1fa7paNezZrxJr6y.json'}

exec(code, env_args)
