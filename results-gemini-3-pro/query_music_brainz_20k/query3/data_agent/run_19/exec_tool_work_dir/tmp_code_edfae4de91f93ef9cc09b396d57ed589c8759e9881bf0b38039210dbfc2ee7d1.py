code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-9876152415190698502'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-8988901171834631000'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)
df_merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')

def normalize_string(s):
    if not s:
        return ""
    return re.sub(r'[^\w\s]', '', s.lower()).strip()

def extract_metadata(row):
    title = str(row['title']) if row['title'] else ""
    artist = str(row['artist']) if row['artist'] else ""
    if artist.lower() in ['none', 'null', 'nan', '[unknown]', 'unknown', '']:
        artist = ""
    artist = artist.replace('_', ' ')
    title = re.sub(r'^\d+[\-\.\s]+', '', title)
    if " - " in title:
        parts = title.split(" - ", 1)
        if len(parts) == 2:
            p1, p2 = parts
            if not artist or normalize_string(artist) == normalize_string(p1):
                artist = p1
                title = p2
    title = re.sub(r'\s*\(.*?\)', '', title)
    return pd.Series([title.strip(), artist.strip()])

df_merged[['final_title', 'final_artist']] = df_merged.apply(extract_metadata, axis=1)
df_merged['group_title'] = df_merged['final_title'].apply(normalize_string)
df_merged['group_artist'] = df_merged['final_artist'].apply(normalize_string)

# Specific check
emerge_rev = df_merged[
    (df_merged['group_title'] == 'emerge') & 
    (df_merged['group_artist'] == 'fischerspooner')
]['total_revenue'].sum()

zo_rev = df_merged[
    (df_merged['group_title'] == 'zo gaat het leven aan je voor') & 
    (df_merged['group_artist'] == 'syb van der ploeg')
]['total_revenue'].sum()

vagga_rev = df_merged[
    (df_merged['group_title'] == 'vagga') & 
    (df_merged['group_artist'] == 'ske')
]['total_revenue'].sum()

letters_rev = df_merged[
    (df_merged['group_title'] == 'letters a short essay') & 
    (df_merged['group_artist'] == 'echolyn')
]['total_revenue'].sum()

print("__RESULT__:")
print(json.dumps({
    "Emerge": emerge_rev,
    "Zo gaat het leven aan je voor": zo_rev,
    "Vagga": vagga_rev,
    "Letters A Short Essay": letters_rev
}))"""

env_args = {'var_function-call-9876152415190698502': 'file_storage/function-call-9876152415190698502.json', 'var_function-call-8988901171834631000': 'file_storage/function-call-8988901171834631000.json', 'var_function-call-10056493367563797489': [{'title': 'None', 'artist': 'None', 'norm_title': 'none', 'norm_artist': 'none', 'total_revenue': 14647.52}, {'title': '001-', 'artist': 'None', 'norm_title': '001', 'norm_artist': 'none', 'total_revenue': 4681.75}, {'title': '005-', 'artist': 'None', 'norm_title': '005', 'norm_artist': 'none', 'total_revenue': 4281.18}, {'title': '002', 'artist': 'None', 'norm_title': '002', 'norm_artist': 'none', 'total_revenue': 4237.16}, {'title': '010-', 'artist': 'None', 'norm_title': '010', 'norm_artist': 'none', 'total_revenue': 4163.48}, {'title': 'Groovey', 'artist': 'Rich Matteson', 'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'total_revenue': 4128.59}, {'title': '004- ', 'artist': ' ', 'norm_title': '004', 'norm_artist': '', 'total_revenue': 4026.71}, {'title': 'The Fire Still Burns', 'artist': 'Russ Ballard', 'norm_title': 'the fire still burns', 'norm_artist': 'russ ballard', 'total_revenue': 3807.4}, {'title': 'Vostok', 'artist': 'Craig Padilla', 'norm_title': 'vostok', 'norm_artist': 'craig padilla', 'total_revenue': 3767.95}, {'title': '003-', 'artist': 'None', 'norm_title': '003', 'norm_artist': 'none', 'total_revenue': 3695.73}], 'var_function-call-14097951440137414417': [{'title': 'Groovey', 'artist': 'Rich Matteson', 'revenue': 4128.59}, {'title': 'The Fire Still Burns', 'artist': 'Russ Ballard', 'revenue': 3807.4}, {'title': 'Vostok', 'artist': 'Craig Padilla', 'revenue': 3767.95}, {'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan', 'revenue': 3241.21}, {'title': 'Beautiful (instrumental)', 'artist': 'Damian Marley', 'revenue': 3228.62}, {'title': 'Private Soul Security', 'artist': 'Down Below', 'revenue': 3218.63}, {'title': 'Bring Back the Love (Spaced Out dub)', 'artist': 'Laura Harris', 'revenue': 3171.7}, {'title': 'Chi to Rome (Broke One edit)', 'artist': 'Lazy Ants & Rob Threezy', 'revenue': 3091.77}, {'title': 'Bad Hearts', 'artist': 'Tights', 'revenue': 3052.75}, {'title': 'Al Stewart - Year of the Cat', 'artist': 'None', 'revenue': 3049.9300000000003}, {'title': 'Skin', 'artist': 'Westworld', 'revenue': 3008.01}, {'title': 'Christmas In My Heart', 'artist': 'Candi Staton', 'revenue': 2969.33}, {'title': 'Here I Am (Nevins Dirtyrock club mix) (re-edit)', 'artist': 'Sertab Erener', 'revenue': 2900.8100000000004}, {'title': 'Peter en de Wolf', 'artist': 'Сергей Сергеевич Прокофьев', 'revenue': 2820.79}, {'title': 'Fogbank (Jack Beats remix)', 'artist': 'Boy 8-Bit', 'revenue': 2809.3100000000004}, {'title': 'Historical Perspective (d)', 'artist': 'Keith Mansfield', 'revenue': 2759.6499999999996}, {'title': '25 Years (original 12" mix)', 'artist': 'The Catch', 'revenue': 2741.55}, {'title': 'Coat of Many Colors', 'artist': 'Dolly Parton', 'revenue': 2656.75}, {'title': 'Inside the Dream Syndicate, Volume I: Day of Niagara (1965)', 'artist': 'John Cale, Tony Conrad, Angus MacLise, La Monte Young and Marian Zazeela', 'revenue': 2653.51}, {'title': 'Oblivion Beckons', 'artist': 'Byzantine', 'revenue': 2638.2400000000002}], 'var_function-call-13493295133801794959': {'groovey': [{'track_id': '6146', 'title': 'Rich Matteson - Groovey', 'artist': 'None', 'album': 'Groovey'}, {'track_id': '7710', 'title': '006-Groovey', 'artist': 'Rich Matteson', 'album': 'Groovey (2009)'}, {'track_id': '8656', 'title': '001-Gator Whale', 'artist': 'Grooveyard', 'album': 'featuring Red Holloway (1996)'}, {'track_id': '8829', 'title': 'Groovey', 'artist': 'Rich Matteson', 'album': 'Groovey'}, {'track_id': '16496', 'title': 'Groovey', 'artist': 'Rich Matteson', 'album': 'Groovey'}, {'track_id': '17312', 'title': 'Groovey', 'artist': 'Rich Matteson', 'album': 'Groovey'}], 'year_of_cat': [{'track_id': '1853', 'title': '008-Year of the Cat', 'artist': 'Al Stewart', 'album': 'Missing You (unknown)'}, {'track_id': '8987', 'title': 'Year of the Cat (Mellow Rock Classics)', 'artist': 'Al_Stewart', 'album': 'Mellow Rock Classics'}, {'track_id': '11082', 'title': 'Al Stewart - Year of the Cat', 'artist': 'None', 'album': 'Mel low Rock Classics'}, {'track_id': '11748', 'title': 'Al Stewart - Year of the Cat', 'artist': 'None', 'album': 'Missing You'}], 'rich_matteson': [{'track_id': '6146', 'title': 'Rich Matteson - Groovey', 'artist': 'None', 'album': 'Groovey'}, {'track_id': '7710', 'title': '006-Groovey', 'artist': 'Rich Matteson', 'album': 'Groovey (2009)'}, {'track_id': '8829', 'title': 'Groovey', 'artist': 'Rich Matteson', 'album': 'Groovey'}, {'track_id': '16496', 'title': 'Groovey', 'artist': 'Rich Matteson', 'album': 'Groovey'}, {'track_id': '17312', 'title': 'Groovey', 'artist': 'Rich Matteson', 'album': 'Groovey'}]}, 'var_function-call-14393901467721926797': [{'title': 'None', 'artist': '', 'group_title': 'none', 'group_artist': '', 'revenue': 14647.52}, {'title': 'Emerge', 'artist': 'Fischerspooner', 'group_title': 'emerge', 'group_artist': 'fischerspooner', 'revenue': 6665.27}, {'title': 'Zo gaat het leven aan je voor', 'artist': 'Syb van der Ploeg', 'group_title': 'zo gaat het leven aan je voor', 'group_artist': 'syb van der ploeg', 'revenue': 6636.1}, {'title': 'Vagga', 'artist': 'Ske', 'group_title': 'vagga', 'group_artist': 'ske', 'revenue': 6611.56}, {'title': 'Letters A Short Essay', 'artist': 'echolyn', 'group_title': 'letters a short essay', 'group_artist': 'echolyn', 'revenue': 6280.0}, {'title': 'Lovers', 'artist': 'Fausto Papetti', 'group_title': 'lovers', 'group_artist': 'fausto papetti', 'revenue': 6259.3}, {'title': 'Ne veruj', 'artist': 'Vrisak generacije', 'group_title': 'ne veruj', 'group_artist': 'vrisak generacije', 'revenue': 6125.339999999999}, {'title': 'Chile', 'artist': 'Neil Biggin', 'group_title': 'chile', 'group_artist': 'neil biggin', 'revenue': 6008.71}, {'title': 'Travel', 'artist': 'Guts Pie Earshot', 'group_title': 'travel', 'group_artist': 'guts pie earshot', 'revenue': 5825.26}, {'title': 'Lookin Boy', 'artist': 'Hotstylz', 'group_title': 'lookin boy', 'group_artist': 'hotstylz', 'revenue': 5712.889999999999}], 'var_function-call-588950911346329333': {'emerge': [{'track_id': '4895', 'title': 'Fischerspooner - Emerge (Dexter remix)', 'artist': 'None', 'album': '1#'}, {'track_id': '6988', 'title': 'Emerge (Dexter remix) (#1)', 'artist': 'Fischerspooner', 'album': '#1'}, {'track_id': '7575', 'title': 'Emerge (Dave Clarke remix)', 'artist': 'Fischerspooner', 'album': 'EmNerge'}, {'track_id': '10166', 'title': 'Emerge (Dexter remix) - #1', 'artist': 'Fischerspooner', 'album': 'None'}, {'track_id': '10606', 'title': 'Emerge (Dexter remix)', 'artist': 'Fischerspooner', 'album': '#1'}, {'track_id': '10981', 'title': 'Funky Emergency (Jazz Brakes, Volume 2)', 'artist': 'DJ Food', 'album': 'Jazz Brakes, Volume 2'}, {'track_id': '17167', 'title': '027-Emerge (Dexter remix)', 'artist': 'Fischerspooner', 'album': '#1 (2003)'}], 'fischerspooner': [{'track_id': '4895', 'title': 'Fischerspooner - Emerge (Dexter remix)', 'artist': 'None', 'album': '1#'}, {'track_id': '6988', 'title': 'Emerge (Dexter remix) (#1)', 'artist': 'Fischerspooner', 'album': '#1'}, {'track_id': '7575', 'title': 'Emerge (Dave Clarke remix)', 'artist': 'Fischerspooner', 'album': 'EmNerge'}, {'track_id': '10166', 'title': 'Emerge (Dexter remix) - #1', 'artist': 'Fischerspooner', 'album': 'None'}, {'track_id': '10606', 'title': 'Emerge (Dexter remix)', 'artist': 'Fischerspooner', 'album': '#1'}, {'track_id': '12272', 'title': '005-Supply & Demand', 'artist': 'Fischerspooner', 'album': 'Entertainment (2009)'}, {'track_id': '17167', 'title': '027-Emerge (Dexter remix)', 'artist': 'Fischerspooner', 'album': '#1 (2003)'}]}, 'var_function-call-4444381430494872303': [{'track_id': '3463', 'title': 'None', 'artist': 'Tea Leaf Green', 'total_revenue': 2098.28}, {'track_id': '19081', 'title': '009- ', 'artist': ' ', 'total_revenue': 1973.87}, {'track_id': '16208', 'title': 'None', 'artist': 'Earth and Fire', 'total_revenue': 1937.5}, {'track_id': '11703', 'title': '005-', 'artist': 'None', 'total_revenue': 1929.18}, {'track_id': '12302', 'title': 'None', 'artist': 'Nicosas de Angelis', 'total_revenue': 1820.85}, {'track_id': '9788', 'title': 'None', 'artist': 'None', 'total_revenue': 1791.84}, {'track_id': '10048', 'title': 'Marilyn Manson  - ♠', 'artist': 'None', 'total_revenue': 1782.61}, {'track_id': '18790', 'title': 'None', 'artist': 'None', 'total_revenue': 1778.92}, {'track_id': '5248', 'title': '002-', 'artist': 'None', 'total_revenue': 1765.68}, {'track_id': '11622', 'title': '023-', 'artist': 'None', 'total_revenue': 1731.76}]}

exec(code, env_args)
