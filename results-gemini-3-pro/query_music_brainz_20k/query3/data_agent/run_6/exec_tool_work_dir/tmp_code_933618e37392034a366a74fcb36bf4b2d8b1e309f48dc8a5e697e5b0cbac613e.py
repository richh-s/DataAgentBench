code = """import pandas as pd
import json
import re

# Load data
with open(locals()['var_function-call-5081543937369851313'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-2523656843503739436'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
# Ensure numeric
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])

df_tracks = pd.DataFrame(tracks_data)

# Merge
# Ensure track_id type consistency (both appear to be strings in JSON)
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

df = pd.merge(df_sales, df_tracks, on='track_id')

def normalize_string(s):
    if not isinstance(s, str):
        return str(s)
    # Remove content in parentheses
    s = re.sub(r'\(.*?\)', '', s)
    # Remove content in brackets just in case
    s = re.sub(r'\[.*?\]', '', s)
    # Replace multiple spaces with single
    s = " ".join(s.split())
    return s.lower()

def resolve_entity(row):
    title = str(row['title'])
    artist = str(row['artist'])
    
    # Missing artist markers
    missing = ['none', 'unknown', '[unknown]', '', 'null']
    
    # If artist is missing, try to split title
    if artist.lower().strip() in missing:
        if ' - ' in title:
            parts = title.split(' - ', 1)
            # Assume Artist - Title
            artist = parts[0]
            title = parts[1]
    
    # Normalize
    clean_title = normalize_string(title)
    clean_artist = normalize_string(artist)
    
    return pd.Series([clean_title, clean_artist])

cleaned_cols = df.apply(resolve_entity, axis=1)
df['clean_title'] = cleaned_cols[0]
df['clean_artist'] = cleaned_cols[1]

# Group
grouped = df.groupby(['clean_artist', 'clean_title'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

print('__RESULT__:')
print(grouped.head(10).to_json(orient='records'))"""

env_args = {'var_function-call-5081543937369851313': 'file_storage/function-call-5081543937369851313.json', 'var_function-call-2523656843503739436': 'file_storage/function-call-2523656843503739436.json'}

exec(code, env_args)
