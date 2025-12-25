code = """import json
import pandas as pd
import re

# Re-load (or reuse variables if state persisted, but safer to reload in fresh context logic)
# Actually, I need to replicate the cleaning logic to filter. 
# I will output the detailed rows for the top groups.

with open(locals()['var_function-call-6059198179457054813'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-1039588835092017339'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

df_sales['track_id'] = df_sales['track_id'].astype(str)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

def normalize(text):
    if text is None: return ""
    s = str(text).lower()
    if s in ['none', 'null', 'unknown', '[unknown]']:
        return ""
    s = re.sub(r'\(.*?\)', '', s)
    s = re.sub(r'\[.*?\]', '', s)
    s = re.sub(r'[^\w\s]', '', s)
    return s.strip()

def process_row(row):
    title_raw = str(row['title']) if row['title'] else ""
    artist_raw = str(row['artist']) if row['artist'] else ""
    
    artist_clean = normalize(artist_raw)
    
    title_parts = title_raw.split(' - ', 1)
    
    final_artist = artist_clean
    final_title = normalize(title_raw)
    
    if artist_clean == "":
        if len(title_parts) == 2:
            pot_artist = normalize(title_parts[0])
            pot_title = normalize(title_parts[1])
            if pot_artist and pot_title:
                final_artist = pot_artist
                final_title = pot_title
    else:
        if len(title_parts) == 2:
            p0 = normalize(title_parts[0])
            p1 = normalize(title_parts[1])
            if p0 == artist_clean:
                final_title = p1
                
    return pd.Series([final_artist, final_title])

df[['clean_artist', 'clean_title']] = df.apply(process_row, axis=1)

# Inspect "003"
mask_003 = (df['clean_title'] == "003")
rows_003 = df[mask_003][['track_id', 'title', 'artist', 'album', 'total_revenue']].head(10).to_dict(orient='records')

# Inspect "rich matteson"
mask_rich = (df['clean_artist'] == "rich matteson") & (df['clean_title'] == "groovey")
rows_rich = df[mask_rich][['track_id', 'title', 'artist', 'album', 'total_revenue']].head(10).to_dict(orient='records')

print("__RESULT__:")
print(json.dumps({"rows_003": rows_003, "rows_rich": rows_rich}))"""

env_args = {'var_function-call-6059198179457054813': 'file_storage/function-call-6059198179457054813.json', 'var_function-call-1039588835092017339': 'file_storage/function-call-1039588835092017339.json', 'var_function-call-2520799401825761242': {'title': 'None', 'artist': 'None', 'revenue_usd': 14647.52, 'clean_title': 'none', 'clean_artist': 'unknown'}, 'var_function-call-5557107916154986499': [{'clean_artist': '', 'clean_title': '003', 'total_revenue': 8582.15}, {'clean_artist': '', 'clean_title': '001', 'total_revenue': 7467.97}, {'clean_artist': '', 'clean_title': '004', 'total_revenue': 7271.32}, {'clean_artist': '', 'clean_title': '005', 'total_revenue': 6155.29}, {'clean_artist': 'rich matteson', 'clean_title': 'groovey', 'total_revenue': 5417.34}, {'clean_artist': 'syb van der ploeg', 'clean_title': 'zo gaat het leven aan je voor', 'total_revenue': 5256.43}, {'clean_artist': '', 'clean_title': '009', 'total_revenue': 5045.7}, {'clean_artist': '', 'clean_title': '002', 'total_revenue': 5013.4400000000005}, {'clean_artist': 'ske', 'clean_title': 'vagga', 'total_revenue': 4981.380000000001}, {'clean_artist': '', 'clean_title': 'kiä meil pahanu', 'total_revenue': 4916.11}]}

exec(code, env_args)
