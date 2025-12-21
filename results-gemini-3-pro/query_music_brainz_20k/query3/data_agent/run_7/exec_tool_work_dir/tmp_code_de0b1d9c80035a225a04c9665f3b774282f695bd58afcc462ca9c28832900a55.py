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

# Minimal cleaning to check specific artist
def clean_artist(a):
    if not isinstance(a, str): return ""
    a = a.lower()
    if a.startswith("the "): a = a[4:]
    return re.sub(r'[^a-z0-9]', '', a)

merged['check_artist'] = merged['artist'].apply(clean_artist)

# Filter for richmatteson
rich = merged[merged['check_artist'] == 'richmatteson']

print("__RESULT__:")
print(rich[['title', 'artist', 'total_revenue']].to_json(orient='records'))"""

env_args = {'var_function-call-14091195230091116524': 'file_storage/function-call-14091195230091116524.json', 'var_function-call-14091195230091115561': 'file_storage/function-call-14091195230091115561.json', 'var_function-call-6181621511931833030': [{'rank': 1, 'title': '[untitled]', 'artist': '[unknown]', 'revenue': 253349.14}, {'rank': 2, 'title': 'None', 'artist': 'None', 'revenue': 14647.52}, {'rank': 3, 'title': '001-', 'artist': 'None', 'revenue': 5866.48}, {'rank': 4, 'title': 'Groovey', 'artist': 'Rich Matteson', 'revenue': 5417.34}, {'rank': 5, 'title': 'Zo gaat het leven aan je voor', 'artist': 'Syb van der Ploeg', 'revenue': 5256.43}], 'var_function-call-3899079882760515651': [{'rank': 1, 'title': 'Groovey', 'artist': 'Rich Matteson', 'revenue': 5417.34}, {'rank': 2, 'title': 'Zo gaat het leven aan je voor', 'artist': 'Syb van der Ploeg', 'revenue': 5256.43}, {'rank': 3, 'title': 'Vagga', 'artist': 'Ske', 'revenue': 4981.38}, {'rank': 4, 'title': 'Emerge (Dexter remix)', 'artist': 'Fischerspooner', 'revenue': 4896.240000000001}, {'rank': 5, 'title': 'Best Friends', 'artist': 'Hans Zimmer', 'revenue': 4806.24}, {'rank': 6, 'title': 'Letters: A Short Essay', 'artist': 'echolyn', 'revenue': 4694.76}, {'rank': 7, 'title': 'Ne veruj', 'artist': 'Vrisak generacije', 'revenue': 4693.259999999999}, {'rank': 8, 'title': 'Travel (live)', 'artist': 'Guts Pie Earshot', 'revenue': 4595.34}, {'rank': 9, 'title': '36-30', 'artist': 'Ian Vine', 'revenue': 4573.98}, {'rank': 10, 'title': 'Siviiliuhri', 'artist': 'Jukka Poika ja Kompostikopla', 'revenue': 4548.4400000000005}], 'var_function-call-8165636878994884958': [{'rank': 1, 'title': 'Groovey', 'artist': 'Rich Matteson', 'revenue': 5417.34}, {'rank': 2, 'title': 'Zo gaat het leven aan je voor', 'artist': 'Syb van der Ploeg', 'revenue': 5256.43}, {'rank': 3, 'title': 'Vagga', 'artist': 'Ske', 'revenue': 4981.38}, {'rank': 4, 'title': 'Emerge (Dexter remix)', 'artist': 'Fischerspooner', 'revenue': 4896.240000000001}, {'rank': 5, 'title': 'Best Friends', 'artist': 'Hans Zimmer', 'revenue': 4806.24}, {'rank': 6, 'title': 'Letters: A Short Essay', 'artist': 'echolyn', 'revenue': 4694.76}, {'rank': 7, 'title': 'Ne veruj', 'artist': 'Vrisak generacije', 'revenue': 4693.259999999999}, {'rank': 8, 'title': 'Bad Hearts', 'artist': 'Tights', 'revenue': 4612.22}, {'rank': 9, 'title': 'Travel (live)', 'artist': 'Guts Pie Earshot', 'revenue': 4595.34}, {'rank': 10, 'title': '36-30', 'artist': 'Ian Vine', 'revenue': 4573.98}]}

exec(code, env_args)
