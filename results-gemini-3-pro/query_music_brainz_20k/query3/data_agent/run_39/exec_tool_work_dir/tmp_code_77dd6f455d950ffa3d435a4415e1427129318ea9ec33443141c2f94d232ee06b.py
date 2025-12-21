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

# Filter out empty or 'none' titles
df = df[df['clean_title'] != ""]
df = df[df['clean_title'] != "none"]

df['entity_key'] = df['clean_artist'] + " | " + df['clean_title']

grouped = df.groupby('entity_key')['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

top_10 = grouped.head(10)

# Check for "emerge"
emerge_tracks = df[df['clean_title'].str.contains("emerge", na=False)][['title', 'artist', 'clean_title', 'clean_artist', 'total_revenue']]

print('__RESULT__:')
print(json.dumps({
    "top_10": top_10.to_dict(orient='records'),
    "emerge_tracks": emerge_tracks.head(10).to_dict(orient='records')
}))"""

env_args = {'var_function-call-18029868950214320737': 'file_storage/function-call-18029868950214320737.json', 'var_function-call-17739212231820982163': 'file_storage/function-call-17739212231820982163.json', 'var_function-call-17897410870431219726': [{'entity_key': 'none | ', 'total_revenue': 50045.21}, {'entity_key': ' | ', 'total_revenue': 34469.57}, {'entity_key': 'none | none', 'total_revenue': 14647.52}, {'entity_key': 'fischerspooner | emerge', 'total_revenue': 6665.27}, {'entity_key': 'syb van der ploeg | zo gaat het leven aan je voor', 'total_revenue': 6636.1}, {'entity_key': 'ske | vagga', 'total_revenue': 6611.56}, {'entity_key': 'fausto papetti | lovers', 'total_revenue': 6259.3}, {'entity_key': 'vrisak generacije | ne veruj', 'total_revenue': 6125.34}, {'entity_key': 'neil biggin | chile', 'total_revenue': 6008.71}, {'entity_key': 'guts pie earshot | travel', 'total_revenue': 5825.26}], 'var_function-call-10266975241949612983': [{'track_id': '15003', 'title': '020-', 'artist': 'None', 'entity_key': 'none | ', 'total_revenue': 1506.69}, {'track_id': '16809', 'title': '009-   ', 'artist': 'None', 'entity_key': 'none | ', 'total_revenue': 986.3}, {'track_id': '7086', 'title': '010-', 'artist': 'None', 'entity_key': 'none | ', 'total_revenue': 1069.66}, {'track_id': '8237', 'title': '007-', 'artist': 'None', 'entity_key': 'none | ', 'total_revenue': 486.09}, {'track_id': '9044', 'title': '001-', 'artist': 'None', 'entity_key': 'none | ', 'total_revenue': 1435.13}, {'track_id': '14742', 'title': '018-', 'artist': 'None', 'entity_key': 'none | ', 'total_revenue': 1005.41}, {'track_id': '15005', 'title': '008-', 'artist': 'None', 'entity_key': 'none | ', 'total_revenue': 1089.64}, {'track_id': '16733', 'title': '012-', 'artist': ' ', 'entity_key': ' | ', 'total_revenue': 1560.87}, {'track_id': '3033', 'title': '006- (Inst-umental)', 'artist': 'None', 'entity_key': 'none | ', 'total_revenue': 420.04}, {'track_id': '4588', 'title': '1', 'artist': '195', 'entity_key': ' | ', 'total_revenue': 842.8}, {'track_id': '8975', 'title': '013', 'artist': '[unknown]', 'entity_key': ' | ', 'total_revenue': 174.09}, {'track_id': '9817', 'title': '009-  ', 'artist': ' ', 'entity_key': ' | ', 'total_revenue': 704.23}, {'track_id': '17910', 'title': '11', 'artist': '240440', 'entity_key': ' | ', 'total_revenue': 1409.67}, {'track_id': '19334', 'title': '013- ', 'artist': ' ', 'entity_key': ' | ', 'total_revenue': 860.35}, {'track_id': '1355', 'title': '005-', 'artist': 'None', 'entity_key': 'none | ', 'total_revenue': 615.7}, {'track_id': '4755', 'title': '016-', 'artist': 'None', 'entity_key': 'none | ', 'total_revenue': 93.62}, {'track_id': '10940', 'title': '025-', 'artist': 'None', 'entity_key': 'none | ', 'total_revenue': 334.34}, {'track_id': '12196', 'title': 'None', 'artist': 'None', 'entity_key': 'none | none', 'total_revenue': 344.89}, {'track_id': '14462', 'title': 'None', 'artist': 'None', 'entity_key': 'none | none', 'total_revenue': 972.52}, {'track_id': '19081', 'title': '009- ', 'artist': ' ', 'entity_key': ' | ', 'total_revenue': 1973.87}]}

exec(code, env_args)
