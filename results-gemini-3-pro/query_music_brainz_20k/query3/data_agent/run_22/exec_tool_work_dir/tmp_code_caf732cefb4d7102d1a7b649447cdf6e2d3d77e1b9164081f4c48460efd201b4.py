code = """import json
import pandas as pd
import re

# Load tracks
with open(locals()['var_function-call-2457622807540925275'], 'r') as f:
    tracks = json.load(f)
df_tracks = pd.DataFrame(tracks)

# Load sales
with open(locals()['var_function-call-6100282308464487853'], 'r') as f:
    sales = json.load(f)
df_sales = pd.DataFrame(sales)

df_sales['revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_tracks['track_id'] = df_tracks['track_id'].astype(str)
df_sales['track_id'] = df_sales['track_id'].astype(str)
df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Helper for inspection
def search_artist(df, artist_fragment):
    # Case insensitive search in artist or title columns
    mask = df['artist'].astype(str).str.lower().str.contains(artist_fragment) | \
           df['title'].astype(str).str.lower().str.contains(artist_fragment)
    return df[mask][['track_id', 'artist', 'title', 'revenue']]

syb_records = search_artist(df, 'syb van der ploeg')
fischerspooner_records = search_artist(df, 'fischerspooner')
ske_records = search_artist(df, 'ske')

print("__RESULT__:")
print(json.dumps({
    "syb": syb_records.to_dict(orient='records'),
    "fischerspooner": fischerspooner_records.to_dict(orient='records'),
    "ske": ske_records.to_dict(orient='records')
}))"""

env_args = {'var_function-call-2457622807540925275': 'file_storage/function-call-2457622807540925275.json', 'var_function-call-6100282308464487853': 'file_storage/function-call-6100282308464487853.json', 'var_function-call-7903873907971748242': {'artist': '[Unknown]', 'title': 'None', 'revenue': 14647.52}, 'var_function-call-1063100188911444143': [{'norm_artist': 'rich matteson', 'norm_title': 'groovey', 'revenue': 5417.34}, {'norm_artist': 'luke bryan', 'norm_title': 'all my friends say (album version)', 'revenue': 4110.55}, {'norm_artist': 'kerstin gier', 'norm_title': 'kapitel 01', 'revenue': 4091.12}, {'norm_artist': 'damian marley', 'norm_title': 'beautiful (instrumental)', 'revenue': 4004.42}, {'norm_artist': 'matthew barber', 'norm_title': 'the story of your life', 'revenue': 3962.97}], 'var_function-call-15419448355779907791': [{'track_id': '2133', 'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan', 'revenue': 1501.6699999999998}, {'track_id': '8656', 'title': '001-Gator Whale', 'artist': 'Grooveyard', 'revenue': 294.01}, {'track_id': '17312', 'title': 'Groovey', 'artist': 'Rich Matteson', 'revenue': 1036.29}, {'track_id': '7710', 'title': '006-Groovey', 'artist': 'Rich Matteson', 'revenue': 251.16}, {'track_id': '6146', 'title': 'Rich Matteson - Groovey', 'artist': 'None', 'revenue': 1288.75}, {'track_id': '10416', 'title': '002-All My Friends Say (album version)', 'artist': 'Luke Bryan', 'revenue': 1070.38}, {'track_id': '16496', 'title': 'Groovey', 'artist': 'Rich Matteson', 'revenue': 949.82}, {'track_id': '12601', 'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan', 'revenue': 1739.54}, {'track_id': '3144', 'title': 'Luke Bryan - All My Friends Say (album version)', 'artist': 'None', 'revenue': 869.34}, {'track_id': '8829', 'title': 'Groovey', 'artist': 'Rich Matteson', 'revenue': 2142.48}], 'var_function-call-15239203607998021422': [{'artist': 'Fischerspooner', 'title': 'Emerge (Dexter remix)', 'revenue': 6665.27}, {'artist': 'Syb van der Ploeg', 'title': 'Zo gaat het leven aan je voor', 'revenue': 6636.1}, {'artist': 'Ske', 'title': 'Vagga', 'revenue': 6611.56}, {'artist': 'Fausto Papetti', 'title': 'Lovers', 'revenue': 6259.3}, {'artist': 'Vrisak generacije', 'title': 'Ne veruj', 'revenue': 6125.339999999999}], 'var_function-call-5750964522534525762': {'fischerspooner': [{'title': 'Emerge (Dave Clarke remix)', 'artist': 'Fischerspooner', 'revenue': 850.86, 'norm_title': 'emerge'}, {'title': 'Emerge (Dexter remix)', 'artist': 'Fischerspooner', 'revenue': 672.1200000000001, 'norm_title': 'emerge'}, {'title': 'Fischerspooner - Emerge (Dexter remix)', 'artist': 'None', 'revenue': 1610.46, 'norm_title': 'emerge'}, {'title': 'Emerge (Dexter remix) (#1)', 'artist': 'Fischerspooner', 'revenue': 1762.8000000000002, 'norm_title': 'emerge'}, {'title': 'Emerge (Dexter remix) - #1', 'artist': 'Fischerspooner', 'revenue': 850.61, 'norm_title': 'emerge  - #1'}, {'title': '027-Emerge (Dexter remix)', 'artist': 'Fischerspooner', 'revenue': 1769.03, 'norm_title': 'emerge'}], 'syb': [{'title': 'Zo gaat het leven aan je voor - Hillich fjoer | Heilig vuur', 'artist': 'Syb van der Ploeg', 'revenue': 2377.59, 'norm_title': 'zo gaat het leven aan je voor - hillich fjoer | heilig vuur'}, {'title': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'artist': 'Syb van der Ploeg', 'revenue': 1754.6800000000003, 'norm_title': 'zo gaat het leven aan je voor'}, {'title': '006-Zo gaat het leven aan je voor', 'artist': 'Syb van der Ploeg', 'revenue': 1379.6699999999998, 'norm_title': 'zo gaat het leven aan je voor'}, {'title': 'Syb van der Ploeg - Zo gaat het leven aan je voor', 'artist': 'None', 'revenue': 1477.38, 'norm_title': 'zo gaat het leven aan je voor'}, {'title': 'Zo gaat het leven aan je voor', 'artist': 'Syb van der Ploeg', 'revenue': 2024.37, 'norm_title': 'zo gaat het leven aan je voor'}]}, 'var_function-call-1935106887581339043': [{'norm_artist': 'fischerspooner', 'norm_title': 'emerge', 'revenue': 6665.27}, {'norm_artist': 'syb van der ploeg', 'norm_title': 'zo gaat het leven aan je voor', 'revenue': 6636.1}, {'norm_artist': 'ske', 'norm_title': 'vagga', 'revenue': 6611.56}, {'norm_artist': 'fausto papetti', 'norm_title': 'lovers', 'revenue': 6259.3}, {'norm_artist': 'vrisak generacije', 'norm_title': 'ne veruj', 'revenue': 6125.339999999999}, {'norm_artist': 'neil biggin', 'norm_title': 'chile', 'revenue': 6008.71}, {'norm_artist': 'guts pie earshot', 'norm_title': 'travel', 'revenue': 5825.26}, {'norm_artist': 'hotstylz', 'norm_title': 'lookin boy', 'revenue': 5712.889999999999}, {'norm_artist': 'rich matteson', 'norm_title': 'groovey', 'revenue': 5668.5}, {'norm_artist': 'pras', 'norm_title': 'ghetto supastar', 'revenue': 5514.57}, {'norm_artist': 'mike oldfield', 'norm_title': 'to be free', 'revenue': 5432.46}, {'norm_artist': 'berlin', 'norm_title': 'sex', 'revenue': 5420.799999999999}, {'norm_artist': 'love amongst ruin', 'norm_title': 'truth', 'revenue': 5379.110000000001}, {'norm_artist': 'wotan', 'norm_title': 'mother forest', 'revenue': 5277.67}, {'norm_artist': 'suzanne de bussac', 'norm_title': 'faded', 'revenue': 5251.56}, {'norm_artist': 'atb', 'norm_title': 'let u go', 'revenue': 5227.45}, {'norm_artist': 'luke bryan', 'norm_title': 'all my friends say', 'revenue': 5180.93}, {'norm_artist': 'lemon d', 'norm_title': 'jah love', 'revenue': 5168.450000000001}, {'norm_artist': 'power of dreams', 'norm_title': 'sky', 'revenue': 5087.81}, {'norm_artist': 'will kimbrough', 'norm_title': 'too beautiful', 'revenue': 4996.46}]}

exec(code, env_args)
