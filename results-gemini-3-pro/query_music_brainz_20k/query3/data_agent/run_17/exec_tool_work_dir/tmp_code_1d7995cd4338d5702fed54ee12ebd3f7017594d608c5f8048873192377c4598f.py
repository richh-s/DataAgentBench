code = """import pandas as pd
import json

sales_file_path = locals()['var_function-call-17358517250979617377']
tracks_file_path = locals()['var_function-call-17358517250979616604']

with open(sales_file_path, 'r') as f:
    sales_data = json.load(f)
with open(tracks_file_path, 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

df_sales['track_id'] = df_sales['track_id'].astype(str)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Lowercase for searching
df['l_title'] = df['title'].astype(str).str.lower()
df['l_artist'] = df['artist'].astype(str).str.lower()

results = {}

# Check for Fischerspooner / Emerge
mask_emerge = (df['l_title'].str.contains('emerge')) & (df['l_artist'].str.contains('fischerspooner') | df['l_title'].str.contains('fischerspooner'))
results['emerge'] = df[mask_emerge][['track_id', 'title', 'artist', 'total_revenue']].to_dict(orient='records')

# Check for Syb / Zo gaat
mask_syb = (df['l_title'].str.contains('zo gaat')) & (df['l_artist'].str.contains('syb') | df['l_title'].str.contains('syb'))
results['syb'] = df[mask_syb][['track_id', 'title', 'artist', 'total_revenue']].to_dict(orient='records')

# Check for Ske / Vagga
mask_ske = (df['l_title'].str.contains('vagga')) & (df['l_artist'].str.contains('ske') | df['l_title'].str.contains('ske'))
results['ske'] = df[mask_ske][['track_id', 'title', 'artist', 'total_revenue']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_function-call-17358517250979617377': 'file_storage/function-call-17358517250979617377.json', 'var_function-call-17358517250979616604': 'file_storage/function-call-17358517250979616604.json', 'var_function-call-14405160276735663835': [{'clean_title': 'none', 'clean_artist': 'none', 'total_revenue': 14647.52}, {'clean_title': '010-', 'clean_artist': 'none', 'total_revenue': 4163.48}, {'clean_title': 'groovey', 'clean_artist': 'rich matteson', 'total_revenue': 4128.59}, {'clean_title': 'the fire still burns', 'clean_artist': 'russ ballard', 'total_revenue': 3807.4}, {'clean_title': 'vostok', 'clean_artist': 'craig padilla', 'total_revenue': 3767.95}, {'clean_title': '001-', 'clean_artist': 'none', 'total_revenue': 3742.44}, {'clean_title': '003-', 'clean_artist': 'none', 'total_revenue': 3446.78}, {'clean_title': '003-', 'clean_artist': '', 'total_revenue': 3394.4}, {'clean_title': '005-', 'clean_artist': 'none', 'total_revenue': 3347.89}, {'clean_title': '002-', 'clean_artist': 'none', 'total_revenue': 3343.61}, {'clean_title': 'all my friends say (album version)', 'clean_artist': 'luke bryan', 'total_revenue': 3241.21}, {'clean_title': 'beautiful (instrumental)', 'clean_artist': 'damian marley', 'total_revenue': 3228.62}, {'clean_title': 'private soul security', 'clean_artist': 'down below', 'total_revenue': 3218.63}, {'clean_title': 'unknown', 'clean_artist': 'none', 'total_revenue': 3218.35}, {'clean_title': 'bring back the love (spaced out dub)', 'clean_artist': 'laura harris', 'total_revenue': 3171.7}, {'clean_title': 'chi to rome (broke one edit)', 'clean_artist': 'lazy ants & rob threezy', 'total_revenue': 3091.77}, {'clean_title': 'bad hearts', 'clean_artist': 'tights', 'total_revenue': 3052.75}, {'clean_title': 'al stewart - year of the cat', 'clean_artist': 'none', 'total_revenue': 3049.93}, {'clean_title': 'skin', 'clean_artist': 'westworld', 'total_revenue': 3008.01}, {'clean_title': 'christmas in my heart', 'clean_artist': 'candi staton', 'total_revenue': 2969.33}], 'var_function-call-10564647232742443246': [{'norm_title': 'emerge', 'norm_artist': 'fischerspooner', 'total_revenue': 6665.27}, {'norm_title': 'zo gaat het leven aan je voor', 'norm_artist': 'syb van der ploeg', 'total_revenue': 6636.1}, {'norm_title': 'vagga', 'norm_artist': 'ske', 'total_revenue': 6611.56}, {'norm_title': 'lovers', 'norm_artist': 'fausto papetti', 'total_revenue': 6259.3}, {'norm_title': 'ne veruj', 'norm_artist': 'vrisak generacije', 'total_revenue': 6125.34}, {'norm_title': 'chile', 'norm_artist': 'neil biggin', 'total_revenue': 6008.71}, {'norm_title': 'travel', 'norm_artist': 'guts pie earshot', 'total_revenue': 5825.26}, {'norm_title': 'lookin boy', 'norm_artist': 'hotstylz', 'total_revenue': 5712.89}, {'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'total_revenue': 5668.5}, {'norm_title': 'ghetto supastar', 'norm_artist': 'pras', 'total_revenue': 5514.57}, {'norm_title': 'to be free', 'norm_artist': 'mike oldfield', 'total_revenue': 5432.46}, {'norm_title': 'sex', 'norm_artist': 'berlin', 'total_revenue': 5420.8}, {'norm_title': 'truth', 'norm_artist': 'love amongst ruin', 'total_revenue': 5379.11}, {'norm_title': 'mother forest', 'norm_artist': 'wotan', 'total_revenue': 5277.67}, {'norm_title': 'faded', 'norm_artist': 'suzanne de bussac', 'total_revenue': 5251.56}, {'norm_title': 'let u go', 'norm_artist': 'atb', 'total_revenue': 5227.45}, {'norm_title': 'all my friends say', 'norm_artist': 'luke bryan', 'total_revenue': 5180.93}, {'norm_title': 'jah love', 'norm_artist': 'lemon d', 'total_revenue': 5168.45}, {'norm_title': 'sky', 'norm_artist': 'power of dreams', 'total_revenue': 5087.81}, {'norm_title': 'too beautiful', 'norm_artist': 'will kimbrough', 'total_revenue': 4996.46}], 'var_function-call-16174425308423729334': {'emerge by fischerspooner': [{'track_id': '7575', 'title': 'Emerge (Dave Clarke remix)', 'artist': 'Fischerspooner', 'total_revenue': 850.86}, {'track_id': '10606', 'title': 'Emerge (Dexter remix)', 'artist': 'Fischerspooner', 'total_revenue': 672.1200000000001}, {'track_id': '4895', 'title': 'Fischerspooner - Emerge (Dexter remix)', 'artist': 'None', 'total_revenue': 1610.46}, {'track_id': '6988', 'title': 'Emerge (Dexter remix) (#1)', 'artist': 'Fischerspooner', 'total_revenue': 1762.8000000000002}, {'track_id': '17167', 'title': '027-Emerge (Dexter remix)', 'artist': 'Fischerspooner', 'total_revenue': 1769.03}], 'zo gaat het leven aan je voor by syb van der ploeg': [{'track_id': '3024', 'title': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'artist': 'Syb van der Ploeg', 'total_revenue': 1754.6800000000003}, {'track_id': '12854', 'title': '006-Zo gaat het leven aan je voor', 'artist': 'Syb van der Ploeg', 'total_revenue': 1379.6699999999998}, {'track_id': '13225', 'title': 'Syb van der Ploeg - Zo gaat het leven aan je voor', 'artist': 'None', 'total_revenue': 1477.38}, {'track_id': '3435', 'title': 'Zo gaat het leven aan je voor', 'artist': 'Syb van der Ploeg', 'total_revenue': 2024.37}], 'vagga by ske': [{'track_id': '6188', 'title': 'Ske - Vagga', 'artist': 'None', 'total_revenue': 1459.5600000000002}, {'track_id': '17878', 'title': '011-Vagga', 'artist': 'Ske', 'total_revenue': 1630.18}, {'track_id': '14686', 'title': 'Vagga (Feelings Are Great)', 'artist': 'Ske', 'total_revenue': 2163.69}, {'track_id': '12735', 'title': 'Vagga', 'artist': 'Ske', 'total_revenue': 1358.13}]}}

exec(code, env_args)
