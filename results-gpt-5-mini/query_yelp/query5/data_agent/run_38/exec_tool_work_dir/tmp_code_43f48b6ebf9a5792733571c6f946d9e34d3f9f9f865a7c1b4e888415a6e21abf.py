code = """import json, re, statistics
import pandas as pd

# Load data from storage file paths
with open(var_call_U9tlk95240Q9j4oZTiXr4VmR, 'r') as f:
    businesses = json.load(f)
with open(var_call_M1x5fe1lFeTIIYVlNnareI7M, 'r') as f:
    reviews = json.load(f)

# Create DataFrames
b_df = pd.DataFrame(businesses)
r_df = pd.DataFrame(reviews)

# Normalize ratings to numeric
r_df['rating'] = pd.to_numeric(r_df['rating'], errors='coerce')

# Map business_ref to business_id by replacing prefix
r_df['business_id'] = r_df['business_ref'].str.replace('businessref_', 'businessid_')

# Helper to detect WiFi
import numpy as np

def has_wifi(attr):
    if attr is None:
        return False
    # If string
    if isinstance(attr, str):
        s = attr.lower()
        if 'wifi' in s:
            # if 'no' appears near wifi, treat as no
            # crude check: if 'no' in s and 'wifi' in s and s.index('no') > s.index('wifi') - 10 and s.index('no') < s.index('wifi') + 20:
            if 'no' in s:
                # if contains 'free' or 'paid' or 'yes' then wifi exists
                if any(k in s for k in ['free','paid','yes']):
                    return True
                return False
            return True
        return False
    # If dict-like
    if isinstance(attr, dict):
        # keys could be 'WiFi' or 'wifi'
        val = None
        for k in attr.keys():
            if k.lower() == 'wifi':
                val = attr[k]
                break
        if val is None:
            return False
        sval = str(val).lower()
        if 'no' in sval:
            return False
        return True
    return False

# Determine WiFi presence for each business
b_df['has_wifi'] = b_df['attributes'].apply(has_wifi)

# Extract state from description using regex
def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # look for pattern ', XX,' where XX are two letters
    m = re.search(r',\s*([A-Z]{2})\s*,', desc)
    if m:
        return m.group(1)
    # also try pattern ' in City, ST,' or ' in City, ST ' with period
    m2 = re.search(r'in\s+[^,]+,\s*([A-Z]{2})\b', desc)
    if m2:
        return m2.group(1)
    return None

b_df['state'] = b_df['description'].apply(extract_state)

# Filter businesses with wifi and state is not null
wifi_b = b_df[(b_df['has_wifi']) & (b_df['state'].notnull())][['business_id','state']]

# Merge reviews with wifi businesses
merged = r_df.merge(wifi_b, on='business_id', how='inner')

# Compute counts of unique businesses offering wifi by state
business_counts = wifi_b.groupby('state')['business_id'].nunique().reset_index().rename(columns={'business_id':'business_count'})

# Compute average rating across reviews for wifi businesses by state
avg_ratings = merged.groupby('state')['rating'].mean().reset_index().rename(columns={'rating':'avg_rating'})

# Combine
comb = business_counts.merge(avg_ratings, on='state', how='left')

# If a state has businesses with wifi but no reviews, avg_rating will be NaN; leave as None
comb['avg_rating'] = comb['avg_rating'].apply(lambda x: None if pd.isna(x) else round(float(x),2))
comb['business_count'] = comb['business_count'].astype(int)

# Find state with highest business_count; if tie choose one with highest avg_rating
if comb.shape[0] == 0:
    result = None
else:
    max_count = comb['business_count'].max()
    candidates = comb[comb['business_count']==max_count].copy()
    # pick with highest avg_rating (None treated as -inf)
    candidates['avg_sort'] = candidates['avg_rating'].apply(lambda x: -9999 if x is None else x)
    # Wait we want highest avg, so use -inf for None, but since we sort descending, use key accordingly
    chosen = candidates.sort_values(by=['avg_sort'], ascending=False).iloc[0]
    result = {
        'state': chosen['state'],
        'business_count': int(chosen['business_count']),
        'average_rating': (None if chosen['avg_rating'] is None else float(chosen['avg_rating']))
    }

# Prepare output
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_9m4DM0zC5a5adja2FEqt9of9': ['business', 'checkin'], 'var_call_gIWjhCIDMTQUTK2phCdFGcpF': ['review', 'tip', 'user'], 'var_call_U9tlk95240Q9j4oZTiXr4VmR': 'file_storage/call_U9tlk95240Q9j4oZTiXr4VmR.json', 'var_call_M1x5fe1lFeTIIYVlNnareI7M': 'file_storage/call_M1x5fe1lFeTIIYVlNnareI7M.json'}

exec(code, env_args)
