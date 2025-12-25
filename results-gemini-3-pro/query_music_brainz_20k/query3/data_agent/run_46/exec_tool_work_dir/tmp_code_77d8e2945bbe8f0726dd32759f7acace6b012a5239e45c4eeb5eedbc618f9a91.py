code = """import json
import pandas as pd
import re

# Load data (re-loading to be safe/clean)
with open(locals()['var_function-call-8471687202024638385'], 'r') as f:
    tracks = pd.DataFrame(json.load(f))
with open(locals()['var_function-call-8471687202024637006'], 'r') as f:
    sales = pd.DataFrame(json.load(f))

sales['total_revenue'] = pd.to_numeric(sales['total_revenue'])
df = pd.merge(tracks, sales, on='track_id')

def extract_artist_title(row):
    title = row['title']
    artist = row['artist']
    if artist in [None, 'None', '[unknown]', '']:
        artist = None
    if title is None:
        title = ""
    if artist is None:
        if " - " in title:
            parts = title.split(" - ", 1)
            return parts[0].strip(), parts[1].strip()
        else:
            return "unknown", title.strip()
    else:
        return artist, title

df[['clean_artist', 'clean_title_raw']] = df.apply(lambda x: pd.Series(extract_artist_title(x)), axis=1)

def normalize_title(t):
    t = t.lower()
    t = re.sub(r'^\d+[-.\s]+', '', t)
    t = re.sub(r'\(.*?\)', '', t)
    t = re.sub(r'\[.*?\]', '', t)
    t = re.sub(r'\bfeat\..*', '', t)
    t = re.sub(r'[^\w\s]', '', t)
    return t.strip()

def normalize_artist(a):
    a = a.lower()
    a = re.sub(r'\bfeat\..*', '', a)
    return a.strip()

df['norm_title'] = df['clean_title_raw'].apply(normalize_title)
df['norm_artist'] = df['clean_artist'].apply(normalize_artist)

# Filter out "junk" for inspection
junk_mask = (df['norm_artist'].isin(['unknown', ''])) | (df['norm_title'].isin(['', 'none']))
junk_df = df[junk_mask]

# Group valid
valid_df = df[~junk_mask]
grouped = valid_df.groupby(['norm_artist', 'norm_title'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

print("__RESULT__:")
print(json.dumps({
    "top_valid": json.loads(grouped.head(5).to_json(orient='records')),
    "junk_sample": json.loads(junk_df[['title', 'artist', 'norm_title', 'norm_artist', 'total_revenue']].head(10).to_json(orient='records')),
    "junk_stats": {
        "count": int(junk_df.shape[0]),
        "total_revenue": float(junk_df['total_revenue'].sum())
    }
}))"""

env_args = {'var_function-call-10791029874110747991': [{'COUNT(*)': '19375'}], 'var_function-call-10791029874110750228': [{'count(DISTINCT track_id)': '19375'}], 'var_function-call-8471687202024638385': 'file_storage/function-call-8471687202024638385.json', 'var_function-call-8471687202024637006': 'file_storage/function-call-8471687202024637006.json', 'var_function-call-14530195528525198333': [{'norm_artist': 'unknown', 'norm_title': '', 'total_revenue': 45147.94}, {'norm_artist': '', 'norm_title': '', 'total_revenue': 21799.12}, {'norm_artist': 'unknown', 'norm_title': 'none', 'total_revenue': 14647.52}, {'norm_artist': 'fischerspooner', 'norm_title': 'emerge', 'total_revenue': 6665.27}, {'norm_artist': 'syb van der ploeg', 'norm_title': 'zo gaat het leven aan je voor', 'total_revenue': 6636.1}, {'norm_artist': 'ske', 'norm_title': 'vagga', 'total_revenue': 6611.56}, {'norm_artist': 'echolyn', 'norm_title': 'letters a short essay', 'total_revenue': 6280.0}, {'norm_artist': 'fausto papetti', 'norm_title': 'lovers', 'total_revenue': 6259.3}, {'norm_artist': 'vrisak generacije', 'norm_title': 'ne veruj', 'total_revenue': 6125.34}, {'norm_artist': 'neil biggin', 'norm_title': 'chile', 'total_revenue': 6008.71}]}

exec(code, env_args)
