code = """import json
import pandas as pd
import re

with open(locals()['var_function-call-8682200878932963124'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-8682200878932962997'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_tracks['track_id'] = df_tracks['track_id'].astype(str)
df_merged = pd.merge(df_tracks, df_sales, on='track_id', how='left')
df_merged['total_revenue'] = df_merged['total_revenue'].fillna(0)

def normalize_title(s):
    if not isinstance(s, str):
        return ''
    s = s.strip().lower()
    if s in ['none', '']:
        return ''
    
    # Remove leading track numbers
    s = re.sub(r'^\d+[\s\-\.]+', '', s)
    
    # Split by " - " or " (" or " ["
    # We use regex split
    parts = re.split(r'\s+-\s+|\s*[\(\[]', s)
    s = parts[0]
    
    # Remove remaining punctuation
    s = re.sub(r'[^\w\s]', '', s)
    
    return s.strip()

def normalize_artist(s):
    if not isinstance(s, str):
        return ''
    s = s.strip().lower()
    if s in ['none', '']:
        return ''
    s = re.sub(r'[^\w\s]', '', s)
    return s.strip()

df_merged['norm_title'] = df_merged['title'].apply(normalize_title)
df_merged['norm_artist'] = df_merged['artist'].apply(normalize_artist)

# Filter valid artists
df_clean = df_merged[(df_merged['norm_title'] != '') & (df_merged['norm_artist'] != '')]

grouped = df_clean.groupby(['norm_title', 'norm_artist']).agg({
    'total_revenue': 'sum',
    'title': 'first',
    'artist': 'first'
}).reset_index()

grouped = grouped.sort_values('total_revenue', ascending=False)
top_10 = grouped.head(10).to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(top_10))"""

env_args = {'var_function-call-8682200878932963124': 'file_storage/function-call-8682200878932963124.json', 'var_function-call-8682200878932962997': 'file_storage/function-call-8682200878932962997.json', 'var_function-call-1519880724859668680': {'title': 'None', 'artist': 'None', 'revenue': 17139.25, 'norm_title': '', 'norm_artist': ''}, 'var_function-call-1274804052475506745': [{'norm_title': '004', 'norm_artist': '', 'total_revenue': 7271.32, 'title': '004-/', 'artist': 'None'}, {'norm_title': '003', 'norm_artist': '', 'total_revenue': 7090.13, 'title': '003-', 'artist': 'None'}, {'norm_title': '005', 'norm_artist': '', 'total_revenue': 6155.29, 'title': '005', 'artist': 'None'}, {'norm_title': '009', 'norm_artist': '', 'total_revenue': 5045.7, 'title': '009-  ', 'artist': ' '}, {'norm_title': '002', 'norm_artist': '', 'total_revenue': 5013.4400000000005, 'title': '002-', 'artist': 'None'}], 'var_function-call-14956051246434708501': [{'norm_title': '004', 'norm_artist': '', 'total_revenue': 7271.32, 'title': '004-/', 'artist': 'None'}, {'norm_title': '003', 'norm_artist': '', 'total_revenue': 7090.13, 'title': '003-', 'artist': 'None'}, {'norm_title': '005', 'norm_artist': '', 'total_revenue': 6155.29, 'title': '005', 'artist': 'None'}, {'norm_title': '009', 'norm_artist': '', 'total_revenue': 5045.7, 'title': '009-  ', 'artist': ' '}, {'norm_title': '002', 'norm_artist': '', 'total_revenue': 5013.4400000000005, 'title': '002-', 'artist': 'None'}, {'norm_title': '010', 'norm_artist': '', 'total_revenue': 4734.360000000001, 'title': '010-', 'artist': 'None'}, {'norm_title': '001', 'norm_artist': '', 'total_revenue': 4681.75, 'title': '00-1', 'artist': 'None'}, {'norm_title': '012', 'norm_artist': '', 'total_revenue': 4641.08, 'title': '012-', 'artist': 'None'}, {'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'total_revenue': 4128.59, 'title': 'Groovey', 'artist': 'Rich Matteson'}, {'norm_title': '006', 'norm_artist': '', 'total_revenue': 3946.7799999999997, 'title': '006-', 'artist': 'None'}, {'norm_title': 'the fire still burns', 'norm_artist': 'russ ballard', 'total_revenue': 3807.4, 'title': 'The Fire Still Burns', 'artist': 'Russ Ballard'}, {'norm_title': 'vostok', 'norm_artist': 'craig padilla', 'total_revenue': 3767.95, 'title': 'Vostok', 'artist': 'Craig Padilla'}, {'norm_title': 'all my friends say album version', 'norm_artist': 'luke bryan', 'total_revenue': 3241.21, 'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan'}, {'norm_title': 'beautiful instrumental', 'norm_artist': 'damian marley', 'total_revenue': 3228.62, 'title': 'Beautiful (instrumental)', 'artist': 'Damian Marley'}, {'norm_title': 'private soul security', 'norm_artist': 'down below', 'total_revenue': 3218.63, 'title': 'Private Soul Security', 'artist': 'Down Below'}, {'norm_title': 'unknown', 'norm_artist': '', 'total_revenue': 3218.35, 'title': 'unknown', 'artist': 'None'}, {'norm_title': 'bring back the love spaced out dub', 'norm_artist': 'laura harris', 'total_revenue': 3171.7, 'title': 'Bring Back the Love (Spaced Out dub)', 'artist': 'Laura Harris'}, {'norm_title': 'chi to rome broke one edit', 'norm_artist': 'lazy ants  rob threezy', 'total_revenue': 3091.77, 'title': 'Chi to Rome (Broke One edit)', 'artist': 'Lazy Ants & Rob Threezy'}, {'norm_title': 'bad hearts', 'norm_artist': 'tights', 'total_revenue': 3052.75, 'title': 'Bad Hearts', 'artist': 'Tights'}, {'norm_title': 'al stewart  year of the cat', 'norm_artist': '', 'total_revenue': 3049.9300000000003, 'title': 'Al Stewart - Year of the Cat', 'artist': 'None'}], 'var_function-call-14205048415460189365': [{'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'total_revenue': 4128.59, 'title': 'Groovey', 'artist': 'Rich Matteson'}, {'norm_title': 'the fire still burns', 'norm_artist': 'russ ballard', 'total_revenue': 3807.4, 'title': 'The Fire Still Burns', 'artist': 'Russ Ballard'}, {'norm_title': 'vostok', 'norm_artist': 'craig padilla', 'total_revenue': 3767.95, 'title': 'Vostok', 'artist': 'Craig Padilla'}, {'norm_title': 'all my friends say album version', 'norm_artist': 'luke bryan', 'total_revenue': 3241.21, 'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan'}, {'norm_title': 'beautiful instrumental', 'norm_artist': 'damian marley', 'total_revenue': 3228.62, 'title': 'Beautiful (instrumental)', 'artist': 'Damian Marley'}, {'norm_title': 'private soul security', 'norm_artist': 'down below', 'total_revenue': 3218.63, 'title': 'Private Soul Security', 'artist': 'Down Below'}, {'norm_title': 'bring back the love spaced out dub', 'norm_artist': 'laura harris', 'total_revenue': 3171.7, 'title': 'Bring Back the Love (Spaced Out dub)', 'artist': 'Laura Harris'}, {'norm_title': 'chi to rome broke one edit', 'norm_artist': 'lazy ants  rob threezy', 'total_revenue': 3091.77, 'title': 'Chi to Rome (Broke One edit)', 'artist': 'Lazy Ants & Rob Threezy'}, {'norm_title': 'bad hearts', 'norm_artist': 'tights', 'total_revenue': 3052.75, 'title': 'Bad Hearts', 'artist': 'Tights'}, {'norm_title': 'skin', 'norm_artist': 'westworld', 'total_revenue': 3008.01, 'title': 'Skin', 'artist': 'Westworld'}], 'var_function-call-5871261560436786024': {'matteson': [{'track_id': '7710', 'title': '006-Groovey', 'artist': 'Rich Matteson'}, {'track_id': '8829', 'title': 'Groovey', 'artist': 'Rich Matteson'}, {'track_id': '16496', 'title': 'Groovey', 'artist': 'Rich Matteson'}, {'track_id': '17312', 'title': 'Groovey', 'artist': 'Rich Matteson'}], 'ballard': [{'track_id': '1154', 'title': 'The Fire Still Burns', 'artist': 'Russ Ballard'}, {'track_id': '1464', 'title': '008-The Fire Still Burns', 'artist': 'Russ Ballard'}, {'track_id': '6911', 'title': 'Come on and Get It - Nothing but Good: 1952-1962', 'artist': 'Hank Ballard and The Midnighters'}, {'track_id': '12644', 'title': 'The Fire Still Burns', 'artist': 'Russ Ballard'}, {'track_id': '13269', 'title': '015-Come on and Get It', 'artist': 'Hank Ballard and The Midnighters'}]}, 'var_function-call-2693288056054293480': [{'norm_title': 'zo gaat het leven aan je voor', 'norm_artist': 'syb van der ploeg', 'total_revenue': 5158.72, 'title': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'artist': 'Syb van der Ploeg'}, {'norm_title': 'vagga', 'norm_artist': 'ske', 'total_revenue': 5152.0, 'title': 'Vagga', 'artist': 'Ske'}, {'norm_title': 'emerge', 'norm_artist': 'fischerspooner', 'total_revenue': 5054.81, 'title': 'Emerge (Dexter remix) (#1)', 'artist': 'Fischerspooner'}, {'norm_title': 'travel', 'norm_artist': 'guts pie earshot', 'total_revenue': 4933.9, 'title': 'Travel (live) (amparo fugaz)', 'artist': 'Guts Pie Earshot'}, {'norm_title': 'stormy', 'norm_artist': 'scott walker', 'total_revenue': 4677.15, 'title': '011-Stormy', 'artist': 'Scott Walker'}, {'norm_title': 'chile', 'norm_artist': 'neil biggin', 'total_revenue': 4676.22, 'title': 'Chile (Re-Loaded)', 'artist': 'Neil Biggin'}, {'norm_title': 'ne veruj', 'norm_artist': 'vrisak generacije', 'total_revenue': 4667.119999999999, 'title': 'Ne veruj (Beer Drinkers Revenge)', 'artist': 'Vrisak generacije'}, {'norm_title': 'lookin boy', 'norm_artist': 'hotstylz', 'total_revenue': 4664.29, 'title': '014-Lookin Boy (feat. Yung Joc)', 'artist': 'Hotstylz'}, {'norm_title': 'dont fucking care', 'norm_artist': 'skabucks', 'total_revenue': 4655.55, 'title': "Don't Fucking Care (Superhero's Finest)", 'artist': 'SkaBucks'}, {'norm_title': 'sex', 'norm_artist': 'berlin', 'total_revenue': 4648.94, 'title': "Sex (I'm A ...) (Retro Lunchbox: Squeeze the Cheeze)", 'artist': 'Berlin'}], 'var_function-call-16263560439053593253': [{'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'total_revenue': 4379.75, 'title': '006-Groovey', 'artist': 'Rich Matteson'}, {'norm_title': 'the fire still burns', 'norm_artist': 'russ ballard', 'total_revenue': 4102.45, 'title': 'The Fire Still Burns', 'artist': 'Russ Ballard'}, {'norm_title': 'zo gaat het leven aan je voor', 'norm_artist': 'syb van der ploeg', 'total_revenue': 5158.72, 'title': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'artist': 'Syb van der Ploeg'}], 'var_function-call-9293337938372873504': {'syb': [{'track_id': '3024', 'title': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'artist': 'Syb van der Ploeg', 'total_revenue': 1754.6800000000003}, {'track_id': '3435', 'title': 'Zo gaat het leven aan je voor', 'artist': 'Syb van der Ploeg', 'total_revenue': 2024.37}, {'track_id': '12620', 'title': 'Zo gaat het leven aan je voor - Hillich fjoer | Heilig vuur', 'artist': 'Syb van der Ploeg', 'total_revenue': 2377.59}, {'track_id': '12854', 'title': '006-Zo gaat het leven aan je voor', 'artist': 'Syb van der Ploeg', 'total_revenue': 1379.6699999999998}], 'ske': [{'track_id': '333', 'title': 'Geltendes Recht - Projekt Aaskereia', 'artist': 'Projekt Aaskereia', 'total_revenue': 1182.18}, {'track_id': '2225', 'title': '005-Reel: Reilly of the White Hill', 'artist': "Billy McComiskey & Andy O'Brien", 'total_revenue': 1293.53}, {'track_id': '2900', 'title': 'Nod Off (Version 1) - aFntastic Spikes Through Balloon', 'artist': 'Skeleton Key', 'total_revenue': 1493.2599999999998}, {'track_id': '4668', 'title': 'Reel: Reilly of the White Hill (Celtic Dances: Jigs & Reels From Ireland)', 'artist': "Billy McComiskey & Andy O'Brien", 'total_revenue': 720.27}, {'track_id': '4977', 'title': 'Reel: Reilly of the White Hill', 'artist': "Billy McComiskey & Andy O'Brien", 'total_revenue': 1255.66}, {'track_id': '7165', 'title': 'Reel: Reilly of the White Hill - Celtic Dances: Jigs & Reels From Ireland', 'artist': "Billy McComiskey & Andy O'Brien", 'total_revenue': 603.56}, {'track_id': '8659', 'title': "008-Time's Cold Grasp", 'artist': 'Glass Skeleton Death March', 'total_revenue': 1251.08}, {'track_id': '12735', 'title': 'Vagga', 'artist': 'Ske', 'total_revenue': 1358.13}, {'track_id': '13611', 'title': "022-I Can't Stay Mad At You", 'artist': 'Skeeter Davis', 'total_revenue': 1070.05}, {'track_id': '14686', 'title': 'Vagga (Feelings Are Great)', 'artist': 'Ske', 'total_revenue': 2163.69}, {'track_id': '15156', 'title': 'Song for Tom - Until They Lay Me Down to Rest', 'artist': 'Grace Askew', 'total_revenue': 1196.83}, {'track_id': '15657', 'title': '014-Dead Sheep', 'artist': 'Skeleton Crew', 'total_revenue': 193.41}, {'track_id': '15900', 'title': "I Wish (Alle 40 Goed 90'ss Volume 2)", 'artist': 'Skee-Lo', 'total_revenue': 493.92}, {'track_id': '16158', 'title': '009-Geltendes Recht', 'artist': 'Projekt Aaskereia', 'total_revenue': 2033.43}, {'track_id': '17662', 'title': 'Vagga - Feelings Are Great', 'artist': 'Ske', 'total_revenue': 602.64}, {'track_id': '17878', 'title': '011-Vagga', 'artist': 'Ske', 'total_revenue': 1630.18}]}}

exec(code, env_args)
