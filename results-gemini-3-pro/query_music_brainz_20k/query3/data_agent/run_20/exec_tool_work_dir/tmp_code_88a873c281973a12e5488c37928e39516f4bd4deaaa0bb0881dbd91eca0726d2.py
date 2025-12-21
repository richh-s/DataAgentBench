code = """import pandas as pd
import json
import re

# Load data
with open(locals()['var_function-call-18223064204633629849'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-4676097286613530552'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

# Convert types
df_sales['revenue_usd'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Merge
df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Normalization functions
def normalize_string(s):
    if not isinstance(s, str):
        return ""
    return s.lower().strip()

def clean_title(title):
    if not isinstance(title, str):
        return ""
    # Lowercase
    t = title.lower().strip()
    # Remove leading numbers like "01 - ", "001-", "1. "
    t = re.sub(r'^\d+[\.\-\s]+', '', t)
    # Remove things in brackets/parentheses like (live), [remix], (2008 remaster)
    # But be careful not to remove essential parts if the whole title is in brackets? Unlikely.
    # Let's remove content in (...) and [...]
    t = re.sub(r'\s*\(.*?\)', '', t)
    t = re.sub(r'\s*\[.*?\]', '', t)
    # Remove extra info after " - " like " - 2008-02-15..." if it looks like metadata
    # For now, let's just strip extra whitespace
    t = re.sub(r'\s+', ' ', t).strip()
    return t

def clean_artist(artist):
    if not isinstance(artist, str) or artist.lower() in ['none', '[unknown]']:
        return "unknown"
    return artist.lower().strip()

df['clean_title'] = df['title'].apply(clean_title)
df['clean_artist'] = df['artist'].apply(clean_artist)

# Group by cleaned attributes
# If artist is unknown, we rely on title. If title is also empty/generic, we might have issues.
# But let's assume valid songs have titles.

# We will group by (clean_artist, clean_title)
grouped = df.groupby(['clean_artist', 'clean_title'])['revenue_usd'].sum().reset_index()

# Sort descending
top_revenue = grouped.sort_values('revenue_usd', ascending=False).head(10)

print("__RESULT__:")
print(top_revenue.to_json(orient='records'))"""

env_args = {'var_function-call-18223064204633629849': 'file_storage/function-call-18223064204633629849.json', 'var_function-call-4676097286613530552': 'file_storage/function-call-4676097286613530552.json'}

exec(code, env_args)
