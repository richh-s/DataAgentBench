code = """import json
import pandas as pd
import re

sales_file_path = locals()['var_function-call-3874821068292434244']
tracks_file_path = locals()['var_function-call-13479378208221018498']

with open(sales_file_path, 'r') as f:
    sales_data = json.load(f)
with open(tracks_file_path, 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

df_sales['track_id'] = df_sales['track_id'].astype(str)
df_sales['total_revenue'] = df_sales['total_revenue'].astype(float)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

df_merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')

df_merged['norm_title'] = df_merged['title'].astype(str).str.lower().str.strip()

# Check for 'ghetto supastar' variations
matches = df_merged[df_merged['norm_title'].str.contains("ghetto supastar")]
grouped_matches = matches.groupby(['title', 'artist'])['total_revenue'].sum().reset_index()

print("__RESULT__:")
print(grouped_matches.to_json(orient='records'))"""

env_args = {'var_function-call-3874821068292434244': 'file_storage/function-call-3874821068292434244.json', 'var_function-call-13479378208221018498': 'file_storage/function-call-13479378208221018498.json', 'var_function-call-13071031815735748921': {'song': 'None', 'artist': 'None', 'revenue': 14647.52}, 'var_function-call-589650206586176752': [{'original_title': '003-', 'original_artist': 'None', 'revenue': 6841.18}, {'original_title': '005-', 'original_artist': 'None', 'revenue': 5222.0}, {'original_title': '009-  ', 'original_artist': ' ', 'revenue': 5045.700000000001}, {'original_title': '004- ', 'original_artist': ' ', 'revenue': 4868.47}, {'original_title': '010-', 'original_artist': 'None', 'revenue': 4734.36}], 'var_function-call-16848924789855013177': [{'original_title': '003-', 'original_artist': 'None', 'revenue': 6841.18}, {'original_title': '005-', 'original_artist': 'None', 'revenue': 5222.0}, {'original_title': '009-  ', 'original_artist': ' ', 'revenue': 5045.700000000001}, {'original_title': '004- ', 'original_artist': ' ', 'revenue': 4868.47}, {'original_title': '010-', 'original_artist': 'None', 'revenue': 4734.36}, {'original_title': 'Groovey', 'original_artist': 'Rich Matteson', 'revenue': 4128.59}, {'original_title': '002-', 'original_artist': ' ', 'revenue': 4119.89}, {'original_title': '006- ', 'original_artist': ' ', 'revenue': 3946.7799999999997}, {'original_title': 'The Fire Still Burns', 'original_artist': 'Russ Ballard', 'revenue': 3807.4}, {'original_title': 'Vostok', 'original_artist': 'Craig Padilla', 'revenue': 3767.95}, {'original_title': '001-', 'original_artist': 'None', 'revenue': 3742.4399999999996}, {'original_title': '012-', 'original_artist': ' ', 'revenue': 3635.13}, {'original_title': 'All My Friends Say (album version)', 'original_artist': 'Luke Bryan', 'revenue': 3241.21}, {'original_title': 'Beautiful (instrumental)', 'original_artist': 'Damian Marley', 'revenue': 3228.62}, {'original_title': 'Private Soul Security', 'original_artist': 'Down Below', 'revenue': 3218.63}, {'original_title': 'unknown', 'original_artist': 'None', 'revenue': 3218.35}, {'original_title': 'Bring Back the Love (Spaced Out dub)', 'original_artist': 'Laura Harris', 'revenue': 3171.7}, {'original_title': 'Chi to Rome (Broke One edit)', 'original_artist': 'Lazy Ants & Rob Threezy', 'revenue': 3091.77}, {'original_title': 'Bad Hearts', 'original_artist': 'Tights', 'revenue': 3052.75}, {'original_title': 'Al Stewart - Year of the Cat', 'original_artist': 'None', 'revenue': 3049.9300000000003}], 'var_function-call-16086799054736622991': {'song': 'Groovey', 'artist': 'Rich Matteson', 'revenue': 4128.59}, 'var_function-call-8615079744666335593': [{'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'total_revenue': 4128.59}, {'norm_title': 'the fire still burns', 'norm_artist': 'russ ballard', 'total_revenue': 3807.4}, {'norm_title': 'vostok', 'norm_artist': 'craig padilla', 'total_revenue': 3767.95}, {'norm_title': 'all my friends say (album version)', 'norm_artist': 'luke bryan', 'total_revenue': 3241.21}, {'norm_title': 'beautiful (instrumental)', 'norm_artist': 'damian marley', 'total_revenue': 3228.62}, {'norm_title': 'private soul security', 'norm_artist': 'down below', 'total_revenue': 3218.63}, {'norm_title': 'bring back the love (spaced out dub)', 'norm_artist': 'laura harris', 'total_revenue': 3171.7}, {'norm_title': 'chi to rome (broke one edit)', 'norm_artist': 'lazy ants & rob threezy', 'total_revenue': 3091.77}, {'norm_title': 'bad hearts', 'norm_artist': 'tights', 'total_revenue': 3052.75}, {'norm_title': 'al stewart - year of the cat', 'norm_artist': '', 'total_revenue': 3049.93}], 'var_function-call-11025977903191235322': [{'title': '006-Groovey', 'artist': 'Rich Matteson', 'total_revenue': 251.16}, {'title': 'A Groovy Kind of Love (Gold & Platinum, Volume 6)', 'artist': 'Phil Collins', 'total_revenue': 1107.87}, {'title': 'Groovey', 'artist': 'Rich Matteson', 'total_revenue': 4128.59}, {'title': 'Rich Matteson - Groovey', 'artist': 'None', 'total_revenue': 1288.75}], 'var_function-call-10828233966727722979': [{'clean_title': 'groovey', 'clean_artist': 'rich matteson', 'revenue': 5668.5}, {'clean_title': 'all my friends say (album version)', 'clean_artist': 'luke bryan', 'revenue': 5180.93}, {'clean_title': 'ghetto supastar (that is what you are)', 'clean_artist': 'pras', 'revenue': 4933.98}, {'clean_title': 'the power of love (rob searle club mix)', 'clean_artist': 'frankie goes to hollywood', 'revenue': 4909.04}, {'clean_title': 'zo gaat het leven aan je voor', 'clean_artist': 'syb van der ploeg', 'revenue': 4881.42}], 'var_function-call-13607297793593756092': [{'title': '002-All My Friends Say (album version)', 'artist': 'Luke Bryan', 'total_revenue': 1070.38}, {'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan', 'total_revenue': 3241.21}, {'title': 'Luke Bryan - All My Friends Say (album version)', 'artist': 'None', 'total_revenue': 869.34}], 'var_function-call-13113459677564662872': [{'title': '002-The Power of Love (Rob Searle club mix)', 'artist': 'Frankie Goes to Hollywood', 'total_revenue': 1379.56}, {'title': 'The Power of Love (Rob Searle club mix)', 'artist': 'Frankie Goes to Hollywood', 'total_revenue': 2317.97}]}

exec(code, env_args)
