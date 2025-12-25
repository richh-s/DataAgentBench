code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-16438138636169770779'], 'r') as f:
    revenue_data = json.load(f)
with open(locals()['var_function-call-17040196689853941222'], 'r') as f:
    track_data = json.load(f)

# Create DataFrames
df_revenue = pd.DataFrame(revenue_data)
df_tracks = pd.DataFrame(track_data)

# Convert track_id to string to ensure matching
df_revenue['track_id'] = df_revenue['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)
df_revenue['total_revenue'] = pd.to_numeric(df_revenue['total_revenue'])

# Merge
df = pd.merge(df_revenue, df_tracks, on='track_id', how='inner')

# Normalization functions
def normalize_string(s):
    if not s or s == 'None' or s == '[unknown]':
        return ''
    s = str(s).lower().strip()
    # Remove text in parenthesis (often contains "live", "remix", "feat", etc.)
    # But be careful: sometimes the title is "Song (Subtitle)".
    # Let's first try exact match on lowercased title and artist.
    return s

def clean_title(t):
    if not t or t == 'None': return ''
    t = str(t).lower().strip()
    # Remove common extra info in parens for better grouping?
    # e.g., "Song (Live)" vs "Song".
    # For now, let's just strip whitespace and lowercase.
    return t

df['norm_title'] = df['title'].apply(clean_title)
df['norm_artist'] = df['artist'].apply(normalize_string)

# Group by norm_title and norm_artist
grouped = df.groupby(['norm_title', 'norm_artist'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

print("__RESULT__:")
print(grouped.head(20).to_json(orient='records'))"""

env_args = {'var_function-call-16438138636169770779': 'file_storage/function-call-16438138636169770779.json', 'var_function-call-17040196689853941222': 'file_storage/function-call-17040196689853941222.json'}

exec(code, env_args)
