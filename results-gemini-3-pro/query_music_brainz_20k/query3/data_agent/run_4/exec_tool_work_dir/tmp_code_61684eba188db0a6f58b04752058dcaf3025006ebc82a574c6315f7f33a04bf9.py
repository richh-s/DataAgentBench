code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-3331083869601689377'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-11133696600522148060'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

# Convert types
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])

df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Merge
df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Normalization function
def normalize_text(text):
    if text is None:
        return ""
    text = str(text).lower().strip()
    # Remove leading numbers like "01-", "001 ", "01."
    text = re.sub(r'^\d+[\.\-\s]+', '', text)
    # Remove special characters but keep spaces
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

df['norm_title'] = df['title'].apply(normalize_text)
df['norm_artist'] = df['artist'].apply(normalize_text)

# Handle cases where artist is 'none', 'unknown', etc.
invalid_artists = ['', 'none', 'unknown', '[unknown]']
df.loc[df['norm_artist'].isin(invalid_artists), 'norm_artist'] = 'unknown'

# Group by normalized title and artist
grouped = df.groupby(['norm_title', 'norm_artist'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values(by='total_revenue', ascending=False)

# Get top 5
top_5 = grouped.head(5)

print("__RESULT__:")
print(top_5.to_json(orient='records'))"""

env_args = {'var_function-call-3331083869601689377': 'file_storage/function-call-3331083869601689377.json', 'var_function-call-11133696600522148060': 'file_storage/function-call-11133696600522148060.json'}

exec(code, env_args)
