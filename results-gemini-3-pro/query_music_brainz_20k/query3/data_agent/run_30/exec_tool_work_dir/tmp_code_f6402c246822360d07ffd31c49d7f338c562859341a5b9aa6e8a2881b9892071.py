code = """import pandas as pd
import json
import re

sales_file = locals()['var_function-call-9771478070084226116']
tracks_file = locals()['var_function-call-14488292253542672495']

with open(sales_file, 'r') as f:
    sales_data = json.load(f)
with open(tracks_file, 'r') as f:
    tracks_data = json.load(f)

sales_df = pd.DataFrame(sales_data)
tracks_df = pd.DataFrame(tracks_data)

sales_df['total_revenue'] = pd.to_numeric(sales_df['total_revenue'])
sales_df['track_id'] = sales_df['track_id'].astype(str)
tracks_df['track_id'] = tracks_df['track_id'].astype(str)

df = pd.merge(sales_df, tracks_df, on='track_id', how='left')

def clean_string(s):
    if not s:
        return ""
    s = str(s).lower().strip()
    if s in ["none", "unknown", "[unknown]", ""]:
        return ""
    return s

def resolve_entity(row):
    title = clean_string(row['title'])
    artist = clean_string(row['artist'])
    title = re.sub(r'^\d+[-.\s]+', '', title)
    if not artist:
        if " - " in title:
            parts = title.split(" - ", 1)
            artist = parts[0].strip()
            title = parts[1].strip()
    return pd.Series([artist, title])

df[['clean_artist', 'clean_title']] = df.apply(resolve_entity, axis=1)

# Debug empty group
empty_group = df[(df['clean_artist'] == "") & (df['clean_title'] == "")]
empty_sample = empty_group[['title', 'artist', 'total_revenue']].head(10).to_dict(orient='records')

# Valid groups
grouped = df.groupby(['clean_artist', 'clean_title'])['total_revenue'].sum().reset_index()
# Filter out empty title
grouped = grouped[grouped['clean_title'] != ""]

top_songs = grouped.sort_values(by='total_revenue', ascending=False).head(5).to_dict(orient='records')

result = {
    "empty_group_sample": empty_sample,
    "top_valid_songs": top_songs
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9771478070084226116': 'file_storage/function-call-9771478070084226116.json', 'var_function-call-14488292253542672495': 'file_storage/function-call-14488292253542672495.json', 'var_function-call-17561032650953691721': [{'clean_artist': '', 'clean_title': '', 'total_revenue': 77153.05}, {'clean_artist': 'rich matteson', 'clean_title': 'groovey', 'total_revenue': 5668.5}, {'clean_artist': 'luke bryan', 'clean_title': 'all my friends say (album version)', 'total_revenue': 5180.93}, {'clean_artist': 'pras', 'clean_title': 'ghetto supastar (that is what you are)', 'total_revenue': 4933.98}, {'clean_artist': 'frankie goes to hollywood', 'clean_title': 'the power of love (rob searle club mix)', 'total_revenue': 4909.04}], 'var_function-call-8593933683819508975': 'Done'}

exec(code, env_args)
