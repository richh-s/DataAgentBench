code = """import pandas as pd
import json
import re

# Load data
with open(locals()['var_function-call-5081543937369851313'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-2523656843503739436'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_tracks = pd.DataFrame(tracks_data)

df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

df = pd.merge(df_sales, df_tracks, on='track_id')

def normalize_string(s):
    if not isinstance(s, str):
        return str(s)
    s = re.sub(r'\(.*?\)', '', s)
    s = re.sub(r'\[.*?\]', '', s)
    s = " ".join(s.split())
    return s.lower()

def resolve_entity(row):
    title = str(row['title'])
    artist = str(row['artist'])
    missing = ['none', 'unknown', '[unknown]', '', 'null']
    if artist.lower().strip() in missing:
        if ' - ' in title:
            parts = title.split(' - ', 1)
            artist = parts[0]
            title = parts[1]
    return pd.Series([normalize_string(title), normalize_string(artist)])

cleaned_cols = df.apply(resolve_entity, axis=1)
df['clean_title'] = cleaned_cols[0]
df['clean_artist'] = cleaned_cols[1]

# Filter garbage
mask = (df['clean_artist'] != 'none') & (df['clean_title'] != 'none') & (~df['clean_title'].str.startswith('00'))
df_valid = df[mask]

grouped = df_valid.groupby(['clean_artist', 'clean_title'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

print('__RESULT__:')
print(grouped.head(5).to_json(orient='records'))

# Check for variants of top candidate
top_candidate = grouped.iloc[0]
print("Top candidate variants:")
variants = df_valid[
    (df_valid['clean_artist'].str.contains(top_candidate['clean_artist'], regex=False)) |
    (df_valid['clean_title'].str.contains(top_candidate['clean_title'], regex=False))
]
# Group by original title/artist to see what was merged
print(variants.groupby(['artist', 'title'])['total_revenue'].sum().reset_index().to_json(orient='records'))"""

env_args = {'var_function-call-5081543937369851313': 'file_storage/function-call-5081543937369851313.json', 'var_function-call-2523656843503739436': 'file_storage/function-call-2523656843503739436.json', 'var_function-call-543709723877492397': [{'clean_artist': 'none', 'clean_title': 'none', 'total_revenue': 14647.52}, {'clean_artist': 'rich matteson', 'clean_title': 'groovey', 'total_revenue': 5417.34}, {'clean_artist': 'syb van der ploeg', 'clean_title': 'zo gaat het leven aan je voor', 'total_revenue': 5256.43}, {'clean_artist': 'ske', 'clean_title': 'vagga', 'total_revenue': 4981.38}, {'clean_artist': 'none', 'clean_title': '001-', 'total_revenue': 4927.17}, {'clean_artist': 'fischerspooner', 'clean_title': 'emerge', 'total_revenue': 4896.24}, {'clean_artist': 'hans zimmer', 'clean_title': 'best friends', 'total_revenue': 4806.24}, {'clean_artist': 'none', 'clean_title': '003-', 'total_revenue': 4773.37}, {'clean_artist': 'vrisak generacije', 'clean_title': 'ne veruj', 'total_revenue': 4693.26}, {'clean_artist': '服部隆之', 'clean_title': 'lifework', 'total_revenue': 4663.91}]}

exec(code, env_args)
