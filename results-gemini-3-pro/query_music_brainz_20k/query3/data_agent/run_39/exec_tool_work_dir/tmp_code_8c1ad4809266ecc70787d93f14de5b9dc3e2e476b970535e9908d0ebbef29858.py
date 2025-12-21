code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-18029868950214320737'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-17739212231820982163'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

# Convert total_revenue to float
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Merge
df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

def clean_text(text):
    if not isinstance(text, str):
        return ""
    # Remove text in parentheses/brackets
    text = re.sub(r'\(.*?\)', '', text)
    text = re.sub(r'\[.*?\]', '', text)
    # Remove leading numbers and dashes (e.g. "01-", "002 ")
    text = re.sub(r'^\s*\d+[-.]?\s*', '', text)
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text.lower()

def resolve_entity(row):
    title = row['title']
    artist = row['artist']
    
    # Handle missing/unknown artist
    if not artist or artist.lower() in ['none', '[unknown]', '']:
        if isinstance(title, str) and ' - ' in title:
            parts = title.split(' - ', 1)
            derived_artist = parts[0]
            derived_title = parts[1]
            # Use derived values
            artist = derived_artist
            title = derived_title
    
    clean_t = clean_text(title)
    clean_a = clean_text(artist)
    
    # Further specific cleaning for known issues if any (like "hWeels of FIRE")
    # Simple heuristic: remove spaces inside words if it looks like a typo? No, that's risky.
    # "En dless Love" -> "Endless Love". 
    # Maybe remove all spaces for comparison?
    
    return clean_t, clean_a

# Apply resolution
resolved = df.apply(resolve_entity, axis=1, result_type='expand')
df['clean_title'] = resolved[0]
df['clean_artist'] = resolved[1]

# Create a unique key
df['entity_key'] = df['clean_artist'] + " | " + df['clean_title']

# Aggregate
grouped = df.groupby('entity_key')['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

print('__RESULT__:')
print(grouped.head(10).to_json(orient='records'))"""

env_args = {'var_function-call-18029868950214320737': 'file_storage/function-call-18029868950214320737.json', 'var_function-call-17739212231820982163': 'file_storage/function-call-17739212231820982163.json'}

exec(code, env_args)
