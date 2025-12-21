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
    if not isinstance(s, str) or s.lower() == 'none':
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

# Filter out 'none' titles
valid_grouped = grouped[grouped['n_title'] != 'none']

if not valid_grouped.empty:
    top_row = valid_grouped.iloc[0]
    
    # Get display info
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
else:
    result_obj = {"error": "No valid tracks found"}

print("__RESULT__:")
print(json.dumps(result_obj))"""

env_args = {'var_function-call-14714155237110464570': 'file_storage/function-call-14714155237110464570.json', 'var_function-call-5674796126939342252': 'file_storage/function-call-5674796126939342252.json', 'var_function-call-436051087863725612': 'file_storage/function-call-436051087863725612.json', 'var_function-call-14566705962041392697': 'file_storage/function-call-14566705962041392697.json', 'var_function-call-5965808366396911371': {'title': 'None', 'artist': 'None', 'revenue': 5201.42, 'ids': ['9788', '18790', '5048']}}

exec(code, env_args)
