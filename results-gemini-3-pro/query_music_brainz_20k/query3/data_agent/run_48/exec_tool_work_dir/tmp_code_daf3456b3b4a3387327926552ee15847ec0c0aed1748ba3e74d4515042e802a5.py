code = """import json
import pandas as pd

# Load data
with open(locals()['var_function-call-4082973403781613330'], 'r') as f:
    sales_data = json.load(f)

with open(locals()['var_function-call-18357211790249148335'], 'r') as f:
    tracks_data = json.load(f)

# Convert to DataFrame
df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

# Ensure track_id is string
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Convert revenue to float
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])

# Join
# df_sales is aggregated by track_id.
# We join to get metadata.
merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Entity Resolution Function
def resolve_entity(row):
    title = str(row['title'])
    artist = str(row['artist'])
    
    if artist in ['None', 'nan', '']:
        artist = None
    
    # Check for "Artist - Title" pattern in title if artist is missing
    if artist is None and ' - ' in title:
        parts = title.split(' - ', 1)
        # Heuristic: assume first part is artist if it's not too long/short? 
        # Or just trust the format.
        possible_artist = parts[0].strip()
        possible_title = parts[1].strip()
        return possible_title.lower(), possible_artist.lower()
        
    # Standard cleanup
    t = title.lower().strip()
    a = artist.lower().strip() if artist else "unknown"
    return t, a

# Apply resolution
merged['resolved_key'] = merged.apply(resolve_entity, axis=1)

# Group by resolved key
grouped = merged.groupby('resolved_key')['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

# Get original names for the top result (just take the first one that maps to the key)
# We can create a mapping from resolved_key to "Display Name"
# Or just print the top resolved keys and their revenues.

print("__RESULT__:")
print(grouped.head(20).to_json(orient='records'))"""

env_args = {'var_function-call-4082973403781613330': 'file_storage/function-call-4082973403781613330.json', 'var_function-call-18357211790249148335': 'file_storage/function-call-18357211790249148335.json'}

exec(code, env_args)
