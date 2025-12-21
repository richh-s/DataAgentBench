code = """import json
import pandas as pd
import re

with open(locals()['var_function-call-4082973403781613330'], 'r') as f:
    sales_data = json.load(f)

with open(locals()['var_function-call-18357211790249148335'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])

merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')

def clean_text(s):
    if not isinstance(s, str):
        return ""
    return s.lower().strip()

def resolve_entity(row):
    title = str(row['title'])
    artist = str(row['artist'])
    
    # Clean prefixes like "006-"
    title = re.sub(r'^\d{3}-', '', title)
    
    # Handle missing artist
    if artist.lower() in ['none', 'nan', '', '[unknown]']:
        artist = None
    
    # Extract artist from title if missing
    # Pattern "Artist - Title"
    if artist is None and ' - ' in title:
        parts = title.split(' - ', 1)
        artist = parts[0].strip()
        title = parts[1].strip()
        
    if artist is None:
        artist = "unknown"
        
    # Remove subtitles / remixes / parentheticals from title
    # Strategy: take the part before " - " if it looks like a subtitle (but careful about "Artist - Title" which is already handled?)
    # Actually, "Zo gaat het leven aan je voor - Hillich fjoer | Heilig vuur" -> Title is "Zo gaat het leven aan je voor", Subtitle is rest.
    # But "Rich Matteson - Groovey" -> Artist "Rich Matteson", Title "Groovey".
    # Since we already handled "Artist - Title" for missing artist, now we are looking at "Title - Subtitle" where Artist is known.
    # OR "Title (Subtitle)".
    
    # Remove (...) and [...]
    title = re.sub(r'\s*[\(\[].*?[\)\]]', '', title)
    
    # Remove " - " suffix if it looks like subtitle?
    # e.g. "Zo gaat het leven aan je voor - Hillich fjoer"
    # If we have an artist, and title has " - ", it's likely "Title - Subtitle".
    if ' - ' in title:
         title = title.split(' - ')[0]
         
    return clean_text(title), clean_text(artist)

merged['resolved_title'] = merged.apply(lambda r: resolve_entity(r)[0], axis=1)
merged['resolved_artist'] = merged.apply(lambda r: resolve_entity(r)[1], axis=1)

grouped = merged.groupby(['resolved_title', 'resolved_artist']).agg({
    'total_revenue': 'sum',
    'title': lambda x: list(x.unique())
}).reset_index()

grouped = grouped.sort_values('total_revenue', ascending=False)
# Filter empty/garbage
grouped = grouped[~grouped['resolved_title'].isin(['', 'none', 'unknown'])]

print("__RESULT__:")
print(grouped.head(10).to_json(orient='records'))"""

env_args = {'var_function-call-4082973403781613330': 'file_storage/function-call-4082973403781613330.json', 'var_function-call-18357211790249148335': 'file_storage/function-call-18357211790249148335.json', 'var_function-call-12420417926037808381': [{'resolved_key': ['none', 'unknown'], 'total_revenue': 14647.52}, {'resolved_key': ['groovey', 'rich matteson'], 'total_revenue': 5417.34}, {'resolved_key': ['010-', 'unknown'], 'total_revenue': 4163.48}, {'resolved_key': ['all my friends say (album version)', 'luke bryan'], 'total_revenue': 4110.55}, {'resolved_key': ['kapitel 01', 'kerstin gier'], 'total_revenue': 4091.12}, {'resolved_key': ['beautiful (instrumental)', 'damian marley'], 'total_revenue': 4004.42}, {'resolved_key': ['the story of your life', 'matthew barber'], 'total_revenue': 3962.97}, {'resolved_key': ['a wand\'ring minstrel i, from "the mikado"', 'sir william gilbert & sir arthur sullivan'], 'total_revenue': 3877.43}, {'resolved_key': ['the fire still burns', 'russ ballard'], 'total_revenue': 3807.4}, {'resolved_key': ['vostok', 'craig padilla'], 'total_revenue': 3767.95}, {'resolved_key': ['oblivion beckons', 'byzantine'], 'total_revenue': 3759.01}, {'resolved_key': ['001-', 'unknown'], 'total_revenue': 3742.44}, {'resolved_key': ['so in love with you', 'kenny rogers'], 'total_revenue': 3642.04}, {'resolved_key': ['dancing in the sun', 'george howard'], 'total_revenue': 3624.33}, {'resolved_key': ['bring back the love (spaced out dub)', 'laura harris'], 'total_revenue': 3611.33}, {'resolved_key': ["9 to 5 (tony senghore's gosh darn it! dub)", 'lady sovereign'], 'total_revenue': 3537.95}, {'resolved_key': ['my mouth and me', 'coal train railroad'], 'total_revenue': 3533.61}, {'resolved_key': ['the power of love (rob searle club mix)', 'frankie goes to hollywood'], 'total_revenue': 3529.48}, {'resolved_key': ['ghetto supastar (that is what you are)', 'pras'], 'total_revenue': 3521.11}, {'resolved_key': ['best friends', 'hans zimmer'], 'total_revenue': 3505.13}], 'var_function-call-6652207537909399200': [{'resolved_title': 'groovey', 'resolved_artist': 'rich matteson', 'total_revenue': 5417.34, 'track_id': 4, 'title': ['Groovey', 'Rich Matteson - Groovey']}, {'resolved_title': 'zo gaat het leven aan je voor', 'resolved_artist': 'syb van der ploeg', 'total_revenue': 5256.43, 'track_id': 3, 'title': ['Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'Syb van der Ploeg - Zo gaat het leven aan je voor', 'Zo gaat het leven aan je voor']}, {'resolved_title': 'vagga', 'resolved_artist': 'ske', 'total_revenue': 4981.38, 'track_id': 3, 'title': ['Ske - Vagga', 'Vagga (Feelings Are Great)', 'Vagga']}, {'resolved_title': 'emerge', 'resolved_artist': 'fischerspooner', 'total_revenue': 4896.24, 'track_id': 4, 'title': ['Emerge (Dave Clarke remix)', 'Emerge (Dexter remix)', 'Fischerspooner - Emerge (Dexter remix)', 'Emerge (Dexter remix) (#1)']}, {'resolved_title': 'best friends', 'resolved_artist': 'hans zimmer', 'total_revenue': 4806.24, 'track_id': 3, 'title': ['Best Friends (Madagascar / Robots)', 'Best Friends', 'Hans Zimmer - Best Friends']}, {'resolved_title': '003-', 'resolved_artist': 'unknown', 'total_revenue': 4773.37, 'track_id': 5, 'title': ['003-', '003- (Instrumenntal)']}, {'resolved_title': 'ne veruj', 'resolved_artist': 'vrisak generacije', 'total_revenue': 4693.26, 'track_id': 3, 'title': ['Ne veruj (Beer Drinkers Revenge)', 'Vrisak generacije - Ne veruj', 'Ne veruj']}, {'resolved_title': 'lifework', 'resolved_artist': '服部隆之', 'total_revenue': 4663.91, 'track_id': 3, 'title': ['服部隆之 - Lifework', 'Lifework (HERO -Original Sound Track)', 'Lifework']}, {'resolved_title': 'travel', 'resolved_artist': 'guts pie earshot', 'total_revenue': 4595.34, 'track_id': 3, 'title': ['Guts Pie Earshot - Travel (live)', 'Travel (live) (amparo fugaz)', 'Travel (live)']}, {'resolved_title': 'rotor', 'resolved_artist': 'tété', 'total_revenue': 4520.89, 'track_id': 3, 'title': ['Tété - Rotor', 'Rotor (Primary Structures)', 'Rotor']}, {'resolved_title': 'lovers', 'resolved_artist': 'fausto papetti', 'total_revenue': 4516.66, 'track_id': 3, 'title': ['Lovers', 'Fausto Papetti - Lovers', 'Lovers (27ª raccolta)']}, {'resolved_title': 'truth', 'resolved_artist': 'love amongst ruin', 'total_revenue': 4491.11, 'track_id': 3, 'title': ['Love Amongst Ruin - Truth', 'Truth', 'Truth (Love Aongst Ruin)']}, {'resolved_title': 'chile', 'resolved_artist': 'neil biggin', 'total_revenue': 4456.97, 'track_id': 3, 'title': ['Neil Biggin - Chile', 'Chile (Re-Loaded)', 'Chile']}, {'resolved_title': 'faded', 'resolved_artist': 'suzanne de bussac', 'total_revenue': 4351.6, 'track_id': 3, 'title': ['Faded (The Valley of Baca)', 'Faded', 'Suzanne de Bussac - Faded']}, {'resolved_title': 'colete', 'resolved_artist': 'forte apache', 'total_revenue': 4347.57, 'track_id': 3, 'title': ['Forte Apache - Colete', 'Colete (Rapina)', 'Colete']}], 'var_function-call-5069747752307880239': {'groovey': [{'track_id': '17312', 'title': 'Groovey', 'artist': 'Rich Matteson', 'total_revenue': 1036.29}, {'track_id': '7710', 'title': '006-Groovey', 'artist': 'Rich Matteson', 'total_revenue': 251.16}, {'track_id': '6146', 'title': 'Rich Matteson - Groovey', 'artist': 'None', 'total_revenue': 1288.75}, {'track_id': '16496', 'title': 'Groovey', 'artist': 'Rich Matteson', 'total_revenue': 949.82}, {'track_id': '8829', 'title': 'Groovey', 'artist': 'Rich Matteson', 'total_revenue': 2142.48}], 'zo': [{'track_id': '12620', 'title': 'Zo gaat het leven aan je voor - Hillich fjoer | Heilig vuur', 'artist': 'Syb van der Ploeg', 'total_revenue': 2377.59}, {'track_id': '3024', 'title': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'artist': 'Syb van der Ploeg', 'total_revenue': 1754.6800000000003}, {'track_id': '12854', 'title': '006-Zo gaat het leven aan je voor', 'artist': 'Syb van der Ploeg', 'total_revenue': 1379.6699999999998}, {'track_id': '13225', 'title': 'Syb van der Ploeg - Zo gaat het leven aan je voor', 'artist': 'None', 'total_revenue': 1477.38}, {'track_id': '3435', 'title': 'Zo gaat het leven aan je voor', 'artist': 'Syb van der Ploeg', 'total_revenue': 2024.37}], 'emerge': [{'track_id': '10981', 'title': 'Funky Emergency (Jazz Brakes, Volume 2)', 'artist': 'DJ Food', 'total_revenue': 917.27}, {'track_id': '7575', 'title': 'Emerge (Dave Clarke remix)', 'artist': 'Fischerspooner', 'total_revenue': 850.86}, {'track_id': '10606', 'title': 'Emerge (Dexter remix)', 'artist': 'Fischerspooner', 'total_revenue': 672.1200000000001}, {'track_id': '4895', 'title': 'Fischerspooner - Emerge (Dexter remix)', 'artist': 'None', 'total_revenue': 1610.46}, {'track_id': '6988', 'title': 'Emerge (Dexter remix) (#1)', 'artist': 'Fischerspooner', 'total_revenue': 1762.8000000000002}, {'track_id': '10166', 'title': 'Emerge (Dexter remix) - #1', 'artist': 'Fischerspooner', 'total_revenue': 850.61}, {'track_id': '17167', 'title': '027-Emerge (Dexter remix)', 'artist': 'Fischerspooner', 'total_revenue': 1769.03}]}}

exec(code, env_args)
