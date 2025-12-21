code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-9876152415190698502'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-8988901171834631000'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

# Convert revenue to float
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])

# Merge
# Note: track_id in sales is int/string, in tracks is string. Ensure consistency.
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

df_merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Entity Resolution
def normalize_text(text):
    if not isinstance(text, str):
        return ""
    # Lowercase
    text = text.lower()
    # Remove content in parenthesis (often extra info like 'live', 'remix' or source info if it's a duplicate source issue)
    # However, 'remix' might be a different track. 
    # The hint says "Different track_ids can represent the same real-world track."
    # usually this means same song, same artist.
    # Let's try removing punctuation and extra spaces.
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

df_merged['norm_title'] = df_merged['title'].apply(normalize_text)
df_merged['norm_artist'] = df_merged['artist'].apply(normalize_text)

# Handle cases where artist is 'none' or 'unknown' or null.
# If artist is missing, we might rely on title.
# But usually artist is important.
# Let's check rows with high revenue.

# Group by normalized title and artist
# We might want to include album, but album names can vary wildly for the same track (e.g. "Greatest Hits" vs "Original Album").
# So grouping by Title and Artist is usually the standard for "Same Song".
grouped = df_merged.groupby(['norm_title', 'norm_artist'])['total_revenue'].sum().reset_index()

# Sort descending
top_revenue = grouped.sort_values('total_revenue', ascending=False).head(10)

# Get the original title and artist for display (just take the first one from the group)
# We need to map back or just output the normalized ones, but better to get a representative original title.
# We can join back to get "representative" title/artist.
results = []
for index, row in top_revenue.iterrows():
    # Find a sample original record
    sample = df_merged[(df_merged['norm_title'] == row['norm_title']) & 
                       (df_merged['norm_artist'] == row['norm_artist'])].iloc[0]
    results.append({
        "title": sample['title'],
        "artist": sample['artist'],
        "norm_title": row['norm_title'],
        "norm_artist": row['norm_artist'],
        "total_revenue": row['total_revenue']
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-9876152415190698502': 'file_storage/function-call-9876152415190698502.json', 'var_function-call-8988901171834631000': 'file_storage/function-call-8988901171834631000.json'}

exec(code, env_args)
