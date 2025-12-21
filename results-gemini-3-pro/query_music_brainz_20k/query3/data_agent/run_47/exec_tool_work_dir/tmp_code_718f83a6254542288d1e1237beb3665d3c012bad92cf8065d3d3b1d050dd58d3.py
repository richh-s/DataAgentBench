code = """import json
import pandas as pd

# Load sales data
with open(locals()['var_function-call-18145844648055813096'], 'r') as f:
    sales_data = json.load(f)

# Load tracks data
with open(locals()['var_function-call-16557127791975595763'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_sales['revenue_usd'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)

df_tracks = pd.DataFrame(tracks_data)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Merge
merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Entity Resolution helper
def normalize(text):
    if text is None:
        return ""
    text = str(text).lower().strip()
    return text

merged['norm_title'] = merged['title'].apply(normalize)
merged['norm_artist'] = merged['artist'].apply(normalize)

# Some entries have artist as 'none' or '[unknown]', maybe treat as empty string?
# But if there are two songs named "Hello" by different unknown artists, are they the same?
# Without better info, I will assume title+artist defines the song.

# Handling messy titles:
# The hint says: duplicates may not match exactly (e.g., different year formats or minor attribute variations).
# So I should group by norm_title and norm_artist.
# Let's inspect the top rows after grouping to see if I need more fuzzy matching.

grouped = merged.groupby(['norm_title', 'norm_artist'])['revenue_usd'].sum().reset_index()
grouped = grouped.sort_values('revenue_usd', ascending=False)

# Print top 10 candidates to inspect
print("__RESULT__:")
print(grouped.head(20).to_json(orient='records'))"""

env_args = {'var_function-call-18145844648055813096': 'file_storage/function-call-18145844648055813096.json', 'var_function-call-16557127791975595763': 'file_storage/function-call-16557127791975595763.json'}

exec(code, env_args)
