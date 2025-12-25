code = """import json
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

def clean_record(row):
    title = str(row['title']).strip()
    artist = str(row['artist']).strip()
    invalid_values = ['None', '[unknown]', 'Unknown', '', 'nan']
    
    # Artist extraction
    if artist in invalid_values and ' - ' in title:
        parts = title.split(' - ', 1)
        if len(parts) == 2:
            p_artist = parts[0].strip()
            p_title = parts[1].strip()
            # Basic validation
            if len(p_artist) < 50 and not re.match(r'^\d+$', p_artist):
                artist = p_artist
                title = p_title
    
    if title in invalid_values: title = ""
    if artist in invalid_values: artist = ""
    return pd.Series([title, artist])

merged[['clean_title', 'clean_artist']] = merged.apply(clean_record, axis=1)

def aggressive_normalize(text):
    if not text: return ""
    text = text.lower()
    # Remove leading track numbers e.g. "001-", "01 ", "1. "
    text = re.sub(r'^\d+[\s\-\.]+', '', text)
    # Remove content in parens
    text = re.sub(r'\(.*?\)', '', text)
    # Remove content in brackets
    text = re.sub(r'\[.*?\]', '', text)
    # Remove " - " and everything after (risky? assume subtitle)
    # For safety, let's only do this if the string is long or specific logic.
    # Actually, for "Zo gaat...", the suffix is " - Hillich fjoer..."
    # Let's try removing " - .*"
    text = re.sub(r'\s-\s.*', '', text)
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

merged['norm_title'] = merged['clean_title'].apply(aggressive_normalize)
merged['norm_artist'] = merged['clean_artist'].apply(aggressive_normalize)

# Filter invalid artists
valid = merged[(merged['norm_artist'] != "") & (merged['norm_title'] != "")]

grouped = valid.groupby(['norm_title', 'norm_artist'])['revenue_usd'].sum().reset_index()
grouped = grouped.sort_values('revenue_usd', ascending=False)

top_candidates = []
for i in range(10):
    if i >= len(grouped): break
    row = grouped.iloc[i]
    nt = row['norm_title']
    na = row['norm_artist']
    rev = row['revenue_usd']
    
    subset = valid[(valid['norm_title'] == nt) & (valid['norm_artist'] == na)]
    display_title = subset['clean_title'].mode()[0]
    display_artist = subset['clean_artist'].mode()[0]
    
    top_candidates.append({
        "rank": i+1,
        "title": display_title,
        "artist": display_artist,
        "revenue": rev,
        "norm_title": nt
    })

print("__RESULT__:")
print(json.dumps(top_candidates))"""

env_args = {'var_function-call-3992495390837066285': 'file_storage/function-call-3992495390837066285.json', 'var_function-call-7409539752900977037': 'file_storage/function-call-7409539752900977037.json', 'var_function-call-16025719920181743167': {'top_20': [{'norm_title': '', 'norm_artist': '', 'revenue_usd': 203103.18}, {'norm_title': 'none', 'norm_artist': 'none', 'revenue_usd': 14647.52}, {'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'revenue_usd': 5417.34}, {'norm_title': '', 'norm_artist': 'unknown', 'revenue_usd': 4851.83}, {'norm_title': '001', 'norm_artist': 'none', 'revenue_usd': 4681.75}, {'norm_title': 'tv', 'norm_artist': '', 'revenue_usd': 4527.58}, {'norm_title': '005', 'norm_artist': 'none', 'revenue_usd': 4281.18}, {'norm_title': '002', 'norm_artist': 'none', 'revenue_usd': 4237.16}, {'norm_title': '010', 'norm_artist': 'none', 'revenue_usd': 4163.48}, {'norm_title': 'zo gaat het leven aan je voor hillich fjoer heilig vuur', 'norm_artist': 'syb van der ploeg', 'revenue_usd': 4132.27}, {'norm_title': 'all my friends say album version', 'norm_artist': 'luke bryan', 'revenue_usd': 4110.55}, {'norm_title': 'kapitel 01', 'norm_artist': 'kerstin gier', 'revenue_usd': 4091.12}, {'norm_title': '004', 'norm_artist': '', 'revenue_usd': 4026.71}, {'norm_title': 'beautiful instrumental', 'norm_artist': 'damian marley', 'revenue_usd': 4004.42}, {'norm_title': 'the story of your life', 'norm_artist': 'matthew barber', 'revenue_usd': 3962.97}, {'norm_title': 'thousand finger man salsoul 30th', 'norm_artist': 'candido', 'revenue_usd': 3934.83}, {'norm_title': 'a wandring minstrel i from the mikado', 'norm_artist': 'sir william gilbert sir arthur sullivan', 'revenue_usd': 3877.43}, {'norm_title': 'fret one grow old inside your wave', 'norm_artist': 'ugly winner', 'revenue_usd': 3844.09}, {'norm_title': 'the fire still burns', 'norm_artist': 'russ ballard', 'revenue_usd': 3807.4}, {'norm_title': 'vostok', 'norm_artist': 'craig padilla', 'revenue_usd': 3767.95}], 'winner': {'title': 'Όνειρα ζωής', 'artist': 'Χρήστος Δάντης', 'revenue': 203103.18}}, 'var_function-call-6781856173906030022': [{'rank': 1, 'title': '004-', 'artist': '', 'norm_title': '004', 'norm_artist': '', 'revenue': 7271.32, 'track_count': 8}, {'rank': 2, 'title': '003-', 'artist': '', 'norm_title': '003', 'norm_artist': '', 'revenue': 7090.13, 'track_count': 7}, {'rank': 3, 'title': '001-', 'artist': '', 'norm_title': '001', 'norm_artist': '', 'revenue': 6283.24, 'track_count': 6}, {'rank': 4, 'title': '005-', 'artist': '', 'norm_title': '005', 'norm_artist': '', 'revenue': 6155.29, 'track_count': 8}, {'rank': 5, 'title': 'Groovey', 'artist': 'Rich Matteson', 'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'revenue': 5417.34, 'track_count': 4}, {'rank': 6, 'title': '009-', 'artist': '', 'norm_title': '009', 'norm_artist': '', 'revenue': 5045.7, 'track_count': 4}, {'rank': 7, 'title': '002-', 'artist': '', 'norm_title': '002', 'norm_artist': '', 'revenue': 5013.4400000000005, 'track_count': 4}, {'rank': 8, 'title': '010-', 'artist': '', 'norm_title': '010', 'norm_artist': '', 'revenue': 4734.360000000001, 'track_count': 5}, {'rank': 9, 'title': '012-', 'artist': '', 'norm_title': '012', 'norm_artist': '', 'revenue': 4641.08, 'track_count': 4}, {'rank': 10, 'title': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'artist': 'Syb van der Ploeg', 'norm_title': 'zo gaat het leven aan je voor hillich fjoer heilig vuur', 'norm_artist': 'syb van der ploeg', 'revenue': 4132.27, 'track_count': 2}], 'var_function-call-15376139809597613316': [{'rank': 1, 'title': 'Groovey', 'artist': 'Rich Matteson', 'revenue': 5417.34, 'track_count': 4}, {'rank': 2, 'title': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'artist': 'Syb van der Ploeg', 'revenue': 4132.27, 'track_count': 2}, {'rank': 3, 'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan', 'revenue': 4110.55, 'track_count': 3}, {'rank': 4, 'title': 'Kapitel 01', 'artist': 'Kerstin Gier', 'revenue': 4091.12, 'track_count': 2}, {'rank': 5, 'title': 'Beautiful (instrumental)', 'artist': 'Damian Marley', 'revenue': 4004.42, 'track_count': 4}, {'rank': 6, 'title': 'The Story of Your Life', 'artist': 'Matthew Barber', 'revenue': 3962.97, 'track_count': 4}, {'rank': 7, 'title': 'Thousand Finger Man (Salsoul 30th)', 'artist': 'Candido', 'revenue': 3934.83, 'track_count': 2}, {'rank': 8, 'title': 'A Wand\'ring Minstrel I, From "The Mikado"', 'artist': 'Sir William Gilbert & Sir Arthur Sullivan', 'revenue': 3877.43, 'track_count': 2}, {'rank': 9, 'title': 'Fret One (Grow Old) (Inside Your Wave)', 'artist': 'Ugly Winner', 'revenue': 3844.09, 'track_count': 2}, {'rank': 10, 'title': 'The Fire Still Burns', 'artist': 'Russ Ballard', 'revenue': 3807.4, 'track_count': 2}], 'var_function-call-1232624291153603118': {'groovey': [{'track_id': '17312', 'title': 'Groovey', 'artist': 'Rich Matteson', 'revenue_usd': 1036.29}, {'track_id': '7710', 'title': '006-Groovey', 'artist': 'Rich Matteson', 'revenue_usd': 251.16}, {'track_id': '6146', 'title': 'Rich Matteson - Groovey', 'artist': 'None', 'revenue_usd': 1288.75}, {'track_id': '16496', 'title': 'Groovey', 'artist': 'Rich Matteson', 'revenue_usd': 949.82}, {'track_id': '8829', 'title': 'Groovey', 'artist': 'Rich Matteson', 'revenue_usd': 2142.48}], 'all_my_friends': [{'track_id': '2133', 'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan', 'revenue_usd': 1501.6699999999998}, {'track_id': '10416', 'title': '002-All My Friends Say (album version)', 'artist': 'Luke Bryan', 'revenue_usd': 1070.38}, {'track_id': '12601', 'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan', 'revenue_usd': 1739.54}, {'track_id': '3144', 'title': 'Luke Bryan - All My Friends Say (album version)', 'artist': 'None', 'revenue_usd': 869.34}], 'zo_gaat': [{'track_id': '12620', 'title': 'Zo gaat het leven aan je voor - Hillich fjoer | Heilig vuur', 'artist': 'Syb van der Ploeg', 'revenue_usd': 2377.59}, {'track_id': '3024', 'title': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'artist': 'Syb van der Ploeg', 'revenue_usd': 1754.6800000000003}, {'track_id': '12854', 'title': '006-Zo gaat het leven aan je voor', 'artist': 'Syb van der Ploeg', 'revenue_usd': 1379.6699999999998}, {'track_id': '13225', 'title': 'Syb van der Ploeg - Zo gaat het leven aan je voor', 'artist': 'None', 'revenue_usd': 1477.38}, {'track_id': '3435', 'title': 'Zo gaat het leven aan je voor', 'artist': 'Syb van der Ploeg', 'revenue_usd': 2024.37}]}}

exec(code, env_args)
