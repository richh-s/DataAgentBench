code = """import json
import re
import pandas as pd

# Load data from storage-provided file paths
with open(var_call_bmGsDrqzEb8WIXr84xa3oUqv, 'r') as f:
    businesses = json.load(f)
with open(var_call_Frbu60r0fEgy6ljG6I74NfbJ, 'r') as f:
    reviews = json.load(f)

# Create DataFrames
df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews)

# Normalize business reference to match review.business_ref
if 'business_id' in df_b.columns:
    df_b['business_ref'] = df_b['business_id'].astype(str).str.replace('businessid_', 'businessref_', regex=False)
else:
    df_b['business_ref'] = None

# US state abbreviations (50 states + DC)
states = {"AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY","DC"}

# Function to extract state from description
pattern = re.compile(r',\s*([A-Z]{2})\b')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = pattern.search(desc)
    if m and m.group(1) in states:
        return m.group(1)
    # fallback: find any two-letter token that is a state
    tokens = re.findall(r'\b([A-Z]{2})\b', desc)
    for t in tokens:
        if t in states:
            return t
    return None

if 'description' in df_b.columns:
    df_b['state'] = df_b['description'].apply(extract_state)
else:
    df_b['state'] = None

# Prepare reviews
if 'rating' in df_r.columns:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
else:
    df_r['rating'] = None

# Merge reviews with business states
merged = df_r.merge(df_b[['business_ref','state']], on='business_ref', how='left')

# Filter to rows with state
merged2 = merged[merged['state'].notna()].copy()

# Aggregate: count reviews per state and average rating across reviews in that state
agg = merged2.groupby('state').agg(review_count=('rating','count'), average_rating=('rating','mean')).reset_index()

if agg.empty:
    result = {'state': None, 'review_count': 0, 'average_rating': None}
else:
    top = agg.sort_values('review_count', ascending=False).iloc[0]
    result = {
        'state': top['state'],
        'review_count': int(top['review_count']),
        'average_rating': round(float(top['average_rating']), 4) if pd.notna(top['average_rating']) else None
    }

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_fpPF93D0p5wuk9Tn3xlYkuTv': ['business', 'checkin'], 'var_call_gpCk0rwl1WBa0LKN6UThykCT': ['review', 'tip', 'user'], 'var_call_bmGsDrqzEb8WIXr84xa3oUqv': 'file_storage/call_bmGsDrqzEb8WIXr84xa3oUqv.json', 'var_call_Frbu60r0fEgy6ljG6I74NfbJ': 'file_storage/call_Frbu60r0fEgy6ljG6I74NfbJ.json'}

exec(code, env_args)
