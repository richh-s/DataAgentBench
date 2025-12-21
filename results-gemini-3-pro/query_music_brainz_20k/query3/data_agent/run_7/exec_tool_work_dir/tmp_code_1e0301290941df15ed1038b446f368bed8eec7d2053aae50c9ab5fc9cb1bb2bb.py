code = """import pandas as pd
import json
import re

tracks_file = locals()['var_function-call-14091195230091116524']
sales_file = locals()['var_function-call-14091195230091115561']

with open(tracks_file, 'r') as f:
    tracks = pd.DataFrame(json.load(f))
with open(sales_file, 'r') as f:
    sales = pd.DataFrame(json.load(f))

tracks['track_id'] = tracks['track_id'].astype(str)
sales['track_id'] = sales['track_id'].astype(str)
sales['total_revenue'] = pd.to_numeric(sales['total_revenue'])

merged = pd.merge(tracks, sales, on='track_id', how='inner')

def clean_artist_title(row):
    title = str(row['title'])
    artist = str(row['artist'])
    if artist.lower() in ['none', '[unknown]', '', 'nan']:
        if ' - ' in title:
            parts = title.split(' - ', 1)
            possible_artist = parts[0].strip()
            possible_title = parts[1].strip()
            if re.match(r'^\d+$', possible_artist):
                return artist, title 
            return possible_artist, possible_title
        return artist, title
    return artist, title

cleaned = merged.apply(clean_artist_title, axis=1)
merged['clean_artist'] = [x[0] for x in cleaned]
merged['clean_title'] = [x[1] for x in cleaned]

def normalize_title(text):
    if not isinstance(text, str):
        return ""
    text = re.sub(r'^\d+[\s-]*', '', text)
    text = text.lower()
    text = re.sub(r'\(.*?\)', '', text)
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'[^a-z0-9]', '', text)
    return text

def normalize_artist(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    if text.startswith("the "):
        text = text[4:]
    text = re.sub(r'\(.*?\)', '', text)
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'[^a-z0-9]', '', text)
    return text

merged['norm_artist'] = merged['clean_artist'].apply(normalize_artist)
merged['norm_title'] = merged['clean_title'].apply(normalize_title)

# Filter for Fischerspooner / Emerge
target_artist = normalize_artist("Fischerspooner")
target_title = normalize_title("Emerge")

group_rows = merged[
    (merged['norm_artist'] == target_artist) & 
    (merged['norm_title'] == target_title)
]

print("__RESULT__:")
print(group_rows[['title', 'artist', 'total_revenue']].to_json(orient='records'))"""

env_args = {'var_function-call-14091195230091116524': 'file_storage/function-call-14091195230091116524.json', 'var_function-call-14091195230091115561': 'file_storage/function-call-14091195230091115561.json', 'var_function-call-6181621511931833030': [{'rank': 1, 'title': '[untitled]', 'artist': '[unknown]', 'revenue': 253349.14}, {'rank': 2, 'title': 'None', 'artist': 'None', 'revenue': 14647.52}, {'rank': 3, 'title': '001-', 'artist': 'None', 'revenue': 5866.48}, {'rank': 4, 'title': 'Groovey', 'artist': 'Rich Matteson', 'revenue': 5417.34}, {'rank': 5, 'title': 'Zo gaat het leven aan je voor', 'artist': 'Syb van der Ploeg', 'revenue': 5256.43}], 'var_function-call-3899079882760515651': [{'rank': 1, 'title': 'Groovey', 'artist': 'Rich Matteson', 'revenue': 5417.34}, {'rank': 2, 'title': 'Zo gaat het leven aan je voor', 'artist': 'Syb van der Ploeg', 'revenue': 5256.43}, {'rank': 3, 'title': 'Vagga', 'artist': 'Ske', 'revenue': 4981.38}, {'rank': 4, 'title': 'Emerge (Dexter remix)', 'artist': 'Fischerspooner', 'revenue': 4896.240000000001}, {'rank': 5, 'title': 'Best Friends', 'artist': 'Hans Zimmer', 'revenue': 4806.24}, {'rank': 6, 'title': 'Letters: A Short Essay', 'artist': 'echolyn', 'revenue': 4694.76}, {'rank': 7, 'title': 'Ne veruj', 'artist': 'Vrisak generacije', 'revenue': 4693.259999999999}, {'rank': 8, 'title': 'Travel (live)', 'artist': 'Guts Pie Earshot', 'revenue': 4595.34}, {'rank': 9, 'title': '36-30', 'artist': 'Ian Vine', 'revenue': 4573.98}, {'rank': 10, 'title': 'Siviiliuhri', 'artist': 'Jukka Poika ja Kompostikopla', 'revenue': 4548.4400000000005}], 'var_function-call-8165636878994884958': [{'rank': 1, 'title': 'Groovey', 'artist': 'Rich Matteson', 'revenue': 5417.34}, {'rank': 2, 'title': 'Zo gaat het leven aan je voor', 'artist': 'Syb van der Ploeg', 'revenue': 5256.43}, {'rank': 3, 'title': 'Vagga', 'artist': 'Ske', 'revenue': 4981.38}, {'rank': 4, 'title': 'Emerge (Dexter remix)', 'artist': 'Fischerspooner', 'revenue': 4896.240000000001}, {'rank': 5, 'title': 'Best Friends', 'artist': 'Hans Zimmer', 'revenue': 4806.24}, {'rank': 6, 'title': 'Letters: A Short Essay', 'artist': 'echolyn', 'revenue': 4694.76}, {'rank': 7, 'title': 'Ne veruj', 'artist': 'Vrisak generacije', 'revenue': 4693.259999999999}, {'rank': 8, 'title': 'Bad Hearts', 'artist': 'Tights', 'revenue': 4612.22}, {'rank': 9, 'title': 'Travel (live)', 'artist': 'Guts Pie Earshot', 'revenue': 4595.34}, {'rank': 10, 'title': '36-30', 'artist': 'Ian Vine', 'revenue': 4573.98}], 'var_function-call-6113633004103165371': [{'title': '006-Groovey', 'artist': 'Rich Matteson', 'total_revenue': 251.16}, {'title': 'Groovey', 'artist': 'Rich Matteson', 'total_revenue': 2142.48}, {'title': 'Groovey', 'artist': 'Rich Matteson', 'total_revenue': 949.82}, {'title': 'Groovey', 'artist': 'Rich Matteson', 'total_revenue': 1036.29}], 'var_function-call-4990698564392712326': [{'track_id': '6146', 'title': 'Rich Matteson - Groovey', 'artist': 'None', 'clean_title': 'Groovey', 'clean_artist': 'Rich Matteson', 'total_revenue': 1288.75}, {'track_id': '8829', 'title': 'Groovey', 'artist': 'Rich Matteson', 'clean_title': 'Groovey', 'clean_artist': 'Rich Matteson', 'total_revenue': 2142.48}, {'track_id': '16496', 'title': 'Groovey', 'artist': 'Rich Matteson', 'clean_title': 'Groovey', 'clean_artist': 'Rich Matteson', 'total_revenue': 949.82}, {'track_id': '17312', 'title': 'Groovey', 'artist': 'Rich Matteson', 'clean_title': 'Groovey', 'clean_artist': 'Rich Matteson', 'total_revenue': 1036.29}], 'var_function-call-8812602263407207670': [{'rank': 1, 'title': 'Emerge (Dexter remix)', 'artist': 'Fischerspooner', 'revenue': 6665.27}, {'rank': 2, 'title': 'Zo gaat het leven aan je voor', 'artist': 'Syb van der Ploeg', 'revenue': 6636.1}, {'rank': 3, 'title': 'Vagga', 'artist': 'Ske', 'revenue': 6611.56}, {'rank': 4, 'title': 'Letters: A Short Essay', 'artist': 'echolyn', 'revenue': 6280.0}, {'rank': 5, 'title': 'Lovers', 'artist': 'Fausto Papetti', 'revenue': 6259.3}, {'rank': 6, 'title': 'Ne veruj', 'artist': 'Vrisak generacije', 'revenue': 6125.339999999999}, {'rank': 7, 'title': 'Chile', 'artist': 'Neil Biggin', 'revenue': 6008.71}, {'rank': 8, 'title': 'Travel (live)', 'artist': 'Guts Pie Earshot', 'revenue': 5825.26}, {'rank': 9, 'title': '005-Someday Sweetheart', 'artist': 'Peggy Lee', 'revenue': 5766.39}, {'rank': 10, 'title': 'Lookin Boy (feat. Yung Joc)', 'artist': 'Hotstylz', 'revenue': 5712.889999999999}]}

exec(code, env_args)
