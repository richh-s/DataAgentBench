code = """import json
import pandas as pd
import re

with open(locals()['var_function-call-2517101731408743361'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-6464260199203399189'], 'r') as f:
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
    # Remove text in parentheses/brackets
    s = re.sub(r'\s*\(.*?\)\s*', '', s)
    s = re.sub(r'\s*\[.*?\]\s*', '', s)
    return s.strip()

def clean_track(row):
    title = str(row['title']).strip()
    artist = str(row['artist']).strip()
    
    missing_vals = ['None', 'null', '[unknown]', '', 'nan', 'Unknown Artist']
    
    # Try splitting if artist is missing
    if artist in missing_vals:
        if ' - ' in title:
            parts = title.split(' - ', 1)
            artist = parts[0].strip()
            title = parts[1].strip()
    
    # Clean title
    clean_t = clean_string(title)
    clean_a = clean_string(artist)
    
    # If title became empty (e.g. was only parens), revert to original
    if not clean_t:
        clean_t = title
        
    return pd.Series([clean_t, clean_a, title, artist])

merged[['clean_title', 'clean_artist', 'orig_title', 'orig_artist']] = merged.apply(clean_track, axis=1)

# Group
grouped = merged.groupby(['clean_artist', 'clean_title'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values(by='total_revenue', ascending=False)

# Filter out None/None
grouped = grouped[~((grouped['clean_artist'].isin(['None', ''])) & (grouped['clean_title'].isin(['None', ''])))]

print("__RESULT__:")
print(grouped.head(15).to_json(orient='records'))"""

env_args = {'var_function-call-9032484242444107887': ['sales'], 'var_function-call-9032484242444109838': ['tracks'], 'var_function-call-2517101731408743361': 'file_storage/function-call-2517101731408743361.json', 'var_function-call-5327854219375283823': [{'COUNT(*)': '19375'}], 'var_function-call-6464260199203399189': 'file_storage/function-call-6464260199203399189.json', 'var_function-call-6131387658296098835': [{'clean_artist': 'None', 'clean_title': 'None', 'total_revenue': 14647.52}, {'clean_artist': 'Rich Matteson', 'clean_title': 'Groovey', 'total_revenue': 5417.34}, {'clean_artist': 'None', 'clean_title': '010-', 'total_revenue': 4163.48}, {'clean_artist': 'Luke Bryan', 'clean_title': 'All My Friends Say (album version)', 'total_revenue': 4110.55}, {'clean_artist': 'Kerstin Gier', 'clean_title': 'Kapitel 01', 'total_revenue': 4091.12}, {'clean_artist': 'Damian Marley', 'clean_title': 'Beautiful (instrumental)', 'total_revenue': 4004.42}, {'clean_artist': 'Matthew Barber', 'clean_title': 'The Story of Your Life', 'total_revenue': 3962.97}, {'clean_artist': 'Sir William Gilbert & Sir Arthur Sullivan', 'clean_title': 'A Wand\'ring Minstrel I, From "The Mikado"', 'total_revenue': 3877.43}, {'clean_artist': 'Russ Ballard', 'clean_title': 'The Fire Still Burns', 'total_revenue': 3807.4}, {'clean_artist': 'Craig Padilla', 'clean_title': 'Vostok', 'total_revenue': 3767.95}]}

exec(code, env_args)
