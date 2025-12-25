code = """import json
import pandas as pd
import re

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
    if s in ['none', 'null', 'unknown', '[unknown]', 'n.a.', 'n/a']:
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
            # Only accept if potential artist is not empty and reasonably long/valid
            if pot_artist:
                final_artist = pot_artist
                final_title = pot_title
    else:
        # If artist is known, check if title contains it
        if len(title_parts) == 2:
            p0 = normalize(title_parts[0])
            p1 = normalize(title_parts[1])
            if p0 == artist_clean:
                final_title = p1
                
    return pd.Series([final_artist, final_title])

df[['clean_artist', 'clean_title']] = df.apply(process_row, axis=1)

# Filter out empty artist
df_valid = df[df['clean_artist'] != ""].copy()

grouped = df_valid.groupby(['clean_artist', 'clean_title'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

top_5 = grouped.head(5).to_dict(orient='records')

# Get details for the top 1
if top_5:
    top_artist = top_5[0]['clean_artist']
    top_title = top_5[0]['clean_title']
    mask_top = (df['clean_artist'] == top_artist) & (df['clean_title'] == top_title)
    top_rows = df[mask_top][['track_id', 'title', 'artist', 'total_revenue']].head(10).to_dict(orient='records')
else:
    top_rows = []

print("__RESULT__:")
print(json.dumps({"top_5": top_5, "top_rows": top_rows}))"""

env_args = {'var_function-call-6059198179457054813': 'file_storage/function-call-6059198179457054813.json', 'var_function-call-1039588835092017339': 'file_storage/function-call-1039588835092017339.json', 'var_function-call-2520799401825761242': {'title': 'None', 'artist': 'None', 'revenue_usd': 14647.52, 'clean_title': 'none', 'clean_artist': 'unknown'}, 'var_function-call-5557107916154986499': [{'clean_artist': '', 'clean_title': '003', 'total_revenue': 8582.15}, {'clean_artist': '', 'clean_title': '001', 'total_revenue': 7467.97}, {'clean_artist': '', 'clean_title': '004', 'total_revenue': 7271.32}, {'clean_artist': '', 'clean_title': '005', 'total_revenue': 6155.29}, {'clean_artist': 'rich matteson', 'clean_title': 'groovey', 'total_revenue': 5417.34}, {'clean_artist': 'syb van der ploeg', 'clean_title': 'zo gaat het leven aan je voor', 'total_revenue': 5256.43}, {'clean_artist': '', 'clean_title': '009', 'total_revenue': 5045.7}, {'clean_artist': '', 'clean_title': '002', 'total_revenue': 5013.4400000000005}, {'clean_artist': 'ske', 'clean_title': 'vagga', 'total_revenue': 4981.380000000001}, {'clean_artist': '', 'clean_title': 'kiä meil pahanu', 'total_revenue': 4916.11}], 'var_function-call-12269920380845207994': {'rows_003': [{'track_id': '13703', 'title': '003- (offvocal)', 'artist': 'marble', 'album': ' (2011)', 'total_revenue': 568.9}, {'track_id': '17949', 'title': '003', 'artist': '03:04', 'album': 'Contours', 'total_revenue': 309.69}, {'track_id': '10708', 'title': '003- ', 'artist': 'My Victory', 'album': 'We are Back! Vol. VI (2012)', 'total_revenue': 777.13}, {'track_id': '7540', 'title': '003-', 'artist': 'None', 'album': ' (1988)', 'total_revenue': 949.57}, {'track_id': '10208', 'title': '003-', 'artist': 'None', 'album': '    (2002)', 'total_revenue': 1045.59}, {'track_id': '2183', 'title': '003-  ', 'artist': 'n.a.', 'album': '  (2004)', 'total_revenue': 1138.59}, {'track_id': '3833', 'title': '003-', 'artist': 'None', 'album': ' (1980)', 'total_revenue': 496.93}, {'track_id': '5576', 'title': '003-', 'artist': ' ', 'album': ' (2003)', 'total_revenue': 1703.85}, {'track_id': '15920', 'title': '003-', 'artist': 'None', 'album': 'Grace and Charm (2005)', 'total_revenue': 954.69}, {'track_id': '19156', 'title': '003- (live)', 'artist': ' ', 'album': '  (2009)', 'total_revenue': 165.43}], 'rows_rich': [{'track_id': '17312', 'title': 'Groovey', 'artist': 'Rich Matteson', 'album': 'Groovey', 'total_revenue': 1036.29}, {'track_id': '6146', 'title': 'Rich Matteson - Groovey', 'artist': 'None', 'album': 'Groovey', 'total_revenue': 1288.75}, {'track_id': '16496', 'title': 'Groovey', 'artist': 'Rich Matteson', 'album': 'Groovey', 'total_revenue': 949.82}, {'track_id': '8829', 'title': 'Groovey', 'artist': 'Rich Matteson', 'album': 'Groovey', 'total_revenue': 2142.48}]}}

exec(code, env_args)
