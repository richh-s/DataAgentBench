code = """import json
import pandas as pd
import re

# Load data using locals()
sales_path = locals()['var_function-call-4051379680636231128']
tracks_path = locals()['var_function-call-8323022647669375919']

with open(sales_path, 'r') as f:
    sales_data = json.load(f)
with open(tracks_path, 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_sales['revenue_usd'] = pd.to_numeric(df_sales['total_revenue'])

df_tracks = pd.DataFrame(tracks_data)

# Merge
df = pd.merge(df_sales, df_tracks, on='track_id')

def clean_str(s):
    if not s or str(s).lower() in ['none', '[unknown]', 'unknown', 'nan']:
        return ""
    # Keep alphanumeric (including unicode)
    # Using filter with isalnum
    return "".join(c for c in str(s).lower() if c.isalnum())

def extract_artist_title(row):
    t = row['title']
    a = row['artist']
    
    a_missing = not a or str(a).lower() in ['none', '[unknown]', 'unknown', 'nan']
    
    if a_missing and t and ' - ' in str(t):
        parts = str(t).split(' - ', 1)
        a = parts[0]
        t = parts[1]
    
    return clean_str(a), clean_str(t), t, a

results = {}

for idx, row in df.iterrows():
    a_clean, t_clean, t_orig, a_orig = extract_artist_title(row)
    
    # If both clean strings are empty, we probably shouldn't group them all together unless they are truly the same.
    # But usually, different unknown tracks have unique IDs. 
    # If we group by (a_clean, t_clean), all unknowns become one. 
    # We should skip aggregation for completely empty keys or handle them by track_id?
    # But the query asks for "Which song". A bunch of unknown songs is not "a song".
    # We will exclude (empty, empty) from valid results for now.
    
    if not a_clean and not t_clean:
        continue

    key = (a_clean, t_clean)
    
    rev = row['revenue_usd']
    
    if key not in results:
        results[key] = {
            'total_revenue': 0.0,
            'titles': [],
            'artists': []
        }
    
    results[key]['total_revenue'] += rev
    results[key]['titles'].append(t_orig)
    results[key]['artists'].append(a_orig)

# Convert to list
final_list = []
for key, val in results.items():
    from collections import Counter
    valid_titles = [str(x) for x in val['titles'] if x and str(x).lower() != 'none']
    valid_artists = [str(x) for x in val['artists'] if x and str(x).lower() not in ['none', '[unknown]']]
    
    disp_title = Counter(valid_titles).most_common(1)[0][0] if valid_titles else (str(val['titles'][0]) if val['titles'] else "Unknown")
    disp_artist = Counter(valid_artists).most_common(1)[0][0] if valid_artists else (str(val['artists'][0]) if val['artists'] else "Unknown")
    
    final_list.append({
        'key': key,
        'revenue': val['total_revenue'],
        'display_title': disp_title,
        'display_artist': disp_artist
    })

# Sort by revenue
final_list.sort(key=lambda x: x['revenue'], reverse=True)

print("__RESULT__:")
print(json.dumps(final_list[:20]))"""

env_args = {'var_function-call-4051379680636231128': 'file_storage/function-call-4051379680636231128.json', 'var_function-call-8323022647669375919': 'file_storage/function-call-8323022647669375919.json', 'var_function-call-3409380784939489692': [{'key': ['', ''], 'revenue': 228323.90999999997, 'display_title': 'unknown', 'display_artist': 'Χρήστος Δάντης'}, {'key': ['', '004'], 'revenue': 7271.32, 'display_title': '004- ', 'display_artist': ' '}, {'key': ['', '003'], 'revenue': 7090.129999999999, 'display_title': '003-', 'display_artist': ' '}, {'key': ['', '001'], 'revenue': 6283.24, 'display_title': '001-', 'display_artist': '[unknown]'}, {'key': ['', '005'], 'revenue': 6155.29, 'display_title': '005-', 'display_artist': ' '}, {'key': ['richmatteson', 'groovey'], 'revenue': 5417.34, 'display_title': 'Groovey', 'display_artist': 'Rich Matteson'}, {'key': ['', '009'], 'revenue': 5045.7, 'display_title': '009-   ', 'display_artist': ' '}, {'key': ['', '002'], 'revenue': 5013.4400000000005, 'display_title': '002-', 'display_artist': ' '}, {'key': ['', '010'], 'revenue': 4734.360000000001, 'display_title': '010-', 'display_artist': ' '}, {'key': ['', '012'], 'revenue': 4641.08, 'display_title': '012-', 'display_artist': ' '}]}

exec(code, env_args)
