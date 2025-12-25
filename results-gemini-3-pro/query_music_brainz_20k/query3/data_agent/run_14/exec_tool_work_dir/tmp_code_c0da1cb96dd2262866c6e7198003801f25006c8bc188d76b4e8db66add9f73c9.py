code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-3742390528333561331'], 'r') as f:
    sales_data = json.load(f)

with open(locals()['var_function-call-494577590784018287'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)
df_sales['revenue_usd'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)
df_merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')

def normalize(text):
    if not isinstance(text, str): return ""
    return text.lower()

df_merged['norm_title_simple'] = df_merged['title'].apply(normalize)
df_merged['norm_artist_simple'] = df_merged['artist'].apply(normalize)

# Candidates to check
candidates = [
    {"name": "Kiä meil pahanu", "keywords": ["pahanu"]},
    {"name": "Groovey", "keywords": ["groovey"]},
    {"name": "The Fire Still Burns", "keywords": ["fire still burns"]},
    {"name": "Three Seasons", "keywords": ["three seasons"]},
    {"name": "L'Escalade obscure", "keywords": ["lescalade obscure", "l'escalade obscure"]},
    {"name": "Stormy", "keywords": ["stormy"]},
    {"name": "Too Beautiful", "keywords": ["too beautiful"]},
    {"name": "Zo gaat het leven aan je voor", "keywords": ["zo gaat het leven"]},
    {"name": "Vostok", "keywords": ["vostok"]},
    {"name": "Travel", "keywords": ["travel"]}
]

results = []

for cand in candidates:
    total_rev = 0
    matched_tracks = []
    
    for _, row in df_merged.iterrows():
        title = row['norm_title_simple']
        # Check if any keyword matches
        match = False
        for k in cand['keywords']:
            if k in title:
                match = True
                break
        
        if match:
            # Optional: check artist consistency if needed, but for now just gather revenue
            # For "Groovey", we saw "Rich Matteson" and "None" (with title including Rich Matteson).
            # For "Kiä meil pahanu", artist was "[tiidmäldä]" or "None".
            total_rev += row['revenue_usd']
            matched_tracks.append((row['title'], row['artist'], row['revenue_usd']))
            
    results.append({
        "name": cand['name'],
        "total_revenue": total_rev,
        "sample_tracks": matched_tracks[:3] # Show first 3 matches
    })

results.sort(key=lambda x: x['total_revenue'], reverse=True)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-3742390528333561331': 'file_storage/function-call-3742390528333561331.json', 'var_function-call-494577590784018287': 'file_storage/function-call-494577590784018287.json', 'var_function-call-15915298125837850317': {'top_song_norm_title': '', 'top_song_norm_artist': '', 'total_revenue': 177420.82, 'sample_title': 'Приходи - Зн@менатель', 'sample_artist': 'Сплин'}, 'var_function-call-1869179159605482992': {'top_5': [{'norm_title': 'none', 'norm_artist': 'none', 'revenue_usd': 14647.52}, {'norm_title': '001', 'norm_artist': 'none', 'revenue_usd': 5866.48}, {'norm_title': '003', 'norm_artist': 'none', 'revenue_usd': 5022.32}, {'norm_title': '005', 'norm_artist': 'none', 'revenue_usd': 4281.18}, {'norm_title': '002', 'norm_artist': 'none', 'revenue_usd': 4237.16}], 'top_song_sample_title': 'None', 'top_song_sample_artist': 'None', 'top_song_sample_album': 'Mijn Restaurant!'}, 'var_function-call-9908902087357812735': [{'norm_title': '003', 'norm_artist': '', 'revenue_usd': 8582.15, 'track_count': 9, 'sample_title': '003-', 'sample_artist': 'None'}, {'norm_title': '001', 'norm_artist': '', 'revenue_usd': 7467.97, 'track_count': 7, 'sample_title': '00-1', 'sample_artist': '[unknown]'}, {'norm_title': '004', 'norm_artist': '', 'revenue_usd': 7271.32, 'track_count': 8, 'sample_title': '004- ', 'sample_artist': ' '}, {'norm_title': '005', 'norm_artist': '', 'revenue_usd': 6155.29, 'track_count': 8, 'sample_title': '005-', 'sample_artist': 'None'}, {'norm_title': '009', 'norm_artist': '', 'revenue_usd': 5045.7, 'track_count': 4, 'sample_title': '009-  ', 'sample_artist': ' '}, {'norm_title': '002', 'norm_artist': '', 'revenue_usd': 5013.4400000000005, 'track_count': 4, 'sample_title': '002', 'sample_artist': 'None'}, {'norm_title': 'kiä meil pahanu', 'norm_artist': '', 'revenue_usd': 4916.11, 'track_count': 3, 'sample_title': 'Kiä meil pahanu? (Mina lätsi Siidile)', 'sample_artist': '[tiidmäldä]'}, {'norm_title': '010', 'norm_artist': '', 'revenue_usd': 4734.360000000001, 'track_count': 5, 'sample_title': '010-', 'sample_artist': 'None'}, {'norm_title': '012', 'norm_artist': '', 'revenue_usd': 4641.08, 'track_count': 4, 'sample_title': '012-', 'sample_artist': ' '}, {'norm_title': '006', 'norm_artist': '', 'revenue_usd': 4366.82, 'track_count': 5, 'sample_title': '006- (Inst-umental)', 'sample_artist': 'None'}, {'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'revenue_usd': 4128.59, 'track_count': 3, 'sample_title': 'Groovey', 'sample_artist': 'Rich Matteson'}, {'norm_title': 'the fire still burns', 'norm_artist': 'russ ballard', 'revenue_usd': 3807.4, 'track_count': 2, 'sample_title': 'The Fire Still Burns', 'sample_artist': 'Russ Ballard'}, {'norm_title': 'three seasons', 'norm_artist': 'swallow', 'revenue_usd': 3803.5, 'track_count': 2, 'sample_title': 'Three Seasons (Aresco)', 'sample_artist': 'Swallow'}, {'norm_title': 'lescalade obscure', 'norm_artist': 'charles koechlin', 'revenue_usd': 3802.76, 'track_count': 2, 'sample_title': "L'Escalade obscure", 'sample_artist': 'Charles Koechlin'}, {'norm_title': 'stormy', 'norm_artist': 'scott walker', 'revenue_usd': 3792.1800000000003, 'track_count': 2, 'sample_title': 'Stormy (Scott: The Collection 1967-1970)', 'sample_artist': 'Scott Walker'}, {'norm_title': 'too beautiful', 'norm_artist': 'will kimbrough', 'revenue_usd': 3784.37, 'track_count': 2, 'sample_title': 'Too Beautiful (Godsend)', 'sample_artist': 'Will Kimbrough'}, {'norm_title': '007', 'norm_artist': '', 'revenue_usd': 3781.89, 'track_count': 5, 'sample_title': '007-', 'sample_artist': 'None'}, {'norm_title': 'zo gaat het leven aan je voor', 'norm_artist': 'syb van der ploeg', 'revenue_usd': 3779.05, 'track_count': 2, 'sample_title': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'sample_artist': 'Syb van der Ploeg'}, {'norm_title': 'vostok', 'norm_artist': 'craig padilla', 'revenue_usd': 3767.95, 'track_count': 3, 'sample_title': 'Vostok', 'sample_artist': 'Craig Padilla'}, {'norm_title': 'travel', 'norm_artist': 'guts pie earshot', 'revenue_usd': 3703.98, 'track_count': 2, 'sample_title': 'Travel (live) (amparo fugaz)', 'sample_artist': 'Guts Pie Earshot'}], 'var_function-call-4412476628665606823': [{'track_id': '523', 'title': '003-Ruralia Hungarica - Molto Vivace', 'artist': 'Erno Dohnanyi', 'album': 'Kreisler: 1928 Victor Recordings: Favourite Short Pieces (unknown)', 'revenue_usd': 232.37}, {'track_id': '1600', 'title': '0003-Autowalker', 'artist': 'OUTABERO', 'album': 'Cuprunoid (2010)', 'revenue_usd': 1655.79}, {'track_id': '2645', 'title': '003-Half Cocked', 'artist': 'Larry the Cable Guy', 'album': 'Tailgate Party (2009)', 'revenue_usd': 1180.34}, {'track_id': '3626', 'title': '003-A Greater Path', 'artist': 'Asterius', 'album': 'A Moment of Singularity (unknown)', 'revenue_usd': 1734.21}, {'track_id': '3907', 'title': '003-Hail, Hail', 'artist': 'Pearl Jam', 'album': '2000-10-11: St. Louis, MO, USA (#54) (2001)', 'revenue_usd': 459.36}, {'track_id': '9190', 'title': '003-Medicine Man', 'artist': 'AgCent Caine', 'album': 'Chillout Fourever (1997)', 'revenue_usd': 474.66}, {'track_id': '10602', 'title': '003-Johnny Vender Hjem fra Krig', 'artist': 'Rde Mor', 'album': 'Sylvesters Drm (1978)', 'revenue_usd': 1529.88}, {'track_id': '11898', 'title': '003-Broken You', 'artist': 'The Lovely and Talented', 'album': 'The Lovely Talented and (2006)', 'revenue_usd': 929.57}, {'track_id': '12455', 'title': '003-Together All', 'artist': 'Novi Singers', 'album': 'Go Right: Jazz From Poland 1963-75 (1999)', 'revenue_usd': 1005.24}, {'track_id': '13261', 'title': "003-Don't Tell Me (Timo Maas mix)", 'artist': 'Madonna', 'album': 'Music (2001)', 'revenue_usd': 845.59}], 'var_function-call-17639897108594362267': [{'norm_title': 'kiä meil pahanu', 'norm_artist': '', 'revenue_usd': 4916.11, 'track_count': 3, 'sample_title': 'Kiä meil pahanu? (Mina lätsi Siidile)', 'sample_artist': '[tiidmäldä]', 'is_valid': True}, {'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'revenue_usd': 4128.59, 'track_count': 3, 'sample_title': 'Groovey', 'sample_artist': 'Rich Matteson', 'is_valid': True}, {'norm_title': 'the fire still burns', 'norm_artist': 'russ ballard', 'revenue_usd': 3807.4, 'track_count': 2, 'sample_title': 'The Fire Still Burns', 'sample_artist': 'Russ Ballard', 'is_valid': True}, {'norm_title': 'three seasons', 'norm_artist': 'swallow', 'revenue_usd': 3803.5, 'track_count': 2, 'sample_title': 'Three Seasons (Aresco)', 'sample_artist': 'Swallow', 'is_valid': True}, {'norm_title': 'lescalade obscure', 'norm_artist': 'charles koechlin', 'revenue_usd': 3802.76, 'track_count': 2, 'sample_title': "L'Escalade obscure", 'sample_artist': 'Charles Koechlin', 'is_valid': True}, {'norm_title': 'stormy', 'norm_artist': 'scott walker', 'revenue_usd': 3792.1800000000003, 'track_count': 2, 'sample_title': 'Stormy (Scott: The Collection 1967-1970)', 'sample_artist': 'Scott Walker', 'is_valid': True}, {'norm_title': 'too beautiful', 'norm_artist': 'will kimbrough', 'revenue_usd': 3784.37, 'track_count': 2, 'sample_title': 'Too Beautiful (Godsend)', 'sample_artist': 'Will Kimbrough', 'is_valid': True}, {'norm_title': 'zo gaat het leven aan je voor', 'norm_artist': 'syb van der ploeg', 'revenue_usd': 3779.05, 'track_count': 2, 'sample_title': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'sample_artist': 'Syb van der Ploeg', 'is_valid': True}, {'norm_title': 'vostok', 'norm_artist': 'craig padilla', 'revenue_usd': 3767.95, 'track_count': 3, 'sample_title': 'Vostok', 'sample_artist': 'Craig Padilla', 'is_valid': True}, {'norm_title': 'travel', 'norm_artist': 'guts pie earshot', 'revenue_usd': 3703.98, 'track_count': 2, 'sample_title': 'Travel (live) (amparo fugaz)', 'sample_artist': 'Guts Pie Earshot', 'is_valid': True}], 'var_function-call-7897479046992249754': [{'track_id': '10921', 'title': 'Kiä meil pahanu? (Mina lätsi Siidile)', 'artist': '[tiidmäldä]', 'album': 'Mina', 'revenue_usd': 1919.82}, {'track_id': '16297', 'title': 'Kiä meil pahanu', 'artist': '[tiidmäldä]', 'album': 'Mina lätsi Siidile', 'revenue_usd': 1712.45}, {'track_id': '5092', 'title': '[tiidmäldä] - Kiä meil pahanu?', 'artist': 'None', 'album': 'Mina lätsi Siidile', 'revenue_usd': 1283.84}], 'var_function-call-2314726390165389979': [{'title': 'Groovey', 'artist': 'Rich Matteson', 'revenue_usd': 1036.29, 'norm_title': 'groovey'}, {'title': '006-Groovey', 'artist': 'Rich Matteson', 'revenue_usd': 251.16, 'norm_title': '006groovey'}, {'title': 'Rich Matteson - Groovey', 'artist': 'None', 'revenue_usd': 1288.75, 'norm_title': 'rich matteson groovey'}, {'title': 'Groovey', 'artist': 'Rich Matteson', 'revenue_usd': 949.82, 'norm_title': 'groovey'}, {'title': 'Groovey', 'artist': 'Rich Matteson', 'revenue_usd': 2142.48, 'norm_title': 'groovey'}]}

exec(code, env_args)
