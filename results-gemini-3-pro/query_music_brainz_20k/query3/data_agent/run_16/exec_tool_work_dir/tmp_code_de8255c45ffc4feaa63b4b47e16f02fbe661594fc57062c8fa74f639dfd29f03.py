code = """import pandas as pd
import json
import re

# Load data
# tracks_data is in var_function-call-12792199908109322560 (file)
# sales_agg is in var_function-call-4064444512275497395 (file)

with open(locals()['var_function-call-12792199908109322560'], 'r') as f:
    tracks = pd.DataFrame(json.load(f))

with open(locals()['var_function-call-4064444512275497395'], 'r') as f:
    sales = pd.DataFrame(json.load(f))

# Convert types
sales['revenue'] = pd.to_numeric(sales['total_revenue'])
sales['track_id'] = sales['track_id'].astype(str)
tracks['track_id'] = tracks['track_id'].astype(str)

# Merge to get track info for sales
# We keep all tracks because we need to resolve entities for all, then map sales to them.
# Actually, we only care about tracks that have sales.
# But for entity resolution, maybe a track with sales is a duplicate of a track without sales?
# The revenue is attached to specific track_ids. We just need to group those track_ids.
# So we can just merge.

df = pd.merge(sales, tracks, on='track_id', how='left')

# Cleaning function
def clean_str(s):
    if s is None:
        return ""
    return str(s).lower().strip()

def parse_artist_title(row):
    title = row['title']
    artist = row['artist']
    
    # Check for None/Unknown artist
    if artist is None or artist.lower() in ['none', '[unknown]', '']:
        # Try to extract from title if " - " is present
        if title and ' - ' in title:
            parts = title.split(' - ', 1)
            return clean_str(parts[0]), clean_str(parts[1])
        else:
            return "unknown", clean_str(title)
    
    return clean_str(artist), clean_str(title)

# Apply cleaning
# We will create new columns 'clean_artist', 'clean_title'
canonical_data = []
for _, row in df.iterrows():
    c_artist, c_title = parse_artist_title(row)
    canonical_data.append((c_artist, c_title))

df['clean_artist'] = [x[0] for x in canonical_data]
df['clean_title'] = [x[1] for x in canonical_data]

# Remove punctuation/extra spaces for better matching
def normalize(s):
    # Remove non-alphanumeric chars (except spaces)
    s = re.sub(r'[^a-z0-9\s]', '', s)
    # Collapse spaces
    s = re.sub(r'\s+', ' ', s)
    return s.strip()

df['norm_artist'] = df['clean_artist'].apply(normalize)
df['norm_title'] = df['clean_title'].apply(normalize)

# Create a grouping key
df['group_key'] = df['norm_artist'] + "|||" + df['norm_title']

# Group by key and sum revenue
result = df.groupby('group_key')['revenue'].sum().reset_index()
result = result.sort_values('revenue', ascending=False)

# Get the top entry
top_entry = result.iloc[0]
top_key = top_entry['group_key']
top_revenue = top_entry['revenue']

# Retrieve original title/artist for display (just take the first one from the group)
# We need to find a representative row for this key
rep_row = df[df['group_key'] == top_key].iloc[0]

output = {
    "top_song_key": top_key,
    "revenue": top_revenue,
    "representative_title": rep_row['title'],
    "representative_artist": rep_row['artist'],
    "clean_title": rep_row['clean_title'],
    "clean_artist": rep_row['clean_artist']
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_function-call-4064444512275497395': 'file_storage/function-call-4064444512275497395.json', 'var_function-call-12792199908109322560': 'file_storage/function-call-12792199908109322560.json'}

exec(code, env_args)
