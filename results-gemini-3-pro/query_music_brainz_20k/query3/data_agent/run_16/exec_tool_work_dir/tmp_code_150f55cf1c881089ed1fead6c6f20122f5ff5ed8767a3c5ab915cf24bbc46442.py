code = """import pandas as pd
import json
import re

with open(locals()['var_function-call-12792199908109322560'], 'r') as f:
    tracks = pd.DataFrame(json.load(f))

with open(locals()['var_function-call-4064444512275497395'], 'r') as f:
    sales = pd.DataFrame(json.load(f))

sales['revenue'] = pd.to_numeric(sales['total_revenue'])
sales['track_id'] = sales['track_id'].astype(str)
tracks['track_id'] = tracks['track_id'].astype(str)

df = pd.merge(sales, tracks, on='track_id', how='left')

# Simple search
luke = df[df['title'].str.contains("Luke Bryan", case=False, na=False) | df['artist'].str.contains("Luke Bryan", case=False, na=False)]
rich = df[df['title'].str.contains("Matteson", case=False, na=False) | df['artist'].str.contains("Matteson", case=False, na=False)]

print("__RESULT__:")
print(json.dumps({
    "Luke Bryan": luke[['title', 'artist', 'revenue']].to_dict(orient='records'),
    "Rich Matteson": rich[['title', 'artist', 'revenue']].to_dict(orient='records')
}))"""

env_args = {'var_function-call-4064444512275497395': 'file_storage/function-call-4064444512275497395.json', 'var_function-call-12792199908109322560': 'file_storage/function-call-12792199908109322560.json', 'var_function-call-6049788629291501520': {'top_song_key': '|||', 'revenue': 203103.18, 'representative_title': 'Приходи - Зн@менатель', 'representative_artist': 'Сплин', 'clean_title': 'приходи - зн@менатель', 'clean_artist': 'сплин'}, 'var_function-call-9212995862074535535': {'top_song_key': 'unknown|||none', 'revenue': 14647.52, 'representative_title': 'None', 'representative_artist': 'None', 'top_5': [{'group_key': 'unknown|||none', 'revenue': 14647.52}, {'group_key': 'unknown|||001', 'revenue': 6283.24}, {'group_key': 'rich matteson|||groovey', 'revenue': 5417.34}, {'group_key': 'unknown|||005', 'revenue': 4281.18}, {'group_key': 'unknown|||002', 'revenue': 4237.16}]}, 'var_function-call-6312241448822558017': [{'track_id': '14719', 'total_revenue': '2522.82', 'revenue': 2522.82}, {'track_id': '5124', 'total_revenue': '2503.1899999999996', 'revenue': 2503.19}, {'track_id': '1344', 'total_revenue': '2500.72', 'revenue': 2500.72}, {'track_id': '6725', 'total_revenue': '2489.81', 'revenue': 2489.81}, {'track_id': '10377', 'total_revenue': '2466.71', 'revenue': 2466.71}, {'track_id': '5050', 'total_revenue': '2466.3100000000004', 'revenue': 2466.31}, {'track_id': '6667', 'total_revenue': '2452.7000000000003', 'revenue': 2452.7}, {'track_id': '7245', 'total_revenue': '2436.9700000000003', 'revenue': 2436.97}, {'track_id': '11641', 'total_revenue': '2428.2200000000003', 'revenue': 2428.22}, {'track_id': '964', 'total_revenue': '2425.61', 'revenue': 2425.61}, {'track_id': '12984', 'total_revenue': '2401.71', 'revenue': 2401.71}, {'track_id': '6208', 'total_revenue': '2385.0299999999997', 'revenue': 2385.03}, {'track_id': '666', 'total_revenue': '2382.74', 'revenue': 2382.74}, {'track_id': '12620', 'total_revenue': '2377.59', 'revenue': 2377.59}, {'track_id': '19232', 'total_revenue': '2368.7499999999995', 'revenue': 2368.75}, {'track_id': '17757', 'total_revenue': '2365.59', 'revenue': 2365.59}, {'track_id': '3462', 'total_revenue': '2359.23', 'revenue': 2359.23}, {'track_id': '9639', 'total_revenue': '2351.68', 'revenue': 2351.68}, {'track_id': '18760', 'total_revenue': '2349.33', 'revenue': 2349.33}, {'track_id': '2516', 'total_revenue': '2346.18', 'revenue': 2346.18}], 'var_function-call-10218576716561416858': [{'key': 'unknown|||none', 'revenue': 14647.52, 'originals': [['None', 'None']]}, {'key': 'unknown|||001', 'revenue': 6283.24, 'originals': [['001-', 'None'], ['00-1', 'None'], ['00-1', '[unknown]']]}, {'key': 'rich matteson|||groovey', 'revenue': 5417.34, 'originals': [['Groovey', 'Rich Matteson'], ['Rich Matteson - Groovey', 'None']]}, {'key': 'unknown|||005', 'revenue': 4281.18, 'originals': [['005-', 'None'], ['005', 'None']]}, {'key': 'unknown|||002', 'revenue': 4237.16, 'originals': [['002', 'None'], ['002-', 'None']]}, {'key': 'unknown|||010', 'revenue': 4163.48, 'originals': [['010-', 'None']]}, {'key': 'syb van der ploeg|||zo gaat het leven aan je voor hillich fjoer | heilig vuur', 'revenue': 4132.27, 'originals': [['Zo gaat het leven aan je voor - Hillich fjoer | Heilig vuur', 'Syb van der Ploeg'], ['Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'Syb van der Ploeg']]}, {'key': 'luke bryan|||all my friends say album version', 'revenue': 4110.55, 'originals': [['All My Friends Say (album version)', 'Luke Bryan'], ['Luke Bryan - All My Friends Say (album version)', 'None']]}, {'key': 'kerstin gier|||kapitel 01', 'revenue': 4091.12, 'originals': [['Kapitel 01', 'Kerstin Gier'], ['Kerstin Gier - Kapitel 01', 'None']]}, {'key': 'damian marley|||beautiful instrumental', 'revenue': 4004.42, 'originals': [['Beautiful (instrumental)', 'Damian Marley'], ['Damian Marley - Beautiful (instrumental)', 'None']]}]}

exec(code, env_args)
