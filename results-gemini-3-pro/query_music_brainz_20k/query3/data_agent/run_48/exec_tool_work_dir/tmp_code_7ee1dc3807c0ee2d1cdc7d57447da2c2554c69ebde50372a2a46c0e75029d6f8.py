code = """import json
import pandas as pd
import re

# Load data
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

def clean_string(s):
    if not isinstance(s, str):
        return ""
    # Remove text in parens? e.g. "Song (Live)" -> "Song"
    # But checking if this is safe. 
    # Let's keep it simple first: lower, strip.
    s = s.lower().strip()
    return s

def resolve_entity(row):
    title = str(row['title'])
    artist = str(row['artist'])
    
    if artist.lower() in ['none', 'nan', '', '[unknown]']:
        artist = None
    
    if artist is None and ' - ' in title:
        parts = title.split(' - ', 1)
        artist = parts[0].strip()
        title = parts[1].strip()
    
    if artist is None:
        artist = "unknown"
        
    # Remove parenthetical info from title for better grouping?
    # e.g. "All My Friends Say (Album Version)" -> "All My Friends Say"
    # e.g. "Beautiful (Instrumental)" -> "Beautiful"
    # e.g. "Song Name - Live" -> "Song Name" (if handled by split above)
    
    # Regex to remove (...) and [...] at the end
    title_clean = re.sub(r'\s*[\(\[].*?[\)\]]', '', title)
    title_clean = clean_string(title_clean)
    artist_clean = clean_string(artist)
    
    return title_clean, artist_clean

merged['resolved_title'] = merged.apply(lambda r: resolve_entity(r)[0], axis=1)
merged['resolved_artist'] = merged.apply(lambda r: resolve_entity(r)[1], axis=1)

# Group
grouped = merged.groupby(['resolved_title', 'resolved_artist']).agg({
    'total_revenue': 'sum',
    'track_id': 'count', # count of tracks aggregated
    'title': lambda x: list(x.unique())
}).reset_index()

grouped = grouped.sort_values('total_revenue', ascending=False)

# Filter out empty/garbage titles
grouped = grouped[grouped['resolved_title'] != 'none']
grouped = grouped[grouped['resolved_title'] != '']
grouped = grouped[grouped['resolved_title'] != '010-'] # saw this in prev output
grouped = grouped[grouped['resolved_title'] != '001-']

print("__RESULT__:")
print(grouped.head(15).to_json(orient='records'))"""

env_args = {'var_function-call-4082973403781613330': 'file_storage/function-call-4082973403781613330.json', 'var_function-call-18357211790249148335': 'file_storage/function-call-18357211790249148335.json', 'var_function-call-12420417926037808381': [{'resolved_key': ['none', 'unknown'], 'total_revenue': 14647.52}, {'resolved_key': ['groovey', 'rich matteson'], 'total_revenue': 5417.34}, {'resolved_key': ['010-', 'unknown'], 'total_revenue': 4163.48}, {'resolved_key': ['all my friends say (album version)', 'luke bryan'], 'total_revenue': 4110.55}, {'resolved_key': ['kapitel 01', 'kerstin gier'], 'total_revenue': 4091.12}, {'resolved_key': ['beautiful (instrumental)', 'damian marley'], 'total_revenue': 4004.42}, {'resolved_key': ['the story of your life', 'matthew barber'], 'total_revenue': 3962.97}, {'resolved_key': ['a wand\'ring minstrel i, from "the mikado"', 'sir william gilbert & sir arthur sullivan'], 'total_revenue': 3877.43}, {'resolved_key': ['the fire still burns', 'russ ballard'], 'total_revenue': 3807.4}, {'resolved_key': ['vostok', 'craig padilla'], 'total_revenue': 3767.95}, {'resolved_key': ['oblivion beckons', 'byzantine'], 'total_revenue': 3759.01}, {'resolved_key': ['001-', 'unknown'], 'total_revenue': 3742.44}, {'resolved_key': ['so in love with you', 'kenny rogers'], 'total_revenue': 3642.04}, {'resolved_key': ['dancing in the sun', 'george howard'], 'total_revenue': 3624.33}, {'resolved_key': ['bring back the love (spaced out dub)', 'laura harris'], 'total_revenue': 3611.33}, {'resolved_key': ["9 to 5 (tony senghore's gosh darn it! dub)", 'lady sovereign'], 'total_revenue': 3537.95}, {'resolved_key': ['my mouth and me', 'coal train railroad'], 'total_revenue': 3533.61}, {'resolved_key': ['the power of love (rob searle club mix)', 'frankie goes to hollywood'], 'total_revenue': 3529.48}, {'resolved_key': ['ghetto supastar (that is what you are)', 'pras'], 'total_revenue': 3521.11}, {'resolved_key': ['best friends', 'hans zimmer'], 'total_revenue': 3505.13}]}

exec(code, env_args)
