code = """import json
import pandas as pd
import re

# Load sales data
sales_file_path = locals()['var_function-call-14714155237110464570']
with open(sales_file_path, 'r') as f:
    sales_list = json.load(f)

# Load tracks data
tracks_file_path = locals()['var_function-call-14566705962041392697']
with open(tracks_file_path, 'r') as f:
    tracks_list = json.load(f)

df_sales = pd.DataFrame(sales_list)
df_tracks = pd.DataFrame(tracks_list)

df_sales['total_revenue'] = df_sales['total_revenue'].astype(float)
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

df = pd.merge(df_sales, df_tracks, on='track_id', how='inner')

def normalize_string(s):
    if not isinstance(s, str):
        return "none"
    s = s.lower()
    s = re.sub(r'\([^)]*\)', '', s)
    s = re.sub(r'\[[^]]*\]', '', s)
    s = re.sub(r'[^\w\s]', '', s)
    s = " ".join(s.split())
    if not s: return "none"
    return s

def clean_row(row):
    title = row['title']
    artist = row['artist']
    n_title = normalize_string(title)
    n_artist = normalize_string(artist)
    return pd.Series([n_title, n_artist])

df[['n_title', 'n_artist']] = df.apply(clean_row, axis=1)

grouped = df.groupby(['n_title', 'n_artist'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

# Get top 10
top_10 = grouped.head(10)
print("Top 10 groups:")
print(top_10)

# Also print the raw rows for the top 3 groups to see what's going on
print("\nDetails for top 3 groups:")
for index, row in grouped.head(3).iterrows():
    print(f"Group: {row['n_title']} | {row['n_artist']}")
    details = df[(df['n_title'] == row['n_title']) & (df['n_artist'] == row['n_artist'])]
    print(details[['track_id', 'title', 'artist', 'album', 'total_revenue']].to_string())
    print("-" * 20)

print("__RESULT__:")
print(json.dumps("Done"))"""

env_args = {'var_function-call-14714155237110464570': 'file_storage/function-call-14714155237110464570.json', 'var_function-call-5674796126939342252': 'file_storage/function-call-5674796126939342252.json', 'var_function-call-436051087863725612': 'file_storage/function-call-436051087863725612.json', 'var_function-call-14566705962041392697': 'file_storage/function-call-14566705962041392697.json', 'var_function-call-5965808366396911371': {'title': 'None', 'artist': 'None', 'revenue': 5201.42, 'ids': ['9788', '18790', '5048']}}

exec(code, env_args)
