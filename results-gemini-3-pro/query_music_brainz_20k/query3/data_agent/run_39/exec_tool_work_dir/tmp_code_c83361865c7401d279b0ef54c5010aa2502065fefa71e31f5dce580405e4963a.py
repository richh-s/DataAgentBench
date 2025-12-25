code = """import json
import pandas as pd
import re

with open(locals()['var_function-call-18029868950214320737'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-17739212231820982163'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = re.sub(r'\(.*?\)', '', text)
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'^\s*\d+[-.]?\s*', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text.lower()

def resolve_entity(row):
    title = row['title']
    artist = row['artist']
    if not artist or artist.lower() in ['none', '[unknown]', '']:
        if isinstance(title, str) and ' - ' in title:
            parts = title.split(' - ', 1)
            artist = parts[0]
            title = parts[1]
    
    clean_t = clean_text(title)
    clean_a = clean_text(artist)
    return clean_t, clean_a

resolved = df.apply(resolve_entity, axis=1, result_type='expand')
df['clean_title'] = resolved[0]
df['clean_artist'] = resolved[1]
df['entity_key'] = df['clean_artist'] + " | " + df['clean_title']

# Inspect the problematic keys
problem_keys = ["none | ", " | ", "none | none"]
problem_rows = df[df['entity_key'].isin(problem_keys)][['track_id', 'title', 'artist', 'entity_key', 'total_revenue']]

print('__RESULT__:')
print(problem_rows.head(20).to_json(orient='records'))"""

env_args = {'var_function-call-18029868950214320737': 'file_storage/function-call-18029868950214320737.json', 'var_function-call-17739212231820982163': 'file_storage/function-call-17739212231820982163.json', 'var_function-call-17897410870431219726': [{'entity_key': 'none | ', 'total_revenue': 50045.21}, {'entity_key': ' | ', 'total_revenue': 34469.57}, {'entity_key': 'none | none', 'total_revenue': 14647.52}, {'entity_key': 'fischerspooner | emerge', 'total_revenue': 6665.27}, {'entity_key': 'syb van der ploeg | zo gaat het leven aan je voor', 'total_revenue': 6636.1}, {'entity_key': 'ske | vagga', 'total_revenue': 6611.56}, {'entity_key': 'fausto papetti | lovers', 'total_revenue': 6259.3}, {'entity_key': 'vrisak generacije | ne veruj', 'total_revenue': 6125.34}, {'entity_key': 'neil biggin | chile', 'total_revenue': 6008.71}, {'entity_key': 'guts pie earshot | travel', 'total_revenue': 5825.26}]}

exec(code, env_args)
