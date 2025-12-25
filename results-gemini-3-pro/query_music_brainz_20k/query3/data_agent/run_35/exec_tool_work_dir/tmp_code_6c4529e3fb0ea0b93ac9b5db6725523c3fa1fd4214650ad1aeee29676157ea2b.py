code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-2634326689479579170'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-2634326689479580217'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')

def normalize_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r'\([^)]*\)', '', text)
    text = re.sub(r'\[[^]]*\]', '', text)
    text = re.sub(r'^\s*\d+[\.\-\s]+', '', text)
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def clean_artist(text):
    if not isinstance(text, str):
        return "unknown"
    norm = normalize_text(text)
    if norm in ["none", "unknown", "", "null"]:
        return "unknown"
    return norm

df_merged['norm_title'] = df_merged['title'].apply(normalize_text)
df_merged['norm_artist'] = df_merged['artist'].apply(clean_artist)

# Check constituents of top groups
top_norm_titles = ["zo gaat het leven aan je voor", "vagga", "emerge"]
mask = df_merged['norm_title'].isin(top_norm_titles)
details = df_merged[mask][['track_id', 'title', 'artist', 'norm_title', 'norm_artist', 'total_revenue']]

print("__RESULT__:")
print(details.to_json(orient='records'))"""

env_args = {'var_function-call-2634326689479579170': 'file_storage/function-call-2634326689479579170.json', 'var_function-call-2634326689479580217': 'file_storage/function-call-2634326689479580217.json', 'var_function-call-8303588462130579925': {'norm_title': 'none', 'norm_artist': 'unknown', 'revenue': 14647.52, 'example_title': 'None', 'example_artist': 'None'}, 'var_function-call-11821774954555155827': [{'norm_title': 'zo gaat het leven aan je voor', 'norm_artist': 'syb van der ploeg', 'total_revenue': 5158.72, 'example_title': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'example_artist': 'Syb van der Ploeg'}, {'norm_title': 'vagga', 'norm_artist': 'ske', 'total_revenue': 5152.0, 'example_title': '011-Vagga', 'example_artist': 'Ske'}, {'norm_title': 'emerge', 'norm_artist': 'fischerspooner', 'total_revenue': 5054.81, 'example_title': 'Emerge (Dave Clarke remix)', 'example_artist': 'Fischerspooner'}, {'norm_title': 'travel', 'norm_artist': 'guts pie earshot', 'total_revenue': 4933.9, 'example_title': '001-Travel (live)', 'example_artist': 'Guts Pie Earshot'}, {'norm_title': 'kiä meil pahanu', 'norm_artist': 'unknown', 'total_revenue': 4916.11, 'example_title': 'Kiä meil pahanu? (Mina lätsi Siidile)', 'example_artist': '[tiidmäldä]'}]}

exec(code, env_args)
