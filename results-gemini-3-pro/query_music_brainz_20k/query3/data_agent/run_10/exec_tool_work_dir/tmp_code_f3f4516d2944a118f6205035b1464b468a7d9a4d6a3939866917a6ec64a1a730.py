code = """# Check for variations
import json
import pandas as pd
import re

with open(locals()['var_function-call-3992495390837066285'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-7409539752900977037'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)
df_sales['revenue_usd'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')
merged['title'] = merged['title'].astype(str).fillna('')
merged['artist'] = merged['artist'].astype(str).fillna('')

# Helper to search
def search(term):
    mask = merged['title'].str.contains(term, case=False, regex=False)
    return merged[mask][['track_id', 'title', 'artist', 'revenue_usd']]

print("__RESULT__:")
print(json.dumps({
    "groovey": search("Groovey").to_dict(orient='records'),
    "all_my_friends": search("All My Friends Say").to_dict(orient='records'),
    "zo_gaat": search("Zo gaat het leven").to_dict(orient='records')
}))"""

env_args = {'var_function-call-3992495390837066285': 'file_storage/function-call-3992495390837066285.json', 'var_function-call-7409539752900977037': 'file_storage/function-call-7409539752900977037.json', 'var_function-call-16025719920181743167': {'top_20': [{'norm_title': '', 'norm_artist': '', 'revenue_usd': 203103.18}, {'norm_title': 'none', 'norm_artist': 'none', 'revenue_usd': 14647.52}, {'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'revenue_usd': 5417.34}, {'norm_title': '', 'norm_artist': 'unknown', 'revenue_usd': 4851.83}, {'norm_title': '001', 'norm_artist': 'none', 'revenue_usd': 4681.75}, {'norm_title': 'tv', 'norm_artist': '', 'revenue_usd': 4527.58}, {'norm_title': '005', 'norm_artist': 'none', 'revenue_usd': 4281.18}, {'norm_title': '002', 'norm_artist': 'none', 'revenue_usd': 4237.16}, {'norm_title': '010', 'norm_artist': 'none', 'revenue_usd': 4163.48}, {'norm_title': 'zo gaat het leven aan je voor hillich fjoer heilig vuur', 'norm_artist': 'syb van der ploeg', 'revenue_usd': 4132.27}, {'norm_title': 'all my friends say album version', 'norm_artist': 'luke bryan', 'revenue_usd': 4110.55}, {'norm_title': 'kapitel 01', 'norm_artist': 'kerstin gier', 'revenue_usd': 4091.12}, {'norm_title': '004', 'norm_artist': '', 'revenue_usd': 4026.71}, {'norm_title': 'beautiful instrumental', 'norm_artist': 'damian marley', 'revenue_usd': 4004.42}, {'norm_title': 'the story of your life', 'norm_artist': 'matthew barber', 'revenue_usd': 3962.97}, {'norm_title': 'thousand finger man salsoul 30th', 'norm_artist': 'candido', 'revenue_usd': 3934.83}, {'norm_title': 'a wandring minstrel i from the mikado', 'norm_artist': 'sir william gilbert sir arthur sullivan', 'revenue_usd': 3877.43}, {'norm_title': 'fret one grow old inside your wave', 'norm_artist': 'ugly winner', 'revenue_usd': 3844.09}, {'norm_title': 'the fire still burns', 'norm_artist': 'russ ballard', 'revenue_usd': 3807.4}, {'norm_title': 'vostok', 'norm_artist': 'craig padilla', 'revenue_usd': 3767.95}], 'winner': {'title': 'Όνειρα ζωής', 'artist': 'Χρήστος Δάντης', 'revenue': 203103.18}}, 'var_function-call-6781856173906030022': [{'rank': 1, 'title': '004-', 'artist': '', 'norm_title': '004', 'norm_artist': '', 'revenue': 7271.32, 'track_count': 8}, {'rank': 2, 'title': '003-', 'artist': '', 'norm_title': '003', 'norm_artist': '', 'revenue': 7090.13, 'track_count': 7}, {'rank': 3, 'title': '001-', 'artist': '', 'norm_title': '001', 'norm_artist': '', 'revenue': 6283.24, 'track_count': 6}, {'rank': 4, 'title': '005-', 'artist': '', 'norm_title': '005', 'norm_artist': '', 'revenue': 6155.29, 'track_count': 8}, {'rank': 5, 'title': 'Groovey', 'artist': 'Rich Matteson', 'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'revenue': 5417.34, 'track_count': 4}, {'rank': 6, 'title': '009-', 'artist': '', 'norm_title': '009', 'norm_artist': '', 'revenue': 5045.7, 'track_count': 4}, {'rank': 7, 'title': '002-', 'artist': '', 'norm_title': '002', 'norm_artist': '', 'revenue': 5013.4400000000005, 'track_count': 4}, {'rank': 8, 'title': '010-', 'artist': '', 'norm_title': '010', 'norm_artist': '', 'revenue': 4734.360000000001, 'track_count': 5}, {'rank': 9, 'title': '012-', 'artist': '', 'norm_title': '012', 'norm_artist': '', 'revenue': 4641.08, 'track_count': 4}, {'rank': 10, 'title': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'artist': 'Syb van der Ploeg', 'norm_title': 'zo gaat het leven aan je voor hillich fjoer heilig vuur', 'norm_artist': 'syb van der ploeg', 'revenue': 4132.27, 'track_count': 2}], 'var_function-call-15376139809597613316': [{'rank': 1, 'title': 'Groovey', 'artist': 'Rich Matteson', 'revenue': 5417.34, 'track_count': 4}, {'rank': 2, 'title': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'artist': 'Syb van der Ploeg', 'revenue': 4132.27, 'track_count': 2}, {'rank': 3, 'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan', 'revenue': 4110.55, 'track_count': 3}, {'rank': 4, 'title': 'Kapitel 01', 'artist': 'Kerstin Gier', 'revenue': 4091.12, 'track_count': 2}, {'rank': 5, 'title': 'Beautiful (instrumental)', 'artist': 'Damian Marley', 'revenue': 4004.42, 'track_count': 4}, {'rank': 6, 'title': 'The Story of Your Life', 'artist': 'Matthew Barber', 'revenue': 3962.97, 'track_count': 4}, {'rank': 7, 'title': 'Thousand Finger Man (Salsoul 30th)', 'artist': 'Candido', 'revenue': 3934.83, 'track_count': 2}, {'rank': 8, 'title': 'A Wand\'ring Minstrel I, From "The Mikado"', 'artist': 'Sir William Gilbert & Sir Arthur Sullivan', 'revenue': 3877.43, 'track_count': 2}, {'rank': 9, 'title': 'Fret One (Grow Old) (Inside Your Wave)', 'artist': 'Ugly Winner', 'revenue': 3844.09, 'track_count': 2}, {'rank': 10, 'title': 'The Fire Still Burns', 'artist': 'Russ Ballard', 'revenue': 3807.4, 'track_count': 2}]}

exec(code, env_args)
