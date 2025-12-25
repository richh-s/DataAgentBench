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
def clean_title(title):
    if not isinstance(title, str):
        return ""
    t = title.lower().strip()
    t = re.sub(r'^\d+[\.\-\s]+', '', t) # Remove leading numbers
    t = re.sub(r'\s*\(.*?\)', '', t) # Remove (...)
    t = re.sub(r'\s*\[.*?\]', '', t) # Remove [...]
    t = re.sub(r'\s+', ' ', t).strip()
    return t

def clean_artist(artist):
    if not isinstance(artist, str) or artist.lower() in ['none', '[unknown]', '']:
        return "unknown"
    return artist.lower().strip()

df['clean_title'] = df['clean_title'] = df['title'].apply(clean_title)
df['clean_artist'] = df['clean_artist'] = df['artist'].apply(clean_artist)

# Filter out bad data
# valid title: len > 1, not "none", not "track"
df_valid = df[
    (df['clean_title'].str.len() > 1) & 
    (df['clean_title'] != 'none') & 
    (df['clean_artist'] != 'unknown')
].copy()

# Group
grouped = df_valid.groupby(['clean_artist', 'clean_title'])['revenue_usd'].sum().reset_index()

# Get top 5
top_revenue = grouped.sort_values('revenue_usd', ascending=False).head(5)

# Join back to get a representative original title/artist for display
# We'll just take the first one found in the group
results = []
for index, row in top_revenue.iterrows():
    # Find one original record
    original = df_valid[
        (df_valid['clean_artist'] == row['clean_artist']) & 
        (df_valid['clean_title'] == row['clean_title'])
    ].iloc[0]
    
    results.append({
        "artist": original['artist'],
        "title": original['title'],
        "clean_artist": row['clean_artist'],
        "clean_title": row['clean_title'],
        "revenue_usd": row['revenue_usd']
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-18223064204633629849': 'file_storage/function-call-18223064204633629849.json', 'var_function-call-4676097286613530552': 'file_storage/function-call-4676097286613530552.json', 'var_function-call-163489723723416212': [{'clean_artist': 'unknown', 'clean_title': '', 'revenue_usd': 43888.21}, {'clean_artist': '', 'clean_title': '', 'revenue_usd': 19489.71}, {'clean_artist': 'unknown', 'clean_title': 'none', 'revenue_usd': 14647.52}, {'clean_artist': 'syb van der ploeg', 'clean_title': 'zo gaat het leven aan je voor', 'revenue_usd': 5158.72}, {'clean_artist': 'ske', 'clean_title': 'vagga', 'revenue_usd': 5152.0}, {'clean_artist': 'fischerspooner', 'clean_title': 'emerge', 'revenue_usd': 5054.81}, {'clean_artist': 'guts pie earshot', 'clean_title': 'travel', 'revenue_usd': 4933.9}, {'clean_artist': 'scott walker', 'clean_title': 'stormy', 'revenue_usd': 4677.15}, {'clean_artist': 'neil biggin', 'clean_title': 'chile', 'revenue_usd': 4676.22}, {'clean_artist': 'vrisak generacije', 'clean_title': 'ne veruj', 'revenue_usd': 4667.12}]}

exec(code, env_args)
