code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-5828808762132496056'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-8680221993785875883'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)
df_sales['revenue_usd'] = pd.to_numeric(df_sales['total_revenue'])
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)
df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# (Insert normalization logic here, same as above)
def clean_string(s):
    if s is None:
        return ""
    return str(s).lower().strip()

def normalize_track(row):
    title = clean_string(row['title'])
    artist = clean_string(row['artist'])
    if artist in ["none", "[unknown]", ""]:
        artist = ""
        if " - " in title:
            parts = title.split(" - ", 1)
            if not re.match(r'^\d+$', parts[0].strip()):
                 artist = parts[0].strip()
                 title = parts[1].strip()
    title_no_num = re.sub(r'^\d+[\.\-]\s*', '', title)
    title_no_num = re.sub(r'^\d+\s+', '', title_no_num)
    if title_no_num.strip() != "":
        title = title_no_num
    title_no_parens = re.sub(r'\(.*?\)', '', title)
    title_no_parens = re.sub(r'\[.*?\]', '', title_no_parens)
    if title_no_parens.strip() != "":
        title = title_no_parens
    if " - " in title:
        title = title.split(" - ")[0]
    return pd.Series([artist.strip(), title.strip()])

df[['norm_artist', 'norm_title']] = df.apply(normalize_track, axis=1)

# Debug: check specific artists
check_artists = ["fischerspooner", "syb van der ploeg", "neil biggin"]
debug_df = df[df['norm_artist'].isin(check_artists)]

print("__RESULT__:")
print(json.dumps({
    "debug_rows": debug_df[['title', 'artist', 'norm_title', 'norm_artist', 'revenue_usd']].head(20).to_dict(orient='records')
}))"""

env_args = {'var_function-call-5828808762132496056': 'file_storage/function-call-5828808762132496056.json', 'var_function-call-8680221993785875883': 'file_storage/function-call-8680221993785875883.json', 'var_function-call-1138439901428454656': {'top_song': {'artist': '', 'title': '', 'total_revenue': 63152.73}, 'top_5': [{'norm_artist': '', 'norm_title': '', 'revenue_usd': 63152.73}, {'norm_artist': '', 'norm_title': 'none', 'revenue_usd': 14647.52}, {'norm_artist': 'syb van der ploeg', 'norm_title': 'zo gaat het leven aan je voor', 'revenue_usd': 9013.69}, {'norm_artist': 'neil biggin', 'norm_title': 'chile', 'revenue_usd': 7744.25}, {'norm_artist': 'fischerspooner', 'norm_title': 'emerge', 'revenue_usd': 7515.88}]}, 'var_function-call-2108406321925842224': {'bad_rows_sample': [{'track_id': '937', 'title': 'None', 'artist': 'J.K. Rowling', 'norm_artist': 'j.k. rowling', 'norm_title': 'none'}, {'track_id': '4157', 'title': 'None', 'artist': 'Sean Terrington Wright', 'norm_artist': 'sean terrington wright', 'norm_title': 'none'}, {'track_id': '4849', 'title': '(ʻUlalena)', 'artist': 'ʻUlalena', 'norm_artist': 'ʻulalena', 'norm_title': ''}, {'track_id': '6138', 'title': 'Bill Clinton - [untitled]', 'artist': 'None', 'norm_artist': 'bill clinton', 'norm_title': ''}, {'track_id': '6416', 'title': 'eLon Bolier - [unknown]', 'artist': 'None', 'norm_artist': 'elon bolier', 'norm_title': ''}, {'track_id': '8206', 'title': 'None', 'artist': 'John Katzenbach', 'norm_artist': 'john katzenbach', 'norm_title': 'none'}, {'track_id': '9948', 'title': '8 (Fuengirola)', 'artist': 'Rordam', 'norm_artist': 'rordam', 'norm_title': ''}, {'track_id': '13435', 'title': '[silence]', 'artist': 'Cornelius', 'norm_artist': 'cornelius', 'norm_title': ''}, {'track_id': '13879', 'title': 'None', 'artist': 'Vitamin C', 'norm_artist': 'vitamin c', 'norm_title': 'none'}, {'track_id': '15003', 'title': '020-', 'artist': 'None', 'norm_artist': '', 'norm_title': ''}, {'track_id': '15267', 'title': 'None', 'artist': 'Dezrok', 'norm_artist': 'dezrok', 'norm_title': 'none'}, {'track_id': '16031', 'title': '[untitled]', 'artist': 'S-Max', 'norm_artist': 's-max', 'norm_title': ''}, {'track_id': '16809', 'title': '009-   ', 'artist': 'None', 'norm_artist': '', 'norm_title': ''}, {'track_id': '18972', 'title': '[untitled]', 'artist': 'Howard Blake', 'norm_artist': 'howard blake', 'norm_title': ''}, {'track_id': '2402', 'title': '001-[unknown]', 'artist': 'Garbage-A-Trois', 'norm_artist': 'garbage-a-trois', 'norm_title': ''}, {'track_id': '3033', 'title': '006- (Inst-umental)', 'artist': 'None', 'norm_artist': '', 'norm_title': ''}, {'track_id': '3971', 'title': 'Tegan and Sara - [encore break]', 'artist': 'None', 'norm_artist': 'tegan and sara', 'norm_title': ''}, {'track_id': '6074', 'title': '[silence] (愛 am BEST)', 'artist': '大塚愛', 'norm_artist': '大塚愛', 'norm_title': ''}, {'track_id': '6428', 'title': '[untitled] (The Canterville Ghost)', 'artist': 'Howard Blake', 'norm_artist': 'howard blake', 'norm_title': ''}, {'track_id': '7650', 'title': 'Les Joyaux de la Princesse - [untitled]', 'artist': 'None', 'norm_artist': 'les joyaux de la princesse', 'norm_title': ''}]}, 'var_function-call-16732425880784581730': {'top_song': {'artist': 'syb van der ploeg', 'title': 'zo gaat het leven aan je voor', 'revenue': 9013.69}, 'top_5': [{'norm_artist': 'syb van der ploeg', 'norm_title': 'zo gaat het leven aan je voor', 'revenue_usd': 9013.69}, {'norm_artist': 'neil biggin', 'norm_title': 'chile', 'revenue_usd': 7744.25}, {'norm_artist': 'fischerspooner', 'norm_title': 'emerge', 'revenue_usd': 7515.88}, {'norm_artist': 'vrisak generacije', 'norm_title': 'ne veruj', 'revenue_usd': 7299.909999999999}, {'norm_artist': 'ske', 'norm_title': 'vagga', 'revenue_usd': 7214.200000000001}]}}

exec(code, env_args)
