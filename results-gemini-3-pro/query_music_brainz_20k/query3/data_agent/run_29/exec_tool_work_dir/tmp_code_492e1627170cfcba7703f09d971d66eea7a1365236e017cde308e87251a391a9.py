code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-2517101731408743361'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-6464260199203399189'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

# Ensure track_id is int for merging if needed, or string. Both look like strings in JSON.
# Check types
# print(df_sales['track_id'].dtype)
# print(df_tracks['track_id'].dtype)
# Convert to string to be safe
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])

# Merge
merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Cleaning function
def clean_track(row):
    title = str(row['title']).strip()
    artist = str(row['artist']).strip()
    
    # Check for missing artist
    missing_artist_values = ['None', 'null', '[unknown]', '', 'nan']
    
    if artist in missing_artist_values:
        # Try to extract from title
        if ' - ' in title:
            parts = title.split(' - ', 1)
            artist_candidate = parts[0].strip()
            title_candidate = parts[1].strip()
            # Heuristic: Artist shouldn't be too long or numeric usually, but let's just trust the split for now
            artist = artist_candidate
            title = title_candidate
        else:
            # Fallback for things like "CharlyGarc\u00edaNobombardeenBuenosAires" if possible? 
            # Without spaces it's hard. We'll leave it as is, artist will be 'None'.
            pass

    # Normalize
    # Remove special chars for comparison? Or just strip and lower?
    # Let's keep it readable but normalized for grouping.
    # We should handle "Diana Ross & Lionel Richie" vs "Diana Ross and Lionel Richie" if possible, 
    # but strict string matching might be safer than over-cleaning.
    
    return pd.Series([title, artist])

merged[['clean_title', 'clean_artist']] = merged.apply(clean_track, axis=1)

# Group by cleaned title and artist
# We should probably filter out where artist is still 'None' if we can't identify the song, 
# but the revenue exists. 
# However, the question asks "Which song".
# We will sum revenue.

grouped = merged.groupby(['clean_artist', 'clean_title'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values(by='total_revenue', ascending=False)

print("__RESULT__:")
print(grouped.head(10).to_json(orient='records'))"""

env_args = {'var_function-call-9032484242444107887': ['sales'], 'var_function-call-9032484242444109838': ['tracks'], 'var_function-call-2517101731408743361': 'file_storage/function-call-2517101731408743361.json', 'var_function-call-5327854219375283823': [{'COUNT(*)': '19375'}], 'var_function-call-6464260199203399189': 'file_storage/function-call-6464260199203399189.json'}

exec(code, env_args)
