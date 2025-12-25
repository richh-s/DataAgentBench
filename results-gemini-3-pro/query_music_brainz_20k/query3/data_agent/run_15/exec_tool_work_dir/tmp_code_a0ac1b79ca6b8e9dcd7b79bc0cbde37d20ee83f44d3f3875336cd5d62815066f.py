code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-1271116417397029887'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-6101111967261760493'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

# Convert types
df_sales['revenue_usd'] = pd.to_numeric(df_sales['total_revenue'], errors='coerce').fillna(0)
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Merge
df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Cleaning functions
def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = re.sub(r"\(.*?\)|\[.*?\]", "", text)
    text = re.sub(r"[^\w\s]", "", text)
    return text.strip().lower()

def clean_artist(text):
    if not isinstance(text, str):
        return "unknown"
    text = text.strip().lower()
    if text in ["none", "unknown", "[unknown]", ""]:
        return "unknown"
    text = re.sub(r"[^\w\s]", "", text)
    return text

def extract_artist_from_title(row):
    title = row['title']
    artist = row['artist']
    if not isinstance(artist, str) or artist.strip().lower() in ["none", "unknown", "[unknown]", ""]:
        if isinstance(title, str) and " - " in title:
            parts = title.split(" - ", 1)
            return parts[0].strip()
    return artist

# Apply extraction
df['temp_artist'] = df.apply(extract_artist_from_title, axis=1)
df['clean_title'] = df['title'].apply(clean_text)
df['clean_artist'] = df['temp_artist'].apply(clean_artist)

# Filter Logic
def is_valid(row):
    title = row['clean_title']
    artist = row['clean_artist']
    
    if title == "" or title == "none" or title == "unknown":
        return False
    
    # Check for known "unknown" placeholders
    if artist in ["unknown", "tiidm\u00e4ld\u00e4", "tiidmalda"]:
        return False
        
    return True

valid_df = df[df.apply(is_valid, axis=1)]

# Group and Sum
grouped = valid_df.groupby(['clean_title', 'clean_artist'])['revenue_usd'].sum().reset_index()
grouped = grouped.sort_values(by='revenue_usd', ascending=False)

# Get top 10 result
top_10 = grouped.head(10).to_dict(orient='records')

top_song = top_10[0]
matches = valid_df[
    (valid_df['clean_title'] == top_song['clean_title']) & 
    (valid_df['clean_artist'] == top_song['clean_artist'])
]

def get_best_str(series):
    valid_vals = series[~series.str.lower().isin(['none', 'unknown', '[unknown]', ''])]
    if not valid_vals.empty:
        return valid_vals.mode()[0]
    return series.mode()[0] if not series.empty else "Unknown"

final_title = get_best_str(matches['title'])
final_artist = get_best_str(matches['temp_artist'])

print("__RESULT__:")
print(json.dumps({"top_10": top_10, "winner": {"title": final_title, "artist": final_artist, "revenue": top_song['revenue_usd']}}))"""

env_args = {'var_function-call-1271116417397029887': 'file_storage/function-call-1271116417397029887.json', 'var_function-call-6101111967261760493': 'file_storage/function-call-6101111967261760493.json', 'var_function-call-5041480887059053554': {'title': 'None', 'artist': 'None', 'clean_title': 'none', 'clean_artist': 'unknown', 'total_revenue': 14647.52}, 'var_function-call-10058895073143176401': {'title': '003-', 'artist': ' ', 'clean_title': '003', 'clean_artist': 'unknown', 'total_revenue': 8582.15}, 'var_function-call-8766509445596430043': [{'clean_title': '003', 'clean_artist': 'unknown', 'revenue_usd': 8582.15}, {'clean_title': '001', 'clean_artist': 'unknown', 'revenue_usd': 7467.97}, {'clean_title': '004', 'clean_artist': 'unknown', 'revenue_usd': 7249.700000000001}, {'clean_title': '005', 'clean_artist': 'unknown', 'revenue_usd': 6155.29}, {'clean_title': '009', 'clean_artist': 'unknown', 'revenue_usd': 5045.7}, {'clean_title': '002', 'clean_artist': 'unknown', 'revenue_usd': 5013.4400000000005}, {'clean_title': 'kiä meil pahanu', 'clean_artist': 'tiidmäldä', 'revenue_usd': 4916.11}, {'clean_title': '010', 'clean_artist': 'unknown', 'revenue_usd': 4734.360000000001}, {'clean_title': '012', 'clean_artist': 'unknown', 'revenue_usd': 4641.08}, {'clean_title': '006', 'clean_artist': 'unknown', 'revenue_usd': 4366.82}], 'var_function-call-1567579355641234032': {'top_10': [{'clean_title': 'kiä meil pahanu', 'clean_artist': 'tiidmäldä', 'revenue_usd': 4916.11}, {'clean_title': 'groovey', 'clean_artist': 'rich matteson', 'revenue_usd': 4128.59}, {'clean_title': 'the fire still burns', 'clean_artist': 'russ ballard', 'revenue_usd': 3807.4}, {'clean_title': 'three seasons', 'clean_artist': 'swallow', 'revenue_usd': 3803.5}, {'clean_title': 'lescalade obscure', 'clean_artist': 'charles koechlin', 'revenue_usd': 3802.76}, {'clean_title': 'stormy', 'clean_artist': 'scott walker', 'revenue_usd': 3792.1800000000003}, {'clean_title': 'too beautiful', 'clean_artist': 'will kimbrough', 'revenue_usd': 3784.37}, {'clean_title': 'zo gaat het leven aan je voor', 'clean_artist': 'syb van der ploeg', 'revenue_usd': 3779.05}, {'clean_title': 'vostok', 'clean_artist': 'craig padilla', 'revenue_usd': 3767.95}, {'clean_title': 'travel', 'clean_artist': 'guts pie earshot', 'revenue_usd': 3703.98}], 'winner': {'title': 'Kiä meil pahanu', 'artist': '[tiidmäldä]', 'revenue': 4916.11}}}

exec(code, env_args)
