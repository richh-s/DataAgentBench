code = """import json
import pandas as pd
import re

# Load sales data
sales_file_path = locals()['var_function-call-5674796126939342252']
with open(sales_file_path, 'r') as f:
    sales_list = json.load(f)

# Load tracks data
tracks_file_path = locals()['var_function-call-14566705962041392697']
with open(tracks_file_path, 'r') as f:
    tracks_list = json.load(f)

# Convert to DataFrames
df_sales = pd.DataFrame(sales_list)
df_tracks = pd.DataFrame(tracks_list)

# Check revenue distribution
df_sales['total_revenue'] = df_sales['total_revenue'].astype(float)
# The list was top 2000 from the sales table query.
print(f"Revenue of 1st track: {df_sales.iloc[0]['total_revenue']}")
print(f"Revenue of 2000th track: {df_sales.iloc[-1]['total_revenue']}")

# Ensure track_id match
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Merge
df = pd.merge(df_sales, df_tracks, on='track_id', how='inner')

# Helper for normalization
def normalize_string(s):
    if not isinstance(s, str):
        return ""
    s = s.lower()
    # Remove content in parenthesis or brackets
    s = re.sub(r'\([^)]*\)', '', s)
    s = re.sub(r'\[[^]]*\]', '', s)
    # Remove punctuation
    s = re.sub(r'[^\w\s]', '', s)
    # Remove extra whitespace
    s = " ".join(s.split())
    return s

def clean_row(row):
    title = row['title']
    artist = row['artist']
    
    n_title = normalize_string(title)
    n_artist = normalize_string(artist)
    
    return pd.Series([n_title, n_artist])

df[['n_title', 'n_artist']] = df.apply(clean_row, axis=1)

# Group by normalized title and artist
grouped = df.groupby(['n_title', 'n_artist'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

# Get top result
top_row = grouped.iloc[0]

# Find original rows for this group to get a nice display name
top_n_title = top_row['n_title']
top_n_artist = top_row['n_artist']
original_rows = df[(df['n_title'] == top_n_title) & (df['n_artist'] == top_n_artist)]
best_display = original_rows.iloc[0]

result_obj = {
    "title": best_display['title'],
    "artist": best_display['artist'],
    "revenue": top_row['total_revenue'],
    "ids": original_rows['track_id'].tolist()
}

print("__RESULT__:")
print(json.dumps(result_obj))"""

env_args = {'var_function-call-14714155237110464570': 'file_storage/function-call-14714155237110464570.json', 'var_function-call-5674796126939342252': 'file_storage/function-call-5674796126939342252.json', 'var_function-call-436051087863725612': 'file_storage/function-call-436051087863725612.json', 'var_function-call-14566705962041392697': 'file_storage/function-call-14566705962041392697.json'}

exec(code, env_args)
