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

def normalize(text):
    if pd.isna(text) or text is None:
        return ""
    s = str(text).strip().lower()
    if s == "none" or s == "nan" or s == "unknown":
        return ""
    return s

df_merged['norm_title'] = df_merged['title'].apply(normalize)
df_merged['norm_artist'] = df_merged['artist'].apply(normalize)

junk_pattern = re.compile(r'^\d+-\s*$')

def is_valid(row):
    title = row['norm_title']
    if not title:
        return False
    if junk_pattern.match(title):
        return False
    return True

valid_songs = df_merged[df_merged.apply(is_valid, axis=1)]

grouped = valid_songs.groupby(['norm_title', 'norm_artist'])['total_revenue'].sum().reset_index()
grouped_sorted = grouped.sort_values(by='total_revenue', ascending=False)

print("__RESULT__:")
print(grouped_sorted.head(10).to_json(orient='records'))"""

env_args = {'var_function-call-3874821068292434244': 'file_storage/function-call-3874821068292434244.json', 'var_function-call-13479378208221018498': 'file_storage/function-call-13479378208221018498.json', 'var_function-call-13071031815735748921': {'song': 'None', 'artist': 'None', 'revenue': 14647.52}, 'var_function-call-589650206586176752': [{'original_title': '003-', 'original_artist': 'None', 'revenue': 6841.18}, {'original_title': '005-', 'original_artist': 'None', 'revenue': 5222.0}, {'original_title': '009-  ', 'original_artist': ' ', 'revenue': 5045.700000000001}, {'original_title': '004- ', 'original_artist': ' ', 'revenue': 4868.47}, {'original_title': '010-', 'original_artist': 'None', 'revenue': 4734.36}], 'var_function-call-16848924789855013177': [{'original_title': '003-', 'original_artist': 'None', 'revenue': 6841.18}, {'original_title': '005-', 'original_artist': 'None', 'revenue': 5222.0}, {'original_title': '009-  ', 'original_artist': ' ', 'revenue': 5045.700000000001}, {'original_title': '004- ', 'original_artist': ' ', 'revenue': 4868.47}, {'original_title': '010-', 'original_artist': 'None', 'revenue': 4734.36}, {'original_title': 'Groovey', 'original_artist': 'Rich Matteson', 'revenue': 4128.59}, {'original_title': '002-', 'original_artist': ' ', 'revenue': 4119.89}, {'original_title': '006- ', 'original_artist': ' ', 'revenue': 3946.7799999999997}, {'original_title': 'The Fire Still Burns', 'original_artist': 'Russ Ballard', 'revenue': 3807.4}, {'original_title': 'Vostok', 'original_artist': 'Craig Padilla', 'revenue': 3767.95}, {'original_title': '001-', 'original_artist': 'None', 'revenue': 3742.4399999999996}, {'original_title': '012-', 'original_artist': ' ', 'revenue': 3635.13}, {'original_title': 'All My Friends Say (album version)', 'original_artist': 'Luke Bryan', 'revenue': 3241.21}, {'original_title': 'Beautiful (instrumental)', 'original_artist': 'Damian Marley', 'revenue': 3228.62}, {'original_title': 'Private Soul Security', 'original_artist': 'Down Below', 'revenue': 3218.63}, {'original_title': 'unknown', 'original_artist': 'None', 'revenue': 3218.35}, {'original_title': 'Bring Back the Love (Spaced Out dub)', 'original_artist': 'Laura Harris', 'revenue': 3171.7}, {'original_title': 'Chi to Rome (Broke One edit)', 'original_artist': 'Lazy Ants & Rob Threezy', 'revenue': 3091.77}, {'original_title': 'Bad Hearts', 'original_artist': 'Tights', 'revenue': 3052.75}, {'original_title': 'Al Stewart - Year of the Cat', 'original_artist': 'None', 'revenue': 3049.9300000000003}], 'var_function-call-16086799054736622991': {'song': 'Groovey', 'artist': 'Rich Matteson', 'revenue': 4128.59}}

exec(code, env_args)
