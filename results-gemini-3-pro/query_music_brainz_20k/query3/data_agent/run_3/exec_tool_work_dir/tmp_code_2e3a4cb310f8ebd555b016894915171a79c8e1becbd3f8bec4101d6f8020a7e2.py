code = """import pandas as pd
import json
import re

# Load sales data
with open(locals()['var_function-call-4743792908613703522'], 'r') as f:
    sales_data = json.load(f)

# Load tracks data
with open(locals()['var_function-call-12334345703939438194'], 'r') as f:
    tracks_data = json.load(f)

# Create DataFrames
df_sales = pd.DataFrame(sales_data)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)

df_tracks = pd.DataFrame(tracks_data)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Merge
df = pd.merge(df_tracks, df_sales, on='track_id', how='left')
df['total_revenue'] = df['total_revenue'].fillna(0.0)

# Normalization function
def normalize(text):
    if not isinstance(text, str):
        return ""
    # Lowercase
    text = text.lower()
    # Remove text in parentheses/brackets (often metadata like remix, live, etc.)
    # But be careful, sometimes it's part of the title.
    # For a broad "song" query, removing might be better.
    # text = re.sub(r'\([^)]*\)', '', text)
    # text = re.sub(r'\[[^\]]*\]', '', text)
    # Remove special chars
    # text = re.sub(r'[^a-z0-9\s]', '', text)
    # Collapse spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

df['norm_title'] = df['title'].apply(normalize)
df['norm_artist'] = df['artist'].apply(normalize)

# Group by normalized title and artist
grouped = df.groupby(['norm_title', 'norm_artist'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

print("__RESULT__:")
print(grouped.head(20).to_json(orient='records'))"""

env_args = {'var_function-call-4743792908613703522': 'file_storage/function-call-4743792908613703522.json', 'var_function-call-12334345703939438194': 'file_storage/function-call-12334345703939438194.json'}

exec(code, env_args)
