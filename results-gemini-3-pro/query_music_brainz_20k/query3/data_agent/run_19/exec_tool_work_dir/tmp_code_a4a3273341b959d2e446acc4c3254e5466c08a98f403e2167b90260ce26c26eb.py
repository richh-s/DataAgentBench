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

df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

df_merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')

def clean_field(text):
    if text is None:
        return ""
    s = str(text).strip()
    if s.lower() in ['none', 'null', 'nan', '[unknown]', 'unknown', '']:
        return ""
    return s

df_merged['clean_title'] = df_merged['title'].apply(clean_field)
df_merged['clean_artist'] = df_merged['artist'].apply(clean_field)

# Filter out rows where title or artist is empty
# (Or maybe just title? If artist is unknown, it might still be a valid song revenue. 
# But if title is missing, it's definitely not a specific song.)
# Based on previous result, "001-" had "None" artist.
# Let's filter out if clean_title is empty or looks like garbage (e.g. "001-", "002").
# Regex to identify "garbage" numeric titles?
# ^[0-9]+[- ]*$ or similar.

def is_valid_title(title):
    if not title:
        return False
    # Check if title is just digits and special chars
    if re.match(r'^[\d\W_]+$', title):
        return False
    return True

df_valid = df_merged[df_merged['clean_title'].apply(is_valid_title)].copy()

# Normalize for grouping
df_valid['norm_title'] = df_valid['clean_title'].apply(lambda x: re.sub(r'[^\w\s]', '', x).lower().strip())
df_valid['norm_artist'] = df_valid['clean_artist'].apply(lambda x: re.sub(r'[^\w\s]', '', x).lower().strip())

# Group
grouped = df_valid.groupby(['norm_title', 'norm_artist'])['total_revenue'].sum().reset_index()

# Sort
top_revenue = grouped.sort_values('total_revenue', ascending=False).head(20)

results = []
for index, row in top_revenue.iterrows():
    # Get representative
    # We want to show the one with the most metadata or just the first
    mask = (df_valid['norm_title'] == row['norm_title']) & (df_valid['norm_artist'] == row['norm_artist'])
    sample = df_valid[mask].iloc[0]
    
    results.append({
        "title": sample['title'],
        "artist": sample['artist'],
        "revenue": row['total_revenue']
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-9876152415190698502': 'file_storage/function-call-9876152415190698502.json', 'var_function-call-8988901171834631000': 'file_storage/function-call-8988901171834631000.json', 'var_function-call-10056493367563797489': [{'title': 'None', 'artist': 'None', 'norm_title': 'none', 'norm_artist': 'none', 'total_revenue': 14647.52}, {'title': '001-', 'artist': 'None', 'norm_title': '001', 'norm_artist': 'none', 'total_revenue': 4681.75}, {'title': '005-', 'artist': 'None', 'norm_title': '005', 'norm_artist': 'none', 'total_revenue': 4281.18}, {'title': '002', 'artist': 'None', 'norm_title': '002', 'norm_artist': 'none', 'total_revenue': 4237.16}, {'title': '010-', 'artist': 'None', 'norm_title': '010', 'norm_artist': 'none', 'total_revenue': 4163.48}, {'title': 'Groovey', 'artist': 'Rich Matteson', 'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'total_revenue': 4128.59}, {'title': '004- ', 'artist': ' ', 'norm_title': '004', 'norm_artist': '', 'total_revenue': 4026.71}, {'title': 'The Fire Still Burns', 'artist': 'Russ Ballard', 'norm_title': 'the fire still burns', 'norm_artist': 'russ ballard', 'total_revenue': 3807.4}, {'title': 'Vostok', 'artist': 'Craig Padilla', 'norm_title': 'vostok', 'norm_artist': 'craig padilla', 'total_revenue': 3767.95}, {'title': '003-', 'artist': 'None', 'norm_title': '003', 'norm_artist': 'none', 'total_revenue': 3695.73}]}

exec(code, env_args)
