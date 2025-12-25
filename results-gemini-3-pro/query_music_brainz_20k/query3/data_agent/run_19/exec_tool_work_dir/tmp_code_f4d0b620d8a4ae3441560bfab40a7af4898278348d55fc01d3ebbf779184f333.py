code = """import json
import pandas as pd
import re

with open(locals()['var_function-call-8988901171834631000'], 'r') as f:
    tracks_data = json.load(f)

df_tracks = pd.DataFrame(tracks_data)

# Helper search
def search(term):
    mask = df_tracks['title'].astype(str).str.contains(term, case=False, na=False) | \
           df_tracks['artist'].astype(str).str.contains(term, case=False, na=False)
    return df_tracks[mask][['track_id', 'title', 'artist', 'album']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps({
    "groovey": search("Groovey"),
    "year_of_cat": search("Year of the Cat"),
    "rich_matteson": search("Rich Matteson")
}))"""

env_args = {'var_function-call-9876152415190698502': 'file_storage/function-call-9876152415190698502.json', 'var_function-call-8988901171834631000': 'file_storage/function-call-8988901171834631000.json', 'var_function-call-10056493367563797489': [{'title': 'None', 'artist': 'None', 'norm_title': 'none', 'norm_artist': 'none', 'total_revenue': 14647.52}, {'title': '001-', 'artist': 'None', 'norm_title': '001', 'norm_artist': 'none', 'total_revenue': 4681.75}, {'title': '005-', 'artist': 'None', 'norm_title': '005', 'norm_artist': 'none', 'total_revenue': 4281.18}, {'title': '002', 'artist': 'None', 'norm_title': '002', 'norm_artist': 'none', 'total_revenue': 4237.16}, {'title': '010-', 'artist': 'None', 'norm_title': '010', 'norm_artist': 'none', 'total_revenue': 4163.48}, {'title': 'Groovey', 'artist': 'Rich Matteson', 'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'total_revenue': 4128.59}, {'title': '004- ', 'artist': ' ', 'norm_title': '004', 'norm_artist': '', 'total_revenue': 4026.71}, {'title': 'The Fire Still Burns', 'artist': 'Russ Ballard', 'norm_title': 'the fire still burns', 'norm_artist': 'russ ballard', 'total_revenue': 3807.4}, {'title': 'Vostok', 'artist': 'Craig Padilla', 'norm_title': 'vostok', 'norm_artist': 'craig padilla', 'total_revenue': 3767.95}, {'title': '003-', 'artist': 'None', 'norm_title': '003', 'norm_artist': 'none', 'total_revenue': 3695.73}], 'var_function-call-14097951440137414417': [{'title': 'Groovey', 'artist': 'Rich Matteson', 'revenue': 4128.59}, {'title': 'The Fire Still Burns', 'artist': 'Russ Ballard', 'revenue': 3807.4}, {'title': 'Vostok', 'artist': 'Craig Padilla', 'revenue': 3767.95}, {'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan', 'revenue': 3241.21}, {'title': 'Beautiful (instrumental)', 'artist': 'Damian Marley', 'revenue': 3228.62}, {'title': 'Private Soul Security', 'artist': 'Down Below', 'revenue': 3218.63}, {'title': 'Bring Back the Love (Spaced Out dub)', 'artist': 'Laura Harris', 'revenue': 3171.7}, {'title': 'Chi to Rome (Broke One edit)', 'artist': 'Lazy Ants & Rob Threezy', 'revenue': 3091.77}, {'title': 'Bad Hearts', 'artist': 'Tights', 'revenue': 3052.75}, {'title': 'Al Stewart - Year of the Cat', 'artist': 'None', 'revenue': 3049.9300000000003}, {'title': 'Skin', 'artist': 'Westworld', 'revenue': 3008.01}, {'title': 'Christmas In My Heart', 'artist': 'Candi Staton', 'revenue': 2969.33}, {'title': 'Here I Am (Nevins Dirtyrock club mix) (re-edit)', 'artist': 'Sertab Erener', 'revenue': 2900.8100000000004}, {'title': 'Peter en de Wolf', 'artist': 'Сергей Сергеевич Прокофьев', 'revenue': 2820.79}, {'title': 'Fogbank (Jack Beats remix)', 'artist': 'Boy 8-Bit', 'revenue': 2809.3100000000004}, {'title': 'Historical Perspective (d)', 'artist': 'Keith Mansfield', 'revenue': 2759.6499999999996}, {'title': '25 Years (original 12" mix)', 'artist': 'The Catch', 'revenue': 2741.55}, {'title': 'Coat of Many Colors', 'artist': 'Dolly Parton', 'revenue': 2656.75}, {'title': 'Inside the Dream Syndicate, Volume I: Day of Niagara (1965)', 'artist': 'John Cale, Tony Conrad, Angus MacLise, La Monte Young and Marian Zazeela', 'revenue': 2653.51}, {'title': 'Oblivion Beckons', 'artist': 'Byzantine', 'revenue': 2638.2400000000002}]}

exec(code, env_args)
